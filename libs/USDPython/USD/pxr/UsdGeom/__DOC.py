def Execute(result):
   result["Xformable"].__doc__ = """
Base class for all transformable prims, which allows arbitrary
sequences of component affine transformations to be encoded.



You may find it useful to review Linear Algebra in UsdGeom while
reading this class description. B{Supported Component Transformation
Operations}

UsdGeomXformable currently supports arbitrary sequences of the
following operations, each of which can be encoded in an attribute of
the proper shape in any supported precision:
   - translate - 3D

   - scale - 3D

   - rotateX - 1D angle in degrees

   - rotateY - 1D angle in degrees

   - rotateZ - 1D angle in degrees

   - rotateABC - 3D where ABC can be any combination of the six
     principle Euler Angle sets: XYZ, XZY, YXZ, YZX, ZXY, ZYX. See note on
     rotation packing order

   - orient - 4D (quaternion)

   - transform - 4x4D
     B{Creating a Component Transformation}

To add components to a UsdGeomXformable prim, simply call AddXformOp()
with the desired op type, as enumerated in UsdGeomXformOp::Type, and
the desired precision, which is one of UsdGeomXformOp::Precision.
Optionally, you can also provide an "op suffix" for the operator that
disambiguates it from other components of the same type on the same
prim.  Application-specific transform schemas can use the suffixes to
fill a role similar to that played by AbcGeom::XformOp's "Hint" enums
for their own round-tripping logic.

We also provide specific "Add" API for each type, for clarity and
conciseness, e.g. AddTranslateOp() , AddRotateXYZOp() etc.

AddXformOp() will return a UsdGeomXformOp object, which is a schema on
a newly created UsdAttribute that provides convenience API for
authoring and computing the component transformations. The
UsdGeomXformOp can then be used to author any number of timesamples
and default for the op.

Each successive call to AddXformOp() adds an operator that will be
applied "more locally" than the preceding operator, just as if we were
pushing transforms onto a transformation stack - which is precisely
what should happen when the operators are consumed by a reader.

If you can, please try to use the UsdGeomXformCommonAPI, which wraps
the UsdGeomXformable with an interface in which Op creation is taken
care of for you, and there is a much higher chance that the data you
author will be importable without flattening into other DCC's, as it
conforms to a fixed set of Scale-Rotate-Translate Ops.

Using the Authoring API B{Data Encoding and Op Ordering}

Because there is no "fixed schema" of operations, all of the
attributes that encode transform operations are dynamic, and are
scoped in the namespace "xformOp". The second component of an
attribute's name provides the *type* of operation, as listed above. An
"xformOp" attribute can have additional namespace components derived
from the *opSuffix* argument to the AddXformOp() suite of methods,
which provides a preferred way of naming the ops such that we can have
multiple "translate" ops with unique attribute names. For example, in
the attribute named "xformOp:translate:maya:pivot", "translate" is the
type of operation and "maya:pivot" is the suffix.

The following ordered list of attribute declarations in usda define a
basic Scale-Rotate-Translate with XYZ Euler angles, wherein the
translation is double-precision, and the remainder of the ops are
single, in which we will:

   - Scale by 2.0 in each dimension

   - Rotate about the X, Y, and Z axes by 30, 60, and 90 degrees,
     respectively

   - Translate by 100 units in the Y direction
     ::

  float3 xformOp:rotateXYZ = (30, 60, 90)
  float3 xformOp:scale = (2, 2, 2)
  double3 xformOp:translate = (0, 100, 0)
  uniform token[] xformOpOrder = [ "xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale" ]

The attributes appear in the dictionary order in which USD, by
default, sorts them. To ensure the ops are recovered and evaluated in
the correct order, the schema introduces the B{xformOpOrder}
attribute, which contains the names of the op attributes, in the
precise sequence in which they should be pushed onto a transform
stack. B{Note} that the order is opposite to what you might expect,
given the matrix algebra described in Linear Algebra in UsdGeom. This
also dictates order of op creation, since each call to AddXformOp()
adds a new op to the end of the B{xformOpOrder} array, as a new "most-
local" operation. See Example 2 below for C++ code that could have
produced this USD.

If it were important for the prim's rotations to be independently
overridable, we could equivalently (at some performance cost) encode
the transformation also like so: ::

  float xformOp:rotateX = 30
  float xformOp:rotateY = 60
  float xformOp:rotateZ = 90
  float3 xformOp:scale = (2, 2, 2)
  double3 xformOp:translate = (0, 100, 0)
  uniform token[] xformOpOrder = [ "xformOp:translate", "xformOp:rotateZ", "xformOp:rotateY", "xformOp:rotateX", "xformOp:scale" ]

Again, note that although we are encoding an XYZ rotation, the three
rotations appear in the B{xformOpOrder} in the opposite order, with Z,
followed, by Y, followed by X.

Were we to add a Maya-style scalePivot to the above example, it might
look like the following: ::

  float3 xformOp:rotateXYZ = (30, 60, 90)
  float3 xformOp:scale = (2, 2, 2)
  double3 xformOp:translate = (0, 100, 0)
  double3 xformOp:translate:scalePivot
  uniform token[] xformOpOrder = [ "xformOp:translate", "xformOp:rotateXYZ", "xformOp:translate:scalePivot", "xformOp:scale" ]

B{Paired "Inverted" Ops}

We have been claiming that the ordered list of ops serves as a set of
instructions to a transform stack, but you may have noticed in the
last example that there is a missing operation - the pivot for the
scale op needs to be applied in its inverse-form as a final (most
local) op! In the AbcGeom::Xform schema, we would have encoded an
actual "final" translation op whose value was authored by the exporter
as the negation of the pivot's value. However, doing so would be
brittle in USD, given that each op can be independently overridden,
and the constraint that one attribute must be maintained as the
negation of the other in order for successful re-importation of the
schema cannot be expressed in USD.

Our solution leverages the B{xformOpOrder} member of the schema,
which, in addition to ordering the ops, may also contain one of two
special tokens that address the paired op and "stack resetting"
behavior.

The "paired op" behavior is encoded as an "!invert!" prefix in
B{xformOpOrder}, as the result of an AddXformOp(isInverseOp=True)
call.  The B{xformOpOrder} for the last example would look like: ::

  uniform token[] xformOpOrder = [ "xformOp:translate", "xformOp:rotateXYZ", "xformOp:translate:scalePivot", "xformOp:scale", "!invert!xformOp:translate:scalePivot" ]

When asked for its value via UsdGeomXformOp::GetOpTransform() , an
"inverted" Op (i.e. the "inverted" half of a set of paired Ops) will
fetch the value of its paired attribute and return its negation. This
works for all op types - an error will be issued if a "transform" type
op is singular and cannot be inverted. When getting the authored value
of an inverted op via UsdGeomXformOp::Get() , the raw, uninverted
value of the associated attribute is returned.

For the sake of robustness, B{setting a value on an inverted op is
disallowed.} Attempting to set a value on an inverted op will result
in a coding error and no value being set.

B{Resetting the Transform Stack}

The other special op/token that can appear in *xformOpOrder* is
*"!resetXformStack!"*, which, appearing as the first element of
*xformOpOrder*, indicates this prim should not inherit the
transformation of its namespace parent. See SetResetXformStack()

B{Expected Behavior for "Missing" Ops}

If an importer expects Scale-Rotate-Translate operations, but a prim
has only translate and rotate ops authored, the importer should assume
an identity scale. This allows us to optimize the data a bit, if only
a few components of a very rich schema (like Maya's) are authored in
the app.

B{Using the C++ API}

#1. Creating a simple transform matrix encoding ::

  bool CreateMatrixWithDefault(UsdGeomXformable const 
& gprim, GfMatrix4d const  &
defValue)
  {
      if (UsdGeomXformOp transform = gprim.MakeMatrixXform()){
          return transform.Set(defValue, UsdTimeCode::Default());
      } else {
          return false;
      }
  }

 #2. Creating the simple SRT from the example above ::

  bool CreateExampleSRT(UsdGeomXformable const 
&
gprim)
  {
      // For insurance, we will make sure there aren't any ordered ops
      // before we start
      gprim.ClearXformOpOrder();
  
      UsdGeomXformOp s, r, t;
      
      if ( !(t = gprim.AddTranslateOp())){
          return false;
      }
      if ( !(r = gprim.AddRotateXYZOp())){
          return false;
      }
      if ( !(s = gprim.AddScaleOp())){
          return false;
      }
  
      return (t.Set(GfVec3d(0, 100, 0), UsdTimeCode::Default()) &&
              r.Set(GfVec3f(30, 60, 90), UsdTimeCode::Default()) &&
              s.Set(GfVec3f(2, 2, 2), UsdTimeCode::Default()));
  }

 #3. Creating a parameterized SRT with pivot using
UsdGeomXformCommonAPI ::

  bool CreateSRTWithDefaults(UsdGeomXformable const 
&
gprim, 
                             GfVec3d const 
&
defTranslate,
                             GfVec3f const 
&
defRotateXYZ,
                             GfVec3f const 
&
defScale,
                             GfVec3f const 
&
defPivot)
  {
      if (UsdGeomXformCommonAPI xform = UsdGeomXformCommonAPI(gprim)){
          return xform.SetXformVectors(defTranslate, defRotateXYZ, defScale,
                                       defPivot, UsdGeomXformCommonAPI::RotationOrderXYZ,
                                       UsdTimeCode::Default());
      } else {
          return false;
      }
  }

 #4. Creating a rotate-only pivot transform with animated rotation and
translation ::

  bool CreateAnimatedTransform(UsdGeomXformable const 
&
gprim, 
                               GfVec3d const 
&
baseTranslate,
                               GfVec3f const 
&
baseRotateXYZ,
                               GfVec3f const 
&
defPivot)
  {
      // Only need to do this if you're overriding an existing scene
      if (!gprim.ClearXformOpOrder()){
          return false;
      }
      
      static const TfToken  pivSuffix("pivot");
      UsdGeomXformOp    trans = gprim.AddTranslateOp();
      UsdGeomXformOp    pivot = gprim.AddTranslateOp(UsdGeomXformOp::PrecisionFloat,
                                                     pivSuffix);
      UsdGeomXformOp   rotate = gprim.AddRotateXYZOp();
      UsdGeomXformOp pivotInv = gprim.AddTranslateOp(UsdGeomXformOp::PrecisionFloat,
                                                     pivSuffix,
                                                     /* isInverseOp = */ true);
      // Now that we have created all the ops, set default values.
      // Note that we do not need to (and cannot) set the value
      // for the pivot's inverse op.
      // For didactic brevity we are eliding success return value checks,
      // but would absolutely have them in exporters!
      trans.Set(baseTranslate, UsdTimeCode::Default());
      pivot.Set(defPivot, UsdTimeCode::Default());
      rotate.Set(baseRotateXYZ, UsdTimeCode::Default());
      
      // Now animate the translation and rotation over a fixed interval with
      // cheesy linear animation.
      GfVec3d  position(baseTranslate);
      GfVec3f  rotation(baseRotateXYZ);
      
      for (double frame = 0; frame < 100.0; frame += 1.0){
          trans.Set(position, frame);
          rotate.Set(rotation, frame);
          position[0] += 5.0;
          rotation[2] += 7.0;
      }
      return true;
  }


"""
   result["Xformable"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomXformable on UsdPrim C{prim}.


Equivalent to UsdGeomXformable::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomXformable on the prim held by C{schemaObj}.


Should be preferred over UsdGeomXformable (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Xformable"].AddRotateXZYOp.im_func.func_doc = """AddRotateXZYOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a rotation op with XZY rotation order to the local stack
represented by this xformable.


Set the angle values of the resulting UsdGeomXformOp B{in degrees}

AddXformOp() , note on angle packing order

"""
   result["Xformable"].AddTransformOp.im_func.func_doc = """AddTransformOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a tranform op (4x4 matrix transformation) to the local stack
represented by this xformable.



AddXformOp() Note: This method takes a precision argument only to be
consistent with the other types of xformOps. The only valid precision
here is double since matrix values cannot be encoded in floating-pt
precision in Sdf.

"""
   result["Xformable"].GetTimeSamples.im_func.func_doc = """**static** GetTimeSamples(times) -> USDGEOM_API bool

times : sequence<double>


Sets C{times} to the union of all the timesamples at which xformOps
that are included in the xformOpOrder attribute are authored.


This clears the C{times} vector before accumulating sample times from
all the xformOps.

UsdAttribute::GetTimeSamples


----------------------------------------------------------------------
GetTimeSamples(orderedXformOps, times) -> USDGEOM_API bool

orderedXformOps : sequence< UsdGeomXformOp >
times : sequence<double>


Returns the union of all the timesamples at which the attributes
belonging to the given C{orderedXformOps} are authored.


This clears the C{times} vector before accumulating sample times from
C{orderedXformOps}.

UsdGeomXformable::GetTimeSamples

"""
   result["Xformable"].AddTranslateOp.im_func.func_doc = """AddTranslateOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a translate operation to the local stack represented by this
xformable.



AddXformOp()

"""
   result["Xformable"].SetResetXformStack.im_func.func_doc = """SetResetXformStack(resetXform) -> USDGEOM_API bool

resetXform : bool


Specify whether this prim's transform should reset the transformation
stack inherited from its parent prim.


By default, parent transforms are inherited. SetResetXformStack() can
be called at any time during authoring, but will always add a
'!resetXformStack!' op as the *first* op in the ordered list, if one
does not exist already. If one already exists, and C{resetXform} is
false, it will remove all ops upto and including the last
"!resetXformStack!" op.

"""
   result["Xformable"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomXformable

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomXformable holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomXformable(stage->GetPrimAtPath(path));


"""
   result["Xformable"].GetResetXformStack.im_func.func_doc = """GetResetXformStack() -> USDGEOM_API bool



Does this prim reset its parent's inherited transformation?


Returns true if "!resetXformStack!" appears *anywhere* in
xformOpOrder. When this returns true, all ops upto the last
"!resetXformStack!" in xformOpOrder are ignored when computing the
local transformation.

"""
   result["Xformable"].AddXformOp.im_func.func_doc = """AddXformOp(opType, precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

opType : XformOp.Type
precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add an affine transformation to the local stack represented by this
Xformable.


This will fail if there is already a transform operation of the same
name in the ordered ops on this prim (i.e. as returned by
GetOrderedXformOps() ), or if an op of the same name exists at all on
the prim with a different precision than that specified.

The newly created operation will become the most-locally applied
transformation on the prim, and will appear last in the list returned
by GetOrderedXformOps() . It is OK to begin authoring values to the
returned UsdGeomXformOp immediately, interspersed with subsequent
calls to AddXformOp() - just note the order of application, which
*can* be changed at any time (and in stronger layers) via
SetXformOpOrder() .

opType

is the type of transform operation, one of UsdGeomXformOp::Type.
precision

allows you to specify the precision with which you desire to encode
the data. This should be one of the values in the enum
UsdGeomXformOp::Precision. opSuffix

allows you to specify the purpose/meaning of the op in the stack. When
opSuffix is specified, the associated attribute's name is set to
"xformOp:<opType>:<opSuffix>". isInverseOp

is used to indicate an inverse transformation operation.

a UsdGeomXformOp that can be used to author to the operation. An error
is issued and the returned object will be invalid (evaluate to false)
if the op being added already exists in xformOpOrder or if the
arguments supplied are invalid.

If the attribute associated with the op already exists, but isn't of
the requested precision, a coding error is issued, but a valid xformOp
is returned with the existing attribute.

"""
   result["Xformable"].ClearXformOpOrder.im_func.func_doc = """ClearXformOpOrder() -> USDGEOM_API bool



Clears the local transform stack.

"""
   result["Xformable"].AddRotateXOp.im_func.func_doc = """AddRotateXOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a rotation about the X-axis to the local stack represented by this
xformable.


Set the angle value of the resulting UsdGeomXformOp B{in degrees}

AddXformOp()

"""
   result["Xformable"].GetXformOpOrderAttr.im_func.func_doc = """GetXformOpOrderAttr() -> USDGEOM_API UsdAttribute



Encodes the sequence of transformation operations in the order in
which they should be pushed onto a transform stack while visiting a
UsdStage 's prims in a graph traversal that will effect the desired
positioning for this prim and its descendant prims.


You should rarely, if ever, need to manipulate this attribute
directly. It is managed by the AddXformOp() , SetResetXformStack() ,
and SetXformOpOrder() , and consulted by GetOrderedXformOps() and
GetLocalTransformation() .

C++ Type: VtArray<TfToken>  Usd Type: SdfValueTypeNames->TokenArray
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["Xformable"].AddRotateYOp.im_func.func_doc = """AddRotateYOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a rotation about the YX-axis to the local stack represented by
this xformable.


Set the angle value of the resulting UsdGeomXformOp B{in degrees}

AddXformOp()

"""
   result["Xformable"].AddScaleOp.im_func.func_doc = """AddScaleOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a scale operation to the local stack represented by this
xformable.



AddXformOp()

"""
   result["Xformable"].AddRotateZYXOp.im_func.func_doc = """AddRotateZYXOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a rotation op with ZYX rotation order to the local stack
represented by this xformable.


Set the angle values of the resulting UsdGeomXformOp B{in degrees}

AddXformOp() , note on angle packing order

"""
   result["Xformable"].MakeMatrixXform.im_func.func_doc = """MakeMatrixXform() -> USDGEOM_API UsdGeomXformOp



Clears the existing local transform stack and creates a new xform op
of type 'transform'.


This API is provided for convenience since this is the most common
xform authoring operation.

ClearXformOpOrder()

AddTransformOp()

"""
   result["Xformable"].AddRotateZOp.im_func.func_doc = """AddRotateZOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a rotation about the Z-axis to the local stack represented by this
xformable.



AddXformOp()

"""
   result["Xformable"].SetXformOpOrder.im_func.func_doc = """SetXformOpOrder(orderedXformOps, resetXformStack) -> USDGEOM_API bool

orderedXformOps : sequence< UsdGeomXformOp >
resetXformStack : bool


Reorder the already-existing transform ops on this prim.


All elements in C{orderedXformOps} must be valid and represent
attributes on this prim. Note that it is *not* required that all the
existing operations be present in C{orderedXformOps}, so this method
can be used to completely change the transformation structure applied
to the prim.

If C{resetXformStack} is set to true, then "!resetXformOp! will be set
as the first op in xformOpOrder, to indicate that the prim does not
inherit its parent's transformation.

If you wish to re-specify a prim's transformation completely in a
stronger layer, you should first call this method with an *empty*
C{orderedXformOps} vector. From there you can call AddXformOp() just
as if you were authoring to the prim from scratch.

false if any of the elements of C{orderedXformOps} are not extant on
this prim, or if an error occurred while authoring the ordering
metadata. Under either condition, no scene description is authored.

GetOrderedXformOps()

"""
   result["Xformable"].TransformMightBeTimeVarying.im_func.func_doc = """TransformMightBeTimeVarying() -> USDGEOM_API bool



Determine whether there is any possibility that this prim's *local*
transformation may vary over time.


The determination is based on a snapshot of the authored state of the
op attributes on the prim, and may become invalid in the face of
further authoring.


----------------------------------------------------------------------
TransformMightBeTimeVarying(ops) -> USDGEOM_API bool

ops : sequence< UsdGeomXformOp >


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Determine whether there is any possibility that this prim's *local*
transformation may vary over time, using a pre-fetched (cached) list
of ordered xform ops supplied by the client.


The determination is based on a snapshot of the authored state of the
op attributes on the prim, and may become invalid in the face of
further authoring.

"""
   result["Xformable"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Xformable"].AddRotateYXZOp.im_func.func_doc = """AddRotateYXZOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a rotation op with YXZ rotation order to the local stack
represented by this xformable.


Set the angle values of the resulting UsdGeomXformOp B{in degrees}

AddXformOp() , note on angle packing order

"""
   result["Xformable"].AddOrientOp.im_func.func_doc = """AddOrientOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a orient op (arbitrary axis/angle rotation) to the local stack
represented by this xformable.



AddXformOp()

"""
   result["Xformable"].AddRotateYZXOp.im_func.func_doc = """AddRotateYZXOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a rotation op with YZX rotation order to the local stack
represented by this xformable.


Set the angle values of the resulting UsdGeomXformOp B{in degrees}

AddXformOp() , note on angle packing order

"""
   result["Xformable"].AddRotateXYZOp.im_func.func_doc = """AddRotateXYZOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a rotation op with XYZ rotation order to the local stack
represented by this xformable.


Set the angle value of the resulting UsdGeomXformOp B{in degrees}

AddXformOp() , note on angle packing order

"""
   result["Xformable"].IsTransformationAffectedByAttrNamed.func_doc = """**static** IsTransformationAffectedByAttrNamed(attrName) -> USDGEOM_API bool

attrName : TfToken


Returns true if the attribute named C{attrName} could affect the local
transformation of an xformable prim.

"""
   result["Xformable"].AddRotateZXYOp.im_func.func_doc = """AddRotateZXYOp(precision, opSuffix, isInverseOp) -> USDGEOM_API UsdGeomXformOp

precision : XformOp.Precision
opSuffix : TfToken
isInverseOp : bool


Add a rotation op with ZXY rotation order to the local stack
represented by this xformable.


Set the angle values of the resulting UsdGeomXformOp B{in degrees}

AddXformOp() , note on angle packing order

"""
   result["Xformable"].CreateXformOpOrderAttr.im_func.func_doc = """CreateXformOpOrderAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetXformOpOrderAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Xformable"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Xformable"].GetTimeSamplesInInterval.im_func.func_doc = """**static** GetTimeSamplesInInterval(interval, times) -> USDGEOM_API bool

interval : GfInterval
times : sequence<double>


Sets C{times} to the union of all the timesamples in the interval,
C{interval}, at which xformOps that are included in the xformOpOrder
attribute are authored.


This clears the C{times} vector before accumulating sample times from
all the xformOps.

UsdAttribute::GetTimeSamples


----------------------------------------------------------------------
GetTimeSamplesInInterval(orderedXformOps, interval, times) -> USDGEOM_API bool

orderedXformOps : sequence< UsdGeomXformOp >
interval : GfInterval
times : sequence<double>


Returns the union of all the timesamples in the C{interval} at which
the attributes belonging to the given C{orderedXformOps} are authored.


This clears the C{times} vector before accumulating sample times from
C{orderedXformOps}.

UsdGeomXformable::GetTimeSamplesInInterval

"""
   result["ConstraintTarget"].__doc__ = """
Schema wrapper for UsdAttribute for authoring and introspecting
attributes that are constraint targets.


Constraint targets correspond roughly to what some DCC's call
locators. They are coordinate frames, represented as (animated or
static) GfMatrix4d values. We represent them as attributes in USD
rather than transformable prims because generally we require no other
coordinated information about a constraint target other than its name
and its matrix value, and because attributes are more concise than
prims.

Because consumer clients often care only about the identity and value
of constraint targets and may be able to usefully consume them without
caring about the actual geometry with which they may logically
correspond, UsdGeom aggregates all constraint targets onto a model's
root prim, assuming that an exporter will use property namespacing
within the constraint target attribute's name to indicate a path to a
prim within the model with which the constraint target may correspond.

To facilitate instancing, and also position-tweaking of baked assets,
we stipulate that constraint target values always be recorded in B
{model-relative transformation space}. In other words, to get the
world-space value of a constraint target, transform it by the local-
to-world transformation of the prim on which it is recorded.
ComputeInWorldSpace() will perform this calculation.

"""
   result["ConstraintTarget"].Set.im_func.func_doc = """Set(value, time) -> USDGEOM_API bool

value : GfMatrix4d
time : UsdTimeCode


Set the attribute value of the ConstraintTarget at C{time}.

"""
   result["ConstraintTarget"].Get.im_func.func_doc = """Get(value, time) -> USDGEOM_API bool

value : GfMatrix4d
time : UsdTimeCode


Get the attribute value of the ConstraintTarget at C{time}.

"""
   result["ConstraintTarget"].IsValid.im_func.func_doc = """**static** IsValid(attr) -> USDGEOM_API bool

attr : UsdAttribute


Test whether a given UsdAttribute represents valid ConstraintTarget,
which implies that creating a UsdGeomConstraintTarget from the
attribute will succeed.


Success implies that C{attr.IsDefined()} is true.

"""
   result["ConstraintTarget"].IsDefined.im_func.func_doc = """IsDefined() -> bool



Return true if the wrapped UsdAttribute::IsDefined() , and in addition
the attribute is identified as a ConstraintTarget.

"""
   result["ConstraintTarget"].GetConstraintAttrName.func_doc = """**static** GetConstraintAttrName(constraintName) -> USDGEOM_API TfToken

constraintName : string


Returns the fully namespaced constraint attribute name, given the
constraint name.

"""
   result["ConstraintTarget"].GetAttr.im_func.func_doc = """GetAttr() -> UsdAttribute



Explicit UsdAttribute extractor.

"""
   result["ConstraintTarget"].ComputeInWorldSpace.im_func.func_doc = """ComputeInWorldSpace(time, xfCache) -> USDGEOM_API GfMatrix4d

time : UsdTimeCode
xfCache : XformCache


Computes the value of the constraint target in world space.


If a valid UsdGeomXformCache is provided in the argument C{xfCache},
it is used to evaluate the CTM of the model to which the constraint
target belongs.

To get the constraint value in model-space (or local space), simply
use UsdGeomConstraintTarget::Get() , since the authored values must
already be in model-space.

"""
   result["ConstraintTarget"].__init__.im_func.func_doc = """__init__()



----------------------------------------------------------------------
__init__(attr) -> USDGEOM_API

attr : UsdAttribute


Speculative constructor that will produce a valid
UsdGeomConstraintTarget when C{attr} already represents an attribute
that is a UsdGeomConstraintTarget, and produces an *invalid*
UsdGeomConstraintTarget otherwise (i.e.


unspecified-bool-type() will return false).

Calling C{UsdGeomConstraintTarget::IsValid(attr)} will return the same
truth value as the object returned by this constructor, but if you
plan to subsequently use the ConstraintTarget anyways, just construct
the object and bool-evaluate it before proceeding.

"""
   result["ConstraintTarget"].GetIdentifier.im_func.func_doc = """GetIdentifier() -> USDGEOM_API TfToken



Get the stored identifier unique to the enclosing model's namespace
for this constraint target.



SetIdentifier()

"""
   result["ConstraintTarget"].SetIdentifier.im_func.func_doc = """SetIdentifier(identifier) -> USDGEOM_API void

identifier : TfToken


Explicitly sets the stored identifier to the given string.


Clients are responsible for ensuring the uniqueness of this identifier
within the enclosing model's namespace.

"""
   result["BBoxCache"].__doc__ = """
Caches bounds by recursively computing and aggregating bounds of
children in world space and aggregating the result back into local
space.


The cache is configured for a specific time and
UsdGeomImageable::GetPurposeAttr() set of purposes. When querying a
bound, transforms and extents are read either from the time specified
or UsdTimeCode::Default() , following TimeSamples, Defaults, and Value
Resolution standard time-sample value resolution. As noted in
SetIncludedPurposes() , changing the included purposes does not
invalidate the cache, because we cache purpose along with the
geometric data.

Child prims that are invisible at the requested time are excluded when
computing a prim's bounds. However, if a bound is requested directly
for an excluded prim, it will be computed. Additionally, only prims
deriving from UsdGeomImageable are included in child bounds
computations.

Unlike standard UsdStage traversals, the traversal performed by the
UsdGeomBBoxCache includes prims that are unloaded (see
UsdPrim::IsLoaded() ). This makes it possible to fetch bounds for a
UsdStage that has been opened without *forcePopulate*, provided the
unloaded model prims have authored extent hints (see
UsdGeomModelAPI::GetExtentsHint() ).

This class is optimized for computing tight B{untransformed "object"
space} bounds for component-models. In the absence of component
models, bounds are optimized for world-space, since there is no other
easily identifiable space for which to optimize, and we cannot
optimize for every prim's local space without performing quadratic
work.

The TfDebug flag, USDGEOM_BBOX, is provided for debugging.

Warnings:
   - This class should only be used with valid UsdPrim objects.

   - This cache does not listen for change notifications; the user is
     responsible for clearing the cache when changes occur.

   - Thread safety: instances of this class may not be used
     concurrently.

   - Plugins may be loaded in order to compute extents for prim types
     provided by that plugin. See
     UsdGeomBoundable::ComputeExtentFromPlugins


"""
   result["BBoxCache"].ComputePointInstanceLocalBound.im_func.func_doc = """ComputePointInstanceLocalBound(instancer, instanceId) -> GfBBox3d

instancer : PointInstancer
instanceId : int64_t


Compute the oriented bounding boxes of the given point instances.

"""
   result["BBoxCache"].__init__.im_func.func_doc = """__init__(time, includedPurposes, useExtentsHint) -> USDGEOM_API

time : UsdTimeCode
includedPurposes : TfTokenVector
useExtentsHint : bool


Construct a new BBoxCache for a specific C{time} and set of
C{includedPurposes}.


Only prims with a purpose that matches the C{includedPurposes} will be
considered when accumulating child bounds. See UsdGeomImageable for
allowed purpose values.

If C{useExtentsHint} is true, then when computing the bounds for any
model-root prim, if the prim is visible at C{time}, we will fetch its
extents hint (via UsdGeomModelAPI::GetExtentsHint() ). If it is
authored, we use it to compute the bounding box for the selected
combination of includedPurposes by combining bounding box hints that
have been cached for various values of purposes.


----------------------------------------------------------------------
__init__(other) -> USDGEOM_API

other : BBoxCache


Copy constructor.

"""
   result["BBoxCache"].ComputeUntransformedBound.im_func.func_doc = """ComputeUntransformedBound(prim) -> USDGEOM_API GfBBox3d

prim : UsdPrim


Computes the bound of the prim's children leveraging any pre-existing,
cached bounds, but does not include the transform (if any) authored on
the prim itself.


B{IMPORTANT:} while the BBox does not contain the local
transformation, in general it may still contain a non-identity
transformation matrix to put the bounds in the correct space.
Therefore, to obtain the correct axis-aligned bounding box, the client
must call ComputeAlignedRange().

See ComputeWorldBound() for notes on performance and error handling.


----------------------------------------------------------------------
ComputeUntransformedBound(prim, pathsToSkip, ctmOverrides) -> USDGEOM_API GfBBox3d

prim : UsdPrim
pathsToSkip : SdfPathSet
ctmOverrides : TfHashMap < SdfPath , GfMatrix4d , SdfPath.Hash >


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the bound of the prim's descendents while excluding the
subtrees rooted at the paths in C{pathsToSkip}.


Additionally, the parameter C{ctmOverrides} is used to specify
overrides to the CTM values of certain paths underneath the prim. The
CTM values in the C{ctmOverrides} map are in the space of the given
prim, C{prim}.

This leverages any pre-existing, cached bounds, but does not include
the transform (if any) authored on the prim itself.

B{IMPORTANT:} while the BBox does not contain the local
transformation, in general it may still contain a non-identity
transformation matrix to put the bounds in the correct space.
Therefore, to obtain the correct axis-aligned bounding box, the client
must call ComputeAlignedRange().

See ComputeWorldBound() for notes on performance and error handling.

"""
   result["BBoxCache"].GetUseExtentsHint.im_func.func_doc = """GetUseExtentsHint() -> bool



Returns whether authored extent hints are used to compute bounding
boxes.

"""
   result["BBoxCache"].ComputePointInstanceRelativeBound.im_func.func_doc = """ComputePointInstanceRelativeBound(instancer, instanceId, relativeToAncestorPrim) -> GfBBox3d

instancer : PointInstancer
instanceId : int64_t
relativeToAncestorPrim : UsdPrim


Compute the bound of the given point instance in the space of an
ancestor prim C{relativeToAncestorPrim}.

"""
   result["BBoxCache"].GetTime.im_func.func_doc = """GetTime() -> UsdTimeCode



Get the current time from which this cache is reading values.

"""
   result["BBoxCache"].ComputeWorldBound.im_func.func_doc = """ComputeWorldBound(prim) -> USDGEOM_API GfBBox3d

prim : UsdPrim


Compute the bound of the given prim in world space, leveraging any
pre-existing, cached bounds.


The bound of the prim is computed, including the transform (if any)
authored on the node itself, and then transformed to world space.

Error handling note: No checking of C{prim} validity is performed. If
C{prim} is invalid, this method will abort the program; therefore it
is the client's responsibility to ensure C{prim} is valid.

"""
   result["BBoxCache"].ComputePointInstanceWorldBounds.im_func.func_doc = """ComputePointInstanceWorldBounds(instancer, instanceIdBegin, numIds, result) -> USDGEOM_API bool

instancer : PointInstancer
instanceIdBegin : int64_t
numIds : size_t
result : GfBBox3d


Compute the bound of the given point instances in world space.


The bounds of each instance is computed and then transformed to world
space. The C{result} pointer must point to C{numIds} GfBBox3d
instances to be filled.

"""
   result["BBoxCache"].ComputePointInstanceRelativeBounds.im_func.func_doc = """ComputePointInstanceRelativeBounds(instancer, instanceIdBegin, numIds, relativeToAncestorPrim, result) -> USDGEOM_API bool

instancer : PointInstancer
instanceIdBegin : int64_t
numIds : size_t
relativeToAncestorPrim : UsdPrim
result : GfBBox3d


Compute the bounds of the given point instances in the space of an
ancestor prim C{relativeToAncestorPrim}.


Write the results to C{result}.

The computed bound excludes the local transform at
C{relativeToAncestorPrim}. The computed bound may be incorrect if
C{relativeToAncestorPrim} is not an ancestor of C{prim}.

The C{result} pointer must point to C{numIds} GfBBox3d instances to be
filled.

"""
   result["BBoxCache"].SetBaseTime.im_func.func_doc = """SetBaseTime(baseTime)

baseTime : UsdTimeCode


Set the base time value for this bbox cache.


This value is used only when computing bboxes for point instancer
instances (see ComputePointInstanceWorldBounds() , for example). See
UsdGeomPointInstancer::ComputeExtentAtTime() for more information. If
unset, the bbox cache uses its time ( GetTime() / SetTime() ) for this
value.

Note that setting the base time does not invalidate any cache entries.

"""
   result["BBoxCache"].Clear.im_func.func_doc = """Clear() -> USDGEOM_API void



Clears all pre-cached values.

"""
   result["BBoxCache"].GetIncludedPurposes.im_func.func_doc = """GetIncludedPurposes() -> TfTokenVector



Get the current set of included purposes.

"""
   result["BBoxCache"].SetIncludedPurposes.im_func.func_doc = """SetIncludedPurposes(includedPurposes) -> USDGEOM_API void

includedPurposes : TfTokenVector


Indicate the set of C{includedPurposes} to use when resolving child
bounds.


Each child's purpose must match one of the elements of this set to be
included in the computation; if it does not, child is excluded.

Note the use of *child* in the docs above, purpose is ignored for the
prim for whose bounds are directly queried.

Changing this value B{does not invalidate existing caches}.

"""
   result["BBoxCache"].ComputePointInstanceUntransformedBound.im_func.func_doc = """ComputePointInstanceUntransformedBound(instancer, instanceId) -> GfBBox3d

instancer : PointInstancer
instanceId : int64_t


Computes the bound of the given point instances, but does not include
the instancer's transform.

"""
   result["BBoxCache"].ComputePointInstanceUntransformedBounds.im_func.func_doc = """ComputePointInstanceUntransformedBounds(instancer, instanceIdBegin, numIds, result) -> USDGEOM_API bool

instancer : PointInstancer
instanceIdBegin : int64_t
numIds : size_t
result : GfBBox3d


Computes the bound of the given point instances, but does not include
the transform (if any) authored on the instancer itself.


B{IMPORTANT:} while the BBox does not contain the local
transformation, in general it may still contain a non-identity
transformation matrix to put the bounds in the correct space.
Therefore, to obtain the correct axis-aligned bounding box, the client
must call ComputeAlignedRange().

The C{result} pointer must point to C{numIds} GfBBox3d instances to be
filled.

"""
   result["BBoxCache"].ClearBaseTime.im_func.func_doc = """ClearBaseTime()



Clear this cache's baseTime if one has been set.


After calling this, the cache will use its time as the baseTime value.

"""
   result["BBoxCache"].GetBaseTime.im_func.func_doc = """GetBaseTime() -> UsdTimeCode



Return the base time if set, otherwise GetTime() .


Use HasBaseTime() to observe if a base time has been set.

"""
   result["BBoxCache"].ComputeLocalBound.im_func.func_doc = """ComputeLocalBound(prim) -> USDGEOM_API GfBBox3d

prim : UsdPrim


Computes the oriented bounding box of the given prim, leveraging any
pre-existing, cached bounds.


The computed bound includes the transform authored on the prim itself,
but does not include any ancestor transforms (it does not include the
local-to-world transform).

See ComputeWorldBound() for notes on performance and error handling.

"""
   result["BBoxCache"].ComputeRelativeBound.im_func.func_doc = """ComputeRelativeBound(prim, relativeToAncestorPrim) -> USDGEOM_API GfBBox3d

prim : UsdPrim
relativeToAncestorPrim : UsdPrim


Compute the bound of the given prim in the space of an ancestor prim,
C{relativeToAncestorPrim}, leveraging any pre-existing cached bounds.


The computed bound excludes the local transform at
C{relativeToAncestorPrim}. The computed bound may be incorrect if
C{relativeToAncestorPrim} is not an ancestor of C{prim}.

"""
   result["BBoxCache"].ComputePointInstanceWorldBound.im_func.func_doc = """ComputePointInstanceWorldBound(instancer, instanceId) -> GfBBox3d

instancer : PointInstancer
instanceId : int64_t


Compute the bound of the given point instance in world space.

"""
   result["BBoxCache"].HasBaseTime.im_func.func_doc = """HasBaseTime() -> bool



Return true if this cache has a baseTime that's been explicitly set,
false otherwise.

"""
   result["BBoxCache"].SetTime.im_func.func_doc = """SetTime(time) -> USDGEOM_API void

time : UsdTimeCode


Use the new C{time} when computing values and may clear any existing
values cached for the previous time.


Setting C{time} to the current time is a no-op.

"""
   result["BBoxCache"].ComputePointInstanceLocalBounds.im_func.func_doc = """ComputePointInstanceLocalBounds(instancer, instanceIdBegin, numIds, result) -> USDGEOM_API bool

instancer : PointInstancer
instanceIdBegin : int64_t
numIds : size_t
result : GfBBox3d


Compute the oriented bounding boxes of the given point instances.


The computed bounds include the transform authored on the instancer
itself, but does not include any ancestor transforms (it does not
include the local-to-world transform).

The C{result} pointer must point to C{numIds} GfBBox3d instances to be
filled.

"""
   result["PointBased"].__doc__ = """
Base class for all UsdGeomGprims that possess points, providing common
attributes such as normals and velocities.

"""
   result["PointBased"].GetNormalsAttr.im_func.func_doc = """GetNormalsAttr() -> USDGEOM_API UsdAttribute



Provide an object-space orientation for individual points, which,
depending on subclass, may define a surface, curve, or free points.


Note that 'normals' should not be authored on any Mesh that is
subdivided, since the subdivision algorithm will define its own
normals. 'normals' is not a generic primvar, but the number of
elements in this attribute will be determined by its 'interpolation'.
See SetNormalsInterpolation() . If 'normals' and 'primvars:normals'
are both specified, the latter has precedence.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Normal3fArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointBased"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomPointBased

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomPointBased holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomPointBased(stage->GetPrimAtPath(path));


"""
   result["PointBased"].GetVelocitiesAttr.im_func.func_doc = """GetVelocitiesAttr() -> USDGEOM_API UsdAttribute



If provided, 'velocities' should be used by renderers to.


compute positions between samples for the 'points' attribute, rather
than interpolating between neighboring 'points' samples. This is the
only reasonable means of computing motion blur for topologically
varying PointBased primitives. It follows that the length of each
'velocities' sample must match the length of the corresponding
'points' sample. Velocity is measured in position units per second, as
per most simulation software. To convert to position units per
UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond() .

See also Applying Timesampled Velocities to Geometry.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Vector3fArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointBased"].CreateNormalsAttr.im_func.func_doc = """CreateNormalsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetNormalsAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointBased"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomPointBased on UsdPrim C{prim}.


Equivalent to UsdGeomPointBased::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomPointBased on the prim held by C{schemaObj}.


Should be preferred over UsdGeomPointBased (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["PointBased"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["PointBased"].GetNormalsInterpolation.im_func.func_doc = """GetNormalsInterpolation() -> USDGEOM_API TfToken



Get the interpolation for the *normals* attribute.


Although 'normals' is not classified as a generic UsdGeomPrimvar (and
will not be included in the results of UsdGeomImageable::GetPrimvars()
) it does require an interpolation specification. The fallback
interpolation, if left unspecified, is UsdGeomTokens->vertex, which
will generally produce smooth shading on a polygonal mesh. To achieve
partial or fully faceted shading of a polygonal mesh with normals, one
should use UsdGeomTokens->faceVarying or UsdGeomTokens->uniform
interpolation.

"""
   result["PointBased"].CreateVelocitiesAttr.im_func.func_doc = """CreateVelocitiesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVelocitiesAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointBased"].SetNormalsInterpolation.im_func.func_doc = """SetNormalsInterpolation(interpolation) -> USDGEOM_API bool

interpolation : TfToken


Set the interpolation for the *normals* attribute.



true upon success, false if C{interpolation} is not a legal value as
defined by UsdGeomPrimvar::IsValidInterpolation() , or if there was a
problem setting the value. No attempt is made to validate that the
normals attr's value contains the right number of elements to match
its interpolation to its prim's topology.

GetNormalsInterpolation()

"""
   result["PointBased"].GetPointsAttr.im_func.func_doc = """GetPointsAttr() -> USDGEOM_API UsdAttribute



The primary geometry attribute for all PointBased primitives,
describes points in (local) space.


C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Point3fArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointBased"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PointBased"].CreatePointsAttr.im_func.func_doc = """CreatePointsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetPointsAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointBased"].ComputeExtent.func_doc = """**static** ComputeExtent(points, extent) -> USDGEOM_API bool

points : VtVec3fArray
extent : VtVec3fArray


Compute the extent for the point cloud defined by points.



true on success, false if extents was unable to be calculated. On
success, extent will contain the axis-aligned bounding box of the
point cloud defined by points.

This function is to provide easy authoring of extent for usd authoring
tools, hence it is static and acts outside a specific prim (as in
attribute based methods).


----------------------------------------------------------------------
ComputeExtent(points, transform, extent) -> USDGEOM_API bool

points : VtVec3fArray
transform : GfMatrix4d
extent : VtVec3fArray


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the extent as if the matrix C{transform} was first applied.

"""
   result["XformCache"].__doc__ = """
A caching mechanism for transform matrices.


For best performance, this object should be reused for multiple CTM
queries.

Instances of this type can be copied, though using Swap() may result
in better performance.

It is valid to cache prims from multiple stages in a single
XformCache.

WARNING: this class does not automatically invalidate cached values
based on changes to the stage from which values were cached.
Additionally, a separate instance of this class should be used per-
thread, calling the Get* methods from multiple threads is not safe, as
they mutate internal state.

"""
   result["XformCache"].GetParentToWorldTransform.im_func.func_doc = """GetParentToWorldTransform(prim) -> USDGEOM_API GfMatrix4d

prim : UsdPrim


Compute the transformation matrix for the given C{prim}, but do NOT
include the transform authored on the prim itself.



This method may mutate internal cache state and is not thread safe.

"""
   result["XformCache"].GetTime.im_func.func_doc = """GetTime() -> UsdTimeCode



Get the current time from which this cache is reading values.

"""
   result["XformCache"].Swap.im_func.func_doc = """Swap(other) -> USDGEOM_API void

other : XformCache


Swap the contents of this XformCache with C{other}.

"""
   result["XformCache"].Clear.im_func.func_doc = """Clear() -> USDGEOM_API void



Clears all pre-cached values.

"""
   result["XformCache"].ComputeRelativeTransform.im_func.func_doc = """ComputeRelativeTransform(prim, ancestor, resetXformStack) -> USDGEOM_API GfMatrix4d

prim : UsdPrim
ancestor : UsdPrim
resetXformStack : bool


Returns the result of concatenating all transforms beneath C{ancestor}
that affect C{prim}.


This includes the local transform of C{prim} itself, but not the local
transform of C{ancestor}. If C{ancestor} is not an ancestor of
C{prim}, the resulting transform is the local-to-world transformation
of C{prim}.  The C{resetXformTsack} pointer must be valid. If any
intermediate prims reset the transform stack, C{resetXformStack} will
be set to true. Intermediate transforms are cached, but the result of
this call itself is not cached.

"""
   result["XformCache"].GetLocalTransformation.im_func.func_doc = """GetLocalTransformation(prim, resetsXformStack) -> USDGEOM_API GfMatrix4d

prim : UsdPrim
resetsXformStack : bool


Returns the local transformation of the prim.


Uses the cached XformQuery to compute the result quickly. The
C{resetsXformStack} pointer must be valid. It will be set to true if
C{prim} resets the transform stack. The result of this call is cached.

"""
   result["XformCache"].SetTime.im_func.func_doc = """SetTime(time) -> USDGEOM_API void

time : UsdTimeCode


Use the new C{time} when computing values and may clear any existing
values cached for the previous time.


Setting C{time} to the current time is a no-op.

"""
   result["XformCache"].__init__.im_func.func_doc = """__init__(time) -> USDGEOM_API

time : UsdTimeCode


Construct a new XformCache for the specified C{time}.


----------------------------------------------------------------------
__init__() -> USDGEOM_API



Construct a new XformCache for UsdTimeCode::Default() .

"""
   result["XformCache"].GetLocalToWorldTransform.im_func.func_doc = """GetLocalToWorldTransform(prim) -> USDGEOM_API GfMatrix4d

prim : UsdPrim


Compute the transformation matrix for the given C{prim}, including the
transform authored on the Prim itself, if present.



This method may mutate internal cache state and is not thread safe.

"""
   result["Cube"].__doc__ = """
Defines a primitive rectilinear cube centered at the origin.


The fallback values for Cube, Sphere, Cone, and Cylinder are set so
that they all pack into the same volume/bounds.

"""
   result["Cube"].CreateSizeAttr.im_func.func_doc = """CreateSizeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSizeAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cube"].GetExtentAttr.im_func.func_doc = """GetExtentAttr() -> USDGEOM_API UsdAttribute



Extent is re-defined on Cube only to provide a fallback value.



UsdGeomGprim::GetExtentAttr() .  C++ Type: VtArray<GfVec3f>  Usd Type:
SdfValueTypeNames->Float3Array  Variability: SdfVariabilityVarying
Fallback Value: [(-1, -1, -1), (1, 1, 1)]

"""
   result["Cube"].CreateExtentAttr.im_func.func_doc = """CreateExtentAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetExtentAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cube"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomCube

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomCube holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomCube(stage->GetPrimAtPath(path));


"""
   result["Cube"].GetSizeAttr.im_func.func_doc = """GetSizeAttr() -> USDGEOM_API UsdAttribute



Indicates the length of each edge of the cube.


If you author *size* you must also author *extent*.

GetExtentAttr()  C++ Type: double  Usd Type: SdfValueTypeNames->Double
Variability: SdfVariabilityVarying  Fallback Value: 2.0

"""
   result["Cube"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Cube"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Cube"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomCube on UsdPrim C{prim}.


Equivalent to UsdGeomCube::Get (prim.GetStage(), prim.GetPath()) for a
*valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomCube on the prim held by C{schemaObj}.


Should be preferred over UsdGeomCube (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Cube"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomCube

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Cylinder"].__doc__ = """
Defines a primitive cylinder with closed ends, centered at the origin,
whose spine is along the specified *axis*.


The fallback values for Cube, Sphere, Cone, and Cylinder are set so
that they all pack into the same volume/bounds.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdGeomTokens. So to set an attribute to the value "rightHanded",
use UsdGeomTokens->rightHanded as the value.

"""
   result["Cylinder"].CreateHeightAttr.im_func.func_doc = """CreateHeightAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHeightAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cylinder"].GetExtentAttr.im_func.func_doc = """GetExtentAttr() -> USDGEOM_API UsdAttribute



Extent is re-defined on Cylinder only to provide a fallback value.



UsdGeomGprim::GetExtentAttr() .  C++ Type: VtArray<GfVec3f>  Usd Type:
SdfValueTypeNames->Float3Array  Variability: SdfVariabilityVarying
Fallback Value: [(-1, -1, -1), (1, 1, 1)]

"""
   result["Cylinder"].CreateRadiusAttr.im_func.func_doc = """CreateRadiusAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRadiusAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cylinder"].CreateExtentAttr.im_func.func_doc = """CreateExtentAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetExtentAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cylinder"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomCylinder

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomCylinder holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomCylinder(stage->GetPrimAtPath(path));


"""
   result["Cylinder"].CreateAxisAttr.im_func.func_doc = """CreateAxisAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAxisAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cylinder"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Cylinder"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomCylinder on UsdPrim C{prim}.


Equivalent to UsdGeomCylinder::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomCylinder on the prim held by C{schemaObj}.


Should be preferred over UsdGeomCylinder (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Cylinder"].GetRadiusAttr.im_func.func_doc = """GetRadiusAttr() -> USDGEOM_API UsdAttribute



The radius of the cylinder.


If you author *radius* you must also author *extent*.

GetExtentAttr()  C++ Type: double  Usd Type: SdfValueTypeNames->Double
Variability: SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["Cylinder"].GetAxisAttr.im_func.func_doc = """GetAxisAttr() -> USDGEOM_API UsdAttribute



The axis along which the spine of the cylinder is aligned.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: Z  Allowed Values : [X, Y, Z]

"""
   result["Cylinder"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomCylinder

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Cylinder"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Cylinder"].GetHeightAttr.im_func.func_doc = """GetHeightAttr() -> USDGEOM_API UsdAttribute



The size of the cylinder's spine along the specified *axis*.


If you author *height* you must also author *extent*.

GetExtentAttr()  C++ Type: double  Usd Type: SdfValueTypeNames->Double
Variability: SdfVariabilityVarying  Fallback Value: 2.0

"""
   result["Scope"].__doc__ = """
Scope is the simplest grouping primitive, and does not carry the
baggage of transformability.


Note that transforms should inherit down through a Scope successfully
- it is just a guaranteed no-op from a transformability perspective.

"""
   result["Scope"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomScope on UsdPrim C{prim}.


Equivalent to UsdGeomScope::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomScope on the prim held by C{schemaObj}.


Should be preferred over UsdGeomScope (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Scope"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomScope

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomScope holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomScope(stage->GetPrimAtPath(path));


"""
   result["Scope"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Scope"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Scope"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomScope

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Gprim"].__doc__ = """
Base class for all geometric primitives.


Gprim encodes basic graphical properties such as *doubleSided* and
*orientation*, and provides primvars for "display color" and
"displayopacity" that travel with geometry to be used as shader
overrides.  For any described attribute *Fallback* *Value* or
*Allowed* *Values* below that are text/tokens, the actual token is
published and defined in UsdGeomTokens. So to set an attribute to the
value "rightHanded", use UsdGeomTokens->rightHanded as the value.

"""
   result["Gprim"].GetDisplayOpacityAttr.im_func.func_doc = """GetDisplayOpacityAttr() -> USDGEOM_API UsdAttribute



Companion to *displayColor* that specifies opacity, broken out as an
independent attribute rather than an rgba color, both so that each can
be independently overridden, and because shaders rarely consume rgba
parameters.


C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Gprim"].CreateDisplayColorPrimvar.im_func.func_doc = """CreateDisplayColorPrimvar(interpolation, elementSize) -> USDGEOM_API UsdGeomPrimvar

interpolation : TfToken
elementSize : int


Convenience function to create the displayColor primvar, optionally
specifying interpolation and elementSize.



CreateDisplayColorAttr() , GetDisplayColorPrimvar()

"""
   result["Gprim"].CreateDisplayOpacityAttr.im_func.func_doc = """CreateDisplayOpacityAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDisplayOpacityAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Gprim"].GetDisplayColorAttr.im_func.func_doc = """GetDisplayColorAttr() -> USDGEOM_API UsdAttribute



It is useful to have an "official" colorSet that can be used as a
display or modeling color, even in the absence of any specified shader
for a gprim.


DisplayColor serves this role; because it is a UsdGeomPrimvar, it can
also be used as a gprim override for any shader that consumes a
*displayColor* parameter.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Color3fArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Gprim"].GetDoubleSidedAttr.im_func.func_doc = """GetDoubleSidedAttr() -> USDGEOM_API UsdAttribute



Although some renderers treat all parametric or polygonal surfaces as
if they were effectively laminae with outward-facing normals on both
sides, some renderers derive significant optimizations by considering
these surfaces to have only a single outward side, typically
determined by control-point winding order and/or *orientation*.


By doing so they can perform "backface culling" to avoid drawing the
many polygons of most closed surfaces that face away from the viewer.

However, it is often advantageous to model thin objects such as paper
and cloth as single, open surfaces that must be viewable from both
sides, always. Setting a gprim's *doubleSided* attribute to C{true}
instructs all renderers to disable optimizations such as backface
culling for the gprim, and attempt (not all renderers are able to do
so, but the USD reference GL renderer always will) to provide forward-
facing normals on each side of the surface for lighting calculations.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityUniform  Fallback Value: False

"""
   result["Gprim"].CreateDisplayColorAttr.im_func.func_doc = """CreateDisplayColorAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDisplayColorAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Gprim"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomGprim on UsdPrim C{prim}.


Equivalent to UsdGeomGprim::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomGprim on the prim held by C{schemaObj}.


Should be preferred over UsdGeomGprim (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Gprim"].GetDisplayColorPrimvar.im_func.func_doc = """GetDisplayColorPrimvar() -> USDGEOM_API UsdGeomPrimvar



Convenience function to get the displayColor Attribute as a Primvar.



GetDisplayColorAttr() , CreateDisplayColorPrimvar()

"""
   result["Gprim"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomGprim

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomGprim holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomGprim(stage->GetPrimAtPath(path));


"""
   result["Gprim"].CreateDoubleSidedAttr.im_func.func_doc = """CreateDoubleSidedAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDoubleSidedAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Gprim"].CreateDisplayOpacityPrimvar.im_func.func_doc = """CreateDisplayOpacityPrimvar(interpolation, elementSize) -> USDGEOM_API UsdGeomPrimvar

interpolation : TfToken
elementSize : int


Convenience function to create the displayOpacity primvar, optionally
specifying interpolation and elementSize.



CreateDisplayOpacityAttr() , GetDisplayOpacityPrimvar()

"""
   result["Gprim"].GetDisplayOpacityPrimvar.im_func.func_doc = """GetDisplayOpacityPrimvar() -> USDGEOM_API UsdGeomPrimvar



Convenience function to get the displayOpacity Attribute as a Primvar.



GetDisplayOpacityAttr() , CreateDisplayOpacityPrimvar()

"""
   result["Gprim"].CreateOrientationAttr.im_func.func_doc = """CreateOrientationAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetOrientationAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Gprim"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Gprim"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Gprim"].GetOrientationAttr.im_func.func_doc = """GetOrientationAttr() -> USDGEOM_API UsdAttribute



Orientation specifies whether the gprim's surface normal should be
computed using the right hand rule, or the left hand rule.


Please see Winding Order, Orientation, and Surface Normals for a
deeper explanation and generalization of orientation to composed
scenes with transformation hierarchies.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: rightHanded  Allowed Values :
[rightHanded, leftHanded]

"""
   result["Boundable"].__doc__ = """
Boundable introduces the ability for a prim to persistently cache a
rectilinear, local-space, extent.


Why Extent and not Bounds ?
===========================

Boundable introduces the notion of "extent", which is a cached
computation of a prim's local-space 3D range for its resolved
attributes B{at the layer and time in which extent is authored}. We
have found that with composed scene description, attempting to cache
pre-computed bounds at interior prims in a scene graph is very
fragile, given the ease with which one can author a single attribute
in a stronger layer that can invalidate many authored caches - or with
which a re-published, referenced asset can do the same.

Therefore, we limit to precomputing (generally) leaf-prim extent,
which avoids the need to read in large point arrays to compute bounds,
and provides UsdGeomBBoxCache the means to efficiently compute and
(session-only) cache intermediate bounds. You are free to compute and
author intermediate bounds into your scenes, of course, which may work
well if you have sufficient locks on your pipeline to guarantee that
once authored, the geometry and transforms upon which they are based
will remain unchanged, or if accuracy of the bounds is not an ironclad
requisite.

When intermediate bounds are authored on Boundable parents, the child
prims will be pruned from BBox computation; the authored extent is
expected to incorporate all child bounds.

"""
   result["Boundable"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomBoundable on UsdPrim C{prim}.


Equivalent to UsdGeomBoundable::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomBoundable on the prim held by C{schemaObj}.


Should be preferred over UsdGeomBoundable (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Boundable"].GetExtentAttr.im_func.func_doc = """GetExtentAttr() -> USDGEOM_API UsdAttribute



Extent is a three dimensional range measuring the geometric extent of
the authored gprim in its own local space (i.e.


its own transform not applied), *without* accounting for any shader-
induced displacement. Whenever any geometry-affecting attribute is
authored for any gprim in a layer, extent must also be authored at the
same timesample; failure to do so will result in incorrect bounds-
computation.

Why Extent and not Bounds? . An authored extent on a prim which has
children is expected to include the extent of all children, as they
will be pruned from BBox computation during traversal.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Float3Array
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Boundable"].CreateExtentAttr.im_func.func_doc = """CreateExtentAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetExtentAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Boundable"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomBoundable

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomBoundable holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomBoundable(stage->GetPrimAtPath(path));


"""
   result["Boundable"].ComputeExtentFromPlugins.func_doc = """**static** ComputeExtentFromPlugins(boundable, time, extent) -> USDGEOM_API bool

boundable : Boundable
time : UsdTimeCode
extent : VtVec3fArray


Compute the extent for the Boundable prim C{boundable} at time
C{time}.


If successful, populates C{extent} with the result and returns
C{true}, otherwise returns C{false}.

The extent computation is based on the concrete type of the prim
represented by C{boundable}. Plugins that provide a Boundable prim
type may implement and register an extent computation for that type
using UsdGeomRegisterComputeExtentFunction. ComputeExtentFromPlugins
will use this function to compute extents for all prims of that type.
If no function has been registered for a prim type, but a function has
been registered for one of its base types, that function will be used
instead.

This function may load plugins in order to access the extent
computation for a prim type.


----------------------------------------------------------------------
ComputeExtentFromPlugins(boundable, time, transform, extent) -> USDGEOM_API bool

boundable : Boundable
time : UsdTimeCode
transform : GfMatrix4d
extent : VtVec3fArray


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the extent as if the matrix C{transform} was first applied.

"""
   result["Boundable"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Boundable"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["__doc__"] = """
B{UsdGeom} defines the 3D graphics-related prim and property schemas
that together form a basis for interchanging geometry between DCC
tools in a graphics pipeline.

Geometric Primitive Schemas
===========================

Currently, all classes in UsdGeom inherit from UsdGeomImageable, whose
intent is to capture any prim type that might want to be rendered or
visualized. This distinction is made for two reasons:
   - so that there *could* be types that would never want to be
     renderered, and can thus be optimized around, for traversals, and also
     to enable validation: for example, in a compatible shading schema,
     only UsdGeomImageable-derived prims should be able to express a
     look/material binding.  - for the common properties described in
     UsdGeomImageable, including visibility, purpose, and the attribute
     schema for UsdGeomPrimvar primvars.

Admittedly, not all of the classes inheriting from UsdGeomImageable
really need to be imageable - they are grouped as they are to avoid
the need for multiple-inheritance, which would arise because some
classes that may not necessarily be imageable are definitely
transformable.

In UsdGeom, all geometry prims are directly transformable. This is
primarily a scalability and complexity management decision, since
prim-count has a strong correlation to total scene composition time
and memory footprint, and eliminating the need for a "shape" node for
every piece of geometry generally reduces overall prim count by
anywhere from 30% to 50%, depending on depth and branching factor of a
scene's namespace hierarchy.

UsdGeomXformable encapsulates the schema for a prim that is
transformable. Readers familiar with AbcGeom's Xform schema will find
Xformable familiar, but more easily introspectable. Xformable
decomposes a transformation into an ordered sequence of ops; unlike
AbcGeom::Xform, which packs the op data into static and varying
arrays, UsdGeomXformable expresses each op as an independent
UsdAttribute. This data layout, while somewhat more expensive to
extract, is much more conducive to "composed scenedescription" because
it allows individual ops to be overridden in stronger layers
independently of all other ops. We provide facilities leveraging core
Usd features that help mitigate the extra cost of reading more
attributes per-prim for performance-sensitive clients.

Of course, UsdGeom still requires a prim schema that simply represents
a transformable prim that scopes other child prims, which is fulfilled
by UsdGeomXform.

You may find it useful to digest the basic assumptions of UsdGeom
linear algebra

UsdGeomGprim is the base class for all "geometric primitives", which
encodes several per-primitive graphics-related properties. Defined
Gprims currently include:
   - UsdGeomMesh

   - UsdGeomNurbsPatch

   - UsdGeomBasisCurves

   - UsdGeomNurbsCurves

   - UsdGeomPoints

   - UsdGeomCapsule

   - UsdGeomCone

   - UsdGeomCube

   - UsdGeomCylinder

   - UsdGeomSphere

We expect there to be some debate around the last five "intrinsic"
Gprims: Capsule, Cone, Cube, Cylinder, and Sphere, as not all DCC's
support them as primitives. In Pixar's pipeline, we in fact rarely
render these primitives, but find them highly useful for their fast
inside/outside tests in defining volumes for lighting effects,
procedural modifiers (such as "kill spheres" for instancers), and
colliders. The last, in particular, is quite useful for interchanging
data with rigid-body simulators. It is necessary to be able to
transmit these volumes from dressing/animation tools to
simulation/lighting/rendering tools, thus their presence in our
schema. We expect to support these and other "non-native" schema types
as some form of proxy or "pass through" prim in DCC's that do not
understand them.

UsdGeomPointInstancer provides a powerful, scalable encoding for
scattering many instances of multiple prototype objects (which can be
arbitrary subtrees of the UsdStage that contains the PointInstancer),
animating both the instances and prototypes, and pruning/masking
instances based on integer ID.

UsdGeomCamera encodes a transformable camera.

UsdGeomModelAPI is an API schema that extends the basic UsdModelAPI
API with concepts unique to models that contain 3D geometry. This
includes:
   - cached extent hints encompassing an entire model

   - API for collecting and extracting all constraint targets for a
     model from the model's root prim.

Linear Algebra in UsdGeom
=========================

To ensure reliable interchange, we stipulate the following
foundational mathematical assumptions, which are codified in the
Graphics Foundations (Gf) math module :
   - Matrices are laid out and indexed in row-major order, such that,
     given a C{GfMatrix4d} datum *mat*, *mat* [3][1] denotes the second
     column of the fourth row.

   - GfVec datatypes are row vectors that B{pre-multiply} matrices to
     effect transformations, which implies, for example, that it is the
     fourth row of a GfMatrix4d that specifies the translation of the
     transformation.

   - All rotation angles are expressed in degrees, not radians.

   - Vector cross-products and rotations intrinsically follow the
     right hand rule.
     So, for example, transforming a vector B{v} by first a Scale matrix
     B{S}, then a Rotation matrix B{R}, and finally a Translation matrix
     B{T} can be written as the following mathematical expression:

B{vt} = B{v}  B{S}  B{R}  B{T} Because Gf exposes transformation
methods on Matrices, not Vectors, to effect this transformation in
Python, one would write: ::

  vt = (S * R * T).Transform(v)

Winding Order, Orientation, and Surface Normals
===============================================

Deriving from the mathematical assumptions in the preceding section,
UsdGeom positions objects in a B{right handed coordinate system}. It
also, by default, applies the right hand rule to compute the
"intrinsic", *surface normal* (also sometimes referred to as the
*geometric normal*) for all non-implicit surface and solid types. That
is, the normal computed from (e.g.) a polygon's sequential vertices
using the right handed winding rule determines the "front" or
"outward" facing direction, that typically, when rendered will receive
lighting calculations and shading.

Since not all modeling and animation packages agree on the right hand
rule, UsdGeomGprim introduces the orientation attribute to enable
individual gprims to select the left hand winding rule, instead. So,
gprims whose *orientation* is "rightHanded" (which is the fallback)
must use the right hand rule to compute their surface normal, while
gprims whose *orientation* is "leftHanded" must use the left hand
rule.

However, any given gprim's local-to-world transformation can *flip*
its effective orientation, when it contains an odd number of negative
scales. This condition can be reliably detected using the (Jacobian)
determinant of the local-to-world transform: if the determinant is
B{less than zero}, then the gprim's orientation has been flipped, and
therefore one must apply the B{opposite} handedness rule when
computing its surface normals (or just flip the computed normals) for
the purposes of hidden surface detection and lighting calculations.

Applying Timesampled Velocities to Geometry
===========================================

UsdGeomPointBased primitives and UsdGeomPointInstancer primitives all
allow the specification of velocities to describe point (or instance)
motion at off-sample UsdTimeCode s, as an alternative to relying on
native UsdStage linear sample interpolation.  Using velocities is the
B{only reliable way} of encoding the motion of primitives whose
topology is varying over time, as adjacent samples' indices may be
unrelated to each other, and the samples themselves may not even
possesss the same number of elements.

To help ensure that all consumers of UsdGeom data will compute
identical posing from the same dataset, we describe how the position
and velocity data should be sampled and combined to produce
"interpolated" positions. There are two cases to consider, for both of
which, we stipulate the following logic:

   - If no *velocities* are authored, then we fall back to the
     "standard" position computation logic: if the timeSamples bracketing a
     requested sample have the same number of elements, apply linear
     interpolation between the two samples; otherwise, use the value of the
     sample with the lower/earlier ordinate.

   - If *velocities* are authored at a higher frequency than *points*
     (or *positions*, in the case of UsdGeomPointInstancer), fall back to
     standard position computation logic. We are effectively considering
     this a silent error condition, because we do not, at this time, want
     to require integration to compute positions.

   - Otherwise, if the bracketing timeSamples for *velocities* from
     the requested timeSample have the *same ordinates* as those for
     *points* then B{use the lower *velocities* timeSample and the lower
     *points* timeSample} for the computations described below.
     B{In summary,} we stipulate that the timeSampling of the *points* and
     *velocities* attributes be compatible. We do not allow velocities to
     be recorded at times at which there is not a corresponding *points*
     sample. This is to simplify and expedite the calculations required to
     compute a position at any requested time. Since most simulators
     produce both a position and velocity at each timeStep, we do not
     believe this restriction should impose an undue burden.

If one requires a pose at only a single point in time, *sampleTime*,
such as when stepping through "sub-frames" in an application like
*usdview*, then we need simply apply the above rules, and if we
successfully sample both *points* and *velocities*, let:

*t points* = the lower bracketing time sample for the evaluated
*points* attribute

*timeScale* = 1.0 / C{stage->GetTimeCodesPerSecond()} ... then

*B{pointsInterpolated} = B{points} + (sampleTime - t points) *
timeScale * B{velocities}*

Computer graphics renderers typically simulate the effect of non-zero
camera shutter intervals (which introduces motion blur into an image)
by sampling moving geometry at multiple, nearby sample times, for each
rendered image, linearly blending the results of each sample. Most, if
not all renderers introduce the simplifying assumption that for any
given image we wish to render, we will not allow the topology of
geometry to change over the time-range we sample for motion blur.

Therefore, if we are sampling a topologically varying,
velocities*-possessing UsdGeomMesh at sample times *t 1*, *t 2*... *t
n* in order to render the mesh with motion blur, we stipulate that all
*n* samples be computed from B{the same sampled points and velocities
values sampled at *sampleTime*}. Therefore, we would compute all *n*
samples using the above formula, but iterating over the *n* samples,
substituting *t i* for *sampleTime*.

Two things to note:

   - Since we are applying strictly linear interpolation, why is it
     useful to compute more than two samples? For UsdGeomPointBased
     primitives, the object-space samples will not require more than two
     samples, although local-to-world transformations may introduce non-
     linear motion. For UsdGeomPointInstancer primitives, which also
     possess an *angularVelocities* attribute for the instances, it may
     often be desirable to sample the instance matrices (and therefore
     *positions*) at a higher frequency since angular motion is non-linear.

   - If the range of *t 1* to *t n* is greater than the recorded
     sampling frequency of *points*, then computing the "singular" value of
     *points* at some time *t other* that is within the range *t 1* to *t
     n* may produce a different value (with differing number of elements)
     than the computed value for the same time using the motion blur
     technique. This derives from our requirement that over the given
     motion range, the topology must not change, so we specifically ignore
     any other *points* or *velocities* samples that occur in the requested
     motion range.

Stage Metrics
=============

The classes described above are concerned with individual primitives
and properties. Some geometic quantities, however, describe aspects of
an entire scene, which we encode as /stage metadata/. For example it
is UsdGeom that allows Encoding Stage UpAxis.

"""
   result["BasisCurves"].__doc__ = """
Basis curves are analagous to RiCurves.


A 'basis' matrix and *vstep* are used to uniformly interpolate the
curves. These curves are often used to render dense aggregate geometry
like hair.

A curves prim may have many curves, determined implicitly by the
length of the 'curveVertexCounts' vector. An individual curve is
composed of one or more curve segments, the smoothly interpolated part
between vertices.

Curves may have a m'type' of either linear or cubic. Linear curve
segments are interpolated between two vertices, and cubic curve
segments are interpolated between 4 vertices. The segment count of a
cubic curve  is determined by the vertex count, the 'wrap'
(periodicity), and the vstep of the basis.

cubic basis

vstep ----

bezier

3

catmullRom

1

bspline

1

hermite

2

power

4

The first segment of a cubic curve is always defined by its first 4
points. The vstep is the increment used to determine what cv
determines the next segment. For a two segment bspline basis curve
(vstep = 1), the first segment will be defined by interpolating
vertices [0, 1, 2, 3] and the second segment will be defined by [1, 2,
3, 4]. For a two segment bezier basis curve (vstep = 3), the first
segment will be defined by interpolating vertices [0, 1, 2, 3] and the
second segment will be defined by [3, 4, 5, 6]. If the vstep is not
one, then you must take special care to make sure that the number of
cvs properly divides by your vstep. If the type of a curve is linear,
the basis matrix and vstep are unused.

When validating curve topology, each entry in the curveVertexCounts
vector must pass this check.

wrap

cubic vertex count validity --------

nonperiodic

(curveVertexCounts[i] - 4) % vstep == 0

periodic

(curveVertexCounts[i]) % vstep == 0

To convert an entry in the curveVertexCounts vector into a segment
count for an individual curve, apply these rules. Sum up all the
results in order to compute how many total segments all curves have.

wrap

segment count [linear curves] -------

nonperiodic

curveVertexCounts[i] - 1

periodic

curveVertexCounts[i]

wrap

segment count [cubic curves] --------

nonperiodic

(curveVertexCounts[i] - 4) / vstep + 1

periodic

curveVertexCounts[i] / vstep

For cubic curves, primvar data can be either interpolated cubically
between vertices or linearly across segments. The corresponding token
for cubic interpolation is 'vertex' and for linear interpolation is
'varying'. Per vertex data should be the same size as the number of
vertices in your curve. Segment varying data is dependent on the wrap
(periodicity) and number of segments in your curve. For linear curves,
varying and vertex data would be interpolated the same way. By
convention varying is the preferred interpolation because of the
association of varying with linear interpolation.

wrap

expected linear (varying) data size -

nonperiodic

segmentCount + 1

periodic

segmentCount

Both curve types additionally define 'constant' interpolation for the
entire prim and 'uniform' interpolation as per curve data.

While not technically UsdGeomPrimvars, the widths and optional normals
also have interpolation metadata. It's common for authored widths to
have constant, varying, or vertex interpolation (see
UsdGeomCurves::GetWidthsInterpolation() ). It's common for authored
normals to have varying interpolation (see
UsdGeomPointBased::GetNormalsInterpolation() ).

This prim represents two different entries in the RI spec: RiBasis and
RiCurves, hence the name "BasisCurves." If we are interested in
specifying a custom basis as RenderMan allows you to do, the basis
enum could be extended with a new "custom" token and with additional
attributes vstep and matrix, but for compatability with AbcGeom and
the rarity of this use case, it is omitted for now.

Example of deriving per curve segment and varying primvar data counts
from the wrap, type, basis, and curveVertexCount.

wrap

type

basis

curveVertexCount

curveSegmentCount

varyingDataCount -----

nonperiodic

linear

N/A

[2 3 2 5]

[1 2 1 4]

[2 3 2 5]

nonperiodic

cubic

bezier

[4 7 10 4 7]

[1 2 3 1 2]

[2 3 4 2 3]

nonperiodic

cubic

bspline

[5 4 6 7]

[2 1 3 4]

[3 2 4 5]

periodic

cubic

bezier

[6 9 6]

[2 3 2]

[2 3 2]

periodic

linear

N/A

[3 7]

[3 7]

[3 7]

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdGeomTokens. So to set an attribute to the value "rightHanded",
use UsdGeomTokens->rightHanded as the value.

"""
   result["BasisCurves"].GetWrapAttr.im_func.func_doc = """GetWrapAttr() -> USDGEOM_API UsdAttribute



if wrap is set to periodic, the curve when rendered will repeat the
initial vertices (dependent on the vstep) to connect the end points.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: nonperiodic  Allowed Values :
[nonperiodic, periodic]

"""
   result["BasisCurves"].ComputeUniformDataSize.im_func.func_doc = """ComputeUniformDataSize(timeCode) -> USDGEOM_API size_t

timeCode : UsdTimeCode


Computes the expected size for data with "uniform" interpolation.


If you're trying to determine what interpolation to use, it is more
efficient to use C{ComputeInterpolationForSize}

"""
   result["BasisCurves"].CreateWrapAttr.im_func.func_doc = """CreateWrapAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetWrapAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BasisCurves"].ComputeInterpolationForSize.im_func.func_doc = """ComputeInterpolationForSize(n, timeCode, info) -> USDGEOM_API TfToken

n : size_t
timeCode : UsdTimeCode
info : ComputeInterpolationInfo


Computes interpolation token for C{n}.


If this returns an empty token and C{info} was non-None, it'll contain
the expected value for each token.

The topology is determined using C{timeCode}.

"""
   result["BasisCurves"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomBasisCurves

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomBasisCurves holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomBasisCurves(stage->GetPrimAtPath(path));


"""
   result["BasisCurves"].ComputeVaryingDataSize.im_func.func_doc = """ComputeVaryingDataSize(timeCode) -> USDGEOM_API size_t

timeCode : UsdTimeCode


Computes the expected size for data with "varying" interpolation.


If you're trying to determine what interpolation to use, it is more
efficient to use C{ComputeInterpolationForSize}

"""
   result["BasisCurves"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomBasisCurves

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["BasisCurves"].ComputeVertexDataSize.im_func.func_doc = """ComputeVertexDataSize(timeCode) -> USDGEOM_API size_t

timeCode : UsdTimeCode


Computes the expected size for data with "vertex" interpolation.


If you're trying to determine what interpolation to use, it is more
efficient to use C{ComputeInterpolationForSize}

"""
   result["BasisCurves"].CreateBasisAttr.im_func.func_doc = """CreateBasisAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetBasisAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BasisCurves"].GetTypeAttr.im_func.func_doc = """GetTypeAttr() -> USDGEOM_API UsdAttribute



Linear curves interpolate linearly between cvs.


Cubic curves use a basis matrix with 4 cvs to interpolate a segment.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: cubic  Allowed Values :
[linear, cubic]

"""
   result["BasisCurves"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomBasisCurves on UsdPrim C{prim}.


Equivalent to UsdGeomBasisCurves::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomBasisCurves on the prim held by C{schemaObj}.


Should be preferred over UsdGeomBasisCurves (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["BasisCurves"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["BasisCurves"].CreateTypeAttr.im_func.func_doc = """CreateTypeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTypeAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BasisCurves"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["BasisCurves"].GetBasisAttr.im_func.func_doc = """GetBasisAttr() -> USDGEOM_API UsdAttribute



the basis specifies the vstep and matrix used for interpolation.


a custom basis could be supported with the addition of a custom token
and an additional set of matrix/vstep parameters. For simplicity and
consistency with AbcGeom, we have omitted this. The order of basis and
default value is intentionally the same as AbcGeom.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: bezier  Allowed Values :
[bezier, bspline, catmullRom, hermite, power]

"""
   result["NurbsCurves"].__doc__ = """
This schema is analagous to NURBS Curves in packages like Maya and
Houdini, often used for interchange of rigging and modeling curves.


Unlike Maya, this curve spec supports batching of multiple curves into
a single prim, widths, and normals in the schema. Additionally, we
require 'numSegments + 2 * degree + 1' knots (2 more than maya does).
This is to be more consistent with RenderMan's NURBS patch
specification.  To express a periodic curve:
   - knot[0] = knot[1] - (knots[-2] - knots[-3];

   - knot[-1] = knot[-2] + (knot[2] - knots[1]);

To express a nonperiodic curve:
   - knot[0] = knot[1];

   - knot[-1] = knot[-2];

In spite of these slight differences in the spec, curves generated in
Maya should be preserved when roundtripping.

'order' and 'range', when representing a batched NurbsCurve should be
authored one value per curve. 'knots' should be the concatentation of
all batched curves.

"""
   result["NurbsCurves"].GetKnotsAttr.im_func.func_doc = """GetKnotsAttr() -> USDGEOM_API UsdAttribute



Knot vector providing curve parameterization.


The length of the slice of the array for the ith curve must be (
curveVertexCount[i] + order[i] ), and its entries must take on
monotonically increasing values.

C++ Type: VtArray<double>  Usd Type: SdfValueTypeNames->DoubleArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsCurves"].GetOrderAttr.im_func.func_doc = """GetOrderAttr() -> USDGEOM_API UsdAttribute



Order of the curve.


Order must be positive and is equal to the degree of the polynomial
basis to be evaluated, plus 1. Its value for the 'i'th curve must be
less than or equal to the number of cvs in the curveVertexCount[i]

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["NurbsCurves"].CreateKnotsAttr.im_func.func_doc = """CreateKnotsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetKnotsAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsCurves"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomNurbsCurves

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomNurbsCurves holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomNurbsCurves(stage->GetPrimAtPath(path));


"""
   result["NurbsCurves"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["NurbsCurves"].GetRangesAttr.im_func.func_doc = """GetRangesAttr() -> USDGEOM_API UsdAttribute



Provides the minimum and maximum parametric values (as defined by
knots) over which the curve is actually defined.


The minimum must be less than the maximum, and greater than or equal
to the value of the knots['i'th curve slice][order[i]-1]. The maxium
must be less than or equal to the last element's value in knots['i'th
curve slice]. Range maps to (vmin, vmax) in the RenderMan spec.

C++ Type: VtArray<GfVec2d>  Usd Type: SdfValueTypeNames->Double2Array
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsCurves"].CreateRangesAttr.im_func.func_doc = """CreateRangesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRangesAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsCurves"].CreateOrderAttr.im_func.func_doc = """CreateOrderAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetOrderAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsCurves"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomNurbsCurves on UsdPrim C{prim}.


Equivalent to UsdGeomNurbsCurves::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomNurbsCurves on the prim held by C{schemaObj}.


Should be preferred over UsdGeomNurbsCurves (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["NurbsCurves"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["NurbsCurves"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomNurbsCurves

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Points"].__doc__ = """
Points are analogous to the RiPoints spec.


Points can be an efficient means of storing and rendering particle
effects comprised of thousands or millions of small particles. Points
generally receive a single shading sample each, which should take
*normals* into account, if present.

While not technically UsdGeomPrimvars, the widths and normals also
have interpolation metadata. It's common for authored widths and
normals to have constant or varying interpolation.

"""
   result["Points"].ComputeExtent.func_doc = """**static** ComputeExtent(points, widths, extent) -> USDGEOM_API bool

points : VtVec3fArray
widths : VtFloatArray
extent : VtVec3fArray


Compute the extent for the point cloud defined by points and widths.



true upon success, false if widths and points are different sized
arrays. On success, extent will contain the axis-aligned bounding box
of the point cloud defined by points with the given widths.

This function is to provide easy authoring of extent for usd authoring
tools, hence it is static and acts outside a specific prim (as in
attribute based methods).


----------------------------------------------------------------------
ComputeExtent(points, widths, transform, extent) -> USDGEOM_API bool

points : VtVec3fArray
widths : VtFloatArray
transform : GfMatrix4d
extent : VtVec3fArray


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the extent as if the matrix C{transform} was first applied.

"""
   result["Points"].CreateIdsAttr.im_func.func_doc = """CreateIdsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetIdsAttr() , and also Create vs Get Property Methods for when to
use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Points"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomPoints

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomPoints holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomPoints(stage->GetPrimAtPath(path));


"""
   result["Points"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomPoints on UsdPrim C{prim}.


Equivalent to UsdGeomPoints::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomPoints on the prim held by C{schemaObj}.


Should be preferred over UsdGeomPoints (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Points"].GetIdsAttr.im_func.func_doc = """GetIdsAttr() -> USDGEOM_API UsdAttribute



Ids are optional; if authored, the ids array should be the same length
as the points array, specifying (at each timesample if point
identities are changing) the id of each point.


The type is signed intentionally, so that clients can encode some
binary state on Id'd points without adding a separate primvar.

C++ Type: VtArray<int64_t>  Usd Type: SdfValueTypeNames->Int64Array
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Points"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Points"].SetWidthsInterpolation.im_func.func_doc = """SetWidthsInterpolation(interpolation) -> USDGEOM_API bool

interpolation : TfToken


Set the interpolation for the *widths* attribute.



true upon success, false if C{interpolation} is not a legal value as
defined by UsdPrimvar::IsValidInterpolation(), or if there was a
problem setting the value. No attempt is made to validate that the
widths attr's value contains the right number of elements to match its
interpolation to its prim's topology.

GetWidthsInterpolation()

"""
   result["Points"].CreateWidthsAttr.im_func.func_doc = """CreateWidthsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetWidthsAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Points"].GetWidthsAttr.im_func.func_doc = """GetWidthsAttr() -> USDGEOM_API UsdAttribute



Widths are defined as the *diameter* of the points, in object space.


'widths' is not a generic Primvar, but the number of elements in this
attribute will be determined by its 'interpolation'. See
SetWidthsInterpolation() . If 'widths' and 'primvars:widths' are both
specified, the latter has precedence.

C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Points"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Points"].GetWidthsInterpolation.im_func.func_doc = """GetWidthsInterpolation() -> USDGEOM_API TfToken



Get the interpolation for the *widths* attribute.


Although 'widths' is not classified as a generic UsdGeomPrimvar (and
will not be included in the results of UsdGeomImageable::GetPrimvars()
) it does require an interpolation specification. The fallback
interpolation, if left unspecified, is UsdGeomTokens->vertex, which
means a width value is specified for each point.

"""
   result["Points"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomPoints

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Sphere"].__doc__ = """
Defines a primitive sphere centered at the origin.


The fallback values for Cube, Sphere, Cone, and Cylinder are set so
that they all pack into the same volume/bounds.

"""
   result["Sphere"].GetExtentAttr.im_func.func_doc = """GetExtentAttr() -> USDGEOM_API UsdAttribute



Extent is re-defined on Sphere only to provide a fallback value.



UsdGeomGprim::GetExtentAttr() .  C++ Type: VtArray<GfVec3f>  Usd Type:
SdfValueTypeNames->Float3Array  Variability: SdfVariabilityVarying
Fallback Value: [(-1, -1, -1), (1, 1, 1)]

"""
   result["Sphere"].CreateRadiusAttr.im_func.func_doc = """CreateRadiusAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRadiusAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Sphere"].CreateExtentAttr.im_func.func_doc = """CreateExtentAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetExtentAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Sphere"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomSphere

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomSphere holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomSphere(stage->GetPrimAtPath(path));


"""
   result["Sphere"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomSphere on UsdPrim C{prim}.


Equivalent to UsdGeomSphere::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomSphere on the prim held by C{schemaObj}.


Should be preferred over UsdGeomSphere (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Sphere"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Sphere"].GetRadiusAttr.im_func.func_doc = """GetRadiusAttr() -> USDGEOM_API UsdAttribute



Indicates the sphere's radius.


If you author *radius* you must also author *extent*.

GetExtentAttr()  C++ Type: double  Usd Type: SdfValueTypeNames->Double
Variability: SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["Sphere"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Sphere"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomSphere

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["SetStageUpAxis"].func_doc = """SetStageUpAxis(stage, axis) -> USDGEOM_API bool

stage : UsdStageWeakPtr
axis : TfToken


Set C{stage} 's upAxis to C{axis}, which must be one of
UsdGeomTokens->y or UsdGeomTokens->z.


UpAxis is stage-level metadata, therefore see UsdStage::SetMetadata()
.

true if upAxis was successfully set.

Encoding Stage UpAxis


----------------------------------------------------------------------
SetStageUpAxis(stage, axis) -> USDGEOM_API bool

stage : UsdStageWeakPtr
axis : TfToken


Set C{stage} 's upAxis to C{axis}, which must be one of
UsdGeomTokens->y or UsdGeomTokens->z.


UpAxis is stage-level metadata, therefore see UsdStage::SetMetadata()
.

true if upAxis was successfully set.

Encoding Stage UpAxis

"""
   result["Subset"].__doc__ = """
Encodes a subset of a piece of geometry (i.e.


a UsdGeomImageable) as a set of indices. Currently only supports
encoding of face-subsets, but could be extended in the future to
support subsets representing edges, segments, points etc.

To apply to a geometric prim, a GeomSubset prim must be defined as a
child of it in namespace. This restriction makes it easy and efficient
to discover subsets of a prim. We might want to relax this restriction
if it's common to have multiple B{families} of subsets on a gprim and
if it's useful to be able to organize subsets belonging to a family
under a common scope. See 'familyName' attribute for more info on
defining a family of subsets.

Note that a GeomSubset isn't an imageable (i.e. doesn't derive from
UsdGeomImageable). So, you can't author B{visibility} for it or
override its B{purpose}.

Materials are bound to GeomSubsets just as they are for regular
geometry using API available in UsdShade (UsdShadeMaterial::Bind).

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdGeomTokens. So to set an attribute to the value "rightHanded",
use UsdGeomTokens->rightHanded as the value.

"""
   result["Subset"].CreateElementTypeAttr.im_func.func_doc = """CreateElementTypeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetElementTypeAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Subset"].SetFamilyType.func_doc = """**static** SetFamilyType(geom, familyName, familyType) -> USDGEOM_API bool

geom : Imageable
familyName : TfToken
familyType : TfToken


This method is used to encode the type of family that the GeomSubsets
on the given geometric prim C{geom}, with the given family name,
C{familyName} belong to.


See UsdGeomSubset::GetFamilyNameAttr for the possible values for
C{familyType}.

When a family of GeomSubsets is tagged as a UsdGeomTokens->partition
or UsdGeomTokens->nonOverlapping, the validity of the data (i.e.
mutual exclusivity and/or wholeness) is not enforced by the authoring
APIs. Use ValidateFamily() to validate the data in a family of
GeomSubsets.

Returns false upon failure to create or set the appropriate attribute
on C{geom}.

"""
   result["Subset"].GetUnassignedIndices.func_doc = """**static** GetUnassignedIndices(subsets, elementCount, time) -> USDGEOM_API VtIntArray

subsets : sequence< UsdGeomSubset >
elementCount : size_t
time : UsdTimeCode


Utility for getting the list of indices that are not assigned to any
of the GeomSubsets in C{subsets} at the timeCode, C{time}, given the
element count (total number of indices in the array being subdivided),
C{elementCount}.

"""
   result["Subset"].CreateGeomSubset.func_doc = """**static** CreateGeomSubset(geom, subsetName, elementType, indices, familyName, familyType) -> USDGEOM_API UsdGeomSubset

geom : Imageable
subsetName : string
elementType : TfToken
indices : VtIntArray
familyName : TfToken
familyType : TfToken


Creates a new GeomSubset below the given C{geom} with the given name,
C{subsetName}, element type, C{elementType} and C{indices}.


If a subset named C{subsetName} already exists below C{geom}, then
this updates its attributes with the values of the provided arguments
(indices value at time 'default' will be updated) and returns it.

The family type is set / updated on C{geom} only if a non-empty value
is passed in for C{familyType} and C{familyName}.

"""
   result["Subset"].GetGeomSubsets.func_doc = """**static** GetGeomSubsets(geom, elementType, familyName) -> USDGEOM_API sequence< UsdGeomSubset >

geom : Imageable
elementType : TfToken
familyName : TfToken


Returns all the GeomSubsets of the given C{elementType} belonging to
the specified family, C{familyName} on the given imageable, C{geom}.


If C{elementType} is empty, then subsets containing all element types
are returned. If C{familyName} is left empty, then all subsets of the
specified C{elementType} will be returned.

"""
   result["Subset"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomSubset

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Subset"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomSubset

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomSubset holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomSubset(stage->GetPrimAtPath(path));


"""
   result["Subset"].ValidateFamily.func_doc = """**static** ValidateFamily(geom, elementType, familyName, reason) -> USDGEOM_API bool

geom : Imageable
elementType : TfToken
familyName : TfToken
reason : string


Validates whether the family of subsets identified by the given
C{familyName} and C{elementType} on the given imageable, C{geom}
contain valid data.


If the family is designated as a partition or as non-overlapping using
SetFamilyType() , then the validity of the data is checked. If the
familyType is "unrestricted", then this performs only bounds checking
of the values in the "indices" arrays.

If C{reason} is not None, then it is populated with a string
explaining why the family is invalid, if it is invalid.

The python version of this method returns a tuple containing a (bool,
string), where the bool has the validity of the family and the string
contains the reason (if it's invalid).

"""
   result["Subset"].GetFamilyType.func_doc = """**static** GetFamilyType(geom, familyName) -> USDGEOM_API TfToken

geom : Imageable
familyName : TfToken


Returns the type of family that the GeomSubsets on the given geometric
prim C{geom}, with the given family name, C{familyName} belong to.


This only returns the token that's encoded on C{geom} and does not
perform any actual validation on the family of GeomSubsets. Please use
ValidateFamily() for such validation.

When familyType is not set on C{geom}, the fallback value
UsdTokens->unrestricted is returned.

"""
   result["Subset"].GetAllGeomSubsets.func_doc = """**static** GetAllGeomSubsets(geom) -> USDGEOM_API sequence< UsdGeomSubset >

geom : Imageable


Returns all the GeomSubsets defined on the given imageable, C{geom}.

"""
   result["Subset"].GetAllGeomSubsetFamilyNames.func_doc = """**static** GetAllGeomSubsetFamilyNames(geom) -> USDGEOM_API TfToken.Set

geom : Imageable


Returns the names of all the families of GeomSubsets defined on the
given imageable, C{geom}.

"""
   result["Subset"].ValidateSubsets.func_doc = """**static** ValidateSubsets(subsets, elementCount, familyType, reason) -> USDGEOM_API bool

subsets : sequence< UsdGeomSubset >
elementCount : size_t
familyType : TfToken
reason : string


Validates the data in the given set of GeomSubsets, C{subsets}, given
the total number of elements in the array being subdivided,
C{elementCount} and the C{familyType} that the subsets belong to.


For proper validation of indices in C{subsets}, all of the GeomSubsets
must have the same 'elementType'.

If one or more subsets contain invalid data, then false is returned
and C{reason} is populated with a string explaining the reason why it
is invalid.

The python version of this method returns a tuple containing a (bool,
string), where the bool has the validity of the subsets and the string
contains the reason (if they're invalid).

"""
   result["Subset"].GetElementTypeAttr.im_func.func_doc = """GetElementTypeAttr() -> USDGEOM_API UsdAttribute



The type of element that the indices target.


Currently only allows "face" and defaults to it.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: face  Allowed Values : [face]

"""
   result["Subset"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Subset"].CreateFamilyNameAttr.im_func.func_doc = """CreateFamilyNameAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFamilyNameAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Subset"].CreateIndicesAttr.im_func.func_doc = """CreateIndicesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetIndicesAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Subset"].CreateUniqueGeomSubset.func_doc = """**static** CreateUniqueGeomSubset(geom, subsetName, elementType, indices, familyName, familyType) -> USDGEOM_API UsdGeomSubset

geom : Imageable
subsetName : string
elementType : TfToken
indices : VtIntArray
familyName : TfToken
familyType : TfToken


Creates a new GeomSubset below the given imageable, C{geom} with the
given name, C{subsetName}, element type, C{elementType} and
C{indices}.


If a subset named C{subsetName} already exists below C{geom}, then
this creates a new subset by appending a suitable index as suffix to
C{subsetName} (eg, subsetName_1) to avoid name collisions.

The family type is set / updated on C{geom} only if a non-empty value
is passed in for C{familyType} and C{familyName}.

"""
   result["Subset"].GetFamilyNameAttr.im_func.func_doc = """GetFamilyNameAttr() -> USDGEOM_API UsdAttribute



The name of the family of subsets that this subset belongs to.


This is optional and is primarily useful when there are multiple
families of subsets under a geometric prim. In some cases, this could
also be used for achieving proper roundtripping of subset data between
DCC apps. When multiple subsets belonging to a prim have the same
familyName, they are said to belong to the family. A *familyType*
value can be encoded on the owner of a family of subsets as a token
using the static method UsdGeomSubset::SetFamilyType() . "familyType"
can have one of the following values:
   - B{UsdGeomTokens->partition} : implies that every element of the
     whole geometry appears exactly once in only one of the subsets
     belonging to the family.

   - B{UsdGeomTokens->nonOverlapping} : an element that appears in one
     subset may not appear in any other subset belonging to the family.

   - B{UsdGeomTokens->unrestricted} : implies that there are no
     restrictions w.r.t. the membership of elements in the subsets. They
     could be overlapping and the union of all subsets in the family may
     not represent the whole.

The validity of subset data is not enforced by the authoring APIs,
however they can be checked using UsdGeomSubset::ValidateFamily() .
C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value:

"""
   result["Subset"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomSubset on UsdPrim C{prim}.


Equivalent to UsdGeomSubset::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomSubset on the prim held by C{schemaObj}.


Should be preferred over UsdGeomSubset (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Subset"].GetIndicesAttr.im_func.func_doc = """GetIndicesAttr() -> USDGEOM_API UsdAttribute



The set of indices included in this subset.


The indices need not be sorted, but the same index should not appear
more than once.

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["Subset"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["NurbsPatch"].__doc__ = """
Encodes a rational or polynomial non-uniform B-spline surface, with
optional trim curves.


The encoding mostly follows that of RiNuPatch and RiTrimCurve:
https://renderman.pixar.com/resources/current/RenderMan/geometricPrimitives.html#rinupatch,
with some minor renaming and coalescing for clarity.

The layout of control vertices in the *points* attribute inherited
from UsdGeomPointBased is row-major with U considered rows, and V
columns.

B{NurbsPatch Form}

The authored points, orders, knots, weights, and ranges are all that
is required to render the nurbs patch. However, the only way to model
closed surfaces with nurbs is to ensure that the first and last
control points along the given axis are coincident. Similarly, to
ensure the surface is not only closed but also C2 continuous, the last
*order* - 1 control points must be (correspondingly) coincident with
the first *order* - 1 control points, and also the spacing of the last
corresponding knots must be the same as the first corresponding knots.

B{Form} is provided as an aid to interchange between modeling and
animation applications so that they can robustly identify the intent
with which the surface was modelled, and take measures (if they are
able) to preserve the continuity/concidence constraints as the surface
may be rigged or deformed.
   - An *open-form* NurbsPatch has no continuity constraints.

   - A *closed-form* NurbsPatch expects the first and last control
     points to overlap

   - A *periodic-form* NurbsPatch expects the first and last *order* -
     1 control points to overlap.
     B{Nurbs vs Subdivision Surfaces}

Nurbs are an important modeling primitive in CAD/CAM tools and early
computer graphics DCC's. Because they have a natural UV
parameterization they easily support "trim curves", which allow smooth
shapes to be carved out of the surface.

However, the topology of the patch is always rectangular, and joining
two nurbs patches together (especially when they have differing
numbers of spans) is difficult to do smoothly. Also, nurbs are not
supported by the Ptex texturing technology ( http://ptex.us).

Neither of these limitations are shared by subdivision surfaces;
therefore, although they do not subscribe to trim-curve-based shaping,
subdivs are often considered a more flexible modeling primitive.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdGeomTokens. So to set an attribute to the value "rightHanded",
use UsdGeomTokens->rightHanded as the value.

"""
   result["NurbsPatch"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomNurbsPatch on UsdPrim C{prim}.


Equivalent to UsdGeomNurbsPatch::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomNurbsPatch on the prim held by C{schemaObj}.


Should be preferred over UsdGeomNurbsPatch (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["NurbsPatch"].GetUVertexCountAttr.im_func.func_doc = """GetUVertexCountAttr() -> USDGEOM_API UsdAttribute



Number of vertices in the U direction.


Should be at least as large as uOrder.

C++ Type: int  Usd Type: SdfValueTypeNames->Int  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].CreateURangeAttr.im_func.func_doc = """CreateURangeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetURangeAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateTrimCurveOrdersAttr.im_func.func_doc = """CreateTrimCurveOrdersAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTrimCurveOrdersAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].GetPointWeightsAttr.im_func.func_doc = """GetPointWeightsAttr() -> USDGEOM_API UsdAttribute



Optionally provides "w" components for each control point, thus must
be the same length as the points attribute.


If authored, the patch will be rational. If unauthored, the patch will
be polynomial, i.e. weight for all points is 1.0.

Some DCC's pre-weight the *points*, but in this schema, *points* are
not pre-weighted.  C++ Type: VtArray<double>  Usd Type:
SdfValueTypeNames->DoubleArray  Variability: SdfVariabilityVarying
Fallback Value: No Fallback

"""
   result["NurbsPatch"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["NurbsPatch"].CreateUKnotsAttr.im_func.func_doc = """CreateUKnotsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetUKnotsAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].GetVRangeAttr.im_func.func_doc = """GetVRangeAttr() -> USDGEOM_API UsdAttribute



Provides the minimum and maximum parametric values (as defined by
vKnots) over which the surface is actually defined.


The minimum must be less than the maximum, and greater than or equal
to the value of vKnots[vOrder-1]. The maxium must be less than or
equal to the last element's value in vKnots.

C++ Type: GfVec2d  Usd Type: SdfValueTypeNames->Double2  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].GetVFormAttr.im_func.func_doc = """GetVFormAttr() -> USDGEOM_API UsdAttribute



Interpret the control grid and knot vectors as representing an open,
geometrically closed, or geometrically closed and C2 continuous
surface along the V dimension.



NurbsPatch Form  C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token
Variability: SdfVariabilityUniform  Fallback Value: open  Allowed
Values : [open, closed, periodic]

"""
   result["NurbsPatch"].GetVVertexCountAttr.im_func.func_doc = """GetVVertexCountAttr() -> USDGEOM_API UsdAttribute



Number of vertices in the V direction.


Should be at least as large as vOrder.

C++ Type: int  Usd Type: SdfValueTypeNames->Int  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].GetVOrderAttr.im_func.func_doc = """GetVOrderAttr() -> USDGEOM_API UsdAttribute



Order in the V direction.


Order must be positive and is equal to the degree of the polynomial
basis to be evaluated, plus 1.

C++ Type: int  Usd Type: SdfValueTypeNames->Int  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].GetTrimCurveRangesAttr.im_func.func_doc = """GetTrimCurveRangesAttr() -> USDGEOM_API UsdAttribute



Flat list of minimum and maximum parametric values (as defined by
*knots*) for each of the *nCurves* curves.


C++ Type: VtArray<GfVec2d>  Usd Type: SdfValueTypeNames->Double2Array
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].CreateVFormAttr.im_func.func_doc = """CreateVFormAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVFormAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateVOrderAttr.im_func.func_doc = """CreateVOrderAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVOrderAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].GetUKnotsAttr.im_func.func_doc = """GetUKnotsAttr() -> USDGEOM_API UsdAttribute



Knot vector for U direction providing U parameterization.


The length of this array must be ( uVertexCount + uOrder), and its
entries must take on monotonically increasing values.

C++ Type: VtArray<double>  Usd Type: SdfValueTypeNames->DoubleArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].CreateTrimCurveKnotsAttr.im_func.func_doc = """CreateTrimCurveKnotsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTrimCurveKnotsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].GetTrimCurveVertexCountsAttr.im_func.func_doc = """GetTrimCurveVertexCountsAttr() -> USDGEOM_API UsdAttribute



Flat list of number of vertices for each of the *nCurves* curves.


C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].CreatePointWeightsAttr.im_func.func_doc = """CreatePointWeightsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetPointWeightsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateUFormAttr.im_func.func_doc = """CreateUFormAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetUFormAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateTrimCurvePointsAttr.im_func.func_doc = """CreateTrimCurvePointsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTrimCurvePointsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateVKnotsAttr.im_func.func_doc = """CreateVKnotsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVKnotsAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].GetURangeAttr.im_func.func_doc = """GetURangeAttr() -> USDGEOM_API UsdAttribute



Provides the minimum and maximum parametric values (as defined by
uKnots) over which the surface is actually defined.


The minimum must be less than the maximum, and greater than or equal
to the value of uKnots[uOrder-1]. The maxium must be less than or
equal to the last element's value in uKnots.

C++ Type: GfVec2d  Usd Type: SdfValueTypeNames->Double2  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].GetVKnotsAttr.im_func.func_doc = """GetVKnotsAttr() -> USDGEOM_API UsdAttribute



Knot vector for V direction providing U parameterization.


The length of this array must be ( vVertexCount + vOrder), and its
entries must take on monotonically increasing values.

C++ Type: VtArray<double>  Usd Type: SdfValueTypeNames->DoubleArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].GetTrimCurveCountsAttr.im_func.func_doc = """GetTrimCurveCountsAttr() -> USDGEOM_API UsdAttribute



Each element specifies how many curves are present in each "loop" of
the trimCurve, and the length of the array determines how many loops
the trimCurve contains.


The sum of all elements is the total nuber of curves in the trim, to
which we will refer as *nCurves* in describing the other trim
attributes.

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].GetTrimCurveKnotsAttr.im_func.func_doc = """GetTrimCurveKnotsAttr() -> USDGEOM_API UsdAttribute



Flat list of parametric values for each of the *nCurves* curves.


There will be as many knots as the sum over all elements of
*vertexCounts* plus the sum over all elements of *orders*.

C++ Type: VtArray<double>  Usd Type: SdfValueTypeNames->DoubleArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].CreateUVertexCountAttr.im_func.func_doc = """CreateUVertexCountAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetUVertexCountAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateTrimCurveCountsAttr.im_func.func_doc = """CreateTrimCurveCountsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTrimCurveCountsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateTrimCurveVertexCountsAttr.im_func.func_doc = """CreateTrimCurveVertexCountsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTrimCurveVertexCountsAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateTrimCurveRangesAttr.im_func.func_doc = """CreateTrimCurveRangesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTrimCurveRangesAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateUOrderAttr.im_func.func_doc = """CreateUOrderAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetUOrderAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomNurbsPatch

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomNurbsPatch holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomNurbsPatch(stage->GetPrimAtPath(path));


"""
   result["NurbsPatch"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomNurbsPatch

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["NurbsPatch"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["NurbsPatch"].GetTrimCurvePointsAttr.im_func.func_doc = """GetTrimCurvePointsAttr() -> USDGEOM_API UsdAttribute



Flat list of homogeneous 2D points (u, v, w) that comprise the
*nCurves* curves.


The number of points should be equal to the um over all elements of
*vertexCounts*.

C++ Type: VtArray<GfVec3d>  Usd Type: SdfValueTypeNames->Double3Array
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].GetUOrderAttr.im_func.func_doc = """GetUOrderAttr() -> USDGEOM_API UsdAttribute



Order in the U direction.


Order must be positive and is equal to the degree of the polynomial
basis to be evaluated, plus 1.

C++ Type: int  Usd Type: SdfValueTypeNames->Int  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].CreateVRangeAttr.im_func.func_doc = """CreateVRangeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVRangeAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].CreateVVertexCountAttr.im_func.func_doc = """CreateVVertexCountAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVVertexCountAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NurbsPatch"].GetTrimCurveOrdersAttr.im_func.func_doc = """GetTrimCurveOrdersAttr() -> USDGEOM_API UsdAttribute



Flat list of orders for each of the *nCurves* curves.


C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["NurbsPatch"].GetUFormAttr.im_func.func_doc = """GetUFormAttr() -> USDGEOM_API UsdAttribute



Interpret the control grid and knot vectors as representing an open,
geometrically closed, or geometrically closed and C2 continuous
surface along the U dimension.



NurbsPatch Form  C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token
Variability: SdfVariabilityUniform  Fallback Value: open  Allowed
Values : [open, closed, periodic]

"""
   result["Mesh"].__doc__ = """
Encodes a mesh surface whose definition and feature-set will converge
with that of OpenSubdiv,
http://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html.


Current exceptions/divergences include:

   - Certain interpolation ("tag") parameters not yet supported

   - Does not (as of 9/2014) yet support hierarchical edits. We do
     intend to provide some encoding in a future version of the schema.

A key property of this mesh schema is that it encodes both subdivision
surfaces, and non-subdived "polygonal meshes", by varying the
*subdivisionScheme* attribute.

A Note About Normals
====================

Normals should not be authored on a subdivided mesh, since subdivision
algorithms define their own normals. They should only be authored for
polygonal meshes.

The 'normals' attribute inherited from UsdGeomPointBased is not a
generic primvar, but the number of elements in this attribute will be
determined by its 'interpolation'. See
UsdGeomPointBased::GetNormalsInterpolation() . If 'normals' and
'primvars:normals' are both specified, the latter has precedence.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdGeomTokens. So to set an attribute to the value "rightHanded",
use UsdGeomTokens->rightHanded as the value.

"""
   result["Mesh"].GetCornerSharpnessesAttr.im_func.func_doc = """GetCornerSharpnessesAttr() -> USDGEOM_API UsdAttribute



The sharpness values for corners: each corner gets a single sharpness
value (Usd.Mesh.SHARPNESS_INFINITE for a perfectly sharp corner), so
the size of this array must match that of 'cornerIndices'.


C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["Mesh"].CreateCornerSharpnessesAttr.im_func.func_doc = """CreateCornerSharpnessesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetCornerSharpnessesAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].GetFaceVertexCountsAttr.im_func.func_doc = """GetFaceVertexCountsAttr() -> USDGEOM_API UsdAttribute



Provides the number of vertices in each face of the mesh, which is
also the number of consecutive indices in 'faceVertexIndices' that
define the face.


The length of this attribute is the number of faces in the mesh. If
this attribute has more than one timeSample, the mesh is considered to
be topologically varying.

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Mesh"].CreateCornerIndicesAttr.im_func.func_doc = """CreateCornerIndicesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetCornerIndicesAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].CreateCreaseSharpnessesAttr.im_func.func_doc = """CreateCreaseSharpnessesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetCreaseSharpnessesAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].GetHoleIndicesAttr.im_func.func_doc = """GetHoleIndicesAttr() -> USDGEOM_API UsdAttribute



The face indices (indexing into the 'faceVertexCounts' attribute) of
all faces that should be made invisible.


C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["Mesh"].GetFaceVaryingLinearInterpolationAttr.im_func.func_doc = """GetFaceVaryingLinearInterpolationAttr() -> USDGEOM_API UsdAttribute



Specifies how face varying data is interpolated.


Valid values are "all" (no smoothing), "cornersPlus1" (the default,
Smooth UV), "none" (Same as "cornersPlus1" but does not infer the
presence of corners where two faceVarying edges meet at a single
face), or "boundaries" (smooth only near vertices that are not at a
discontinuous boundary).

See
http://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html
#face-varying-interpolation-rules

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: cornersPlus1  Allowed Values :
[all, none, boundaries, cornersOnly, cornersPlus1, cornersPlus2]

"""
   result["Mesh"].ValidateTopology.func_doc = """**static** ValidateTopology(faceVertexIndices, faceVertexCounts, numPoints, reason) -> USDGEOM_API bool

faceVertexIndices : VtIntArray
faceVertexCounts : VtIntArray
numPoints : size_t
reason : string


Validate the topology of a mesh.


This validates that the sum of C{faceVertexCounts} is equal to the
size of the C{faceVertexIndices} array, and that all face vertex
indices in the C{faceVertexIndices} array are in the range [0,
numPoints). Returns true if the topology is valid, or false otherwise.
If the topology is invalid and C{reason} is non-null, an error message
describing the validation error will be set.

"""
   result["Mesh"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomMesh

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Mesh"].CreateCreaseIndicesAttr.im_func.func_doc = """CreateCreaseIndicesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetCreaseIndicesAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomMesh

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomMesh holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomMesh(stage->GetPrimAtPath(path));


"""
   result["Mesh"].CreateHoleIndicesAttr.im_func.func_doc = """CreateHoleIndicesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHoleIndicesAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].GetCornerIndicesAttr.im_func.func_doc = """GetCornerIndicesAttr() -> USDGEOM_API UsdAttribute



The vertex indices of all vertices that are sharp corners.


C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["Mesh"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomMesh on UsdPrim C{prim}.


Equivalent to UsdGeomMesh::Get (prim.GetStage(), prim.GetPath()) for a
*valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomMesh on the prim held by C{schemaObj}.


Should be preferred over UsdGeomMesh (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Mesh"].CreateTriangleSubdivisionRuleAttr.im_func.func_doc = """CreateTriangleSubdivisionRuleAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTriangleSubdivisionRuleAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].GetFaceVertexIndicesAttr.im_func.func_doc = """GetFaceVertexIndicesAttr() -> USDGEOM_API UsdAttribute



Flat list of the index (into the 'points' attribute) of each vertex of
each face in the mesh.


If this attribute has more than one timeSample, the mesh is considered
to be topologically varying.

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Mesh"].GetCreaseLengthsAttr.im_func.func_doc = """GetCreaseLengthsAttr() -> USDGEOM_API UsdAttribute



The length of this array specifies the number of creases on the
surface.


Each element gives the number of (must be adjacent) vertices in each
crease, whose indices are linearly laid out in the 'creaseIndices'
attribute. Since each crease must be at least one edge long, each
element of this array should be greater than one.

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["Mesh"].GetInterpolateBoundaryAttr.im_func.func_doc = """GetInterpolateBoundaryAttr() -> USDGEOM_API UsdAttribute



Specifies how interpolation boundary face edges are interpolated.


Valid values are "none", "edgeAndCorner" (the default), or "edgeOnly".

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: edgeAndCorner  Allowed Values :
[none, edgeAndCorner, edgeOnly]

"""
   result["Mesh"].CreateCreaseLengthsAttr.im_func.func_doc = """CreateCreaseLengthsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetCreaseLengthsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].CreateSubdivisionSchemeAttr.im_func.func_doc = """CreateSubdivisionSchemeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSubdivisionSchemeAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].GetSubdivisionSchemeAttr.im_func.func_doc = """GetSubdivisionSchemeAttr() -> USDGEOM_API UsdAttribute



The subdivision scheme to be applied to the surface.


Valid values are "catmullClark" (the default), "loop", "bilinear", and
"none" (i.e. a polymesh with no subdivision - the primary difference
between schemes "bilinear" and "none" is that bilinearly subdivided
meshes can be considered watertight, whereas there is no such
guarantee for un-subdivided polymeshes, and more mesh features (e.g.
holes) may apply to bilinear meshes but not polymeshes. Polymeshes
*may* be lighterweight and faster to render, depending on renderer and
render mode.)

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: catmullClark  Allowed Values :
[catmullClark, loop, bilinear, none]

"""
   result["Mesh"].GetCreaseIndicesAttr.im_func.func_doc = """GetCreaseIndicesAttr() -> USDGEOM_API UsdAttribute



The indices of all vertices forming creased edges.


The size of this array must be equal to the sum of all elements of the
'creaseLengths' attribute.

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["Mesh"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Mesh"].CreateInterpolateBoundaryAttr.im_func.func_doc = """CreateInterpolateBoundaryAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetInterpolateBoundaryAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].CreateFaceVaryingLinearInterpolationAttr.im_func.func_doc = """CreateFaceVaryingLinearInterpolationAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFaceVaryingLinearInterpolationAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].CreateFaceVertexIndicesAttr.im_func.func_doc = """CreateFaceVertexIndicesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFaceVertexIndicesAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Mesh"].GetTriangleSubdivisionRuleAttr.im_func.func_doc = """GetTriangleSubdivisionRuleAttr() -> USDGEOM_API UsdAttribute



Specifies what weights are used during triangle subdivision for the
Catmull-Clark scheme.


Valid values are "catmullClark" (the default) and "smooth".

See
http://graphics.pixar.com/opensubdiv/docs/subdivision_surfaces.html
#triangle-subdivision-rule

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: catmullClark  Allowed Values :
[catmullClark, smooth]

"""
   result["Mesh"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Mesh"].GetCreaseSharpnessesAttr.im_func.func_doc = """GetCreaseSharpnessesAttr() -> USDGEOM_API UsdAttribute



The per-crease or per-edge sharpness for all creases
(Usd.Mesh.SHARPNESS_INFINITE for a perfectly sharp crease).


Since 'creaseLengths' encodes the number of vertices in each crease,
the number of elements in this array will be either len(creaseLengths)
or the sum over all X of (creaseLengths[X] - 1). Note that while the
RI spec allows each crease to have either a single sharpness or a
value per-edge, USD will encode either a single sharpness per crease
on a mesh, or sharpnesses for all edges making up the creases on a
mesh.

C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["Mesh"].CreateFaceVertexCountsAttr.im_func.func_doc = """CreateFaceVertexCountsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFaceVertexCountsAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PrimvarsAPI"].__doc__ = """
UsdGeomPrimvarsAPI encodes geometric "primitive variables", as
UsdGeomPrimvar, which interpolate across a primitive's topology, can
override shader inputs, and inherit down namespace.

"""
   result["PrimvarsAPI"].GetPrimvars.im_func.func_doc = """GetPrimvars() -> USDGEOM_API sequence< UsdGeomPrimvar >



Return valid UsdGeomPrimvar objects for all defined Primvars on this
prim.


Although we hope eventually to make this faster, this is currently a
fairly expensive operation. If you know you'll need to process other
attributes as well, you might do better by fetching all the attributes
at once, and using the pattern described in Using Primvars to test
individual attributes.

"""
   result["PrimvarsAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomPrimvarsAPI on UsdPrim C{prim}.


Equivalent to UsdGeomPrimvarsAPI::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomPrimvarsAPI on the prim held by C{schemaObj}.


Should be preferred over UsdGeomPrimvarsAPI (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["PrimvarsAPI"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomPrimvarsAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomPrimvarsAPI holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomPrimvarsAPI(stage->GetPrimAtPath(path));


"""
   result["PrimvarsAPI"].HasPrimvar.im_func.func_doc = """HasPrimvar(name) -> USDGEOM_API bool

name : TfToken


Is there a defined Primvar C{name} on this prim?


Name lookup will account for Primvar namespacing.

GetPrimvar()

"""
   result["PrimvarsAPI"].FindInheritedPrimvars.im_func.func_doc = """FindInheritedPrimvars() -> USDGEOM_API sequence< UsdGeomPrimvar >



Like GetPrimvars() , but searches instead for authored primvars
inherited from ancestor prims.


Primvars are only inherited if they do not exist on the prim itself.
The returned primvars will be bound to attributes on the corresponding
ancestor prims. Only primvars with authored values are inherited;
fallback values are not inherited. The order of the returned primvars
is undefined.

"""
   result["PrimvarsAPI"].GetPrimvar.im_func.func_doc = """GetPrimvar(name) -> USDGEOM_API UsdGeomPrimvar

name : TfToken


Return the Primvar attribute named by C{name}, which will be valid if
a Primvar attribute definition already exists.


Name lookup will account for Primvar namespacing, which means that
this method will succeed in some cases where ::

  UsdGeomPrimvar(prim->GetAttribute(name))

 will not, unless C{name} is properly namespace prefixed.

HasPrimvar()

"""
   result["PrimvarsAPI"].GetAuthoredPrimvars.im_func.func_doc = """GetAuthoredPrimvars() -> USDGEOM_API sequence< UsdGeomPrimvar >



Like GetPrimvars() , but exclude primvars that have no authored scene
description.

"""
   result["PrimvarsAPI"].FindInheritedPrimvar.im_func.func_doc = """FindInheritedPrimvar(name) -> USDGEOM_API UsdGeomPrimvar

name : TfToken


Like GetPrimvar() , but searches instead for the named primvar
inherited on ancestor prim.


Primvars are only inherited if they do not exist on the prim itself.
The returned primvar will be bound to the attribute on the
corresponding ancestor prim.

"""
   result["PrimvarsAPI"].CreatePrimvar.im_func.func_doc = """CreatePrimvar(attrName, typeName, interpolation, elementSize) -> USDGEOM_API UsdGeomPrimvar

attrName : TfToken
typeName : SdfValueTypeName
interpolation : TfToken
elementSize : int


Author scene description to create an attribute on this prim that will
be recognized as Primvar (i.e.


will present as a valid UsdGeomPrimvar).

The name of the created attribute may or may not be the specified
C{attrName}, due to the possible need to apply property namespacing
for primvars. See Creating and Accessing Primvars for more
information. Creation may fail and return an invalid Primvar if
C{attrName} contains a reserved keyword, such as the "indices" suffix
we use for indexed primvars.

The behavior with respect to the provided C{typeName} is the same as
for UsdAttributes::Create(), and C{interpolation} and C{elementSize}
are as described in UsdGeomPrimvar::GetInterpolation() and
UsdGeomPrimvar::GetElementSize() .

If C{interpolation} and/or C{elementSize} are left unspecified, we
will author no opinions for them, which means any (strongest) opinion
already authored in any contributing layer for these fields will
become the Primvar's values, or the fallbacks if no opinions have been
authored.

an invalid UsdGeomPrimvar if we failed to create a valid attribute, a
valid UsdGeomPrimvar otherwise. It is not an error to create over an
existing, compatible attribute.

UsdPrim::CreateAttribute() , UsdGeomPrimvar::IsPrimvar()

"""
   result["PrimvarsAPI"].HasInheritedPrimvar.im_func.func_doc = """HasInheritedPrimvar(name) -> USDGEOM_API bool

name : TfToken


Is there an inherited Primvar C{name} on this prim? The name given is
the primvar name, not its underlying attribute name.



FindInheritedPrimvar()

"""
   result["PrimvarsAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PrimvarsAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Camera"].__doc__ = """
Transformable camera.


Describes optical properties of a camera via a common set of
attributes that provide control over the camera's frustum as well as
its depth of field. For stereo, the left and right camera are
individual prims tagged through the stereoRole attribute.

There is a corresponding class GfCamera, which can hold the state of a
camera (at a particular time). UsdGeomCamera::GetCamera() and
UsdGeomCamera::SetFromCamera() convert between a USD camera prim and a
GfCamera.

To obtain the camera's location in world space, call the following on
a UsdGeomCamera 'camera': ::

  GfMatrix4d camXform = camera.ComputeLocalToWorldTransform(time);

B{Cameras in USD are always "Y up", regardless of the stage's
orientation (i.e. UsdGeomGetStageUpAxis() ).} This means that the
inverse of 'camXform' (the VIEW half of the MODELVIEW transform in
OpenGL parlance) will transform the world such that the camera is at
the origin, looking down the -Z axis, with Y as the up axis.

Linear Algebra in UsdGeom For any described attribute *Fallback*
*Value* or *Allowed* *Values* below that are text/tokens, the actual
token is published and defined in UsdGeomTokens. So to set an
attribute to the value "rightHanded", use UsdGeomTokens->rightHanded
as the value.

"""
   result["Camera"].CreateVerticalApertureOffsetAttr.im_func.func_doc = """CreateVerticalApertureOffsetAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVerticalApertureOffsetAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].CreateShutterOpenAttr.im_func.func_doc = """CreateShutterOpenAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShutterOpenAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].GetShutterOpenAttr.im_func.func_doc = """GetShutterOpenAttr() -> USDGEOM_API UsdAttribute



Frame relative shutter open time in UsdTimeCode units (negative value
indicates that the shutter opens before the current frame time).


Used for motion blur.

C++ Type: double  Usd Type: SdfValueTypeNames->Double  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["Camera"].CreateShutterCloseAttr.im_func.func_doc = """CreateShutterCloseAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShutterCloseAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].GetCamera.im_func.func_doc = """GetCamera(time) -> USDGEOM_API GfCamera

time : UsdTimeCode


Creates a GfCamera object from the attribute values at C{time}.

"""
   result["Camera"].CreateHorizontalApertureOffsetAttr.im_func.func_doc = """CreateHorizontalApertureOffsetAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHorizontalApertureOffsetAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].CreateProjectionAttr.im_func.func_doc = """CreateProjectionAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetProjectionAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].GetShutterCloseAttr.im_func.func_doc = """GetShutterCloseAttr() -> USDGEOM_API UsdAttribute



Frame relative shutter close time, analogous comments from
shutter:open apply.


A value greater or equal to shutter:open should be authored, otherwise
there is no exposure and a renderer should produce a black image.

C++ Type: double  Usd Type: SdfValueTypeNames->Double  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["Camera"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomCamera

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Camera"].CreateFStopAttr.im_func.func_doc = """CreateFStopAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFStopAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].CreateFocusDistanceAttr.im_func.func_doc = """CreateFocusDistanceAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFocusDistanceAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].GetFStopAttr.im_func.func_doc = """GetFStopAttr() -> USDGEOM_API UsdAttribute



Lens aperture.


Defaults to 0.0, which turns off focusing.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["Camera"].GetClippingPlanesAttr.im_func.func_doc = """GetClippingPlanesAttr() -> USDGEOM_API UsdAttribute



Additional, arbitrarily oriented clipping planes.


A vector (a,b,c,d) encodes a clipping plane that cuts off (x,y,z) with
a * x + b * y + c * z + d * 1<0 where (x,y,z) are the coordinates in
the camera's space.

C++ Type: VtArray<GfVec4f>  Usd Type: SdfValueTypeNames->Float4Array
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["Camera"].CreateStereoRoleAttr.im_func.func_doc = """CreateStereoRoleAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetStereoRoleAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].CreateClippingPlanesAttr.im_func.func_doc = """CreateClippingPlanesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetClippingPlanesAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].GetVerticalApertureOffsetAttr.im_func.func_doc = """GetVerticalApertureOffsetAttr() -> USDGEOM_API UsdAttribute



Vertical aperture offset in the same units as verticalAperture.


Defaults to 0.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["Camera"].CreateHorizontalApertureAttr.im_func.func_doc = """CreateHorizontalApertureAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHorizontalApertureAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].GetFocalLengthAttr.im_func.func_doc = """GetFocalLengthAttr() -> USDGEOM_API UsdAttribute



Perspective focal length in millimeters (or, more general, tenths of a
world unit).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 50.0

"""
   result["Camera"].CreateFocalLengthAttr.im_func.func_doc = """CreateFocalLengthAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFocalLengthAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomCamera on UsdPrim C{prim}.


Equivalent to UsdGeomCamera::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomCamera on the prim held by C{schemaObj}.


Should be preferred over UsdGeomCamera (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Camera"].GetVerticalApertureAttr.im_func.func_doc = """GetVerticalApertureAttr() -> USDGEOM_API UsdAttribute



Vertical aperture in millimeters (or, more general, tenths of a world
unit).


Defaults to the standard 35mm spherical projector aperture.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 15.2908000946

"""
   result["Camera"].SetFromCamera.im_func.func_doc = """SetFromCamera(camera, time) -> USDGEOM_API void

camera : GfCamera
time : UsdTimeCode


Write attribute values from C{camera} for C{time}.

"""
   result["Camera"].GetHorizontalApertureOffsetAttr.im_func.func_doc = """GetHorizontalApertureOffsetAttr() -> USDGEOM_API UsdAttribute



Horizontal aperture offset in the same units as horizontalAperture.


Defaults to 0.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["Camera"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Camera"].GetProjectionAttr.im_func.func_doc = """GetProjectionAttr() -> USDGEOM_API UsdAttribute



C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: perspective  Allowed Values :
[perspective, orthographic]

"""
   result["Camera"].GetClippingRangeAttr.im_func.func_doc = """GetClippingRangeAttr() -> USDGEOM_API UsdAttribute



Near and far clipping distances in centimeters (or, more general,
world units).


C++ Type: GfVec2f  Usd Type: SdfValueTypeNames->Float2  Variability:
SdfVariabilityVarying  Fallback Value: (1, 1000000)

"""
   result["Camera"].CreateClippingRangeAttr.im_func.func_doc = """CreateClippingRangeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetClippingRangeAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomCamera

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomCamera holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomCamera(stage->GetPrimAtPath(path));


"""
   result["Camera"].GetHorizontalApertureAttr.im_func.func_doc = """GetHorizontalApertureAttr() -> USDGEOM_API UsdAttribute



Horizontal aperture in millimeters (or, more general, tenths of a
world unit).


Defaults to the standard 35mm spherical projector aperture.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 20.9549999237

"""
   result["Camera"].CreateVerticalApertureAttr.im_func.func_doc = """CreateVerticalApertureAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVerticalApertureAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Camera"].GetStereoRoleAttr.im_func.func_doc = """GetStereoRoleAttr() -> USDGEOM_API UsdAttribute



If different from mono, the camera is intended to be the left or right
camera of a stereo setup.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: mono  Allowed Values : [mono,
left, right]

"""
   result["Camera"].GetFocusDistanceAttr.im_func.func_doc = """GetFocusDistanceAttr() -> USDGEOM_API UsdAttribute



Distance from the camera to the focus plane in centimeters (or more
general, world units).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["Camera"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Cone"].__doc__ = """
Defines a primitive cone, centered at the origin, whose spine is along
the specified *axis*, with the apex of the cone pointing in the
direction of the positive axis.


The fallback values for Cube, Sphere, Cone, and Cylinder are set so
that they all pack into the same volume/bounds.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdGeomTokens. So to set an attribute to the value "rightHanded",
use UsdGeomTokens->rightHanded as the value.

"""
   result["Cone"].CreateHeightAttr.im_func.func_doc = """CreateHeightAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHeightAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cone"].GetExtentAttr.im_func.func_doc = """GetExtentAttr() -> USDGEOM_API UsdAttribute



Extent is re-defined on Cone only to provide a fallback value.



UsdGeomGprim::GetExtentAttr() .  C++ Type: VtArray<GfVec3f>  Usd Type:
SdfValueTypeNames->Float3Array  Variability: SdfVariabilityVarying
Fallback Value: [(-1, -1, -1), (1, 1, 1)]

"""
   result["Cone"].CreateRadiusAttr.im_func.func_doc = """CreateRadiusAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRadiusAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cone"].CreateExtentAttr.im_func.func_doc = """CreateExtentAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetExtentAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cone"].CreateAxisAttr.im_func.func_doc = """CreateAxisAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAxisAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Cone"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomCone on UsdPrim C{prim}.


Equivalent to UsdGeomCone::Get (prim.GetStage(), prim.GetPath()) for a
*valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomCone on the prim held by C{schemaObj}.


Should be preferred over UsdGeomCone (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Cone"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomCone

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomCone holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomCone(stage->GetPrimAtPath(path));


"""
   result["Cone"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Cone"].GetHeightAttr.im_func.func_doc = """GetHeightAttr() -> USDGEOM_API UsdAttribute



The size of the cone's spine along the specified *axis*.


If you author *height* you must also author *extent*.

GetExtentAttr()  C++ Type: double  Usd Type: SdfValueTypeNames->Double
Variability: SdfVariabilityVarying  Fallback Value: 2.0

"""
   result["Cone"].GetRadiusAttr.im_func.func_doc = """GetRadiusAttr() -> USDGEOM_API UsdAttribute



The radius of the cone.


If you author *radius* you must also author *extent*.

GetExtentAttr()  C++ Type: double  Usd Type: SdfValueTypeNames->Double
Variability: SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["Cone"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Cone"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomCone

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Cone"].GetAxisAttr.im_func.func_doc = """GetAxisAttr() -> USDGEOM_API UsdAttribute



The axis along which the spine of the cone is aligned.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: Z  Allowed Values : [X, Y, Z]

"""
   result["XformCommonAPI"].__doc__ = """
This class provides API for authoring and retrieving a standard set of
component transformations which include a scale, a rotation, a scale-
rotate pivot and a translation.


The goal of the API is to enhance component-wise interchange. It
achieves this by limiting the set of allowed basic ops and by
specifying the order in which they are applied. In addition to the
basic set of ops, the 'resetXformStack' bit can also be set to
indicate whether the underlying xformable resets the parent
transformation (i.e. does not inherit it's parent's transformation).

UsdGeomXformCommonAPI::GetResetXformStack()

UsdGeomXformCommonAPI::SetResetXformStack() The operator-bool for the
class will inform you whether an existing xformable is compatible with
this API.

The scale-rotate pivot is represented by a pair of (translate,
inverse-translate) xformOps around the scale and rotate operations.
The rotation operation can be any of the six allowed Euler angle sets.

UsdGeomXformOp::Type. The xformOpOrder of an xformable that has all of
the supported basic ops is as follows: ["xformOp:translate",
"xformOp:translate:pivot", "xformOp:rotateXYZ", "xformOp:scale",
"!invert!xformOp:translate:pivot"].

It is worth noting that all of the ops are optional. For example, an
xformable may have only a translate or a rotate. It would still be
considered as compatible with this API. Individual SetTranslate() ,
SetRotate() , SetScale() and SetPivot() methods are provided by this
API to allow such sparse authoring.

Manipulating the xformOpOrder attribute manually or using the API
provided in UsdGeomXformable to add or remove xformOps causes the
UsdGeomXformCommonAPI object to contain invalid or stale information.
A new UsdGeomXformCommonAPI object must be created with the xformable
after invoking any operation on the underlying xformable that would
cause the xformOpOrder to change.

"""
   result["XformCommonAPI"].SetResetXformStack.im_func.func_doc = """SetResetXformStack(resetXformStack) -> USDGEOM_API bool

resetXformStack : bool


Set whether the xformable resets the transform stack.


i.e., does not inherit the parent transformation.

"""
   result["XformCommonAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


----------------------------------------------------------------------
__init__(xformable)

xformable : Xformable

"""
   result["XformCommonAPI"].RotationOrder.__doc__ = """
Enumerates the rotation order of the 3-angle Euler rotation.

"""
   result["XformCommonAPI"].SetXformVectors.im_func.func_doc = """SetXformVectors(translation, rotation, scale, pivot, rotOrder, time) -> USDGEOM_API bool

translation : GfVec3d
rotation : GfVec3f
scale : GfVec3f
pivot : GfVec3f
rotOrder : RotationOrder
time : UsdTimeCode


Set values for the various component xformOps at a given C{time}.


Calling this method will call all of the supported ops to be created,
even if they only contain default (identity) values.

To author individual operations selectively, use the Set[OpType]()
API.

Once the rotation order has been established for a given xformable
(either because of an already defined (and compatible) rotate op or
from calling SetXformVectors() or SetRotate() ), it cannot be changed.

"""
   result["XformCommonAPI"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomXformCommonAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomXformCommonAPI holding the xformable adhering to this
API at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this API, return an invalid API object. This is
shorthand for the following: ::

  UsdGeomXformCommonAPI(UsdGeomXformable(stage->GetPrimAtPath(path)));


"""
   result["XformCommonAPI"].SetRotate.im_func.func_doc = """SetRotate(rotation, rotOrder, time) -> USDGEOM_API bool

rotation : GfVec3f
rotOrder : XformCommonAPI.RotationOrder
time : UsdTimeCode


Set rotation at C{time} to C{rotation}.

"""
   result["XformCommonAPI"].SetScale.im_func.func_doc = """SetScale(scale, time) -> USDGEOM_API bool

scale : GfVec3f
time : UsdTimeCode


Set scale at C{time} to C{scale}.

"""
   result["XformCommonAPI"].SetPivot.im_func.func_doc = """SetPivot(pivot, time) -> USDGEOM_API bool

pivot : GfVec3f
time : UsdTimeCode


Set pivot position at C{time} to C{pivot}.

"""
   result["XformCommonAPI"].GetResetXformStack.im_func.func_doc = """GetResetXformStack() -> USDGEOM_API bool



Returns whether the xformable resets the transform stack.


i.e., does not inherit the parent transformation.

"""
   result["XformCommonAPI"].GetXformVectorsByAccumulation.im_func.func_doc = """GetXformVectorsByAccumulation(translation, rotation, scale, pivot, rotOrder, time) -> USDGEOM_API bool

translation : GfVec3d
rotation : GfVec3f
scale : GfVec3f
pivot : GfVec3f
rotOrder : XformCommonAPI.RotationOrder
time : UsdTimeCode


Retrieve values of the various component xformOps at a given C{time}.


Identity values are filled in for the component xformOps that don't
exist or don't have an authored value.

This method allows some additional flexibility for xform schemas that
do not strictly adhere to the xformCommonAPI. For incompatible
schemas, this method will attempt to reduce the schema into one from
which component vectors can be extracted by accumulating xformOp
transforms of the common types.

When the underlying xformable has a compatible xform schema, the usual
component value extraction method is used instead. When the xform
schema is incompatible and it cannot be reduced by accumulating
transforms, it performs a full-on matrix decomposition to XYZ rotation
order.

"""
   result["XformCommonAPI"].GetXformVectors.im_func.func_doc = """GetXformVectors(translation, rotation, scale, pivot, rotOrder, time) -> USDGEOM_API bool

translation : GfVec3d
rotation : GfVec3f
scale : GfVec3f
pivot : GfVec3f
rotOrder : RotationOrder
time : UsdTimeCode


Retrieve values of the various component xformOps at a given C{time}.


Identity values are filled in for the component xformOps that don't
exist or don't have an authored value.

This method works even on prims with an incompatible xform schema,
i.e. when the bool operator returns false. When the underlying
xformable has an incompatible xform schema, it performs a full-on
matrix decomposition to XYZ rotation order.

"""
   result["XformCommonAPI"].SetTranslate.im_func.func_doc = """SetTranslate(translation, time) -> USDGEOM_API bool

translation : GfVec3d
time : UsdTimeCode


Set translation at C{time} to C{translation}.

"""
   result["Xform"].__doc__ = """
Concrete prim schema for a transform, which implements Xformable.

"""
   result["Xform"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomXform on UsdPrim C{prim}.


Equivalent to UsdGeomXform::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomXform on the prim held by C{schemaObj}.


Should be preferred over UsdGeomXform (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Xform"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomXform

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomXform holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomXform(stage->GetPrimAtPath(path));


"""
   result["Xform"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Xform"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Xform"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomXform

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["CollectionAPI"].__doc__ = """
Deprecated

This API schema has been deprecated in favor of UsdCollectionAPI.

This is a general purpose API schema, used to describe a collection of
heterogeneous objects within the scene. "Objects" here may be prims,
properties or face-sets belonging to prims. It's an add-on schema that
can be applied many times to a prim with different collection names.
All the properties authored by the schema are namespaced under
"collection:". The given name of the collection provides additional
namespacing for the various per-collection properties, which include
the following:

   - B{rel collection:collectionName} - specifies a list of targets
     that are included in the collection. These can be entire prims or
     prims with faces.

   - B{int[] collection:collectionName:targetFaceCounts} - is authored
     if the collection restricts to a face-set for any of its targets. It
     contains an element for each target: zero if the target has no face-
     restriction, or the number of consecutive face-indices in the
     associated targetFaceIndices property that correspond to the target.

   - B{int[] collection:myCollection:targetFaceIndices} - contains the
     list of face indices that correspond to the various face counts in the
     associated targetFaceCounts property, for targets that have a face-
     restriction.

Each target object may only appear once in a collection since the
targets of a single relationship form a unique set. Note that we have
not referred anywhere to meshes or polygons in this class.  We use the
term "face" generically, as this schema could be used equally well to
create collections containing UsdGeomCurves.

Here's some sample code to create a collection on a prim and include a
set of objects in the collection: ::

  UsdGeomModelAPI model(stage.GetPrimAtPath("/path/to/model"));
  UsdGeomMesh sphere(stage.GetPrimAtPath("/path/to/sphereMesh"));
  UsdGeomMesh cube(stage.GetPrimAtPath("/path/to/cubeMesh"));
  
  UsdGeomCollectionAPI geomCollection = UsdGeomCollectionAPI::Create(model, 
      "geometry");
  
  // This adds the entire sphere as a target of the collection.
  geomCollection.AddTarget(sphere.GetPath());
  
  VtIntArray cubeFaceIndices;
  // ... populate faceIndices here.
  // This adds the specified set of faceIndices belonging to the cube as a 
  // target of the collection.
  geomCollection.AddTarget(cube.GetPath(), cubeFaceIndices);

An alternate way to author a collection is by setting the individual
collection properties directly via API available in
UsdGeomCollectionAPI_PropertyValueAPI. ::

  VtIntArray targetFaceCounts(2);
  # face count of 0 indicates that the entire prim is part of the collection.
  targetFaceCounts[0] = 0;
  targetFaceCounts[1] = cubeFaceIndices.size();
  
  VtIntArray targetFaceIndices;
  // 
... insert face indices belonging to the targets with face-
restrictions 
  // ... here.
  
  // Set the targets of the collection.
  SdfPathVector targets;
  targets.push_back(sphere.GetPath());
  targets.push_back(cube.GetPath());
  geomCollection.SetTargets(targets)
  
  // Set the targetFaceIndices and targetFaceCounts.
  geomCollection.SetTargetFaceCounts(targetFaceCounts);
  geomCollection.SetTargetFaceIndices(targetFaceIndices);


"""
   result["CollectionAPI"].GetTargetFaceIndices.im_func.func_doc = """GetTargetFaceIndices(targetFaceIndices, time) -> USDGEOM_API bool

targetFaceIndices : VtIntArray
time : UsdTimeCode


Retrieves the targetFaceCounts property value at the given C{time}.


Returns false if no value is authored or if the "targetFaceIndices"
property does not exist.

UsdGeomCollectionAPI::SetTargetFaceIndices()

"""
   result["CollectionAPI"].Create.func_doc = """**static** Create(prim, name, targets, targetFaceCounts, targetFaceIndices) -> USDGEOM_API UsdGeomCollectionAPI

prim : UsdPrim
name : TfToken
targets : SdfPathVector
targetFaceCounts : VtIntArray
targetFaceIndices : VtIntArray


Creates a new collection on the given C{prim} with the given C{name}.


If C{targets}, C{targetFaceCounts} and C{targetFaceIndices} are set if
specified. No validation is performed on the values passed in.

If a collection already exists with the given name, it's targets are
reset to the specified set of targets, if C{targets} is non-empty.


----------------------------------------------------------------------
Create(schemaObj, name, targets, targetFaceCounts, targetFaceIndices) -> USDGEOM_API UsdGeomCollectionAPI

schemaObj : UsdSchemaBase
name : TfToken
targets : SdfPathVector
targetFaceCounts : VtIntArray
targetFaceIndices : VtIntArray


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Creates a new collection with the given C{name} on the prim held in
the given C{schemaObj}.


If C{targets}, C{targetFaceCounts} and C{targetFaceIndices} are set if
specified. No validation is performed on the values passed in.

If a collection already exists with the given name, it's targets are
reset to the specified set of targets, if C{targets} is non-empty.

"""
   result["CollectionAPI"].CreateTargetsRel.im_func.func_doc = """CreateTargetsRel() -> USDGEOM_API UsdRelationship



Creates the relationship that targets the prims included in the
collection.



GetTargetsRel()

"""
   result["CollectionAPI"].GetTargetsRel.im_func.func_doc = """GetTargetsRel() -> USDGEOM_API UsdRelationship



Returns the relationship that targets the prims included in the
collection.



GetTargets()

"""
   result["CollectionAPI"].SetTargets.im_func.func_doc = """SetTargets(targets) -> USDGEOM_API bool

targets : SdfPathVector


Sets the paths to target objects that belong to the collection.

"""
   result["CollectionAPI"].GetTargetFaceCounts.im_func.func_doc = """GetTargetFaceCounts(targetFaceCounts, time) -> USDGEOM_API bool

targetFaceCounts : VtIntArray
time : UsdTimeCode


Retrieves the targetFaceCounts property value at the given C{time}.


Returns false if no value is authored or if the "targetFaceCounts"
property does not exist.

UsdGeomCollectionAPI::SetTargetFaceCounts()

UsdGeomCollectionAPI::GetFaceIndices()

"""
   result["CollectionAPI"].GetCollections.func_doc = """**static** GetCollections(prim) -> USDGEOM_API sequence< UsdGeomCollectionAPI >

prim : UsdPrim


Returns the list of all collections on the given prim, C{prim}.


This will return both empty and non-empty collections.


----------------------------------------------------------------------
GetCollections(schemaObj) -> USDGEOM_API sequence< UsdGeomCollectionAPI >

schemaObj : UsdSchemaBase


Returns the list of all face-sets on the prim held by C{schemaObj}.

"""
   result["CollectionAPI"].GetCollectionName.im_func.func_doc = """GetCollectionName() -> TfToken



Returns the name of the collection.

"""
   result["CollectionAPI"].Validate.im_func.func_doc = """Validate(reason) -> USDGEOM_API bool

reason : string


Validates the properties belonging to the collection.


Returns true if the collection has all valid properties. Returns false
and populates the C{reason} output argument if the collection is
invalid.

Here's the list of validations performed by this method:
   - A collection is considered to be invalid if it has no data
     authored. i.e. when the collection relationship does not exist.

   - The number of entries in "targetFaceCounts" should match the
     number of targets in the collection over all timeSamples.

   - The sum all values in the "targetFaceCounts" array should be
     equal to the length of the "targetFaceIndices" array over all
     timeSamples.


"""
   result["CollectionAPI"].AddTarget.im_func.func_doc = """AddTarget(target, faceIndices, time) -> USDGEOM_API bool

target : SdfPath
faceIndices : VtIntArray
time : UsdTimeCode


Adds a new target, C{target} to the collection.


The list of face indices in the array, C{faceIndices} is used to
specify a face-restriction on the target at the given time, C{time}.

Returns true only upon success.

Here are a few things worth noting about this method:

   - The target face-count is gleaned from the length of the
     C{faceIndices} array.

   - If C{faceIndices} is empty and there is an existing value for
     "targetFaceCounts", then 0 is appended to the list of target face-
     counts to indicate that the entire target is included in the
     collection.

   - If C{faceIndices} is empty and the collection does have not a
     value for the "targetFaceCounts" property, then only the target is
     appended. targetFaceCounts and targetFaceIndices are not authored (or
     even created) in this case.


"""
   result["CollectionAPI"].CreateTargetFaceIndicesAttr.im_func.func_doc = """CreateTargetFaceIndicesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


Creates the "targetFaceIndices" attribute associated with the
collection.


Create vs Get Property Methods for when to use Get vs Create. If
specified, author C{defaultValue} as the attribute's default, sparsely
(when it makes sense to do so) if C{writeSparsely} is C{true} - the
default for C{writeSparsely} is C{false}.

GetFaceIndicesAttr()

"""
   result["CollectionAPI"].GetTargetFaceIndicesAttr.im_func.func_doc = """GetTargetFaceIndicesAttr() -> USDGEOM_API UsdAttribute



Returns the "targetFaceIndices" attribute associated with the
collection.


C++ Type: VtIntArray  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying

GetTargetFaceIndices()

"""
   result["CollectionAPI"].GetTargets.im_func.func_doc = """GetTargets(targets) -> USDGEOM_API bool

targets : SdfPathVector


Returns the B{unresolved paths} to target objects belonging to the
collection.


Since a collection can include a relationship, no relationship
forwarding is performed by the method. i.e., if the collection targets
a relationship, the target relationship is returned (and not the
ultimate targets of the target relationship).

UsdRelationship::GetTargets

"""
   result["CollectionAPI"].IsEmpty.im_func.func_doc = """IsEmpty() -> USDGEOM_API bool



Returns true if the collection has no targets.

"""
   result["CollectionAPI"].GetTargetFaceCountsAttr.im_func.func_doc = """GetTargetFaceCountsAttr() -> USDGEOM_API UsdAttribute



Returns the "targetFaceCounts" attribute associated with the
collection.


C++ Type: VtIntArray  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying

GetTargetFaceCounts()

"""
   result["CollectionAPI"].__init__.im_func.func_doc = """__init__(prim, name)

prim : UsdPrim
name : TfToken


Construct a UsdGeomCollectionAPI with the given C{name} on the UsdPrim
C{prim}.


----------------------------------------------------------------------
__init__(schemaObj, name)

schemaObj : UsdSchemaBase
name : TfToken


Construct a UsdGeomCollectionAPI with the given C{name} on the prim
held by C{schemaObj}.

"""
   result["CollectionAPI"].CreateTargetFaceCountsAttr.im_func.func_doc = """CreateTargetFaceCountsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


Creates the "targetFaceCounts" attribute associated with the
collection.


Create vs Get Property Methods for when to use Get vs Create. If
specified, author C{defaultValue} as the attribute's default, sparsely
(when it makes sense to do so) if C{writeSparsely} is C{true} - the
default for C{writeSparsely} is C{false}.

GetTargetFaceCountsAttr()

"""
   result["CollectionAPI"].SetTargetFaceIndices.im_func.func_doc = """SetTargetFaceIndices(targetFaceIndices, time) -> USDGEOM_API bool

targetFaceIndices : VtIntArray
time : UsdTimeCode


Sets the list of face indices belonging to the targets of the
collection that have a face-restriction.


The total number of face indices should be equal to the sum of all
entires in the associated "targetFaceCounts" value.

Returns true if the value was authored successfully, false otherwise.

UsdGeomCollectionAPI::GetTargetFaceIndices()

UsdGeomCollectionAPI::SetTargetFaceCounts()

"""
   result["CollectionAPI"].SetTargetFaceCounts.im_func.func_doc = """SetTargetFaceCounts(targetFaceCounts, time) -> USDGEOM_API bool

targetFaceCounts : VtIntArray
time : UsdTimeCode


Sets the targetFaceCounts property of the collection at the given
C{time}.


Returns true if the value was authored successfully, false otherwise.

If the collection restricts to a face-set for any of its targets, then
"targetFaceCounts" specifies the number of faces included in the
various targets. The number of entries in C{targetFaceCounts} should
always match the number of targets. If a target does not have a face
restriction, then it's count is set to 0, to indicate that the entire
prim is included in the collection.

UsdGeomCollectionAPI::GetTargetFaceCounts()

"""
   result["XformOp"].__doc__ = """
Schema wrapper for UsdAttribute for authoring and computing
transformation operations, as consumed by UsdGeomXformable schema.


The semantics of an op are determined primarily by its name, which
allows us to decode an op very efficiently. All ops are independent
attributes, which must live in the "xformOp" property namespace. The
op's primary name within the namespace must be one of
UsdGeomXformOpTypes, which determines the type of transformation
operation, and its secondary name (or suffix) within the namespace
(which is not required to exist), can be any name that distinguishes
it from other ops of the same type. Suffixes are generally imposed by
higer level xform API schemas.

B{On packing order of rotateABC triples}  The order in which the axis
rotations are recorded in a Vec3* for the six *rotateABC* Euler
triples B{is always the same:} vec[0] = X, vec[1] = Y, vec[2] = Z. The
*A*, *B*, *C* in the op name dictate the order in which their
corresponding elements are consumed by the rotation, not how they are
laid out.

"""
   result["XformOp"].GetOpTransform.im_func.func_doc = """**static** GetOpTransform(time) -> USDGEOM_API GfMatrix4d

time : UsdTimeCode


Return the 4x4 matrix that applies the transformation encoded in this
op at C{time}.


Returns the identity matrix and issues a coding error if the op is
invalid.

If the op is valid, but has no authored value, the identity matrix is
returned and no error is issued.


----------------------------------------------------------------------
GetOpTransform(opType, opVal, isInverseOp) -> USDGEOM_API GfMatrix4d

opType : Type
opVal : VtValue
isInverseOp : bool


Return the 4x4 matrix that applies the transformation encoded by op
C{opType} and data value C{opVal}.


If C{isInverseOp} is true, then the inverse of the tranformation
represented by the op/value pair is returned.

An error will be issued if C{opType} is not one of the values in the
enum UsdGeomXformOp::Type or if C{opVal} cannot be converted to a
suitable input to C{opType}

"""
   result["XformOp"].GetTypeName.im_func.func_doc = """GetTypeName() -> SdfValueTypeName




UsdAttribute::GetTypeName()

"""
   result["XformOp"].GetPrecision.im_func.func_doc = """GetPrecision() -> USDGEOM_API Precision



Returns the precision level of the xform op.

"""
   result["XformOp"].MightBeTimeVarying.im_func.func_doc = """MightBeTimeVarying() -> bool



Determine whether there is any possibility that this op's value may
vary over time.


The determination is based on a snapshot of the authored state of the
op, and may become invalid in the face of further authoring.

"""
   result["XformOp"].IsDefined.im_func.func_doc = """IsDefined() -> bool



Return true if the wrapped UsdAttribute::IsDefined() , and in addition
the attribute is identified as a XformOp.

"""
   result["XformOp"].__init__.im_func.func_doc = """__init__(prim, opType, precision, opSuffix, inverse)

prim : UsdPrim
opType : Type
precision : Precision
opSuffix : TfToken
inverse : bool


----------------------------------------------------------------------
__init__()



----------------------------------------------------------------------
__init__(attr, isInverseOp) -> USDGEOM_API

attr : UsdAttribute
isInverseOp : bool


Speculative constructor that will produce a valid UsdGeomXformOp when
C{attr} already represents an attribute that is XformOp, and produces
an *invalid* XformOp otherwise (i.e.


unspecified_bool_type() will return false).

Calling C{UsdGeomXformOp::IsXformOp(attr)} will return the same truth
value as this constructor, but if you plan to subsequently use the
XformOp anyways, just use this constructor.

C{isInverseOp} is set to true to indicate an inverse transformation
op.

This constructor exists mainly for internal use. Clients should use
AddXformOp API (or one of Add*Op convenience API) to create and retain
a copy of an UsdGeomXformOp object.

"""
   result["XformOp"].GetTimeSamples.im_func.func_doc = """GetTimeSamples(times) -> bool

times : sequence<double>


Populates the list of time samples at which the associated attribute
is authored.

"""
   result["XformOp"].SplitName.im_func.func_doc = """SplitName() -> sequence<string>




UsdAttribute::SplitName()

"""
   result["XformOp"].GetOpName.im_func.func_doc = """**static** GetOpName(opType, opSuffix, inverse) -> USDGEOM_API TfToken

opType : Type
opSuffix : TfToken
inverse : bool


Returns the xformOp's name as it appears in xformOpOrder, given the
opType, the (optional) suffix and whether it is an inverse operation.


----------------------------------------------------------------------
GetOpName() -> USDGEOM_API TfToken



Returns the opName as it appears in the xformOpOrder attribute.


This will begin with "!invert!:xformOp:" if it is an inverse xform
operation. If it is not an inverse xformOp, it will begin with
'xformOp:'.

This will be empty for an invalid xformOp.

"""
   result["XformOp"].Type.__doc__ = """
Enumerates the set of all transformation operation types.

"""
   result["XformOp"].Get.im_func.func_doc = """Get(value, time) -> bool

value : T
time : UsdTimeCode


Get the attribute value of the XformOp at C{time}.



For inverted ops, this returns the raw, uninverted value.

"""
   result["XformOp"].GetNamespace.im_func.func_doc = """GetNamespace() -> TfToken




UsdAttribute::GetNamespace()

"""
   result["XformOp"].GetAttr.im_func.func_doc = """GetAttr() -> UsdAttribute



Explicit UsdAttribute extractor.

"""
   result["XformOp"].GetName.im_func.func_doc = """GetName() -> TfToken




UsdAttribute::GetName()

"""
   result["XformOp"].IsInverseOp.im_func.func_doc = """IsInverseOp() -> bool



Returns whether the xformOp represents an inverse operation.

"""
   result["XformOp"].Set.im_func.func_doc = """Set(value, time) -> bool

value : T
time : UsdTimeCode


Set the attribute value of the XformOp at C{time}.



This only works on non-inverse operations. If invoked on an inverse
xform operation, a coding error is issued and no value is authored.

"""
   result["XformOp"].Precision.__doc__ = """
Precision with which the value of the tranformation operation is
encoded.

"""
   result["XformOp"].GetBaseName.im_func.func_doc = """GetBaseName() -> TfToken




UsdAttribute::GetBaseName()

"""
   result["XformOp"].GetNumTimeSamples.im_func.func_doc = """GetNumTimeSamples() -> size_t



Returns the number of time samples authored for this xformOp.

"""
   result["XformOp"].GetOpType.im_func.func_doc = """GetOpType() -> Type



Return the operation type of this op, one of UsdGeomXformOp::Type.

"""
   result["XformOp"].GetTimeSamplesInInterval.im_func.func_doc = """GetTimeSamplesInInterval(interval, times) -> bool

interval : GfInterval
times : sequence<double>


Populates the list of time samples within the given C{interval}, at
which the associated attribute is authored.

"""
   result["FaceSetAPI"].__doc__ = """
Deprecated

This class has been deprecated in favor of the concrete typed-schema
"UsdGeomSubset".

This is a general purpose API schema used to describe many different
organizations and modifications of a prim's faces' behavior. It's an
add-on schema that can be applied many times to a prim with different
face-set names. All the properties authored by the schema are
namespaced under "faceSet:". The given name of the face-set provides
additional namespacing for the various per-face-set properties, which
include the following:

   - B{bool isPartition} - must the sets of enumerated faces be
     mutually exclusive? I.e. can the same index appear more than once in
     faceIndices?

   - B{int[] faceCounts} - length of faceCounts is the number of
     distinct groups of faces in this FaceSet. Element i gives the number
     of faces in the i'th group. The membership of each set can be variable
     over time, but the number of groups must be uniform over time, and the
     schema will enforce this.

   - B{int[] faceIndices} - flattened list of all the faces in the
     face-set, with the faces of each group laid out sequentially

   - B{rel binding} - (optional) if authored, possesses as many
     targets as there are groups of faces
     The B{binding} property elevates the schema beyond being purely a
     set; it allows us to effectively customize/specialize each group of
     faces in the set by establishing a relationship per-face-group to
     another prim that contains properties that consumers can consider to
     be overrides to whatever values are provided by the prim that contains
     the faceSets, with the following caveats:

   - This schema makes no specific statement or behavioral constraint
     on what properties should be considered overridable by the target of a
     per-face-group binding. Specific prim schemas that define face-sets
     meaningful to them should declare what the expected behavior should
     be, with respect to their core properties.

   - The targets of a single relationship themselves form a unique
     set. This means that you cannot have two different face-groups in a
     face-set that have the same B{binding} target. You must merge the
     groups into one.
     Note that we have not referred anywhere to meshes or polygons in this
     class.  We use the term "face" generically, as this schema could be
     used equally well to partition curves within a UsdGeomCurves-derived
     schema. Renderer support for variation among curves in batched curves
     primitives is spotty, as of 2015, however.

Here's some sample code to create a face-set on a mesh prim and bind
the different face groups in the face-set to different targets: ::

  UsdGeomMesh mesh(stage.GetPrimAtPath("/path/to/mesh"));
  
  
// Create a face-
set named "look" on the mesh prim.
  UsdGeomFaceSetAPI lookFaceSet = UsdGeomFaceSetAPI::Create(mesh, "look")
  
  VtIntArray faceGroup1, faceGroup2;
  // ... populate faceGroup1 and faceGroup2 with the desired set of face 
  // ... indices.
  
  SdfPath look1Path("/path/to/look1");
  SdfPath look2Path("/path/to/look2");
  
  // Now, bind faceGroup1 to look1 and faceGroup2 to look2.
  lookFaceSet.AppendFaceGroup(faceGroup1, look1Path);
  lookFaceSet.AppendFaceGroup(faceGroup2, look2Path);

An alternate way to author face groups belonging to the face-set would
be to set the face-set properties directly using the API provided in
UsdGeomFaceSetAPI_PropertyValueAPI. ::

  VtIntArray faceCounts(2);
  faceCounts[0] = faceGroup1.size();
  faceCounts[1] = faceGroup2.size();
  lookFaceSet.SetFaceCounts(faceCounts);
  
  VtIntArray faceIndices;
  // ... insert indices from faceGroup1 and faceGroup2 into faceIndices here.
  lookFaceSet.SetFaceIndices(faceIndices);
  
  lookFaceSet.SetBindingTargets([look1Path, look2Path])


"""
   result["FaceSetAPI"].GetFaceIndicesAttr.im_func.func_doc = """GetFaceIndicesAttr() -> USDGEOM_API UsdAttribute



Returns the "faceIndices" attribute associated with the face-set.


C++ Type: VtIntArray  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying

GetFaceIndices()

"""
   result["FaceSetAPI"].GetIsPartitionAttr.im_func.func_doc = """GetIsPartitionAttr() -> USDGEOM_API UsdAttribute



Returns the "isPartition" attribute associated with the face-set.


This attribute deternines whether the set of enumerated faces must be
mutually exclusive.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityUniform

GetIsPartition()

"""
   result["FaceSetAPI"].Create.func_doc = """**static** Create(prim, setName, isPartition) -> USDGEOM_API UsdGeomFaceSetAPI

prim : UsdPrim
setName : TfToken
isPartition : bool


Creates a new face-set on the given C{prim} with the given C{setName}.


The existence of a face-set on a prim is identified by the presence of
the associated isPartition attribute. Hence, this function also
creates the isPartition attribute and sets it to C{isPartition}.


----------------------------------------------------------------------
Create(schemaObj, setName, isPartition) -> USDGEOM_API UsdGeomFaceSetAPI

schemaObj : UsdSchemaBase
setName : TfToken
isPartition : bool


Creates a new face-set with the given C{setName} on the prim held in
the given C{schemaObj}.


The existence of a face-set on a prim is identified by the presence of
the associated isPartition attribute. Hence, this function also
creates the isPartition attribute and sets it to C{isPartition}.

"""
   result["FaceSetAPI"].SetIsPartition.im_func.func_doc = """SetIsPartition(isPartition) -> USDGEOM_API bool

isPartition : bool


Set whether the set of enumerated faces must be mutually exclusive.


If B{isPartition} is true, then any given face index can appear only
once in the B{faceIndices} attribute value belonging to the face-set.

"""
   result["FaceSetAPI"].__init__.im_func.func_doc = """__init__(prim, setName)

prim : UsdPrim
setName : TfToken


Construct a UsdGeomFaceSetAPI with the given C{setName} on the UsdPrim
C{prim}.


----------------------------------------------------------------------
__init__(schemaObj, setName)

schemaObj : UsdSchemaBase
setName : TfToken


Construct a USdGeomFaceSetAPI with the given C{setName} on the prim
held by C{schemaObj}.

"""
   result["FaceSetAPI"].SetFaceCounts.im_func.func_doc = """SetFaceCounts(faceCounts, time) -> USDGEOM_API bool

faceCounts : VtIntArray
time : UsdTimeCode


Sets the lengths of various groups of faces belonging to this face-set
at UsdTimeCode C{time}.


Length of faceCounts is the number of distinct groups of faces in this
face-set. Element i gives the number of faces in the i'th group. The
membership of each set can be variable over time, but the number of
groups must be uniform over time, and this schema will enforce this.

UsdGeomFaceSetAPI::GetFaceCounts()

"""
   result["FaceSetAPI"].CreateBindingTargetsRel.im_func.func_doc = """CreateBindingTargetsRel() -> USDGEOM_API UsdRelationship



Creates the "bindingTargets" relationship associated with the face-set
and returns it.


GetBindingTargetsRel()

"""
   result["FaceSetAPI"].GetBindingTargetsRel.im_func.func_doc = """GetBindingTargetsRel() -> USDGEOM_API UsdRelationship



Returns the "bindingTargets" relationship associated with the face-
set.


GetBindingTargets()

"""
   result["FaceSetAPI"].CreateIsPartitionAttr.im_func.func_doc = """CreateIsPartitionAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


Creates the "isPartition" attribute associated with the face-set.


Create vs Get Property Methods for when to use Get vs Create. If
specified, author C{defaultValue} as the attribute's default, sparsely
(when it makes sense to do so) if C{writeSparsely} is C{true} - the
default for C{writeSparsely} is C{false}.

"""
   result["FaceSetAPI"].GetIsPartition.im_func.func_doc = """GetIsPartition() -> USDGEOM_API bool



Returns whether the set of enumerated faces must be mutually
exclusive.


If this returns true, then any given face index can appear only once
in the B{faceIndices} attribute value belonging to the face-set.

"""
   result["FaceSetAPI"].GetBindingTargets.im_func.func_doc = """GetBindingTargets(bindings) -> USDGEOM_API bool

bindings : SdfPathVector


Returns the B{resolved paths} to target prims that the different
groups of faces in this face-set are bound to.


In a valid face-set, the number of C{bindings} always matches the
number of groups of faces.

"""
   result["FaceSetAPI"].GetFaceCountsAttr.im_func.func_doc = """GetFaceCountsAttr() -> USDGEOM_API UsdAttribute



Returns the "faceCounts" attribute associated with the face-set.


C++ Type: VtIntArray  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying

GetFaceCounts()

"""
   result["FaceSetAPI"].CreateFaceCountsAttr.im_func.func_doc = """CreateFaceCountsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


Creates the "faceCounts" attribute associated with the face-set.


Create vs Get Property Methods for when to use Get vs Create. If
specified, author C{defaultValue} as the attribute's default, sparsely
(when it makes sense to do so) if C{writeSparsely} is C{true} - the
default for C{writeSparsely} is C{false}.

GetFaceCountsAttr()

"""
   result["FaceSetAPI"].SetFaceIndices.im_func.func_doc = """SetFaceIndices(faceIndices, time) -> USDGEOM_API bool

faceIndices : VtIntArray
time : UsdTimeCode


Sets the flattened list of all the faces in the face-set, with the
faces of each group laid out sequentially at UsdTimeCode, C{time}.



UsdGeomFaceSetAPI::GetFaceCounts()

UsdGeomFaceSetAPI::SetFaceIndices()

"""
   result["FaceSetAPI"].SetBindingTargets.im_func.func_doc = """SetBindingTargets(bindings) -> USDGEOM_API bool

bindings : SdfPathVector


Sets the paths to target prims that the different groups of faces in
this face-set are bound to.


The number of C{bindings} should match the number of groups of faces.

"""
   result["FaceSetAPI"].Validate.im_func.func_doc = """Validate(reason) -> USDGEOM_API bool

reason : string


Validates the attribute values belonging to the face-set.


Returns true if the face-set has all valid attribute values. Returns
false and populates the C{reason} output argument if the face-set has
invalid attribute values.

Here's the list of validations performed by this method:
   - If the faceSet is a partition, the face indices must be mutually
     exclusive.

   - The size of faceIndices array should matche the sum of values in
     the faceCounts array.

   - The number of elements in faceCounts must not vary over time.

   - If binding targets exist, their number should match the length of
     the faceCounts array.


"""
   result["FaceSetAPI"].GetFaceSetName.im_func.func_doc = """GetFaceSetName() -> TfToken



Returns the name of the face-set.

"""
   result["FaceSetAPI"].GetFaceIndices.im_func.func_doc = """GetFaceIndices(faceIndices, time) -> USDGEOM_API bool

faceIndices : VtIntArray
time : UsdTimeCode


Returns the flattened list of all the faces in the face-set, with the
faces of each group laid out sequentially at UsdTimeCode, C{time}.



UsdGeomFaceSetAPI::GetFaceCounts()

UsdGeomFaceSetAPI::SetFaceIndices()

"""
   result["FaceSetAPI"].CreateFaceIndicesAttr.im_func.func_doc = """CreateFaceIndicesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


Creates the "faceIndices" attribute associated with the face-set.


Create vs Get Property Methods for when to use Get vs Create. If
specified, author C{defaultValue} as the attribute's default, sparsely
(when it makes sense to do so) if C{writeSparsely} is C{true} - the
default for C{writeSparsely} is C{false}.

GetFaceIndicesAttr()

"""
   result["FaceSetAPI"].GetFaceCounts.im_func.func_doc = """GetFaceCounts(faceCounts, time) -> USDGEOM_API bool

faceCounts : VtIntArray
time : UsdTimeCode


Returns the lengths of various groups of faces belonging to this face-
set at UsdTimeCode C{time}.


Length of faceCounts is the number of distinct groups of faces in this
face-set. Element i gives the number of faces in the i'th group. The
membership of each set can be variable over time, but the number of
groups must be uniform over time, and this schema will enforce this.

UsdGeomFaceSetAPI::GetFaceIndices()

UsdGeomFaceSetAPI::SetFaceCounts()

"""
   result["FaceSetAPI"].GetFaceSets.func_doc = """**static** GetFaceSets(prim) -> USDGEOM_API sequence< UsdGeomFaceSetAPI >

prim : UsdPrim


Returns the list of all face-sets on the given prim, C{prim}.


A face-set will be included in the list only if the corresponding
isPartition attribute is present on the prim.


----------------------------------------------------------------------
GetFaceSets(schemaObj) -> USDGEOM_API sequence< UsdGeomFaceSetAPI >

schemaObj : UsdSchemaBase


Returns the list of all face-sets on the prim held by C{schemaObj}.

"""
   result["FaceSetAPI"].AppendFaceGroup.im_func.func_doc = """AppendFaceGroup(faceIndices, bindingTarget, time) -> USDGEOM_API bool

faceIndices : VtIntArray
bindingTarget : SdfPath
time : UsdTimeCode


Appends a new face group containing the given C{faceIndices} to an
existing face-set at the specified time ordinate, C{time} and binds it
to the given C{bindingTarget}.


Returns true only upon success.

Here are a few things worth noting about this method:

   - The faceCount is gleaned from the length of the C{faceIndices}
     argument.

   - If C{bindingTarget} is empty, but there is already a face-group
     authored with a non-empty bindingTarget, a warning is issued and no
     edits are performed.

   - Similarly, if bindingTarget is not empty, but there is already a
     face-group authored without binding targets, a warning is issued and
     no edits are performed.

   - If the face groups belonging to the face-set are animated, then a
     new face group is B{appended} if there are existing face groups
     authored at the given time ordinate.

   - If there are no existing face groups authored at the given time
     ordinate, then the face group being added will be the only one at
     C{time}.


"""
   result["ModelAPI"].__doc__ = """
UsdGeomModelAPI extends the generic UsdModelAPI schema with geometry
specific concepts such as cached extents for the entire model,
constraint targets, and geometry-inspired extensions to the payload
lofting process.


As described in GetExtentsHint() below, it is useful to cache extents
at the model level. UsdGeomModelAPI provides schema for computing and
storing these cached extents, which can be consumed by
UsdGeomBBoxCache to provide fast access to precomputed extents that
will be used as the model's bounds ( see
UsdGeomBBoxCache::UsdGeomBBoxCache() ).

Draw Modes
==========

Draw modes provide optional alternate imaging behavior for USD
subtrees with kind model. *model:drawMode* (which is inheritable) and
*model:applyDrawMode* (which is not) are resolved into a decision to
stop traversing the scene graph at a certain point, and replace a USD
subtree with proxy geometry.

The value of *model:drawMode* determines the type of proxy geometry:
   - *origin* - Draw the model-space basis vectors of the replaced
     prim.

   - *bounds* - Draw the model-space bounding box of the replaced
     prim.

   - *cards* - Draw textured quads as a placeholder for the replaced
     prim.

   - *default* - An explicit opinion to draw the USD subtree as
     normal.

*model:drawMode* is inheritable so that a whole scene, a large group,
or all prototypes of a model hierarchy PointInstancer can be assigned
a draw mode with a single attribute edit. *model:applyDrawMode* is
meant to be written when an asset is authored, and provides
flexibility for different asset types. For example, a character
assembly (composed of character, clothes, etc) might have
*model:applyDrawMode* set at the top of the subtree so the whole group
can be drawn as a single card object. An effects subtree might have
*model:applyDrawMode* set at a lower level so each particle group
draws individually.

Models of kind component are treated as if *model:applyDrawMode* were
true. This means a prim is drawn with proxy geometry when: the prim
has kind component, and/or *model:applyDrawMode* is set; and the prim
or an ancestor has a non-default value for *model:drawMode*. A value
for *model:drawMode* on a child prim takes precedence over a value on
a parent prim.

Cards Geometry
==============

The specific geometry used in cards mode is controlled by the
*model:cardGeometry* attribute:
   - *cross* - Generate a quad normal to each basis direction and
     negative. Locate each quad so that it bisects the model extents.

   - *box* - Generate a quad normal to each basis direction and
     negative. Locate each quad on a face of the model extents, facing out.

   - *fromTexture* - Generate a quad for each supplied texture from
     attributes stored in that texture's metadata.

For *cross* and *box* mode, the extents are calculated for purposes
*default*, *proxy*, and *render*, at their earliest authored time. If
the model has no textures, all six card faces are rendered using
*model:drawModeColor*. If one or more textures are present, only axes
with one or more textures assigned are drawn. For each axis, if both
textures (positive and negative) are specified, they'll be used on the
corresponding card faces; if only one texture is specified, it will be
mapped to the opposite card face after being flipped on the texture's
s-axis. Any card faces with invalid asset paths will be drawn with
*model:drawModeColor*.

Both *model:cardGeometry* and *model:drawModeColor* should be authored
on the prim where the draw mode takes effect, since these attributes
are not inherited.

For *fromTexture* mode, only card faces with valid textures assigned
are drawn. The geometry is generated by pulling the *worldtoscreen*
attribute out of texture metadata. This is expected to be a 4x4 matrix
mapping the model-space position of the card quad to the clip-space
quad with corners (-1,-1,0) and (1,1,0). The card vertices are
generated by transforming the clip-space corners by the inverse of
*worldtoscreen*. Textures are mapped so that (s) and (t) map to (+x)
and (+y) in clip space. If the metadata cannot be read in the right
format, or the matrix can't be inverted, the card face is not drawn.

All card faces are drawn and textured as single-sided.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdGeomTokens. So to set an attribute to the value "rightHanded",
use UsdGeomTokens->rightHanded as the value.

"""
   result["ModelAPI"].Apply.func_doc = """**static** Apply(prim) -> USDGEOM_API UsdGeomModelAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "GeomModelAPI" to the token-
valued, listOp metadata *apiSchemas* on the prim.

A valid UsdGeomModelAPI object is returned upon success. An invalid
(or empty) UsdGeomModelAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["ModelAPI"].CreateModelCardTextureZPosAttr.im_func.func_doc = """CreateModelCardTextureZPosAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelCardTextureZPosAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].GetExtentsHint.im_func.func_doc = """GetExtentsHint(extents, time) -> USDGEOM_API bool

extents : VtVec3fArray
time : UsdTimeCode


Retrieve the authored value (if any) of this model's "extentsHint".


Persistent caching of bounds in USD is a potentially perilous
endeavor, given that:
   - It is very easy to add overrides in new super-layers that
     invalidate the cached bounds, and no practical way to automatically
     detect when this happens

   - It is possible for references to be allowed to "float", so that
     asset updates can flow directly into cached scenes. Such changes in
     referenced scene description can also invalidate cached bounds in
     referencing layers.
     For these reasons, as a general rule, we only persistently cache leaf
     gprim extents in object space. However, even with cached gprim
     extents, computing bounds can be expensive. Since model-level bounds
     are so useful to many graphics applications, we make an exception,
     with some caveats. The "extentsHint" should be considered entirely
     optional (whereas gprim extent is not); if authored, it should
     contains the extents for various values of gprim purposes. The extents
     for different values of purpose are stored in a linear Vec3f array as
     pairs of GfVec3f values in the order specified by
     UsdGeomImageable::GetOrderedPurposeTokens() . This list is trimmed to
     only include non-empty extents. i.e., if a model has only default and
     render geoms, then it will only have 4 GfVec3f values in its
     extentsHint array. We do not skip over zero extents, so if a model has
     only default and proxy geom, we will author six GfVec3f 's, the middle
     two representing an zero extent for render geometry.

A UsdGeomBBoxCache can be configured to first consult the cached
extents when evaluating model roots, rather than descending into the
models for the full computation. This is not the default behavior, and
gives us a convenient way to validate that the cached extentsHint is
still valid.

C{true} if a value was fetched; C{false} if no value was authored, or
on error. It is an error to make this query of a prim that is not a
model root.

UsdGeomImageable::GetPurposeAttr() ,
UsdGeomImageable::GetOrderedPurposeTokens()

"""
   result["ModelAPI"].CreateModelCardTextureYPosAttr.im_func.func_doc = """CreateModelCardTextureYPosAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelCardTextureYPosAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].GetModelDrawModeAttr.im_func.func_doc = """GetModelDrawModeAttr() -> USDGEOM_API UsdAttribute



Alternate imaging mode; applied to this prim or child prims where
*model:applyDrawMode* is true, or where the prim has kind *component*.


See Draw Modes for mode descriptions.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback  Allowed Values :
[origin, bounds, cards, default]

"""
   result["ModelAPI"].CreateModelCardTextureZNegAttr.im_func.func_doc = """CreateModelCardTextureZNegAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelCardTextureZNegAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].GetModelCardTextureYNegAttr.im_func.func_doc = """GetModelCardTextureYNegAttr() -> USDGEOM_API UsdAttribute



In *cards* imaging mode, the texture applied to the Y- quad.


The texture axes (s,t) are mapped to model-space axes (-x, -z).

C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["ModelAPI"].CreateConstraintTarget.im_func.func_doc = """CreateConstraintTarget(constraintName) -> USDGEOM_API UsdGeomConstraintTarget

constraintName : string


Creates a new constraint target with the given name,
C{constraintName}.


If the constraint target already exists, then the existing target is
returned. If it does not exist, a new one is created and returned.

"""
   result["ModelAPI"].ComputeExtentsHint.im_func.func_doc = """ComputeExtentsHint(bboxCache) -> USDGEOM_API VtVec3fArray

bboxCache : BBoxCache


For the given model, compute the value for the extents hint with the
given C{bboxCache}.


C{bboxCache} should be setup with the appropriate time. After calling
this function, the C{bboxCache} may have it's included purposes
changed.

C{bboxCache} should not be in use by any other thread while this
method is using it in a thread.

"""
   result["ModelAPI"].GetModelCardTextureXNegAttr.im_func.func_doc = """GetModelCardTextureXNegAttr() -> USDGEOM_API UsdAttribute



In *cards* imaging mode, the texture applied to the X- quad.


The texture axes (s,t) are mapped to model-space axes (y, -z).

C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["ModelAPI"].GetModelCardTextureZPosAttr.im_func.func_doc = """GetModelCardTextureZPosAttr() -> USDGEOM_API UsdAttribute



In *cards* imaging mode, the texture applied to the Z+ quad.


The texture axes (s,t) are mapped to model-space axes (x, -y).

C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["ModelAPI"].CreateModelDrawModeColorAttr.im_func.func_doc = """CreateModelDrawModeColorAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelDrawModeColorAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].GetModelDrawModeColorAttr.im_func.func_doc = """GetModelDrawModeColorAttr() -> USDGEOM_API UsdAttribute



The base color of imaging prims inserted for alternate imaging modes.


For *origin* and *bounds* modes, this controls line color; for *cards*
mode, this controls the fallback quad color. If unspecified, it should
be interpreted as (0.18, 0.18, 0.18).

C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Float3  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["ModelAPI"].GetExtentsHintAttr.im_func.func_doc = """GetExtentsHintAttr() -> USDGEOM_API UsdAttribute



Returns the custom 'extentsHint' attribute if it exits.

"""
   result["ModelAPI"].GetModelCardTextureZNegAttr.im_func.func_doc = """GetModelCardTextureZNegAttr() -> USDGEOM_API UsdAttribute



In *cards* imaging mode, the texture applied to the Z- quad.


The texture axes (s,t) are mapped to model-space axes (-x, -y).

C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["ModelAPI"].SetExtentsHint.im_func.func_doc = """SetExtentsHint(extents, time) -> USDGEOM_API bool

extents : VtVec3fArray
time : UsdTimeCode


Authors the extentsHint array for this model at the given time.



GetExtentsHint()

"""
   result["ModelAPI"].CreateModelCardTextureXPosAttr.im_func.func_doc = """CreateModelCardTextureXPosAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelCardTextureXPosAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].GetModelCardTextureYPosAttr.im_func.func_doc = """GetModelCardTextureYPosAttr() -> USDGEOM_API UsdAttribute



In *cards* imaging mode, the texture applied to the Y+ quad.


The texture axes (s,t) are mapped to model-space axes (x, -z).

C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["ModelAPI"].CreateModelApplyDrawModeAttr.im_func.func_doc = """CreateModelApplyDrawModeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelApplyDrawModeAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].GetConstraintTargets.im_func.func_doc = """GetConstraintTargets() -> USDGEOM_API sequence< UsdGeomConstraintTarget >



Returns all the constraint targets belonging to the model.


Only valid constraint targets in the "constraintTargets" namespace are
returned by this method.

"""
   result["ModelAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["ModelAPI"].CreateModelDrawModeAttr.im_func.func_doc = """CreateModelDrawModeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelDrawModeAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].CreateModelCardTextureXNegAttr.im_func.func_doc = """CreateModelCardTextureXNegAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelCardTextureXNegAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].GetModelApplyDrawModeAttr.im_func.func_doc = """GetModelApplyDrawModeAttr() -> USDGEOM_API UsdAttribute



If true, and this prim or parent prims have *model:drawMode* set,
apply an alternate imaging mode to this prim.


See Draw Modes.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["ModelAPI"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomModelAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomModelAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomModelAPI(stage->GetPrimAtPath(path));


"""
   result["ModelAPI"].GetModelCardGeometryAttr.im_func.func_doc = """GetModelCardGeometryAttr() -> USDGEOM_API UsdAttribute



The geometry to generate for imaging prims inserted for *cards*
imaging mode.


See Cards Geometry for geometry descriptions. If unspecified, it
should be interpreted as *cross*.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback  Allowed Values :
[cross, box, fromTexture]

"""
   result["ModelAPI"].ComputeModelDrawMode.im_func.func_doc = """ComputeModelDrawMode() -> USDGEOM_API TfToken



Calculate the effective model:drawMode of this prim, as defined by its
closest ancestral authored opinion, if any.


If no opinion for model:drawMode is authored on this prim or any of
its ancestors, its computed model:drawMode is UsdGeomTokens->default_
. Otherwise, its computed model:drawMode is that of its closest
ancestor with an authored model:drawMode.

This function should be considered a reference implementation for
correctness. B{If called on each prim in the context of a traversal we
will perform massive overcomputation, because sibling prims share sub-
problems in the query that can be efficiently cached, but are not
(cannot be) by this simple implementation.} If you have control of
your traversal, it will be far more efficient to manage model:drawMode
on a stack as you traverse.

GetModelDrawModeAttr()

"""
   result["ModelAPI"].CreateModelCardTextureYNegAttr.im_func.func_doc = """CreateModelCardTextureYNegAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelCardTextureYNegAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].CreateModelCardGeometryAttr.im_func.func_doc = """CreateModelCardGeometryAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetModelCardGeometryAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ModelAPI"].GetConstraintTarget.im_func.func_doc = """GetConstraintTarget(constraintName) -> USDGEOM_API UsdGeomConstraintTarget

constraintName : string


Get the constraint target with the given name, C{constraintName}.


If the requested constraint target does not exist, then an invalid
UsdConstraintTarget object is returned.

"""
   result["ModelAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomModelAPI on UsdPrim C{prim}.


Equivalent to UsdGeomModelAPI::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomModelAPI on the prim held by C{schemaObj}.


Should be preferred over UsdGeomModelAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["ModelAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["ModelAPI"].GetModelCardTextureXPosAttr.im_func.func_doc = """GetModelCardTextureXPosAttr() -> USDGEOM_API UsdAttribute



In *cards* imaging mode, the texture applied to the X+ quad.


The texture axes (s,t) are mapped to model-space axes (-y, -z).

C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Imageable"].__doc__ = """
Base class for all prims that may require rendering or visualization
of some sort.


The primary attributes of Imageable are *visibility* and *purpose*,
which each provide instructions for what geometry should be included
for processing by rendering and other computations.

<Deprecated>Imageable also provides API for accessing primvars, which
have been moved to the UsdGeomPrimvarsAPI schema. This API is planned
to be removed, UsdGeomPrimvarsAPI should be used directly instead.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdGeomTokens. So to set an attribute to the value "rightHanded",
use UsdGeomTokens->rightHanded as the value.

"""
   result["Imageable"].HasPrimvar.im_func.func_doc = """HasPrimvar(name) -> USDGEOM_API bool

name : TfToken


Is there a defined Primvar C{name} on this prim?


Name lookup will account for Primvar namespacing.

GetPrimvar()

"""
   result["Imageable"].CreateVisibilityAttr.im_func.func_doc = """CreateVisibilityAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVisibilityAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Imageable"].CreatePrimvar.im_func.func_doc = """CreatePrimvar(attrName, typeName, interpolation, elementSize) -> USDGEOM_API UsdGeomPrimvar

attrName : TfToken
typeName : SdfValueTypeName
interpolation : TfToken
elementSize : int


Author scene description to create an attribute on this prim that will
be recognized as Primvar (i.e.


will present as a valid UsdGeomPrimvar).

The name of the created attribute may or may not be the specified
C{attrName}, due to the possible need to apply property namespacing
for primvars. See Creating and Accessing Primvars for more
information. Creation may fail and return an invalid Primvar if
C{attrName} contains a reserved keyword, such as the "indices" suffix
we use for indexed primvars.

The behavior with respect to the provided C{typeName} is the same as
for UsdAttributes::Create(), and C{interpolation} and C{elementSize}
are as described in UsdGeomPrimvar::GetInterpolation() and
UsdGeomPrimvar::GetElementSize() .

If C{interpolation} and/or C{elementSize} are left unspecified, we
will author no opinions for them, which means any (strongest) opinion
already authored in any contributing layer for these fields will
become the Primvar's values, or the fallbacks if no opinions have been
authored.

an invalid UsdGeomPrimvar if we failed to create a valid attribute, a
valid UsdGeomPrimvar otherwise. It is not an error to create over an
existing, compatible attribute.

UsdPrim::CreateAttribute() , UsdGeomPrimvar::IsPrimvar()

"""
   result["Imageable"].CreateProxyPrimRel.im_func.func_doc = """CreateProxyPrimRel() -> USDGEOM_API UsdRelationship



See GetProxyPrimRel() , and also Create vs Get Property Methods for
when to use Get vs Create.

"""
   result["Imageable"].ComputeUntransformedBound.im_func.func_doc = """ComputeUntransformedBound(time, purpose1, purpose2, purpose3, purpose4) -> USDGEOM_API GfBBox3d

time : UsdTimeCode
purpose1 : TfToken
purpose2 : TfToken
purpose3 : TfToken
purpose4 : TfToken


Compute the untransformed bound of this prim, at the specified
C{time}, and for the specified purposes.


The bound of the prim is computed in its object space, ignoring any
transforms authored on or above the prim.

It is an error to not specify any purposes, which will result in the
return of an empty box.

B{If you need to compute bounds for multiple prims on a stage, it will
be much, much more efficient to instantiate a UsdGeomBBoxCache and
query it directly; doing so will reuse sub-computations shared by the
prims.}

"""
   result["Imageable"].ComputeVisibility.im_func.func_doc = """ComputeVisibility(time) -> USDGEOM_API TfToken

time : UsdTimeCode


Calculate the effective visibility of this prim, as defined by its
most ancestral authored "invisible" opinion, if any.


A prim is considered visible at the current C{time} if none of its
Imageable ancestors express an authored "invisible" opinion, which is
what leads to the "simple pruning" behavior described in
GetVisibilityAttr() .

This function should be considered a reference implementation for
correctness. B{If called on each prim in the context of a traversal we
will perform massive overcomputation, because sibling prims share sub-
problems in the query that can be efficiently cached, but are not
(cannot be) by this simple implementation.} If you have control of
your traversal, it will be far more efficient to manage visibility on
a stack as you traverse.

GetVisibilityAttr()

"""
   result["Imageable"].MakeVisible.im_func.func_doc = """MakeVisible(time) -> USDGEOM_API void

time : UsdTimeCode


Make the imageable visible if it is invisible at the given time.


Since visibility is pruning, this may need to override some ancestor's
visibility and all-but-one of the ancestor's children's visibility,
for all the ancestors of this prim up to the highest ancestor that is
explicitly invisible, to preserve the visibility state.

If MakeVisible() (or MakeInvisible() ) is going to be applied to all
the prims on a stage, ancestors must be processed prior to descendants
to get the correct behavior.

When visibility is animated, this only works when it is invoked
sequentially at increasing time samples. If visibility is already
authored and animated in the scene, calling MakeVisible() at an
arbitrary (in-between) frame isn't guaranteed to work.

This will only work properly if all ancestor prims of the imageable
are B{defined}, as the imageable schema is only valid on defined
prims.

Be sure to set the edit target to the layer containing the strongest
visibility opinion or to a stronger layer.

MakeInvisible()

ComputeVisibility()

"""
   result["Imageable"].GetVisibilityAttr.im_func.func_doc = """GetVisibilityAttr() -> USDGEOM_API UsdAttribute



Visibility is meant to be the simplest form of "pruning" visibility
that is supported by most DCC apps.


Visibility is animatable, allowing a sub-tree of geometry to be
present for some segment of a shot, and absent from others; unlike the
action of deactivating geometry prims, invisible geometry is still
available for inspection, for positioning, for defining volumes, etc.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: inherited  Allowed Values :
[inherited, invisible]

"""
   result["Imageable"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomImageable

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomImageable holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomImageable(stage->GetPrimAtPath(path));


"""
   result["Imageable"].FindInheritedPrimvars.im_func.func_doc = """FindInheritedPrimvars() -> USDGEOM_API sequence< UsdGeomPrimvar >



Like GetPrimvars() , but searches instead for authored primvars
inherited from ancestor prims.


Primvars are only inherited if they do not exist on the prim itself.
The returned primvars will be bound to attributes on the corresponding
ancestor prims. Only primvars with authored values are inherited;
fallback values are not inherited. The order of the returned primvars
is undefined.

"""
   result["Imageable"].GetPrimvar.im_func.func_doc = """GetPrimvar(name) -> USDGEOM_API UsdGeomPrimvar

name : TfToken


Return the Primvar attribute named by C{name}, which will be valid if
a Primvar attribute definition already exists.


Name lookup will account for Primvar namespacing, which means that
this method will succeed in some cases where ::

  UsdGeomPrimvar(prim->GetAttribute(name))

 will not, unless C{name} is properly namespace prefixed.

HasPrimvar()

"""
   result["Imageable"].ComputeWorldBound.im_func.func_doc = """ComputeWorldBound(time, purpose1, purpose2, purpose3, purpose4) -> USDGEOM_API GfBBox3d

time : UsdTimeCode
purpose1 : TfToken
purpose2 : TfToken
purpose3 : TfToken
purpose4 : TfToken


Compute the bound of this prim in world space, at the specified
C{time}, and for the specified purposes.


The bound of the prim is computed, including the transform (if any)
authored on the node itself, and then transformed to world space.

It is an error to not specify any purposes, which will result in the
return of an empty box.

B{If you need to compute bounds for multiple prims on a stage, it will
be much, much more efficient to instantiate a UsdGeomBBoxCache and
query it directly; doing so will reuse sub-computations shared by the
prims.}

"""
   result["Imageable"].ComputePurpose.im_func.func_doc = """ComputePurpose() -> USDGEOM_API TfToken



Calculate the effective purpose of this prim, as defined by its most
ancestral authored non-"default" opinion, if any.


If no opinion for purpose is authored on prim or any of its ancestors,
its computed purpose is UsdGeomTokens->default_ . Otherwise, its
computed purpose is that of its highest ancestor with an authored
purpose of something other than UsdGeomTokens->default_

In other words, all of a stage's root prims inherit the *purpose*
UsdGeomTokens->default_ from the pseudoroot, and that value will be
B{inherited} by all of their descendants, until a
descendant</Some/path/to/nonDefault>contains some other, authored
value of *purpose*. The computed purpose of that prim B{and all of its
descendants} will be that prim's authored value, regardless of what
*putpose* opinions its own descendant prims may express.

This function should be considered a reference implementation for
correctness. B{If called on each prim in the context of a traversal we
will perform massive overcomputation, because sibling prims share sub-
problems in the query that can be efficiently cached, but are not
(cannot be) by this simple implementation.} If you have control of
your traversal, it will be far more efficient to manage purpose, along
with visibility, on a stack as you traverse.

GetPurposeAttr()

"""
   result["Imageable"].SetProxyPrim.im_func.func_doc = """SetProxyPrim(proxy) -> USDGEOM_API bool

proxy : UsdPrim


Convenience function for authoring the *renderProxy* rel on this prim
to target the given C{proxy} prim.


To facilitate authoring on sparse or unloaded stages, we do not
perform any validation of this prim's purpose or the type or purpoes
of the specified prim.

ComputeProxyPrim() , GetProxyPrimRel()


----------------------------------------------------------------------
SetProxyPrim(proxy) -> USDGEOM_API bool

proxy : UsdSchemaBase


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Imageable"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomImageable on UsdPrim C{prim}.


Equivalent to UsdGeomImageable::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomImageable on the prim held by C{schemaObj}.


Should be preferred over UsdGeomImageable (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Imageable"].HasInheritedPrimvar.im_func.func_doc = """HasInheritedPrimvar(name) -> USDGEOM_API bool

name : TfToken


Is there an inherited Primvar C{name} on this prim? The name given is
the primvar name, not its underlying attribute name.



FindInheritedPrimvar()

"""
   result["Imageable"].GetPurposeAttr.im_func.func_doc = """GetPurposeAttr() -> USDGEOM_API UsdAttribute



Purpose is a concept we have found useful in our pipeline for
classifying geometry into categories that can each be independently
included or excluded from traversals of prims on a stage, such as
rendering or bounding-box computation traversals.


The fallback purpose, *default* indicates that a prim has "no special
purpose" and should generally be included in all traversals. Subtrees
rooted at a prim with purpose *render* should generally only be
included when performing a "final quality" render. Subtrees rooted at
a prim with purpose *proxy* should generally only be included when
performing a lightweight proxy render (such as openGL). Finally,
subtrees rooted at a prim with purpose *guide* should generally only
be included when an interactive application has been explicitly asked
to "show guides".

In the previous paragraph, when we say "subtrees rooted at a prim", we
mean the most ancestral or tallest subtree that has an authored, non-
default opinion. If the purpose of</RootPrim>is set to "render", then
the effective purpose of</RootPrim/ChildPrim>will be "render" even if
that prim has a different authored value for purpose. B{See
ComputePurpose() for details of how purpose inherits down namespace}.

As demonstrated in UsdGeomBBoxCache, a traverser should be ready to
accept combinations of included purposes as an input.

Purpose *render* can be useful in creating "light blocker" geometry
for raytracing interior scenes. Purposes *render* and *proxy* can be
used together to partition a complicated model into a lightweight
proxy representation for interactive use, and a fully realized,
potentially quite heavy, representation for rendering. One can use
UsdVariantSets to create proxy representations, but doing so requires
that we recompose parts of the UsdStage in order to change to a
different runtime level of detail, and that does not interact well
with the needs of multithreaded rendering. Purpose provides us with a
better tool for dynamic, interactive complexity management.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: default  Allowed Values :
[default, render, proxy, guide]

"""
   result["Imageable"].MakeInvisible.im_func.func_doc = """MakeInvisible(time) -> USDGEOM_API void

time : UsdTimeCode


Makes the imageable invisible if it is visible at the given time.



When visibility is animated, this only works when it is invoked
sequentially at increasing time samples. If visibility is already
authored and animated in the scene, calling MakeVisible() at an
arbitrary (in-between) frame isn't guaranteed to work.

Be sure to set the edit target to the layer containing the strongest
visibility opinion or to a stronger layer.

MakeVisible()

ComputeVisibility()

"""
   result["Imageable"].GetPrimvars.im_func.func_doc = """GetPrimvars() -> USDGEOM_API sequence< UsdGeomPrimvar >



Return valid UsdGeomPrimvar objects for all defined Primvars on this
prim.


Although we hope eventually to make this faster, this is currently a
fairly expensive operation. If you know you'll need to process other
attributes as well, you might do better by fetching all the attributes
at once, and using the pattern described in Using Primvars to test
individual attributes.

"""
   result["Imageable"].FindInheritedPrimvar.im_func.func_doc = """FindInheritedPrimvar(name) -> USDGEOM_API UsdGeomPrimvar

name : TfToken


Like GetPrimvar() , but searches instead for the named primvar
inherited on ancestor prim.


Primvars are only inherited if they do not exist on the prim itself.
The returned primvar will be bound to the attribute on the
corresponding ancestor prim.

"""
   result["Imageable"].GetOrderedPurposeTokens.func_doc = """**static** GetOrderedPurposeTokens() -> USDGEOM_API  TfTokenVector



Returns an ordered list of allowed values of the purpose attribute.


The ordering is important because it defines the protocol between
UsdGeomModelAPI and UsdGeomBBoxCache for caching and retrieving
extents hints by purpose.

The order is: [default, render, proxy, guide]

See

UsdGeomModelAPI::GetExtentsHint() .

GetOrderedPurposeTokens()

"""
   result["Imageable"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Imageable"].ComputeLocalToWorldTransform.im_func.func_doc = """ComputeLocalToWorldTransform(time) -> USDGEOM_API GfMatrix4d

time : UsdTimeCode


Compute the transformation matrix for this prim at the given time,
including the transform authored on the Prim itself, if present.


B{If you need to compute the transform for multiple prims on a stage,
it will be much, much more efficient to instantiate a
UsdGeomXformCache and query it directly; doing so will reuse sub-
computations shared by the prims.}

"""
   result["Imageable"].ComputeParentToWorldTransform.im_func.func_doc = """ComputeParentToWorldTransform(time) -> USDGEOM_API GfMatrix4d

time : UsdTimeCode


Compute the transformation matrix for this prim at the given time,
*NOT* including the transform authored on the prim itself.


B{If you need to compute the transform for multiple prims on a stage,
it will be much, much more efficient to instantiate a
UsdGeomXformCache and query it directly; doing so will reuse sub-
computations shared by the prims.}

"""
   result["Imageable"].CreatePurposeAttr.im_func.func_doc = """CreatePurposeAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetPurposeAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Imageable"].ComputeLocalBound.im_func.func_doc = """ComputeLocalBound(time, purpose1, purpose2, purpose3, purpose4) -> USDGEOM_API GfBBox3d

time : UsdTimeCode
purpose1 : TfToken
purpose2 : TfToken
purpose3 : TfToken
purpose4 : TfToken


Compute the bound of this prim in local space, at the specified
C{time}, and for the specified purposes.


The bound of the prim is computed, including the transform (if any)
authored on the node itself.

It is an error to not specify any purposes, which will result in the
return of an empty box.

B{If you need to compute bounds for multiple prims on a stage, it will
be much, much more efficient to instantiate a UsdGeomBBoxCache and
query it directly; doing so will reuse sub-computations shared by the
prims.}

"""
   result["Imageable"].GetAuthoredPrimvars.im_func.func_doc = """GetAuthoredPrimvars() -> USDGEOM_API sequence< UsdGeomPrimvar >



Like GetPrimvars() , but exclude primvars that have no authored scene
description.

"""
   result["Imageable"].GetProxyPrimRel.im_func.func_doc = """GetProxyPrimRel() -> USDGEOM_API UsdRelationship



The *proxyPrim* relationship allows us to link a prim whose *purpose*
is "render" to its (single target) purpose="proxy" prim.


This is entirely optional, but can be useful in several scenarios:

   - In a pipeline that does pruning (for complexity management) by
     deactivating prims composed from asset references, when we deactivate
     a purpose="render" prim, we will be able to discover and additionally
     deactivate its associated purpose="proxy" prim, so that preview
     renders reflect the pruning accurately.

   - DCC importers may be able to make more aggressive optimizations
     for interactive processing and display if they can discover the proxy
     for a given render prim.

   - With a little morework, a Hydra-based application will be able to
     map a picked proxy prim back to its render geometry for selection.

It is only valid to author the proxyPrim relationship on prims whose
purpose is "render".

"""
   result["Imageable"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Primvar"].__doc__ = """
Schema wrapper for UsdAttribute for authoring and introspecting
attributes that are primvars.


UsdGeomPrimvar provides API for authoring and retrieving the
additional data required to encode an attribute as a "Primvar", which
is a convenient contraction of RenderMan's "Primitive Variable"
concept, which is represented in Alembic as "arbitrary geometry
parameters" (arbGeomParams).

This includes the attribute's interpolation across the primitive
(which RenderMan refers to as its class specifier and Alembic as its
"geometry scope" ); it also includes the attribute's elementSize,
which states how many values in the value array must be aggregated for
each element on the primitive. An attribute's TypeName also factors
into the encoding of Primvar.

What is the Purpose of a Primvar?
=================================

There are three key aspects of Primvar identity:
   - Primvars define a value that can vary across the primitive on
     which they are defined, via prescribed interpolation rules

   - Taken collectively on a prim, its Primvars describe the "per-
     primitiveoverrides" to the material to which the prim is bound.
     Different renderers may communicate the variables to the shaders using
     different mechanisms over which Usd has no control; Primvars simply
     provide the classification that any renderer should use to locate
     potential overrides. Do please note that primvars override parameters
     on UsdShadeShader objects, *not* Interface Attributes on
     UsdShadeMaterial prims.

   - *Primvars inherit down scene namespace.* Regular USD attributes
     only apply to the prim on which they are specified, but primvars
     implicitly also apply to any child prims, unless those child prims
     have their own opinions about those primvars. This capability
     necessarily entails added cost to check for inherited values, but the
     benefit is that it allows concise encoding of certain opinions that
     broadly affect large amounts of geometry. See
     UsdGeomImageable::FindInheritedPrimvars() .

Creating and Accessing Primvars
===============================

The B{only} way to create a new Primvar in scene description is by
calling UsdGeomImageable::CreatePrimvar() . One cannot "enhance" or
"promote" an already existing attribute into a Primvar, because doing
so may require a namespace edit to rename the attribute, which cannot,
in general, be done within a single UsdEditContext. Instead, create a
new UsdGeomPrimvar using UsdGeomImageable::CreatePrimvar() , and then
copy the existing attribute onto the new UsdGeomPrimvar.

Primvar names can contain arbitrary sub-namespaces. The behavior of
UsdGeomImageable::GetPrimvar(TfToken const & name) is to prepend
"primvars:" onto 'name' if it is not already a prefix, and return the
result, which means we do not have any ambiguity between the primvars
"primvars:nsA:foo" and "primvars:nsB:foo". B{There are reserved
keywords that may not be used as the base names of primvars,} and
attempting to create Primvars of these names will result in a coding
error. The reserved keywords are tokens the Primvar uses internally to
encode various features, such as the "indices" keyword used by Indexed
Primvars.

If a client wishes to access an already-extant attribute as a Primvar,
(which may or may not actually be valid Primvar), they can use the
speculative constructor like so: ::

  if (UsdGeomPrimvar primvar = UsdGeomPrimvar(usdAttr)){
      TfToken interpolation = primvar.GetInterpolation();
      int     elementSize = primvar.GetElementSize();
      ...
  }

(or if you possess UsdProperty objects instead, as the result of a
UsdPrim::GetProperties() call...) ::

  if (UsdGeomPrimvar primvar = UsdGeomPrimvar(usdProp.As<UsdAttribute>())){
  }

Python does not permit the 'assignment in conditional" pattern, so the
above example in python would be: ::

  primvar = Usd.Primvar(usdAttr)
  if primvar:
      interpolation = primvar.GetInterpolation()
      elementSize = primvar.GetElementSize()
      ...

As discussed in greater detail in Indexed Primvars, primvars can
optionally contain a (possibly time-varying) indexing attribute that
establishes a sharing topology for elements of the primvar. Consumers
can always chose to ignore the possibility of indexed data by
exclusively using the ComputeFlattened() API. If a client wishes to
preserve indexing in their processing of a primvar, we suggest a
pattern like the following, which accounts for the fact that a
stronger layer can block a primvar's indexing from a weaker layer, via
UsdGeomPrimvar::BlockIndices() : ::

  VtValue values;
  VtIntArray indices;
  
  if (primvar.Get(&values, timeCode)){
      if (primvar.GetIndices(&indices, timeCode)){
          // primvar is indexed: validate/process values and indices together
      }
      else {
          // primvar is not indexed: validate/process values as flat array
      }
  }

UsdGeomPrimvar presents a small slice of the UsdAttribute API - enough
to extract the data that comprises the "Declaration info", and get/set
of the attribute value. A UsdGeomPrimvar also auto-converts to
UsdAttribute, so you can pass a UsdGeomPrimvar to any function that
accepts a UsdAttribute or const-ref thereto.

Primvar Allowed Scene Description Types and Plurality
=====================================================

There are no limitations imposed on the allowable scene description
types for Primvars; it is the responsibility of each consuming client
to perform renderer-specific conversions, if need be (the USD
distribution will include reference RenderMan conversion utilities).

A note about type plurality of Primvars: It is legitimate for a
Primvar to be of scalar or array type, and again, consuming clients
must be prepared to accommodate both. However, while it is not
possible, in all cases, for USD to *prevent* one from *changing* the
type of an attribute in different layers or variants of an asset, it
is never a good idea to do so. This is relevant because, except in a
few special cases, it is not possible to encode an *interpolation* of
any value greater than *constant* without providing multiple (i.e.
array) data values. Therefore, if there is any possibility that
downstream clients might need to change a Primvar's interpolation, the
Primvar-creator should encode it as an array rather than a scalar.

Why allow scalar values at all, then? First, sometimes it brings
clarity to (use of) a shader's API to acknowledge that some parameters
are meant to be single-valued over a shaded primitive. Second, many
DCC's provide far richer affordances for editing scalars than they do
array values, and we feel it is safer to let the content creator make
the decision/tradeoff of which kind of flexibility is more relevant,
rather than leaving it to an importer/exporter pair to interpret.

Also, like all attributes, Primvars can be time-sampled, and values
can be authored and consumed just as any other attribute. There is
currently no validation that the length of value arrays matches to the
size required by a gprim's topology, interpolation, and elementSize.

For consumer convenience, we provide GetDeclarationInfo() , which
returns all the type information (other than topology) needed to
compute the required array size, which is also all the information
required to prepare the Primvar's value for consumption by a renderer.

Lifetime Management and Primvar Validity
========================================

UsdGeomPrimvar has an explicit bool operator that validates that the
attribute IsDefined() and thus valid for querying and authoring values
and metadata. This is a fairly expensive query that we do B{not}
cache, so if client code retains UsdGeomPrimvar objects, it should
manage its object validity closely, for performance. An ideal pattern
is to listen for UsdNotice::StageContentsChanged notifications, and
revalidate/refetch its retained UsdGeomPrimvar s only then, and
otherwise use them without validity checking.

Interpolation of Geometric Primitive Variables
==============================================

In the following explanation of the meaning of the various
kinds/levels of Primvar interpolation, each bolded bullet gives the
name of the token in UsdGeomTokens that provides the value. So to set
a Primvar's interpolation to "varying", one would: ::

  primvar.SetInterpolation(UsdGeomTokens->varying);

Reprinted and adapted from the RPS documentation, which contains
further details, *interpolation* describes how the Primvar will be
interpolated over the uv parameter space of a surface primitive (or
curve or pointcloud). The possible values are:
   - B{constant} One value remains constant over the entire surface
     primitive.

   - B{uniform} One value remains constant for each uv patch segment
     of the surface primitive (which is a *face* for meshes).

   - B{varying} Four values are interpolated over each uv patch
     segment of the surface. Bilinear interpolation is used for
     interpolation between the four values.

   - B{vertex} Values are interpolated between each vertex in the
     surface primitive. The basis function of the surface is used for
     interpolation between vertices.

   - B{faceVarying} For polygons and subdivision surfaces, four values
     are interpolated over each face of the mesh. Bilinear interpolation is
     used for interpolation between the four values.

UsdGeomPrimvar As Example of Attribute Schema
=============================================

Just as UsdSchemaBase and its subclasses provide the pattern for how
to layer schema onto the generic UsdPrim object, UsdGeomPrimvar
provides an example of how to layer schema onto a generic UsdAttribute
object. In both cases, the schema object wraps and contains the
UsdObject.

Primvar Namespace Inheritance
=============================

Primvar values can be inherited down namespace. That is, a primvar
value set on a prim will also apply to any child prims, unless those
children have their own opinions about those named primvars.

UsdGeomImageable::FindInheritedPrimvars() .

"""
   result["Primvar"].__init__.im_func.func_doc = """__init__()



----------------------------------------------------------------------
__init__(attr) -> USDGEOM_API

attr : UsdAttribute


Speculative constructor that will produce a valid UsdGeomPrimvar when
C{attr} already represents an attribute that is Primvar, and produces
an *invalid* Primvar otherwise (i.e.


operator bool() will return false).

Calling C{UsdGeomPrimvar::IsPrimvar(attr)} will return the same truth
value as this constructor, but if you plan to subsequently use the
Primvar anyways, just use this constructor, as demonstrated in the
class documentation.


----------------------------------------------------------------------
__init__(prim, attrName, typeName)

prim : UsdPrim
attrName : TfToken
typeName : SdfValueTypeName


Factory for UsdGeomImageable 's use, so that we can encapsulate the
logic of what discriminates Primvar in this class, while preserving
the pattern that attributes can only be created via their container
objects.


The name of the created attribute may or may not be the specified
C{attrName}, due to the possible need to apply property namespacing
for Primvar.

The behavior with respect to the provided C{typeName} is the same as
for UsdAttributes::Create().

an invalid UsdGeomPrimvar if we failed to create a valid attribute, a
valid UsdGeomPrimvar otherwise. It is not an error to create over an
existing, compatible attribute. It is a failed verification for
C{prim} to be invalid/expired

UsdPrim::CreateAttribute()

"""
   result["Primvar"].IsDefined.im_func.func_doc = """IsDefined() -> bool



Return true if the wrapped UsdAttribute::IsDefined() , and in addition
the attribute is identified as a Primvar.

"""
   result["Primvar"].SetElementSize.im_func.func_doc = """SetElementSize(eltSize) -> USDGEOM_API bool

eltSize : int


Set the elementSize for this Primvar.


Errors and returns false if C{eltSize} less than 1.

GetElementSize()

"""
   result["Primvar"].GetTimeSamples.im_func.func_doc = """GetTimeSamples(times) -> USDGEOM_API bool

times : sequence<double>


Populates a vector with authored sample times for this primvar.


Returns false on error.

This considers any timeSamples authored on the associated "indices"
attribute if the primvar is indexed.

UsdAttribute::GetTimeSamples

"""
   result["Primvar"].SplitName.im_func.func_doc = """SplitName() -> sequence<string>




UsdAttribute::SplitName()

"""
   result["Primvar"].GetTypeName.im_func.func_doc = """GetTypeName() -> SdfValueTypeName




UsdAttribute::GetTypeName()

"""
   result["Primvar"].SetInterpolation.im_func.func_doc = """SetInterpolation(interpolation) -> USDGEOM_API bool

interpolation : TfToken


Set the Primvar's interpolation.


Errors and returns false if C{interpolation} is out of range as
defined by IsValidInterpolation() . No attempt is made to validate
that the Primvar's value contains the right number of elements to
match its interpolation to its topology.

GetInterpolation() , Interpolation of Geometric Primitive Variables

"""
   result["Primvar"].Get.im_func.func_doc = """Get(value, time) -> bool

value : T
time : UsdTimeCode


Get the attribute value of the Primvar at C{time}.



Usd_Handling_Indexed_Primvars for proper handling of indexed primvars


----------------------------------------------------------------------
Get(value, time) -> USDGEOM_API bool

value : string
time : UsdTimeCode


----------------------------------------------------------------------
Get(value, time) -> USDGEOM_API bool

value : VtStringArray
time : UsdTimeCode


----------------------------------------------------------------------
Get(value, time) -> USDGEOM_API bool

value : VtValue
time : UsdTimeCode

"""
   result["Primvar"].GetNamespace.im_func.func_doc = """GetNamespace() -> TfToken




UsdAttribute::GetNamespace()

"""
   result["Primvar"].GetAttr.im_func.func_doc = """GetAttr() -> UsdAttribute



Explicit UsdAttribute extractor.

"""
   result["Primvar"].GetDeclarationInfo.im_func.func_doc = """GetDeclarationInfo(name, typeName, interpolation, elementSize) -> USDGEOM_API void

name : TfToken
typeName : SdfValueTypeName
interpolation : TfToken
elementSize : int


Convenience function for fetching all information required to properly
declare this Primvar.


The C{name} returned is the "client name", stripped of the "primvars"
namespace, i.e. equivalent to GetPrimvarName()

May also be more efficient than querying key individually.

"""
   result["Primvar"].BlockIndices.im_func.func_doc = """BlockIndices() -> USDGEOM_API void



Block the indices that were previously set.


This effectively makes an indexed primvar no longer indexed. This is
useful when overriding an existing primvar.

"""
   result["Primvar"].IsPrimvar.func_doc = """**static** IsPrimvar(attr) -> USDGEOM_API bool

attr : UsdAttribute


Test whether a given UsdAttribute represents valid Primvar, which
implies that creating a UsdGeomPrimvar from the attribute will
succeed.


Success implies that C{attr.IsDefined()} is true.

"""
   result["Primvar"].ValueMightBeTimeVarying.im_func.func_doc = """ValueMightBeTimeVarying() -> USDGEOM_API bool



Return true if it is possible, but not certain, that this primvar's
value changes over time, false otherwise.


This considers time-varyingness of the associated "indices" attribute
if the primvar is indexed.

UsdAttribute::ValueMightBeTimeVarying

"""
   result["Primvar"].GetInterpolation.im_func.func_doc = """GetInterpolation() -> USDGEOM_API TfToken



Return the Primvar's interpolation, which is UsdGeomTokens->constant
if unauthored.


Interpolation determines how the Primvar interpolates over a geometric
primitive. See Interpolation of Geometric Primitive Variables

"""
   result["Primvar"].HasAuthoredElementSize.im_func.func_doc = """HasAuthoredElementSize() -> USDGEOM_API bool



Has elementSize been explicitly authored on this Primvar?



GetElementSize()

"""
   result["Primvar"].NameContainsNamespaces.im_func.func_doc = """NameContainsNamespaces() -> USDGEOM_API bool



Does this primvar contain any namespaces other than the "primvars:"
namespace?


Some clients may only wish to consume primvars that have no extra
namespaces in their names, for ease of translating to other systems
that do not allow namespaces.

"""
   result["Primvar"].GetName.im_func.func_doc = """GetName() -> TfToken




UsdAttribute::GetName()

"""
   result["Primvar"].SetIdTarget.im_func.func_doc = """SetIdTarget(path) -> USDGEOM_API bool

path : SdfPath


This primvar must be of String or StringArray type for this method to
succeed.


If not, a coding error is raised.

UsdGeomPrimvar_Id_primvars

"""
   result["Primvar"].IsIndexed.im_func.func_doc = """IsIndexed() -> USDGEOM_API bool



Returns true if the primvar is indexed, i.e., if it has an associated
"indices" attribute.


If you are going to query the indices anyways, prefer to simply
consult the return-value of GetIndices() , which will be more
efficient.

"""
   result["Primvar"].IsValidInterpolation.func_doc = """**static** IsValidInterpolation(interpolation) -> USDGEOM_API bool

interpolation : TfToken


Validate that the provided C{interpolation} is a valid setting for
interpolation as defined by Interpolation of Geometric Primitive
Variables.

"""
   result["Primvar"].Set.im_func.func_doc = """Set(value, time) -> bool

value : T
time : UsdTimeCode


Set the attribute value of the Primvar at C{time}.

"""
   result["Primvar"].ComputeFlattened.im_func.func_doc = """ComputeFlattened(value, time) -> bool

value : VtArray <ScalarType>
time : UsdTimeCode


Computes the flattened value of the primvar at C{time}.


If the primvar is not indexed or if the value type of this primvar is
a scalar, this returns the authored value, which is the same as Get()
. Hence, it's safe to call ComputeFlattened() on non-indexed primvars.


----------------------------------------------------------------------
ComputeFlattened(value, time) -> USDGEOM_API bool

value : VtValue
time : UsdTimeCode


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the flattened value of the primvar at C{time} as a VtValue.


If the primvar is not indexed or if the value type of this primvar is
a scalar, this returns the authored value, which is the same as Get()
. Hence, it's safe to call ComputeFlattened() on non-indexed primvars.

"""
   result["Primvar"].GetPrimvarName.im_func.func_doc = """GetPrimvarName() -> USDGEOM_API TfToken



Returns the primvar's name, devoid of the "primvars:" namespace.


This is the name by which clients should refer to the primvar, if not
by its full attribute name - i.e. they should B{not}, in general, use
GetBaseName() . In the error condition in which this Primvar object is
not backed by a properly namespaced UsdAttribute, return an empty
TfToken.

"""
   result["Primvar"].CreateIndicesAttr.im_func.func_doc = """CreateIndicesAttr() -> USDGEOM_API UsdAttribute



Returns the existing indices attribute if the primvar is indexed or
creates a new one.

"""
   result["Primvar"].GetBaseName.im_func.func_doc = """GetBaseName() -> TfToken




UsdAttribute::GetBaseName()

"""
   result["Primvar"].HasAuthoredInterpolation.im_func.func_doc = """HasAuthoredInterpolation() -> USDGEOM_API bool



Has interpolation been explicitly authored on this Primvar?



GetInterpolationSize()

"""
   result["Primvar"].GetElementSize.im_func.func_doc = """GetElementSize() -> USDGEOM_API int



Return the "element size" for this Primvar, which is 1 if unauthored.


If this Primvar's type is *not* an array type, (e.g. "Vec3f[]"), then
elementSize is irrelevant.

ElementSize does *not* generally encode the length of an array-type
primvar, and rarely needs to be authored. ElementSize can be thought
of as a way to create an "aggregate interpolatable type", by dictating
how many consecutive elements in the value array should be taken as an
atomic element to be interpolated over a gprim.

For example, spherical harmonics are often represented as a collection
of nine floating-point coefficients, and the coefficients need to be
sampled across a gprim's surface: a perfect case for primvars.
However, USD has no C{float9} datatype. But we can communicate the
aggregation of nine floats successfully to renderers by declaring a
simple float-array valued primvar, and setting its *elementSize* to 9.
To author a *uniform* spherical harmonic primvar on a Mesh of 42
faces, the primvar's array value would contain 9*42 = 378 float
elements.

"""
   result["Primvar"].IsIdTarget.im_func.func_doc = """IsIdTarget() -> USDGEOM_API bool



Returns true if the primvar is an Id primvar.



UsdGeomPrimvar_Id_primvars

"""
   result["Primvar"].SetIndices.im_func.func_doc = """SetIndices(indices, time) -> USDGEOM_API bool

indices : VtIntArray
time : UsdTimeCode


Sets the indices value of the indexed primvar at C{time}.


The values in the indices array must be valid indices into the
authored array returned by Get() . The element numerality of the
primvar's 'interpolation' metadata applies to the "indices" array, not
the attribute value array (returned by Get() ).

"""
   result["Primvar"].GetUnauthoredValuesIndex.im_func.func_doc = """GetUnauthoredValuesIndex() -> USDGEOM_API int



Returns the index that represents unauthored values in the indices
array.



SetUnauthoredValuesIndex()

"""
   result["Primvar"].GetIndices.im_func.func_doc = """GetIndices(indices, time) -> USDGEOM_API bool

indices : VtIntArray
time : UsdTimeCode


Returns the value of the indices array associated with the indexed
primvar at C{time}.



SetIndices() , Proper Client Handling of "Indexed" Primvars

"""
   result["Primvar"].SetUnauthoredValuesIndex.im_func.func_doc = """SetUnauthoredValuesIndex(unauthoredValuesIndex) -> USDGEOM_API bool

unauthoredValuesIndex : int


Set the index that represents unauthored values in the indices array.


Some apps (like Maya) allow you to author primvars sparsely over a
surface. Since most apps can't handle sparse primvars, Maya needs to
provide a value even for the elements it didn't author. This metadatum
provides a way to recover the information in apps that do support
sparse authoring / representation of primvars.

The fallback value of unauthoredValuesIndex is -1, which indicates
that there are no unauthored values.

GetUnauthoredValuesIndex()

"""
   result["Primvar"].GetIndicesAttr.im_func.func_doc = """GetIndicesAttr() -> USDGEOM_API UsdAttribute



Returns a valid indices attribute if the primvar is indexed.


Returns an invalid attribute otherwise.

"""
   result["Primvar"].GetTimeSamplesInInterval.im_func.func_doc = """GetTimeSamplesInInterval(interval, times) -> USDGEOM_API bool

interval : GfInterval
times : sequence<double>


Populates a vector with authored sample times in C{interval}.


This considers any timeSamples authored on the associated "indices"
attribute if the primvar is indexed.

UsdAttribute::GetTimeSamplesInInterval

"""
   result["PointInstancer"].__doc__ = """
Encodes vectorized instancing of multiple, potentially animated,
prototypes (object/instance masters), which can be arbitrary
prims/subtrees on a UsdStage.


PointInstancer is a "multi instancer", as it allows multiple
prototypes to be scattered among its "points". We use a
UsdRelationship *prototypes* to identify and order all of the possible
prototypes, by targeting the root prim of each prototype. The ordering
imparted by relationships associates a zero-based integer with each
prototype, and it is these integers we use to identify the prototype
of each instance, compactly, and allowing prototypes to be swapped out
without needing to reauthor all of the per-instance data.

The PointInstancer schema is designed to scale to billions of
instances, which motivates the choice to split the per-instance
transformation into position, (quaternion) orientation, and scales,
rather than a 4x4 matrix per-instance. In addition to requiring fewer
bytes even if all elements are authored (32 bytes vs 64 for a single-
precision 4x4 matrix), we can also be selective about which attributes
need to animate over time, for substantial data reduction in many
cases.

Note that PointInstancer is *not* a Gprim, since it is not a graphical
primitive by any stretch of the imagination. It *is*, however,
Boundable, since we will sometimes want to treat the entire
PointInstancer similarly to a procedural, from the perspective of
inclusion or framing.

Varying Instance Identity over Time
===================================

PointInstancers originating from simulations often have the
characteristic that points/instances are "born", move around for some
time period, and then die (or leave the area of interest). In such
cases, billions of instances may be birthed over time, while at any
*specific* time, only a much smaller number are actually alive. To
encode this situation efficiently, the simulator may re-use indices in
the instance arrays, when a particle dies, its index will be taken
over by a new particle that may be birthed in a much different
location. This presents challenges both for identity-tracking, and for
motion-blur.

We facilitate identity tracking by providing an optional, animatable
*ids* attribute, that specifies the 64 bit integer ID of the particle
at each index, at each point in time. If the simulator keeps
monotonically increasing a particle-count each time a new particle is
birthed, it will serve perfectly as particle *ids*.

We facilitate motion blur for varying-topology particle streams by
optionally allowing per-instance *velocities* and *angularVelocities*
to be authored. If instance transforms are requested at a time between
samples and either of the velocity attributes is authored, then we
will not attempt to interpolate samples of *positions* or
*orientations*. If not authored, and the bracketing samples have the
same length, then we will interpolate.

Computing an Instance Transform
===============================

Each instance's transformation is a combination of the SRT affine
transform described by its scale, orientation, and position, applied
*after* (i.e. less locally) than the transformation computed at the
root of the prototype it is instancing. In other words, to put an
instance of a PointInstancer into the space of the PointInstancer's
parent prim:

   - Apply (most locally) the authored transformation for
     *prototypes[protoIndices[i]]*

   - If *scales* is authored, next apply the scaling matrix from
     *scales[i]*

   - If *orientations* is authored: B{if *angularVelocities* is
     authored}, first multiply *orientations[i]* by the unit quaternion
     derived by scaling *angularVelocities[i]* by the time differential
     from the left-bracketing timeSample for *orientation* to the requested
     evaluation time *t*, storing the result in *R*, B{else} assign *R*
     directly from *orientations[i]*. Apply the rotation matrix derived
     from *R*.

   - Apply the translation derived from *positions[i]*. If
     *velocities* is authored, apply the translation deriving from
     *velocities[i]* scaled by the time differential from the left-
     bracketing timeSample for *positions* to the requested evaluation time
     *t*.

   - Least locally, apply the transformation authored on the
     PointInstancer prim itself (or the
     UsdGeomImageable::ComputeLocalToWorldTransform() of the PointInstancer
     to put the instance directly into world space)

If neither *velocities* nor *angularVelocities* are authored, we
fallback to standard position and orientation computation logic (using
linear interpolation between timeSamples) as described by Applying
Timesampled Velocities to Geometry.

B{Scaling Velocities for Interpolation}

When computing time-differentials by which to apply velocity or
angularVelocity to positions or orientations, we must scale by ( 1.0 /
UsdStage::GetTimeCodesPerSecond() ), because velocities are recorded
in units/second, while we are interpolating in UsdTimeCode ordinates.

Additionally, if *motion:velocityScale* is authored or inherited (see
UsdGeomMotionAPI::ComputeVelocityScale() ), it is used to scale both
the velocity and angular velocity by a constant value during
computation. The *motion:velocityScale* attribute is encoded by
UsdGeomMotionAPI.

We provide both high and low-level API's for dealing with the
transformation as a matrix, both will compute the instance matrices
using multiple threads; the low-level API allows the client to cache
unvarying inputs so that they need not be read duplicately when
computing over time.

See also Applying Timesampled Velocities to Geometry.

Primvars on PointInstancer
==========================

Primvars authored on a PointInstancer prim should always be applied to
each instance with *constant* interpolation at the root of the
instance. When you are authoring primvars on a PointInstancer, think
about it as if you were authoring them on a point-cloud (e.g. a
UsdGeomPoints gprim). The same interpolation rules for points apply
here, substituting "instance" for "point".

In other words, the (constant) value extracted for each instance from
the authored primvar value depends on the authored *interpolation* and
*elementSize* of the primvar, as follows:
   - B{constant} or B{uniform} : the entire authored value of the
     primvar should be applied exactly to each instance.

   - B{varying}, B{vertex}, or B{faceVarying} : the first
     *elementSize* elements of the authored primvar array should be
     assigned to instance zero, the second *elementSize* elements should be
     assigned to instance one, and so forth.

Masking Instances: "Deactivating" and Invising
==============================================

Often a PointInstancer is created "upstream" in a graphics pipeline,
and the needs of "downstream" clients necessitate eliminating some of
the instances from further consideration. Accomplishing this pruning
by re-authoring all of the per-instance attributes is not very
attractive, since it may mean destructively editing a large quantity
of data. We therefore provide means of "masking" instances by ID, such
that the instance data is unmolested, but per-instance transform and
primvar data can be retrieved with the no-longer-desired instances
eliminated from the (smaller) arrays. PointInstancer allows two
independent means of masking instances by ID, each with different
features that meet the needs of various clients in a pipeline. Both
pruning features' lists of ID's are combined to produce the mask
returned by ComputeMaskAtTime() .

If a PointInstancer has no authored *ids* attribute, the masking
features will still be available, with the integers specifying element
position in the *protoIndices* array rather than ID.

The first masking feature encodes a list of IDs in a list-editable
metadatum called *inactiveIds*, which, although it does not have any
similar impact to stage population as prim activation, it shares with
that feature that its application is uniform over all time. Because it
is list-editable, we can *sparsely* add and remove instances from it
in many layers.

This sparse application pattern makes *inactiveIds* a good choice when
further downstream clients may need to reverse masking decisions made
upstream, in a manner that is robust to many kinds of future changes
to the upstream data.

See ActivateId() , ActivateIds() , DeactivateId() , DeactivateIds() ,
ActivateAllIds()

The second masking feature encodes a list of IDs in a time-varying
Int64Array-valued UsdAttribute called *invisibleIds*, since it shares
with Imageable visibility the ability to animate object visibility.

Unlike *inactiveIds*, overriding a set of opinions for *invisibleIds*
is not at all straightforward, because one will, in general need to
reauthor (in the overriding layer) B{all} timeSamples for the
attribute just to change one Id's visibility state, so it cannot be
authored sparsely. But it can be a very useful tool for situations
like encoding pre-computed camera-frustum culling of geometry when
either or both of the instances or the camera is animated.

See VisId() , VisIds() , InvisId() , InvisIds() , VisAllIds()

Processing and Not Processing Prototypes
========================================

Any prim in the scenegraph can be targetted as a prototype by the
*prototypes* relationship. We do not, however, provide a specific
mechanism for identifying prototypes as geometry that should not be
drawn (or processed) in their own, local spaces in the scenegraph. We
encourage organizing all prototypes as children of the PointInstancer
prim that consumes them, and pruning "raw" processing and drawing
traversals when they encounter a PointInstancer prim; this is what the
UsdGeomBBoxCache and UsdImaging engines do.

There *is* a pattern one can deploy for organizing the prototypes such
that they will automatically be skipped by basic
UsdPrim::GetChildren() or UsdPrimRange traversals. Usd prims each have
a specifier of "def", "over", or "class". The default traversals skip
over prims that are "pure overs" or classes. So to protect prototypes
from all generic traversals and processing, place them under a prim
that is just an "over". For example, ::

  01 def PointInstancer "Crowd_Mid"
  02 {
  03     rel prototypes = [ </Crowd_Mid/Prototypes/MaleThin_Business>, </Crowd_Mid/Prototypes/MaleTine_Casual> ]
  04     
  05     over "Prototypes" 
  06     {
  07          def "MaleThin_Business" (
  08              references = [@MaleGroupA/usd/MaleGroupA.usd@</MaleGroupA>]
  09              variants = {
  10                  string modelingVariant = "Thin"
  11                  string costumeVariant = "BusinessAttire"
  12              }
  13          )
  14          { ... }
  15          
  16          def "MaleThin_Casual"
  17          ...
  18     }
  19 }


"""
   result["PointInstancer"].ComputeInstanceTransformsAtTimes.im_func.func_doc = """ComputeInstanceTransformsAtTimes(xformsArray, times, baseTime, doProtoXforms, applyMask) -> USDGEOM_API bool

xformsArray : sequence< VtArray < GfMatrix4d >>
times : sequence< UsdTimeCode >
baseTime : UsdTimeCode
doProtoXforms : ProtoXformInclusion
applyMask : MaskApplication


Compute the per-instance transforms as in
ComputeInstanceTransformsAtTime, but using multiple sample times.


An array of matrix arrays is returned where each matrix array contains
the instance transforms for the corresponding time in C{times}.

times

- A vector containing the UsdTimeCodes at which we want to sample.

"""
   result["PointInstancer"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomPointInstancer on UsdPrim C{prim}.


Equivalent to UsdGeomPointInstancer::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomPointInstancer on the prim held by C{schemaObj}.


Should be preferred over UsdGeomPointInstancer (schemaObj.GetPrim()),
as it preserves SchemaBase state.

"""
   result["PointInstancer"].CreateProtoIndicesAttr.im_func.func_doc = """CreateProtoIndicesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetProtoIndicesAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointInstancer"].GetIdsAttr.im_func.func_doc = """GetIdsAttr() -> USDGEOM_API UsdAttribute



Ids are optional; if authored, the ids array should be the same length
as the *protoIndices* array, specifying (at each timeSample if
instance identities are changing) the id of each instance.


The type is signed intentionally, so that clients can encode some
binary state on Id'd instances without adding a separate primvar. See
also Varying Instance Identity over Time

C++ Type: VtArray<int64_t>  Usd Type: SdfValueTypeNames->Int64Array
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointInstancer"].ComputeExtentAtTime.im_func.func_doc = """ComputeExtentAtTime(extent, time, baseTime) -> USDGEOM_API bool

extent : VtVec3fArray
time : UsdTimeCode
baseTime : UsdTimeCode


Compute the extent of the point instancer based on the per-instance,
"PointInstancer relative" transforms at C{time}, as described in
Computing an Instance Transform.


If there is no error, we return C{true} and C{extent} will be the
tightest bounds we can compute efficiently. If an error occurs,
C{false} will be returned and C{extent} will be left untouched.

For now, this uses a UsdGeomBBoxCache with the "default", "proxy", and
"render" purposes.

extent

- the out parameter for the extent. On success, it will contain two
elements representing the min and max. time

- UsdTimeCode at which we want to evaluate the extent baseTime

- required for correct interpolation between samples when *velocities*
or *angularVelocities* are present. If there are samples for
*positions* and *velocities* at t1 and t2, normal value resolution
would attempt to interpolate between the two samples, and if they
could not be interpolated because they differ in size (common in cases
where velocity is authored), will choose the sample at t1. When
sampling for the purposes of motion-blur, for example, it is common,
when rendering the frame at t2, to sample at [ t2-shutter/2,
t2+shutter/2 ] for a shutter interval of *shutter*. The first sample
falls between t1 and t2, but we must sample at t2 and apply velocity-
based interpolation based on those samples to get a correct result. In
such scenarios, one should provide a C{baseTime} of t2 when querying
*both* samples. If your application does not care about off-sample
interpolation, it can supply the same value for C{baseTime} that it
does for C{time}. When C{baseTime} is less than or equal to C{time},
we will choose the lower bracketing timeSample.


----------------------------------------------------------------------
ComputeExtentAtTime(extent, time, baseTime, transform) -> USDGEOM_API bool

extent : VtVec3fArray
time : UsdTimeCode
baseTime : UsdTimeCode
transform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the extent as if the matrix C{transform} was first applied.

"""
   result["PointInstancer"].GetScalesAttr.im_func.func_doc = """GetScalesAttr() -> USDGEOM_API UsdAttribute



If authored, per-instance scale to be applied to each instance, before
any rotation is applied.


See also Computing an Instance Transform.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Float3Array
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointInstancer"].CreatePrototypesRel.im_func.func_doc = """CreatePrototypesRel() -> USDGEOM_API UsdRelationship



See GetPrototypesRel() , and also Create vs Get Property Methods for
when to use Get vs Create.

"""
   result["PointInstancer"].CreateOrientationsAttr.im_func.func_doc = """CreateOrientationsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetOrientationsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointInstancer"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomPointInstancer

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomPointInstancer holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomPointInstancer(stage->GetPrimAtPath(path));


"""
   result["PointInstancer"].GetPositionsAttr.im_func.func_doc = """GetPositionsAttr() -> USDGEOM_API UsdAttribute



B{Required property}.


Per-instance position. See also Computing an Instance Transform.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Point3fArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointInstancer"].GetPrototypesRel.im_func.func_doc = """GetPrototypesRel() -> USDGEOM_API UsdRelationship



B{Required property}.


Orders and targets the prototype root prims, which can be located
anywhere in the scenegraph that is convenient, although we promote
organizing prototypes as children of the PointInstancer. The position
of a prototype in this relationship defines the value an instance
would specify in the *protoIndices* attribute to instance that
prototype. Since relationships are uniform, this property cannot be
animated.

"""
   result["PointInstancer"].GetInvisibleIdsAttr.im_func.func_doc = """GetInvisibleIdsAttr() -> USDGEOM_API UsdAttribute



A list of id's to make invisible at the evaluation time.


See invisibleIds: Animatable Masking.

C++ Type: VtArray<int64_t>  Usd Type: SdfValueTypeNames->Int64Array
Variability: SdfVariabilityVarying  Fallback Value: []

"""
   result["PointInstancer"].InvisId.im_func.func_doc = """InvisId(id, time) -> USDGEOM_API bool

id : int64_t
time : UsdTimeCode


Ensure that the instance identified by C{id} is invisible at C{time}.


This will cause *invisibleIds* to first be broken down (keyed) at
C{time}, causing all animation in weaker layers that the current
UsdEditTarget to be overridden. Has no effect on any timeSamples other
than the one at C{time}.

An invised instance is guaranteed not to render if the renderer honors
masking.

"""
   result["PointInstancer"].GetProtoIndicesAttr.im_func.func_doc = """GetProtoIndicesAttr() -> USDGEOM_API UsdAttribute



B{Required property}.


Per-instance index into *prototypes* relationship that identifies what
geometry should be drawn for each instance. B{Topology attribute} -
can be animated, but at a potential performance impact for streaming.

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointInstancer"].CreatePositionsAttr.im_func.func_doc = """CreatePositionsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetPositionsAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointInstancer"].GetOrientationsAttr.im_func.func_doc = """GetOrientationsAttr() -> USDGEOM_API UsdAttribute



If authored, per-instance orientation of each instance about its
prototype's origin, represented as a unit length quaternion, which
allows us to encode it with sufficient precision in a compact GfQuath.


It is client's responsibility to ensure that authored quaternions are
unit length; the convenience API below for authoring orientations from
rotation matrices will ensure that quaternions are unit length, though
it will not make any attempt to select the "better (for
interpolationwith respect to neighboring samples)" of the two possible
quaternions that encode the rotation.

See also Computing an Instance Transform.

C++ Type: VtArray<GfQuath>  Usd Type: SdfValueTypeNames->QuathArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointInstancer"].CreateIdsAttr.im_func.func_doc = """CreateIdsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetIdsAttr() , and also Create vs Get Property Methods for when to
use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointInstancer"].DeactivateId.im_func.func_doc = """DeactivateId(id) -> USDGEOM_API bool

id : int64_t


Ensure that the instance identified by C{id} is inactive over all
time.


This deactivation is encoded sparsely, affecting no other instances.

A deactivated instance is guaranteed not to render if the renderer
honors masking.

"""
   result["PointInstancer"].ComputeExtentAtTimes.im_func.func_doc = """ComputeExtentAtTimes(extents, times, baseTime) -> USDGEOM_API bool

extents : sequence<VtVec3fArray>
times : sequence< UsdTimeCode >
baseTime : UsdTimeCode


Compute the extent of the point instancer as in ComputeExtentAtTime,
but across multiple C{times}.


This is equivalent to, but more efficient than, calling
ComputeExtentAtTime several times. Each element in C{extents} is the
computed extent at the corresponding time in C{times}.

As in ComputeExtentAtTime, if there is no error, we return C{true} and
C{extents} will be the tightest bounds we can compute efficiently. If
an error occurs computing the extent at any time, C{false} will be
returned and C{extents} will be left untouched.

times

- A vector containing the UsdTimeCodes at which we want to sample.


----------------------------------------------------------------------
ComputeExtentAtTimes(extents, times, baseTime, transform) -> USDGEOM_API bool

extents : sequence<VtVec3fArray>
times : sequence< UsdTimeCode >
baseTime : UsdTimeCode
transform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the extent as if the matrix C{transform} was first applied at
each time.

"""
   result["PointInstancer"].GetVelocitiesAttr.im_func.func_doc = """GetVelocitiesAttr() -> USDGEOM_API UsdAttribute



If provided, per-instance 'velocities' will be used to compute
positions between samples for the 'positions' attribute, rather than
interpolating between neighboring 'positions' samples.


Velocities should be considered mandatory if both *protoIndices* and
*positions* are animated. Velocity is measured in position units per
second, as per most simulation software. To convert to position units
per UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond() .

See also Computing an Instance Transform, Applying Timesampled
Velocities to Geometry.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Vector3fArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointInstancer"].ActivateId.im_func.func_doc = """ActivateId(id) -> USDGEOM_API bool

id : int64_t


Ensure that the instance identified by C{id} is active over all time.


This activation is encoded sparsely, affecting no other instances.

This does not guarantee that the instance will be rendered, because it
may still be "invisible" due to C{id} being present in the
*invisibleIds* attribute (see VisId() , InvisId() )

"""
   result["PointInstancer"].ActivateIds.im_func.func_doc = """ActivateIds(ids) -> USDGEOM_API bool

ids : VtInt64Array


Ensure that the instances identified by C{ids} are active over all
time.


This activation is encoded sparsely, affecting no other instances.

This does not guarantee that the instances will be rendered, because
each may still be "invisible" due to its presence in the
*invisibleIds* attribute (see VisId() , InvisId() )

"""
   result["PointInstancer"].GetAngularVelocitiesAttr.im_func.func_doc = """GetAngularVelocitiesAttr() -> USDGEOM_API UsdAttribute



If authored, per-instance angular velocity vector to be used for
interoplating orientations.


Angular velocities should be considered mandatory if both
*protoIndices* and *orientations* are animated. Angular velocity is
measured in B{degrees} per second. To convert to degrees per
UsdTimeCode, divide by UsdStage::GetTimeCodesPerSecond() .

See also Computing an Instance Transform.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Vector3fArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PointInstancer"].CreateInvisibleIdsAttr.im_func.func_doc = """CreateInvisibleIdsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetInvisibleIdsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointInstancer"].CreateVelocitiesAttr.im_func.func_doc = """CreateVelocitiesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVelocitiesAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointInstancer"].ActivateAllIds.im_func.func_doc = """ActivateAllIds() -> USDGEOM_API bool



Ensure that all instances are active over all time.


This does not guarantee that the instances will be rendered, because
each may still be "invisible" due to its presence in the
*invisibleIds* attribute (see VisId() , InvisId() )

"""
   result["PointInstancer"].InvisIds.im_func.func_doc = """InvisIds(ids, time) -> USDGEOM_API bool

ids : VtInt64Array
time : UsdTimeCode


Ensure that the instances identified by C{ids} are invisible at
C{time}.


This will cause *invisibleIds* to first be broken down (keyed) at
C{time}, causing all animation in weaker layers that the current
UsdEditTarget to be overridden. Has no effect on any timeSamples other
than the one at C{time}.

An invised instance is guaranteed not to render if the renderer honors
masking.

"""
   result["PointInstancer"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PointInstancer"].ComputeMaskAtTime.im_func.func_doc = """ComputeMaskAtTime(time, ids) -> USDGEOM_API sequence<bool>

time : UsdTimeCode
ids : VtInt64Array


Computes a presence mask to be applied to per-instance data arrays
based on authored *inactiveIds*, *invisibleIds*, and *ids*.


If no *ids* attribute has been authored, then the values in
*inactiveIds* and *invisibleIds* will be interpreted directly as
indices of *protoIndices*.

If C{ids} is non-None, it is assumed to be the id-mapping to apply,
and must match the length of *protoIndices* at C{time}. If None, we
will call GetIdsAttr() .Get(time)

If all "live" instances at UsdTimeCode C{time} pass the mask, we will
return an B{empty} mask so that clients can trivially recognize the
common "no masking" case. The returned mask can be used with
ApplyMaskToArray() , and will contain a C{true} value for every
element that should survive.

"""
   result["PointInstancer"].VisIds.im_func.func_doc = """VisIds(ids, time) -> USDGEOM_API bool

ids : VtInt64Array
time : UsdTimeCode


Ensure that the instances identified by C{ids} are visible at C{time}.


This will cause *invisibleIds* to first be broken down (keyed) at
C{time}, causing all animation in weaker layers that the current
UsdEditTarget to be overridden. Has no effect on any timeSamples other
than the one at C{time}. If the *invisibleIds* attribute is not
authored or is blocked, this operation is a no-op.

This does not guarantee that the instances will be rendered, because
each may still be "inactive" due to C{id} being present in the
*inactivevIds* metadata (see ActivateId() , DeactivateId() )

"""
   result["PointInstancer"].CreateScalesAttr.im_func.func_doc = """CreateScalesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetScalesAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PointInstancer"].DeactivateIds.im_func.func_doc = """DeactivateIds(ids) -> USDGEOM_API bool

ids : VtInt64Array


Ensure that the instances identified by C{ids} are inactive over all
time.


This deactivation is encoded sparsely, affecting no other instances.

A deactivated instance is guaranteed not to render if the renderer
honors masking.

"""
   result["PointInstancer"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomPointInstancer

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["PointInstancer"].ComputeInstanceTransformsAtTime.im_func.func_doc = """**static** ComputeInstanceTransformsAtTime(xforms, time, baseTime, doProtoXforms, applyMask) -> USDGEOM_API bool

xforms : VtArray < GfMatrix4d >
time : UsdTimeCode
baseTime : UsdTimeCode
doProtoXforms : ProtoXformInclusion
applyMask : MaskApplication


Compute the per-instance, "PointInstancer relative" transforms given
the positions, scales, orientations, velocities and angularVelocities
at C{time}, as described in Computing an Instance Transform.


This will return C{false} and leave C{xforms} untouched if:
   - C{xforms} is None

   - one of C{time} and C{baseTime} is numeric and the other is
     UsdTimeCode::Default() (they must either both be numeric or both be
     default)

   - there is no authored *protoIndices* attribute or *positions*
     attribute

   - the size of any of the per-instance attributes does not match the
     size of *protoIndices*

   - C{doProtoXforms} is C{IncludeProtoXform} but an index value in
     *protoIndices* is outside the range [0, prototypes.size())

   - C{applyMask} is C{ApplyMask} and a mask is set but the size of
     the mask does not match the size of *protoIndices*.

If there is no error, we will return C{true} and C{xforms} will
contain the computed transformations.

xforms

- the out parameter for the transformations. Its size will depend on
the authored data and C{applyMask} time

- UsdTimeCode at which we want to evaluate the transforms baseTime

- required for correct interpolation between samples when *velocities*
or *angularVelocities* are present. If there are samples for
*positions* and *velocities* at t1 and t2, normal value resolution
would attempt to interpolate between the two samples, and if they
could not be interpolated because they differ in size (common in cases
where velocity is authored), will choose the sample at t1. When
sampling for the purposes of motion-blur, for example, it is common,
when rendering the frame at t2, to sample at [ t2-shutter/2,
t2+shutter/2 ] for a shutter interval of *shutter*. The first sample
falls between t1 and t2, but we must sample at t2 and apply velocity-
based interpolation based on those samples to get a correct result. In
such scenarios, one should provide a C{baseTime} of t2 when querying
*both* samples. If your application does not care about off-sample
interpolation, it can supply the same value for C{baseTime} that it
does for C{time}. When C{baseTime} is less than or equal to C{time},
we will choose the lower bracketing timeSample. Selecting sample times
with respect to baseTime will be performed independently for positions
and orientations. doProtoXforms

- specifies whether to include the root transformation of each
instance's prototype in the instance's transform. Default is to
include it, but some clients may want to apply the proto transform as
part of the prototype itself, so they can specify C{ExcludeProtoXform}
instead. applyMask

- specifies whether to apply ApplyMaskToArray() to the computed
result. The default is C{ApplyMask}.


----------------------------------------------------------------------
ComputeInstanceTransformsAtTime(xforms, stage, time, protoIndices, positions, velocities, velocitiesSampleTime, scales, orientations, angularVelocities, angularVelocitiesSampleTime, protoPaths, mask, velocityScale) -> USDGEOM_API bool

xforms : VtArray < GfMatrix4d >
stage : UsdStageWeakPtr
time : UsdTimeCode
protoIndices : VtIntArray
positions : VtVec3fArray
velocities : VtVec3fArray
velocitiesSampleTime : UsdTimeCode
scales : VtVec3fArray
orientations : VtQuathArray
angularVelocities : VtVec3fArray
angularVelocitiesSampleTime : UsdTimeCode
protoPaths : SdfPathVector
mask : sequence<bool>
velocityScale : float


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Perform the per-instance transform computation as described in
Computing an Instance Transform.


This does the same computation as the non-static
ComputeInstanceTransformsAtTime method, but takes all data as
parameters rather than accessing authored data.

xforms

- the out parameter for the transformations. Its size will depend on
the given data and C{applyMask} stage

- the UsdStage time

- time at which we want to evaluate the transforms protoIndices

- array containing all instance prototype indices. positions

- array containing all instance positions. This array must be the same
size as C{protoIndices}. velocities

- array containing all instance velocities. This array must be either
the same size as C{protoIndices} or empty. If it is empty, transforms
are computed as if all velocities were zero in all dimensions.
velocitiesSampleTime

- time at which the samples from C{velocities} were taken. scales

- array containing all instance scales. This array must be either the
same size as C{protoIndices} or empty. If it is empty, transforms are
computed with no change in scale. orientations

- array containing all instance orientations. This array must be
either the same size as C{protoIndices} or empty. If it is empty,
transforms are computed with no change in orientation
angularVelocities

- array containing all instance angular velocities. This array must be
either the same size as C{protoIndices} or empty. If it is empty,
transforms are computed as if all angular velocities were zero in all
dimensions. angularVelocitiesSampleTime

- time at which the samples from C{angularVelocities} were taken.
protoPaths

- array containing the paths for all instance prototypes. If this
array is not empty, prototype transforms are applied to the instance
transforms. mask

- vector containing a mask to apply to the computed result. This
vector must be either the same size as C{protoIndices} or empty. If it
is empty, no mask is applied. velocityScale

- factor used to artificially increase the effect of velocity and
angular velocity on positions and orientations respectively.

"""
   result["PointInstancer"].VisAllIds.im_func.func_doc = """VisAllIds(time) -> USDGEOM_API bool

time : UsdTimeCode


Ensure that all instances are visible at C{time}.


Operates by authoring an empty array at C{time}.

This does not guarantee that the instances will be rendered, because
each may still be "inactive" due to its id being present in the
*inactivevIds* metadata (see ActivateId() , DeactivateId() )

"""
   result["PointInstancer"].VisId.im_func.func_doc = """VisId(id, time) -> USDGEOM_API bool

id : int64_t
time : UsdTimeCode


Ensure that the instance identified by C{id} is visible at C{time}.


This will cause *invisibleIds* to first be broken down (keyed) at
C{time}, causing all animation in weaker layers that the current
UsdEditTarget to be overridden. Has no effect on any timeSamples other
than the one at C{time}. If the *invisibleIds* attribute is not
authored or is blocked, this operation is a no-op.

This does not guarantee that the instance will be rendered, because it
may still be "inactive" due to C{id} being present in the
*inactivevIds* metadata (see ActivateId() , DeactivateId() )

"""
   result["PointInstancer"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["PointInstancer"].CreateAngularVelocitiesAttr.im_func.func_doc = """CreateAngularVelocitiesAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAngularVelocitiesAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["MotionAPI"].__doc__ = """
UsdGeomMotionAPI encodes data that can live on any prim that may
affect computations involving:



   - computed motion for motion blur

   - sampling for motion blur

For example, UsdGeomMotionAPI provides *velocityScale* (
GetVelocityScaleAttr() ) for controlling how motion-blur samples
should be computed by velocity-consuming schemas.

"""
   result["MotionAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomMotionAPI on UsdPrim C{prim}.


Equivalent to UsdGeomMotionAPI::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomMotionAPI on the prim held by C{schemaObj}.


Should be preferred over UsdGeomMotionAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["MotionAPI"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomMotionAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomMotionAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomMotionAPI(stage->GetPrimAtPath(path));


"""
   result["MotionAPI"].ComputeVelocityScale.im_func.func_doc = """ComputeVelocityScale(time) -> USDGEOM_API float

time : UsdTimeCode


Compute the inherited value of *velocityScale* at C{time}, i.e.


the authored value on the prim closest to this prim in namespace,
resolved upwards through its ancestors in namespace.

the inherited value, or 1.0 if neither the prim nor any of its
ancestors possesses an authored value.

this is a reference implementation that is not particularly efficient
if evaluating over many prims, because it does not share inherited
results.

"""
   result["MotionAPI"].GetVelocityScaleAttr.im_func.func_doc = """GetVelocityScaleAttr() -> USDGEOM_API UsdAttribute



VelocityScale is an B{inherited} float attribute that velocity-based
schemas (e.g.


PointBased, PointInstancer) can consume to compute interpolated
positions and orientations by applying velocity and angularVelocity,
which is required for interpolating between samples when topology is
varying over time. Although these quantities are generally physically
computed by a simulator, sometimes we require more or less motion-blur
to achieve the desired look.  VelocityScale allows artists to dial-in,
as a post-sim correction, a scale factor to be applied to the velocity
prior to computing interpolated positions from it.

See also ComputeVelocityScale()

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["MotionAPI"].Apply.func_doc = """**static** Apply(prim) -> USDGEOM_API UsdGeomMotionAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "MotionAPI" to the token-valued,
listOp metadata *apiSchemas* on the prim.

A valid UsdGeomMotionAPI object is returned upon success. An invalid
(or empty) UsdGeomMotionAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["MotionAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["MotionAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["MotionAPI"].CreateVelocityScaleAttr.im_func.func_doc = """CreateVelocityScaleAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVelocityScaleAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["GetFallbackUpAxis"].func_doc = """GetFallbackUpAxis() -> USDGEOM_API TfToken



Return the site-level fallback up axis as a TfToken.


In a generic installation of USD, the fallback will be "Y". This can
be changed to "Z" by adding, in a plugInfo.json file discoverable by
USD's PlugPlugin mechanism: ::

  "UsdGeomMetrics": {
      "upAxis": "Z"
  }

If more than one such entry is discovered and the values for upAxis
differ, we will issue a warning during the first call to this
function, and ignore all of them, so that we devolve to deterministic
behavior of Y up axis until the problem is rectified.


----------------------------------------------------------------------
GetFallbackUpAxis() -> USDGEOM_API TfToken



Return the site-level fallback up axis as a TfToken.


In a generic installation of USD, the fallback will be "Y". This can
be changed to "Z" by adding, in a plugInfo.json file discoverable by
USD's PlugPlugin mechanism: ::

  "UsdGeomMetrics": {
      "upAxis": "Z"
  }

If more than one such entry is discovered and the values for upAxis
differ, we will issue a warning during the first call to this
function, and ignore all of them, so that we devolve to deterministic
behavior of Y up axis until the problem is rectified.

"""
   result["Capsule"].__doc__ = """
Defines a primitive capsule, i.e.


a cylinder capped by two half spheres, centered at the origin, whose
spine is along the specified *axis*.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdGeomTokens. So to set an attribute to the value "rightHanded",
use UsdGeomTokens->rightHanded as the value.

"""
   result["Capsule"].CreateHeightAttr.im_func.func_doc = """CreateHeightAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHeightAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Capsule"].CreateRadiusAttr.im_func.func_doc = """CreateRadiusAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRadiusAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Capsule"].CreateExtentAttr.im_func.func_doc = """CreateExtentAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetExtentAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Capsule"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomCapsule

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomCapsule holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomCapsule(stage->GetPrimAtPath(path));


"""
   result["Capsule"].CreateAxisAttr.im_func.func_doc = """CreateAxisAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAxisAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Capsule"].GetExtentAttr.im_func.func_doc = """GetExtentAttr() -> USDGEOM_API UsdAttribute



Extent is re-defined on Capsule only to provide a fallback value.



UsdGeomGprim::GetExtentAttr() .  C++ Type: VtArray<GfVec3f>  Usd Type:
SdfValueTypeNames->Float3Array  Variability: SdfVariabilityVarying
Fallback Value: [(-0.5, -0.5, -1), (0.5, 0.5, 1)]

"""
   result["Capsule"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomCapsule on UsdPrim C{prim}.


Equivalent to UsdGeomCapsule::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomCapsule on the prim held by C{schemaObj}.


Should be preferred over UsdGeomCapsule (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Capsule"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Capsule"].GetHeightAttr.im_func.func_doc = """GetHeightAttr() -> USDGEOM_API UsdAttribute



The size of the capsule's spine along the specified *axis* excluding
the size of the two half spheres, i.e.


the size of the cylinder portion of the capsule. If you author
*height* you must also author *extent*.

GetExtentAttr()  C++ Type: double  Usd Type: SdfValueTypeNames->Double
Variability: SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["Capsule"].GetRadiusAttr.im_func.func_doc = """GetRadiusAttr() -> USDGEOM_API UsdAttribute



The radius of the capsule.


If you author *radius* you must also author *extent*.

GetExtentAttr()  C++ Type: double  Usd Type: SdfValueTypeNames->Double
Variability: SdfVariabilityVarying  Fallback Value: 0.5

"""
   result["Capsule"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Capsule"].Define.func_doc = """**static** Define(stage, path) -> USDGEOM_API UsdGeomCapsule

stage : UsdStagePtr
path : SdfPath


Attempt to ensure a *UsdPrim* adhering to this schema at C{path} is
defined (according to UsdPrim::IsDefined() ) on this stage.


If a prim adhering to this schema at C{path} is already defined on
this stage, return that prim. Otherwise author an *SdfPrimSpec* with
*specifier* == *SdfSpecifierDef* and this schema's prim type name for
the prim at C{path} at the current EditTarget. Author *SdfPrimSpec* s
with C{specifier} == *SdfSpecifierDef* and empty typeName at the
current EditTarget for any nonexistent, or existing but not *Defined*
ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["Capsule"].GetAxisAttr.im_func.func_doc = """GetAxisAttr() -> USDGEOM_API UsdAttribute



The axis along which the spine of the capsule is aligned.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: Z  Allowed Values : [X, Y, Z]

"""
   result["GetStageUpAxis"].func_doc = """GetStageUpAxis(stage) -> USDGEOM_API TfToken

stage : UsdStageWeakPtr


Fetch and return C{stage} 's upAxis.


If unauthored, will return the value provided by
UsdGeomGetFallbackUpAxis() . Exporters, however, are strongly
encouraged to always set the upAxis for every USD file they create.

one of: UsdGeomTokens->y or UsdGeomTokens->z, unless there was an
error, in which case returns an empty TfToken

Encoding Stage UpAxis


----------------------------------------------------------------------
GetStageUpAxis(stage) -> USDGEOM_API TfToken

stage : UsdStageWeakPtr


Fetch and return C{stage} 's upAxis.


If unauthored, will return the value provided by
UsdGeomGetFallbackUpAxis() . Exporters, however, are strongly
encouraged to always set the upAxis for every USD file they create.

one of: UsdGeomTokens->y or UsdGeomTokens->z, unless there was an
error, in which case returns an empty TfToken

Encoding Stage UpAxis

"""
   result["Curves"].__doc__ = """
Base class for BasisCurves and NurbsCurves.


The BasisCurves schema is designed to be analagous to RenderMan's
RiCurves and RiBasis, while the NurbsCurve schema is designed to be
analgous to the NURBS curves found in packages like Maya and Houdini
while retaining their consistency with the RenderMan specification for
NURBS Patches.

"""
   result["Curves"].ComputeExtent.func_doc = """**static** ComputeExtent(points, widths, extent) -> USDGEOM_API bool

points : VtVec3fArray
widths : VtFloatArray
extent : VtVec3fArray


Compute the extent for the curves defined by points and widths.



true upon success, false if unable to calculate extent. On success,
extent will contain an approximate axis-aligned bounding box of the
curve defined by points with the given widths.

This function is to provide easy authoring of extent for usd authoring
tools, hence it is static and acts outside a specific prim (as in
attribute based methods).


----------------------------------------------------------------------
ComputeExtent(points, widths, transform, extent) -> USDGEOM_API bool

points : VtVec3fArray
widths : VtFloatArray
transform : GfMatrix4d
extent : VtVec3fArray


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the extent as if the matrix C{transform} was first applied.

"""
   result["Curves"].CreateCurveVertexCountsAttr.im_func.func_doc = """CreateCurveVertexCountsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetCurveVertexCountsAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Curves"].Get.func_doc = """**static** Get(stage, path) -> USDGEOM_API UsdGeomCurves

stage : UsdStagePtr
path : SdfPath


Return a UsdGeomCurves holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdGeomCurves(stage->GetPrimAtPath(path));


"""
   result["Curves"].GetCurveVertexCountsAttr.im_func.func_doc = """GetCurveVertexCountsAttr() -> USDGEOM_API UsdAttribute



Curves-derived primitives can represent multiple distinct, potentially
disconnected curves.


The length of 'curveVertexCounts' gives the number of such curves, and
each element describes the number of vertices in the corresponding
curve

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Curves"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDGEOM_API  TfType


"""
   result["Curves"].SetWidthsInterpolation.im_func.func_doc = """SetWidthsInterpolation(interpolation) -> USDGEOM_API bool

interpolation : TfToken


Set the interpolation for the *widths* attribute.



true upon success, false if C{interpolation} is not a legal value as
defined by UsdPrimvar::IsValidInterpolation(), or if there was a
problem setting the value. No attempt is made to validate that the
widths attr's value contains the right number of elements to match its
interpolation to its prim's topology.

GetWidthsInterpolation()

"""
   result["Curves"].CreateWidthsAttr.im_func.func_doc = """CreateWidthsAttr(defaultValue, writeSparsely) -> USDGEOM_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetWidthsAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Curves"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdGeomCurves on UsdPrim C{prim}.


Equivalent to UsdGeomCurves::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdGeomCurves on the prim held by C{schemaObj}.


Should be preferred over UsdGeomCurves (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Curves"].GetWidthsAttr.im_func.func_doc = """GetWidthsAttr() -> USDGEOM_API UsdAttribute



Provides width specification for the curves, whose application will
depend on whether the curve is oriented (normals are defined for it),
in which case widths are "ribbon width", or unoriented, in which case
widths are cylinder width.


'widths' is not a generic Primvar, but the number of elements in this
attribute will be determined by its 'interpolation'. See
SetWidthsInterpolation() . If 'widths' and 'primvars:widths' are both
specified, the latter has precedence.

C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Curves"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDGEOM_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Curves"].GetWidthsInterpolation.im_func.func_doc = """GetWidthsInterpolation() -> USDGEOM_API TfToken



Get the interpolation for the *widths* attribute.


Although 'widths' is not classified as a generic UsdGeomPrimvar (and
will not be included in the results of UsdGeomImageable::GetPrimvars()
) it does require an interpolation specification. The fallback
interpolation, if left unspecified, is UsdGeomTokens->vertex, which
means a width value is specified at the end of each curve segment.

"""