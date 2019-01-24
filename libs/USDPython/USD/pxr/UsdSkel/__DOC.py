def Execute(result):
   result["Binding"].__doc__ = """
Helper object that describes the binding of a skeleton to a set of
skinnable objects.


The set of skinnable objects is given as UsdSkelSkinningQuery prims,
which can be used both to identify the skinned prim as well compute
skinning properties of the prim.

"""
   result["Binding"].GetSkeleton.im_func.func_doc = """GetSkeleton() -> Skeleton



Returns the bound skeleton.

"""
   result["Binding"].GetSkinningTargets.im_func.func_doc = """GetSkinningTargets() -> VtArray < UsdSkelSkinningQuery >



Returns the set skinning targets.

"""
   result["Binding"].__init__.im_func.func_doc = """__init__()



----------------------------------------------------------------------
__init__(skel, skinningQueries)

skel : Skeleton
skinningQueries : VtArray < UsdSkelSkinningQuery >

"""
   result["AnimMapper"].__doc__ = """"""
   result["AnimMapper"].Remap.im_func.func_doc = """Remap(source, target, elementSize, defaultValue) -> bool

source : VtArray <T>
target : VtArray <T>
elementSize : int
defaultValue : T


Typed remapping of data from C{source} into C{target}.


The C{source} array provides a run of C{elementSize} elements for each
path in the \em sourceOrder. These elements are remapped and copied
over the C{target} array. Prior to remapping, the C{target} array is
resized to the size of the \em targetOrder (as given at mapper
construction time) multiplied by the C{elementSize}. New elements
created in the array are initialized to C{defaultValue}, if provided.


----------------------------------------------------------------------
Remap(source, target, elementSize, defaultValue) -> USDSKEL_API bool

source : VtValue
target : VtValue
elementSize : int
defaultValue : VtValue


Type-erased remapping of data from C{source} into C{target}.


The C{source} array provides a run of C{elementSize} elements for each
path in the \em sourceOrder. These elements are remapped and copied
over the C{target} array. Prior to remapping, the C{target} array is
resized to the size of the \em targetOrder (as given at mapper
construction time) multiplied by the C{elementSize}. New elements
created in the array are initialized to C{defaultValue}, if provided.
Remapping is supported for registered Sdf array value types only.

"""
   result["AnimMapper"].RemapTransforms.im_func.func_doc = """RemapTransforms(source, target, elementSize) -> USDSKEL_API bool

source : VtMatrix4dArray
target : VtMatrix4dArray
elementSize : int


Convenience method for the common task of remapping transform arrays.


This performs the same operation as Remap() , but sets the matrix
identity as the default value.

"""
   result["AnimMapper"].IsSparse.im_func.func_doc = """IsSparse() -> USDSKEL_API bool



Returns true if this is a sparse mapping.


A sparse mapping means that not all target values will be overridden
by source values, when mapped with Remap() .

"""
   result["AnimMapper"].IsNull.im_func.func_doc = """IsNull() -> USDSKEL_API bool



Returns true if this is a null mapping.


No source elements of a null map are mapped to the target.

"""
   result["AnimMapper"].IsIdentity.im_func.func_doc = """IsIdentity() -> USDSKEL_API bool



Returns true if this is an identity map.


The source and target orders of an identity map are identical.

"""
   result["AnimMapper"].__init__.im_func.func_doc = """__init__() -> USDSKEL_API



Construct a null mapper.


----------------------------------------------------------------------
__init__(sourceOrder, targetOrder) -> USDSKEL_API

sourceOrder : VtTokenArray
targetOrder : VtTokenArray


Construct a mapper for mapping data from C{sourceOrder} to
C{targetOrder}.


----------------------------------------------------------------------
__init__(sourceOrder, sourceOrderSize, targetOrder, targetOrderSize) -> USDSKEL_API

sourceOrder : TfToken
sourceOrderSize : size_t
targetOrder : TfToken
targetOrderSize : size_t


Construct a mapper for mapping data from C{sourceOrder} to
C{targetOrder}, each being arrays of size C{sourceOrderSize}  and
C{targetOrderSize}, respectively.

"""
   result["SkeletonQuery"].__doc__ = """
Primary interface to reading *bound* skeleton data.


This is used to query properties such as resolved transforms and
animation bindings, as bound through the UsdSkelBindingAPI.

A UsdSkelSkeletonQuery can not be constructed directly, and instead
must be constructed through a UsdSkelCache instance. This is done as
follows: ::

  // Global cache, intended to persist.
  UsdSkelCache skelCache;
  // Populate the cache for a skel root.
  skelCache.Populate(UsdSkelRoot(skelRootPrim));
  
  if (UsdSkelSkeletonQuery skelQuery = skelCache.GetSkelQuery(skelPrim)) {
      ...
  }


"""
   result["SkeletonQuery"].GetAnimQuery.im_func.func_doc = """GetAnimQuery() -> USDSKEL_API  UsdSkelAnimQuery



Returns the animation query that provides animation for the bound
skeleton instance, if any.

"""
   result["SkeletonQuery"].GetJointWorldBindTransforms.im_func.func_doc = """GetJointWorldBindTransforms(xforms) -> USDSKEL_API bool

xforms : VtMatrix4dArray


Returns the world space joint transforms at bind time.

"""
   result["SkeletonQuery"].GetTopology.im_func.func_doc = """GetTopology() -> USDSKEL_API  UsdSkelTopology



Returns the topology of the bound skeleton instance, if any.

"""
   result["SkeletonQuery"].ComputeSkinningTransforms.im_func.func_doc = """ComputeSkinningTransforms(xforms, time) -> USDSKEL_API bool

xforms : VtMatrix4dArray
time : UsdTimeCode


Compute transforms representing the change in transformation of a
joint from its rest pose, in skeleton space.


I.e., ::

  inverse(bindTransform)*jointTransform

These are the transforms usually required for skinning.

"""
   result["SkeletonQuery"].GetJointOrder.im_func.func_doc = """GetJointOrder() -> USDSKEL_API VtTokenArray



Returns an arrray of joint paths, given as tokens, describing the
order and parent-child relationships of joints in the skeleton.



UsdSkelSkeleton::GetJointOrder

"""
   result["SkeletonQuery"].ComputeJointWorldTransforms.im_func.func_doc = """ComputeJointWorldTransforms(xforms, xfCache, atRest) -> USDSKEL_API bool

xforms : VtMatrix4dArray
xfCache : UsdGeomXformCache
atRest : bool


Compute joint transforms in world space, at whatever time is
configured on C{xfCache}.


This is equivalent to computing skel-space joint transforms with
CmoputeJointSkelTransforms(), and then concatenating all transforms by
the local-to-world transform of the Skeleton prim. If C{atRest} is
true, any bound animation source is ignored, and transforms are
computed from the rest pose.

"""
   result["SkeletonQuery"].GetSkeleton.im_func.func_doc = """GetSkeleton() -> USDSKEL_API  UsdSkelSkeleton



Returns the bound skeleton instance, if any.

"""
   result["SkeletonQuery"].GetPrim.im_func.func_doc = """GetPrim() -> USDSKEL_API UsdPrim



Returns the underlying Skeleton primitive corresponding to the bound
skeleton instance, if any.

"""
   result["SkeletonQuery"].ComputeJointSkelTransforms.im_func.func_doc = """ComputeJointSkelTransforms(xforms, time, atRest) -> USDSKEL_API bool

xforms : VtMatrix4dArray
time : UsdTimeCode
atRest : bool


Compute joint transforms in skeleton space, at C{time}.


This concatenates joint transforms as computed from
ComputeJointLocalTransforms() . If C{atRest} is true, any bound
animation source is ignored, and transforms are computed from the rest
pose. The skeleton-space transforms of the rest pose are cached
internally.

"""
   result["SkeletonQuery"].ComputeJointLocalTransforms.im_func.func_doc = """ComputeJointLocalTransforms(xforms, time, atRest) -> USDSKEL_API bool

xforms : VtMatrix4dArray
time : UsdTimeCode
atRest : bool


Compute joint transforms in joint-local space, at C{time}.


This returns transforms in joint order of the skeleton. If C{atRest}
is false and an animation source is bound, local transforms defined by
the animation are mapped into the skeleton's joint order. Any
transforms not defined by the animation source use the transforms from
the rest pose as a fallback value. If valid transforms cannot be
computed for the animation source, the C{xforms} are instead set to
the rest transforms.

"""
   result["Animation"].__doc__ = """
Describes a skel animation, where joint animation is stored in a
vectorized form.


See the extended Skel Animation documentation for more information.

"""
   result["Animation"].CreateScalesAttr.im_func.func_doc = """CreateScalesAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetScalesAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Animation"].Get.func_doc = """**static** Get(stage, path) -> USDSKEL_API UsdSkelAnimation

stage : UsdStagePtr
path : SdfPath


Return a UsdSkelAnimation holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdSkelAnimation(stage->GetPrimAtPath(path));


"""
   result["Animation"].CreateJointsAttr.im_func.func_doc = """CreateJointsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetJointsAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Animation"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSKEL_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Animation"].GetTranslationsAttr.im_func.func_doc = """GetTranslationsAttr() -> USDSKEL_API UsdAttribute



Joint-local translations of all affected joints.


Array length should match the size of the *joints* attribute.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Float3Array
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Animation"].GetJointsAttr.im_func.func_doc = """GetJointsAttr() -> USDSKEL_API UsdAttribute



Array of tokens identifying which joints this animation's data applies
to.


The tokens for joints correspond to the tokens of Skeleton primitives.
The order of the joints as listed here may vary from the order of
joints on the Skeleton itself.

C++ Type: VtArray<TfToken>  Usd Type: SdfValueTypeNames->TokenArray
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["Animation"].CreateBlendShapeWeightsAttr.im_func.func_doc = """CreateBlendShapeWeightsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetBlendShapeWeightsAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Animation"].CreateRotationsAttr.im_func.func_doc = """CreateRotationsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRotationsAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Animation"].GetRotationsAttr.im_func.func_doc = """GetRotationsAttr() -> USDSKEL_API UsdAttribute



Joint-local unit quaternion rotations of all affected joints, in
32-bit precision.


Array length should match the size of the *joints* attribute.

C++ Type: VtArray<GfQuatf>  Usd Type: SdfValueTypeNames->QuatfArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Animation"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSKEL_API  TfType


"""
   result["Animation"].GetBlendShapeWeightsAttr.im_func.func_doc = """GetBlendShapeWeightsAttr() -> USDSKEL_API UsdAttribute



Array of weight values for each blend shape.


Each weight value is associated with the corresponding blend shape
identified within the *blendShapes* token array, and therefore must
have the same length as *blendShapes.

C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Animation"].GetScalesAttr.im_func.func_doc = """GetScalesAttr() -> USDSKEL_API UsdAttribute



Joint-local scales of all affected joints, in 16 bit precision.


Array length should match the size of the *joints* attribute.

C++ Type: VtArray<GfVec3h>  Usd Type: SdfValueTypeNames->Half3Array
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Animation"].GetBlendShapesAttr.im_func.func_doc = """GetBlendShapesAttr() -> USDSKEL_API UsdAttribute



Array of tokens identifying which blend shapes this animation's data
applies to.


The tokens for blendShapes correspond to the tokens set in the
*skel:blendShapes* binding property of the UsdSkelBindingAPI.

C++ Type: VtArray<TfToken>  Usd Type: SdfValueTypeNames->TokenArray
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["Animation"].CreateTranslationsAttr.im_func.func_doc = """CreateTranslationsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTranslationsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Animation"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdSkelAnimation on UsdPrim C{prim}.


Equivalent to UsdSkelAnimation::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdSkelAnimation on the prim held by C{schemaObj}.


Should be preferred over UsdSkelAnimation (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Animation"].CreateBlendShapesAttr.im_func.func_doc = """CreateBlendShapesAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetBlendShapesAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Animation"].Define.func_doc = """**static** Define(stage, path) -> USDSKEL_API UsdSkelAnimation

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
   result["NormalizeWeights"].func_doc = """NormalizeWeights(weights, numInfluencesPerComponent) -> USDSKEL_API bool

weights : VtFloatArray
numInfluencesPerComponent : int


Helper method to normalize weight values across each consecutive run
of C{numInfluencesPerComponent} elements.


----------------------------------------------------------------------
NormalizeWeights(weights, numInfluencesPerComponent) -> USDSKEL_API bool

weights : VtFloatArray
numInfluencesPerComponent : int


Helper method to normalize weight values across each consecutive run
of C{numInfluencesPerComponent} elements.

"""
   result["ExpandConstantInfluencesToVarying"].func_doc = """ExpandConstantInfluencesToVarying(indices, size) -> USDSKEL_API bool

indices : VtIntArray
size : size_t


Convert an array of constant influences (joint weights or indices) to
an array of varying influences.


The C{size} should match the size of required for 'vertex'
interpolation on the type geometry primitive. Typically, this is the
number of points. This is a convenience function for clients that
don't understand constant (rigid) weighting.


----------------------------------------------------------------------
ExpandConstantInfluencesToVarying(weights, size) -> USDSKEL_API bool

weights : VtFloatArray
size : size_t


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ExpandConstantInfluencesToVarying(indices, size) -> USDSKEL_API bool

indices : VtIntArray
size : size_t


Convert an array of constant influences (joint weights or indices) to
an array of varying influences.


The C{size} should match the size of required for 'vertex'
interpolation on the type geometry primitive. Typically, this is the
number of points. This is a convenience function for clients that
don't understand constant (rigid) weighting.


----------------------------------------------------------------------
ExpandConstantInfluencesToVarying(weights, size) -> USDSKEL_API bool

weights : VtFloatArray
size : size_t


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["IsSkinnablePrim"].func_doc = """IsSkinnablePrim(prim) -> USDSKEL_API bool

prim : UsdPrim


Returns true if C{prim} is considered to be a skinnable primitive.


Whether or not the prim is actually skinned additionally depends on
whether or not the prim has a bound skeleton, and prop joint
influences.


----------------------------------------------------------------------
IsSkinnablePrim(prim) -> USDSKEL_API bool

prim : UsdPrim


Returns true if C{prim} is considered to be a skinnable primitive.


Whether or not the prim is actually skinned additionally depends on
whether or not the prim has a bound skeleton, and prop joint
influences.

"""
   result["InbetweenShape"].__doc__ = """
Schema wrapper for UsdAttribute for authoring and introspecting
attributes that serve as inbetween shapes of a UsdSkelBlendShape.


Inbetween shapes allow an explicit shape to be specified when the
blendshape to which it's bound is evaluated at a certain weight. For
example, rather than performing piecewise linear interpolation between
a primary shape and the rest shape at weight 0.5, an inbetween shape
could be defined at the weight. For weight values greater than 0.5, a
shape would then be resolved by linearly interpolating between the
inbetween shape and the primary shape, while for weight values less
than or equal to 0.5, the shape is resolved by linearly interpolating
between the inbetween shape and the primary shape.

"""
   result["InbetweenShape"].IsInbetween.func_doc = """**static** IsInbetween(attr) -> USDSKEL_API bool

attr : UsdAttribute


Test whether a given UsdAttribute represents a valid Inbetween, which
implies that creating a UsdSkelInbetweenShape from the attribute will
succeed.


Succes implies that C{attr.IsDefined()} is true.

"""
   result["InbetweenShape"].HasAuthoredWeight.im_func.func_doc = """HasAuthoredWeight() -> USDSKEL_API bool



Has weight been explicitly authored on this shape?



GetWeight()

"""
   result["InbetweenShape"].IsDefined.im_func.func_doc = """IsDefined() -> bool



Return true if the wrapped UsdAttribute::IsDefined() , and in addition
the attribute is identified as an Inbetween.

"""
   result["InbetweenShape"].GetAttr.im_func.func_doc = """GetAttr() -> UsdAttribute



Explicit UsdAttribute extractor.

"""
   result["InbetweenShape"].GetOffsets.im_func.func_doc = """GetOffsets(offsets) -> USDSKEL_API bool

offsets : VtVec3fArray

"""
   result["InbetweenShape"].SetWeight.im_func.func_doc = """SetWeight(weight) -> USDSKEL_API bool

weight : float


Set the location at which the shape is applied.

"""
   result["InbetweenShape"].GetWeight.im_func.func_doc = """GetWeight() -> USDSKEL_API float



Return the location at which the shape is applied.

"""
   result["InbetweenShape"].__init__.im_func.func_doc = """__init__()



Default constructor returns an invalid inbetween shape.


----------------------------------------------------------------------
__init__(attr) -> USDSKEL_API

attr : UsdAttribute


Speculative constructor that will produce a valid
UsdSkelInbetweenShape when C{attr} already represents an attribute
that is an Inbetween, and produces an *invalid* Inbetween otherwise
(i.e.


operator bool() will return false).

Calling C{UsdSkelInbetweenShape::IsInbetween(attr)} will return the
same truth value as this constructor, but if you plan to subsequently
use the Inbetween anyways, just use this constructor.

"""
   result["__doc__"] = """
B{UsdSkel} defines schemas and API that form a basis for interchanging
both skeletally skinned meshes and joint animations between DCC tools
in a graphics pipeline.

API Manual
==========

This manual contains API documentation for the UsdSkel module, along
with an introduction key schemas and API concepts.

B{API Manual}

   - UsdSkel Introduction
   - Overview and Purpose
   - What UsdSkel Is Not

   - Terminology

   - What Can Be Skinned?

   - Transforms and Transform Spaces

   - Schema Overview
   - Skinning an Arm
   - Skinning an Arm: The Skel Root

   - Skinning an Arm: Defining a Skeleton

   - Skinning an Arm: Skel Animations

   - Skinning an Arm: Binding Skeletons to Prims

   - Skinning an Arm: Joint Influences

   - Skinning an Arm: Geom Bind Transform

   - UsdSkel API Introduction
   - Querying Skeleton Structure And Animation

   - Joint Paths and Names

   - Querying the Joint Hierarchy

   - Skeleton Bindings

   - Discovering Bindings On Skinnable Primitives

   - UsdSkel_API_ExtractingJointInfluences

   - Schemas In-Depth
   - UsdSkel_Schemas_Overview

   - Joint Order

   - Skeleton Root Schema

   - Skeleton Schema
   - Skeleton Schema: Joint Hierarchy

   - Skel Animation Schema
   - Skel Animation Schema: Binding to Skeletons

   - Blend Shape Schema

   - Binding API Schema
   - BindingAPI: Binding Skeletons

   - UsdSkel_BindingAPI_JointInfluences

   - UsdSkel_BindingAPI_RigidDeformations

   - BindingAPI: Storing Influences

   - BindingAPI: Binding Blend Shapes

   - Instancing in UsdSkel
   - Instancing the "Bind State"

   - Instancing Example

   - Object Model
   - UsdSkelCache: Persistent Skeleton Cache

   - UsdSkelSkeletonQuery: Skeleton Resolver

   - UsdSkelAnimQuery: Animation Resolver

   - UsdSkelSkinningQuery: Resolving Joint Influences and Skinning

   - UsdSkelAnimMapper: Remapping Data Between Different Orders

   - Best Practices


"""
   result["BlendShape"].__doc__ = """
Describes a target blend shape, possibly containing inbetween shapes.


See the extended Blend Shape Schema documentation for information.

"""
   result["BlendShape"].GetInbetweens.im_func.func_doc = """GetInbetweens() -> USDSKEL_API sequence< UsdSkelInbetweenShape >



Return valid UsdSkelInbetweenShape objects for all defined Inbetweens
on this prim.

"""
   result["BlendShape"].Get.func_doc = """**static** Get(stage, path) -> USDSKEL_API UsdSkelBlendShape

stage : UsdStagePtr
path : SdfPath


Return a UsdSkelBlendShape holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdSkelBlendShape(stage->GetPrimAtPath(path));


"""
   result["BlendShape"].CreateInbetween.im_func.func_doc = """CreateInbetween(name) -> USDSKEL_API UsdSkelInbetweenShape

name : TfToken


Author scene description to create an attribute on this prim that will
be recognized as an Inbetween (i.e.


will present as a valid UsdSkelInbetweenShape).

The name of the created attribute or may or may not be the specified
C{attrName}, due to the possible need to apply property namespacing.
Creation may fail and return an invalid Inbetwen if C{attrName}
contains a reserved keyword.

an invalid UsdSkelInbetweenShape if we failed to create a valid
attribute, a valid UsdSkelInbetweenShape otherwise. It is not an error
to create over an existing, compatible attribute.

UsdSkelInbetweenShape::IsInbetween()

"""
   result["BlendShape"].GetOffsetsAttr.im_func.func_doc = """GetOffsetsAttr() -> USDSKEL_API UsdAttribute



B{Required property}.


Position offsets which, when added to the base pose, provides the
target shape.

C++ Type: VtArray<GfVec3f>  Usd Type: SdfValueTypeNames->Vector3fArray
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["BlendShape"].GetAuthoredInbetweens.im_func.func_doc = """GetAuthoredInbetweens() -> USDSKEL_API sequence< UsdSkelInbetweenShape >



Like GetInbetweens() , but exclude inbetwens that have no authored
scene / description.

"""
   result["BlendShape"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSKEL_API  TfType


"""
   result["BlendShape"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdSkelBlendShape on UsdPrim C{prim}.


Equivalent to UsdSkelBlendShape::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdSkelBlendShape on the prim held by C{schemaObj}.


Should be preferred over UsdSkelBlendShape (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["BlendShape"].GetPointIndicesAttr.im_func.func_doc = """GetPointIndicesAttr() -> USDSKEL_API UsdAttribute



B{Optional property}.


Indices into the original mesh that correspond to the values in
*offsets* and of any inbetween shapes. If authored, the number of
elements must be equal to the number of elements in the *offsets*
array.

C++ Type: VtArray<unsigned int>  Usd Type:
SdfValueTypeNames->UIntArray  Variability: SdfVariabilityUniform
Fallback Value: No Fallback

"""
   result["BlendShape"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSKEL_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["BlendShape"].Define.func_doc = """**static** Define(stage, path) -> USDSKEL_API UsdSkelBlendShape

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
   result["BlendShape"].CreateOffsetsAttr.im_func.func_doc = """CreateOffsetsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetOffsetsAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BlendShape"].GetInbetween.im_func.func_doc = """GetInbetween(name) -> USDSKEL_API UsdSkelInbetweenShape

name : TfToken


Return the Inbetween corresponding to the attribute named C{name},
which will be valid if an Inbetween attribute definition already
exists.


Name lookup will account for Inbetween namespacing, which means that
this method will succeed in some cases where C{UsdSkelInbetweenShape
(prim->GetAttribute(name))} will not, unless C{name} has the proper
namespace prefix.

HasInbetween()

"""
   result["BlendShape"].CreatePointIndicesAttr.im_func.func_doc = """CreatePointIndicesAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetPointIndicesAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BlendShape"].HasInbetween.im_func.func_doc = """HasInbetween(name) -> USDSKEL_API bool

name : TfToken


Return true if there is a defined Inbetween named C{name} on this
prim.


Name lookup will account for Inbetween namespacing.

GetInbetween()

"""
   result["BakeSkinning"].func_doc = """BakeSkinning(root, interval) -> USDSKEL_API bool

root : Root
interval : GfInterval


Bake the effect of skinning prims directly into points and transforms,
over C{interval}.


This is intended to serve as a complete reference implementation,
providing a ground truth for testing and validation purposes. Since
baking the effect of skinning will undo any IO gains that skeletal
posing provides, this method should not be used outside the context of
testing. This method should only be used for testing or for
transmitting animation to an application that does not understand
UsdSkel skinning.


----------------------------------------------------------------------
BakeSkinning(range, interval) -> USDSKEL_API bool

range : UsdPrimRange
interval : GfInterval


Overload of UsdSkelBakeSkinning, which bakes the effect of skinning
prims directly into points and transforms, for all SkelRoot prims in
C{range}.


----------------------------------------------------------------------
BakeSkinning(root, interval) -> USDSKEL_API bool

root : Root
interval : GfInterval


Bake the effect of skinning prims directly into points and transforms,
over C{interval}.


This is intended to serve as a complete reference implementation,
providing a ground truth for testing and validation purposes. Since
baking the effect of skinning will undo any IO gains that skeletal
posing provides, this method should not be used outside the context of
testing. This method should only be used for testing or for
transmitting animation to an application that does not understand
UsdSkel skinning.


----------------------------------------------------------------------
BakeSkinning(range, interval) -> USDSKEL_API bool

range : UsdPrimRange
interval : GfInterval


Overload of UsdSkelBakeSkinning, which bakes the effect of skinning
prims directly into points and transforms, for all SkelRoot prims in
C{range}.

"""
   result["Root"].__doc__ = """
Boundable prim type used to identify a scope beneath which skeletally-
posed primitives are defined.


A SkelRoot must be defined at or above a skinned primitive for any
skinning behaviors in UsdSkel.

See the extented Skel Root Schema documentation for more information.

"""
   result["Root"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSKEL_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Root"].Get.func_doc = """**static** Get(stage, path) -> USDSKEL_API UsdSkelRoot

stage : UsdStagePtr
path : SdfPath


Return a UsdSkelRoot holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdSkelRoot(stage->GetPrimAtPath(path));


"""
   result["Root"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSKEL_API  TfType


"""
   result["Root"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdSkelRoot on UsdPrim C{prim}.


Equivalent to UsdSkelRoot::Get (prim.GetStage(), prim.GetPath()) for a
*valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdSkelRoot on the prim held by C{schemaObj}.


Should be preferred over UsdSkelRoot (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Root"].Find.func_doc = """**static** Find(prim) -> USDSKEL_API UsdSkelRoot

prim : UsdPrim


Returns the skel root at or above C{prim}, or an invalid schema object
if no ancestor prim is defined as a skel root.

"""
   result["Root"].Define.func_doc = """**static** Define(stage, path) -> USDSKEL_API UsdSkelRoot

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
   result["ComputeJointLocalTransforms"].func_doc = """ComputeJointLocalTransforms(topology, xforms, inverseXforms, jointLocalXforms, rootInverseXform) -> USDSKEL_API bool

topology : Topology
xforms : VtMatrix4dArray
inverseXforms : VtMatrix4dArray
jointLocalXforms : VtMatrix4dArray
rootInverseXform : GfMatrix4d


Compute joint transforms in joint-local space.


Transforms are computed from C{xforms}, holding concatenated joint
transforms, and C{inverseXforms}, providing the inverse of each of
those transforms. If the root transforms include an additional,
external transformation  eg., such as the skel local-to-world
transformation  then the inverse of that transform should be passed as
C{rootInverseXform}. If no C{rootInverseXform} is provided, then
C{xform} and C{inverseXforms} should be based on joint transforms
computed in skeleton space. Each transform array must be sized to the
number of joints from C{topology}.


----------------------------------------------------------------------
ComputeJointLocalTransforms(topology, xforms, inverseXforms, jointLocalXforms, rootInverseXform) -> USDSKEL_API bool

topology : Topology
xforms : GfMatrix4d
inverseXforms : GfMatrix4d
jointLocalXforms : GfMatrix4d
rootInverseXform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ComputeJointLocalTransforms(topology, xforms, inverseXforms, jointLocalXforms, rootInverseXform) -> USDSKEL_API bool

topology : Topology
xforms : VtMatrix4dArray
inverseXforms : VtMatrix4dArray
jointLocalXforms : VtMatrix4dArray
rootInverseXform : GfMatrix4d


Compute joint transforms in joint-local space.


Transforms are computed from C{xforms}, holding concatenated joint
transforms, and C{inverseXforms}, providing the inverse of each of
those transforms. If the root transforms include an additional,
external transformation  eg., such as the skel local-to-world
transformation  then the inverse of that transform should be passed as
C{rootInverseXform}. If no C{rootInverseXform} is provided, then
C{xform} and C{inverseXforms} should be based on joint transforms
computed in skeleton space. Each transform array must be sized to the
number of joints from C{topology}.


----------------------------------------------------------------------
ComputeJointLocalTransforms(topology, xforms, inverseXforms, jointLocalXforms, rootInverseXform) -> USDSKEL_API bool

topology : Topology
xforms : GfMatrix4d
inverseXforms : GfMatrix4d
jointLocalXforms : GfMatrix4d
rootInverseXform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["SkinPointsLBS"].func_doc = """SkinPointsLBS(geomBindTransform, jointXforms, jointIndices, jointWeights, numInfluencesPerPoint, points) -> USDSKEL_API bool

geomBindTransform : GfMatrix4d
jointXforms : VtMatrix4dArray
jointIndices : VtIntArray
jointWeights : VtFloatArray
numInfluencesPerPoint : int
points : VtVec3fArray


Skin points using linear blend skinning (LBS).


The C{jointXforms} are skinning transforms, given in *skeleton space*,
while the C{geomBindTransform} provides the transform that transforms
the initial C{points} into the same *skeleton space* that the skinning
transforms were computed in.


----------------------------------------------------------------------
SkinPointsLBS(geomBindTransform, jointXforms, numJoints, jointIndices, jointWeights, numInfluences, numInfluencesPerPoint, points, numPoints, forceSerial) -> USDSKEL_API bool

geomBindTransform : GfMatrix4d
jointXforms : GfMatrix4d
numJoints : size_t
jointIndices : int
jointWeights : float
numInfluences : size_t
numInfluencesPerPoint : int
points : GfVec3f
numPoints : size_t
forceSerial : bool


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
SkinPointsLBS(geomBindTransform, jointXforms, jointIndices, jointWeights, numInfluencesPerPoint, points) -> USDSKEL_API bool

geomBindTransform : GfMatrix4d
jointXforms : VtMatrix4dArray
jointIndices : VtIntArray
jointWeights : VtFloatArray
numInfluencesPerPoint : int
points : VtVec3fArray


Skin points using linear blend skinning (LBS).


The C{jointXforms} are skinning transforms, given in *skeleton space*,
while the C{geomBindTransform} provides the transform that transforms
the initial C{points} into the same *skeleton space* that the skinning
transforms were computed in.


----------------------------------------------------------------------
SkinPointsLBS(geomBindTransform, jointXforms, numJoints, jointIndices, jointWeights, numInfluences, numInfluencesPerPoint, points, numPoints, forceSerial) -> USDSKEL_API bool

geomBindTransform : GfMatrix4d
jointXforms : GfMatrix4d
numJoints : size_t
jointIndices : int
jointWeights : float
numInfluences : size_t
numInfluencesPerPoint : int
points : GfVec3f
numPoints : size_t
forceSerial : bool


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ResizeInfluences"].func_doc = """ResizeInfluences(indices, srcNumInfluencesPerComponent, newNumInfluencesPerComponent) -> USDSKEL_API bool

indices : VtIntArray
srcNumInfluencesPerComponent : int
newNumInfluencesPerComponent : int


Resize the number of influences per component in a weight or indices
array, which initially has C{srcNumInfluencesPerComponent} influences
to have no more than C{newNumInfluencesPerComponent} influences per
component.


If the size decreases, influences are additionally re-normalized. This
is a convenience method for clients that require a fixed number of of
influences.


----------------------------------------------------------------------
ResizeInfluences(weights, srcNumInfluencesPerComponent, newNumInfluencesPerComponent) -> USDSKEL_API bool

weights : VtFloatArray
srcNumInfluencesPerComponent : int
newNumInfluencesPerComponent : int


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ResizeInfluences(indices, srcNumInfluencesPerComponent, newNumInfluencesPerComponent) -> USDSKEL_API bool

indices : VtIntArray
srcNumInfluencesPerComponent : int
newNumInfluencesPerComponent : int


Resize the number of influences per component in a weight or indices
array, which initially has C{srcNumInfluencesPerComponent} influences
to have no more than C{newNumInfluencesPerComponent} influences per
component.


If the size decreases, influences are additionally re-normalized. This
is a convenience method for clients that require a fixed number of of
influences.


----------------------------------------------------------------------
ResizeInfluences(weights, srcNumInfluencesPerComponent, newNumInfluencesPerComponent) -> USDSKEL_API bool

weights : VtFloatArray
srcNumInfluencesPerComponent : int
newNumInfluencesPerComponent : int


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Topology"].__doc__ = """
Object holding information describing skeleton topology.


This provides the hierarchical information needed to reason about
joint relationships in a manner suitable to computations.

"""
   result["Topology"].GetParent.im_func.func_doc = """GetParent(index) -> int

index : size_t


Returns the parent joint of the C{index'th} joint, Returns -1 for
joints with no parent (roots).

"""
   result["Topology"].GetParentIndices.im_func.func_doc = """GetParentIndices() -> VtIntArray


"""
   result["Topology"].__init__.im_func.func_doc = """__init__() -> USDSKEL_API



Construct an empty topology.


----------------------------------------------------------------------
__init__(paths) -> USDSKEL_API

paths : VtTokenArray


Construct a skel topology from C{paths}, an array holding ordered
joint paths as tokens.


Internally, each token must be converted to an SdfPath. If SdfPath
objects are already accessible, it is more efficient to use the
construct taking an SdfPath array.


----------------------------------------------------------------------
__init__(paths, size) -> USDSKEL_API

paths : TfToken
size : size_t


Construct a skel topology from C{paths}, an array of size C{size},
holding ordered joint paths as tokens.


----------------------------------------------------------------------
__init__(paths) -> USDSKEL_API

paths : SdfPathVector


Construct a skel topology from C{paths}, an array of joint paths.


----------------------------------------------------------------------
__init__(paths, size) -> USDSKEL_API

paths : SdfPath
size : size_t


Construct a skel topology from C{paths}, an array of joints paths of
size C{size}.


----------------------------------------------------------------------
__init__(parentIndices) -> USDSKEL_API

parentIndices : VtIntArray


Construct a skel topology from an array of parent indices.


For each joint, this provides the parent index of that joint, or -1 if
none.

"""
   result["Topology"].GetNumJoints.im_func.func_doc = """GetNumJoints() -> size_t


"""
   result["Topology"].Validate.im_func.func_doc = """Validate(reason) -> USDSKEL_API bool

reason : string


Validate the topology.


If validation is unsuccessful, a reason why will be written to
C{reason}, if provided.

"""
   result["IsSkelAnimationPrim"].func_doc = """IsSkelAnimationPrim(prim) -> USDSKEL_API bool

prim : UsdPrim


Returns true if C{prim} is a valid skel animation source.


----------------------------------------------------------------------
IsSkelAnimationPrim(prim) -> USDSKEL_API bool

prim : UsdPrim


Returns true if C{prim} is a valid skel animation source.

"""
   result["SortInfluences"].func_doc = """SortInfluences(indices, weights, numInfluencesPerComponent) -> USDSKEL_API bool

indices : VtIntArray
weights : VtFloatArray
numInfluencesPerComponent : int


Sort joint influences such that highest weight values come first.


----------------------------------------------------------------------
SortInfluences(indices, weights, numInfluencesPerComponent) -> USDSKEL_API bool

indices : VtIntArray
weights : VtFloatArray
numInfluencesPerComponent : int


Sort joint influences such that highest weight values come first.

"""
   result["ComputeJointsExtent"].func_doc = """ComputeJointsExtent(joints, extent, pad, rootXform) -> USDSKEL_API bool

joints : VtMatrix4dArray
extent : VtVec3fArray
pad : float
rootXform : GfMatrix4d


Compute an extent from a set of skel-space joint transform.


The C{rootXform} may also be set to provide an additional root
transformation on top of all joints, which is useful for computing
extent relative to a different space.


----------------------------------------------------------------------
ComputeJointsExtent(xforms, numXforms, extent, pad, rootXform) -> USDSKEL_API bool

xforms : GfMatrix4d
numXforms : size_t
extent : VtVec3fArray
pad : float
rootXform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ComputeJointsExtent(joints, extent, pad, rootXform) -> USDSKEL_API bool

joints : VtMatrix4dArray
extent : VtVec3fArray
pad : float
rootXform : GfMatrix4d


Compute an extent from a set of skel-space joint transform.


The C{rootXform} may also be set to provide an additional root
transformation on top of all joints, which is useful for computing
extent relative to a different space.


----------------------------------------------------------------------
ComputeJointsExtent(xforms, numXforms, extent, pad, rootXform) -> USDSKEL_API bool

xforms : GfMatrix4d
numXforms : size_t
extent : VtVec3fArray
pad : float
rootXform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ConcatJointTransforms"].func_doc = """ConcatJointTransforms(topology, jointLocalXforms, xforms, rootXform) -> USDSKEL_API bool

topology : Topology
jointLocalXforms : VtMatrix4dArray
xforms : VtMatrix4dArray
rootXform : GfMatrix4d


Compute concatenated joint transforms.


This concatenates transforms from C{jointLocalXforms}, providing joint
transforms in joint-local space. If C{rootXform} is not provided, or
is the identity, the resulting joint transforms will be given in
skeleton space. Any additional transformations may be provided on
C{rootXform} if an additional level of transformation  such as the
skel local to world transform  are desired. Each transform array must
be sized to the number of joints from C{topology}.


----------------------------------------------------------------------
ConcatJointTransforms(topology, jointLocalXforms, xforms, rootXform) -> USDSKEL_API bool

topology : Topology
jointLocalXforms : GfMatrix4d
xforms : GfMatrix4d
rootXform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ConcatJointTransforms(topology, jointLocalXforms, xforms, rootXform) -> USDSKEL_API bool

topology : Topology
jointLocalXforms : VtMatrix4dArray
xforms : VtMatrix4dArray
rootXform : GfMatrix4d


Compute concatenated joint transforms.


This concatenates transforms from C{jointLocalXforms}, providing joint
transforms in joint-local space. If C{rootXform} is not provided, or
is the identity, the resulting joint transforms will be given in
skeleton space. Any additional transformations may be provided on
C{rootXform} if an additional level of transformation  such as the
skel local to world transform  are desired. Each transform array must
be sized to the number of joints from C{topology}.


----------------------------------------------------------------------
ConcatJointTransforms(topology, jointLocalXforms, xforms, rootXform) -> USDSKEL_API bool

topology : Topology
jointLocalXforms : GfMatrix4d
xforms : GfMatrix4d
rootXform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["AnimQuery"].__doc__ = """
Class providing efficient queries of primitives that provide skel
animation.

"""
   result["AnimQuery"].ComputeBlendShapeWeights.im_func.func_doc = """ComputeBlendShapeWeights(weights, time) -> USDSKEL_API bool

weights : VtFloatArray
time : UsdTimeCode

"""
   result["AnimQuery"].ComputeJointLocalTransformComponents.im_func.func_doc = """ComputeJointLocalTransformComponents(translations, rotations, scales, time) -> USDSKEL_API bool

translations : VtVec3fArray
rotations : VtQuatfArray
scales : VtVec3hArray
time : UsdTimeCode


Compute translation,rotation,scale components of the joint transforms
in joint-local space.


This is provided to facilitate direct streaming of animation data in a
form that can efficiently be processed for animation blending.

"""
   result["AnimQuery"].GetJointTransformTimeSamples.im_func.func_doc = """GetJointTransformTimeSamples(times) -> USDSKEL_API bool

times : sequence<double>


Get the time samples at which values contributing to joint transforms
are set.


This only computes the time samples for sampling transforms in joint-
local space, and does not include time samples affecting the root
transformation.

UsdAttribute::GetTimeSamples

"""
   result["AnimQuery"].GetJointOrder.im_func.func_doc = """GetJointOrder() -> USDSKEL_API VtTokenArray



Returns an array of tokens describing the ordering of joints in the
animation.



UsdSkelSkeleton::GetJointOrder

"""
   result["AnimQuery"].GetJointTransformTimeSamplesInInterval.im_func.func_doc = """GetJointTransformTimeSamplesInInterval(interval, times) -> USDSKEL_API bool

interval : GfInterval
times : sequence<double>


Get the time samples at which values contributing to joint transforms
are set, over C{interval}.


This only computes the time samples for sampling transforms in joint-
local space, and does not include time samples affecting the root
transformation.

UsdAttribute::GetTimeSamplesInInterval

"""
   result["AnimQuery"].GetBlendShapeOrder.im_func.func_doc = """GetBlendShapeOrder() -> USDSKEL_API VtTokenArray



Returns an array of tokens describing the ordering of blend shape
channels in the animation.

"""
   result["AnimQuery"].ComputeJointLocalTransforms.im_func.func_doc = """ComputeJointLocalTransforms(xforms, time) -> USDSKEL_API bool

xforms : VtMatrix4dArray
time : UsdTimeCode


Compute joint transforms in joint-local space.


Transforms are returned in the order specified by the joint ordering
of the animation primitive itself.

"""
   result["AnimQuery"].GetPrim.im_func.func_doc = """GetPrim() -> USDSKEL_API UsdPrim



Return the primitive this anim query reads from.

"""
   result["AnimQuery"].JointTransformsMightBeTimeVarying.im_func.func_doc = """JointTransformsMightBeTimeVarying() -> USDSKEL_API bool



Return true if it possible, but not certain, that joint transforms
computed through this animation query change over time, false
otherwise.



UsdAttribute::ValueMightBeTimeVayring

"""
   result["Skeleton"].__doc__ = """
Describes a skeleton.


See the extended Skeleton Schema documentation for more information.

"""
   result["Skeleton"].CreateJointsAttr.im_func.func_doc = """CreateJointsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetJointsAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Skeleton"].CreateRestTransformsAttr.im_func.func_doc = """CreateRestTransformsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRestTransformsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Skeleton"].GetJointsAttr.im_func.func_doc = """GetJointsAttr() -> USDSKEL_API UsdAttribute



An array of path tokens identifying the set of joints that make up the
skeleton, and their order.


Each token in the array must be valid when parsed as an SdfPath. The
parent-child relationships of the corresponding paths determine the
parent-child relationships of each joint.

C++ Type: VtArray<TfToken>  Usd Type: SdfValueTypeNames->TokenArray
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["Skeleton"].Get.func_doc = """**static** Get(stage, path) -> USDSKEL_API UsdSkelSkeleton

stage : UsdStagePtr
path : SdfPath


Return a UsdSkelSkeleton holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdSkelSkeleton(stage->GetPrimAtPath(path));


"""
   result["Skeleton"].GetRestTransformsAttr.im_func.func_doc = """GetRestTransformsAttr() -> USDSKEL_API UsdAttribute



Specifies the rest-pose transforms of each joint in B{local space}, in
the ordering imposed by *joints*.


This provides fallback values for joint transforms when a Skeleton
either has no bound animation source, or when that animation source
only contains animation for a subset of a Skeleton's joints.

C++ Type: VtArray<GfMatrix4d>  Usd Type:
SdfValueTypeNames->Matrix4dArray  Variability: SdfVariabilityUniform
Fallback Value: No Fallback

"""
   result["Skeleton"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdSkelSkeleton on UsdPrim C{prim}.


Equivalent to UsdSkelSkeleton::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdSkelSkeleton on the prim held by C{schemaObj}.


Should be preferred over UsdSkelSkeleton (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Skeleton"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSKEL_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Skeleton"].CreateBindTransformsAttr.im_func.func_doc = """CreateBindTransformsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetBindTransformsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Skeleton"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSKEL_API  TfType


"""
   result["Skeleton"].GetBindTransformsAttr.im_func.func_doc = """GetBindTransformsAttr() -> USDSKEL_API UsdAttribute



Specifies the bind-pose transforms of each joint in B{world space}, in
the ordering imposed by *joints*.


C++ Type: VtArray<GfMatrix4d>  Usd Type:
SdfValueTypeNames->Matrix4dArray  Variability: SdfVariabilityUniform
Fallback Value: No Fallback

"""
   result["Skeleton"].Define.func_doc = """**static** Define(stage, path) -> USDSKEL_API UsdSkelSkeleton

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
   result["SkinTransformLBS"].func_doc = """SkinTransformLBS(geomBindTransform, jointXforms, jointIndices, jointWeights, xform) -> USDSKEL_API bool

geomBindTransform : GfMatrix4d
jointXforms : VtMatrix4dArray
jointIndices : VtIntArray
jointWeights : VtFloatArray
xform : GfMatrix4d


Skin a transform using linear blend skinning (LBS).


The C{jointXforms} are skinning transforms, given in *skeleton space*,
while the C{geomBindTransform} provides the transform that initially
places a primitive in that same *skeleton space*.


----------------------------------------------------------------------
SkinTransformLBS(geomBindTransform, jointXforms, numJoints, jointIndices, jointWeights, numInfluences, xform) -> USDSKEL_API bool

geomBindTransform : GfMatrix4d
jointXforms : GfMatrix4d
numJoints : size_t
jointIndices : int
jointWeights : float
numInfluences : size_t
xform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
SkinTransformLBS(geomBindTransform, jointXforms, jointIndices, jointWeights, xform) -> USDSKEL_API bool

geomBindTransform : GfMatrix4d
jointXforms : VtMatrix4dArray
jointIndices : VtIntArray
jointWeights : VtFloatArray
xform : GfMatrix4d


Skin a transform using linear blend skinning (LBS).


The C{jointXforms} are skinning transforms, given in *skeleton space*,
while the C{geomBindTransform} provides the transform that initially
places a primitive in that same *skeleton space*.


----------------------------------------------------------------------
SkinTransformLBS(geomBindTransform, jointXforms, numJoints, jointIndices, jointWeights, numInfluences, xform) -> USDSKEL_API bool

geomBindTransform : GfMatrix4d
jointXforms : GfMatrix4d
numJoints : size_t
jointIndices : int
jointWeights : float
numInfluences : size_t
xform : GfMatrix4d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Cache"].__doc__ = """
Thread-safe cache for accessing query objects for evaluating skeletal
data.


This provides caching of major structural components, such as skeletal
topology. In a streaming context, this cache is intended to persist.

"""
   result["Cache"].GetAnimQuery.im_func.func_doc = """GetAnimQuery(prim) -> USDSKEL_API UsdSkelAnimQuery

prim : UsdPrim


Get an anim query corresponding to C{prim}.


This does not require Populate() to be called on the cache.

"""
   result["Cache"].ComputeSkelBinding.im_func.func_doc = """ComputeSkelBinding(skelRoot, skel, binding) -> USDSKEL_API bool

skelRoot : Root
skel : Skeleton
binding : Binding


Compute the bindings corresponding to a single skeleton, bound beneath
C{skelRoot}.

"""
   result["Cache"].Populate.im_func.func_doc = """Populate(root) -> USDSKEL_API bool

root : Root


Populate the cache for the skeletal data beneath prim C{root}.

"""
   result["Cache"].Clear.im_func.func_doc = """Clear() -> USDSKEL_API void


"""
   result["Cache"].ComputeSkelBindings.im_func.func_doc = """ComputeSkelBindings(skelRoot, bindings) -> USDSKEL_API bool

skelRoot : Root
bindings : sequence< UsdSkelBinding >


Compute the set of skeleton bindings beneath C{skelRoot}.

"""
   result["Cache"].GetSkelQuery.im_func.func_doc = """GetSkelQuery(skel) -> USDSKEL_API UsdSkelSkeletonQuery

skel : Skeleton


Get a skel query for computing properties of C{skel}.


This does not require Populate() to be called on the cache.

"""
   result["Cache"].__init__.im_func.func_doc = """__init__() -> USDSKEL_API


"""
   result["Cache"].GetSkinningQuery.im_func.func_doc = """GetSkinningQuery(prim) -> USDSKEL_API UsdSkelSkinningQuery

prim : UsdPrim


Get a skinning query at C{prim}.


Skinning queries are defined at any skinnable prims (I.e., boundable
prims with fully defined joint influences).

The caller must first Populate() the cache with the skel root
containing C{prim} in order for any skinning queries to be
discoverabble.

"""
   result["BindingAPI"].__doc__ = """
Provides API for authoring and extracting all the skinning-related
data that lives in the "geometry hierarchy" of prims and models that
want to be skeletally deformed.


See the extended UsdSkelBindingAPI schema documentation for more about
bindings and how they apply in a scene graph.

"""
   result["BindingAPI"].CreateGeomBindTransformAttr.im_func.func_doc = """CreateGeomBindTransformAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetGeomBindTransformAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BindingAPI"].GetAnimationSourceRel.im_func.func_doc = """GetAnimationSourceRel() -> USDSKEL_API UsdRelationship



Animation source to be bound to Skeleton primitives at or beneath the
location at which this property is defined.

"""
   result["BindingAPI"].GetInheritedAnimationSource.im_func.func_doc = """GetInheritedAnimationSource() -> USDSKEL_API UsdPrim



Returns the animation source bound at this prim, or one of its
ancestors.

"""
   result["BindingAPI"].GetInheritedSkeleton.im_func.func_doc = """GetInheritedSkeleton() -> USDSKEL_API UsdSkelSkeleton



Returns the skeleton bound at this prim, or one of its ancestors.

"""
   result["BindingAPI"].CreateJointIndicesAttr.im_func.func_doc = """CreateJointIndicesAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetJointIndicesAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BindingAPI"].GetSkeleton.im_func.func_doc = """GetSkeleton(skel) -> USDSKEL_API bool

skel : Skeleton


Convenience method to query the Skeleton bound on this prim.


Returns true if a Skeleton binding is defined, and sets C{skel} to the
target skel. The resulting Skeleton may still be invalid, if the
Skeleton has been explicitly *unbound*.

This does not resolved inherited skeleton bindings.

"""
   result["BindingAPI"].CreateJointIndicesPrimvar.im_func.func_doc = """CreateJointIndicesPrimvar(constant, elementSize) -> USDSKEL_API UsdGeomPrimvar

constant : bool
elementSize : int


Convenience function to create the jointIndices primvar, optionally
specifying elementSize.


If C{constant} is true, the resulting primvar is configured with
'constant' interpolation, and describes a rigid deformation.
Otherwise, the primvar is configured with 'vertex' interpolation, and
describes joint influences that vary per point.

CreateJointIndicesAttr() , GetJointIndicesPrimvar()

"""
   result["BindingAPI"].SetRigidJointInfluence.im_func.func_doc = """SetRigidJointInfluence(jointIndex, weight) -> USDSKEL_API bool

jointIndex : int
weight : float


Convenience method for defining joints influences that make a
primitive rigidly deformed by a single joint.

"""
   result["BindingAPI"].GetJointWeightsPrimvar.im_func.func_doc = """GetJointWeightsPrimvar() -> USDSKEL_API UsdGeomPrimvar



Convenience function to get the jointWeights attribute as a primvar.



GetJointWeightsAttr, GetInheritedJointWeightsPrimvar

"""
   result["BindingAPI"].CreateJointsAttr.im_func.func_doc = """CreateJointsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetJointsAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BindingAPI"].GetJointIndicesAttr.im_func.func_doc = """GetJointIndicesAttr() -> USDSKEL_API UsdAttribute



Indices into the *joints* attribute of the closest (in namespace)
bound Skeleton that affect each point of a PointBased gprim.


The primvar can have either *constant* or *vertex* interpolation. This
primvar's *elementSize* will determine how many joint influences apply
to each point. Indices must point be valid. Null influences should be
defined by setting values in jointWeights to zero. See UsdGeomPrimvar
for more information on interpolation and elementSize.

C++ Type: VtArray<int>  Usd Type: SdfValueTypeNames->IntArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["BindingAPI"].Get.func_doc = """**static** Get(stage, path) -> USDSKEL_API UsdSkelBindingAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdSkelBindingAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdSkelBindingAPI(stage->GetPrimAtPath(path));


"""
   result["BindingAPI"].GetJointsAttr.im_func.func_doc = """GetJointsAttr() -> USDSKEL_API UsdAttribute



An (optional) array of tokens defining the list of joints to which
jointIndices apply.


If not defined, jointIndices applies to the ordered list of joints
defined in the bound Skeleton's *joints* attribute. If undefined on a
primitive, the primitive inherits the value of the nearest ancestor
prim, if any.

C++ Type: VtArray<TfToken>  Usd Type: SdfValueTypeNames->TokenArray
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["BindingAPI"].GetSkeletonRel.im_func.func_doc = """GetSkeletonRel() -> USDSKEL_API UsdRelationship



Skeleton to be bound to this prim and its descendents that possess a
mapping and weighting to the joints of the identified Skeleton.

"""
   result["BindingAPI"].CreateSkeletonRel.im_func.func_doc = """CreateSkeletonRel() -> USDSKEL_API UsdRelationship



See GetSkeletonRel() , and also Create vs Get Property Methods for
when to use Get vs Create.

"""
   result["BindingAPI"].GetBlendShapesAttr.im_func.func_doc = """GetBlendShapesAttr() -> USDSKEL_API UsdAttribute



An array of tokens defining the order onto which blend shape weights
from an animation source map onto the *skel:blendShapeTargets* rel of
a binding site.


If authored, the number of elements must be equal to the number of
targets in the *blendShapeTargets* rel. This property is not inherited
hierarchically, and is expected to be authored directly on the
skinnable primitive to which the blend shapes apply.

C++ Type: VtArray<TfToken>  Usd Type: SdfValueTypeNames->TokenArray
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["BindingAPI"].GetBlendShapeTargetsRel.im_func.func_doc = """GetBlendShapeTargetsRel() -> USDSKEL_API UsdRelationship



Ordered list of all target blend shapes.


This property is not inherited hierarchically, and is expected to be
authored directly on the skinnable primitive to which the the blend
shapes apply.

"""
   result["BindingAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdSkelBindingAPI on UsdPrim C{prim}.


Equivalent to UsdSkelBindingAPI::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdSkelBindingAPI on the prim held by C{schemaObj}.


Should be preferred over UsdSkelBindingAPI (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["BindingAPI"].CreateAnimationSourceRel.im_func.func_doc = """CreateAnimationSourceRel() -> USDSKEL_API UsdRelationship



See GetAnimationSourceRel() , and also Create vs Get Property Methods
for when to use Get vs Create.

"""
   result["BindingAPI"].CreateJointWeightsAttr.im_func.func_doc = """CreateJointWeightsAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetJointWeightsAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BindingAPI"].CreateBlendShapesAttr.im_func.func_doc = """CreateBlendShapesAttr(defaultValue, writeSparsely) -> USDSKEL_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetBlendShapesAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["BindingAPI"].GetAnimationSource.im_func.func_doc = """GetAnimationSource(prim) -> USDSKEL_API bool

prim : UsdPrim


Convenience method to query the animation source bound on this prim.


Returns true if an animation source binding is defined, and sets
C{prim} to the target prim. The resulting primitive may still be
invalid, if the prim has been explicitly *unbound*.

This does not resolved inherited animation source bindings.

"""
   result["BindingAPI"].Apply.func_doc = """**static** Apply(prim) -> USDSKEL_API UsdSkelBindingAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "BindingAPI" to the token-valued,
listOp metadata *apiSchemas* on the prim.

A valid UsdSkelBindingAPI object is returned upon success. An invalid
(or empty) UsdSkelBindingAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["BindingAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSKEL_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["BindingAPI"].CreateBlendShapeTargetsRel.im_func.func_doc = """CreateBlendShapeTargetsRel() -> USDSKEL_API UsdRelationship



See GetBlendShapeTargetsRel() , and also Create vs Get Property
Methods for when to use Get vs Create.

"""
   result["BindingAPI"].GetJointIndicesPrimvar.im_func.func_doc = """GetJointIndicesPrimvar() -> USDSKEL_API UsdGeomPrimvar



Convenience function to get the jointIndices attribute as a primvar.



GetJointIndicesAttr, GetInheritedJointWeightsPrimvar

"""
   result["BindingAPI"].GetGeomBindTransformAttr.im_func.func_doc = """GetGeomBindTransformAttr() -> USDSKEL_API UsdAttribute



Encodes the bind-time world space transforms of the prim.


If the transform is identical for a group of gprims that share a
common ancestor, the transform may be authored on the ancestor, to
"inherit" down to all the leaf gprims. If this transform is unset, an
identity transform is used instead.

C++ Type: GfMatrix4d  Usd Type: SdfValueTypeNames->Matrix4d
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["BindingAPI"].CreateJointWeightsPrimvar.im_func.func_doc = """CreateJointWeightsPrimvar(constant, elementSize) -> USDSKEL_API UsdGeomPrimvar

constant : bool
elementSize : int


Convenience function to create the jointWeights primvar, optionally
specifying elementSize.


If C{constant} is true, the resulting primvar is configured with
'constant' interpolation, and describes a rigid deformation.
Otherwise, the primvar is configured with 'vertex' interpolation, and
describes joint influences that vary per point.

CreateJointWeightsAttr() , GetJointWeightsPrimvar()

"""
   result["BindingAPI"].GetJointWeightsAttr.im_func.func_doc = """GetJointWeightsAttr() -> USDSKEL_API UsdAttribute



Weights for the joints that affect each point of a PointBased gprim.


The primvar can have either *constant* or *vertex* interpolation. This
primvar's *elementSize* will determine how many joints influences
apply to each point. The length, interpolation, and elementSize of
*jointWeights* must match that of *jointIndices*. See UsdGeomPrimvar
for more information on interpolation and elementSize.

C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["BindingAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSKEL_API  TfType


"""
   result["MakeTransform"].func_doc = """MakeTransform(translate, rotate, scale) -> USDSKEL_API GfMatrix4d

translate : GfVec3f
rotate : GfMatrix3f
scale : GfVec3h


Create a transform from translate/rotate/scale components.


This performs the inverse of UsdSkelDecomposeTransform.


----------------------------------------------------------------------
MakeTransform(translate, rotate, scale) -> USDSKEL_API GfMatrix4d

translate : GfVec3f
rotate : GfQuatf
scale : GfVec3h


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
MakeTransform(translate, rotate, scale) -> USDSKEL_API GfMatrix4d

translate : GfVec3f
rotate : GfMatrix3f
scale : GfVec3h


Create a transform from translate/rotate/scale components.


This performs the inverse of UsdSkelDecomposeTransform.


----------------------------------------------------------------------
MakeTransform(translate, rotate, scale) -> USDSKEL_API GfMatrix4d

translate : GfVec3f
rotate : GfQuatf
scale : GfVec3h


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["PackedJointAnimation"].__doc__ = """
Deprecated.


Please use SkelAnimation instead.

"""
   result["PackedJointAnimation"].Get.func_doc = """**static** Get(stage, path) -> USDSKEL_API UsdSkelPackedJointAnimation

stage : UsdStagePtr
path : SdfPath


Return a UsdSkelPackedJointAnimation holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdSkelPackedJointAnimation(stage->GetPrimAtPath(path));


"""
   result["PackedJointAnimation"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdSkelPackedJointAnimation on UsdPrim C{prim}.


Equivalent to UsdSkelPackedJointAnimation::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdSkelPackedJointAnimation on the prim held by
C{schemaObj}.


Should be preferred over UsdSkelPackedJointAnimation
(schemaObj.GetPrim()), as it preserves SchemaBase state.

"""
   result["PackedJointAnimation"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSKEL_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PackedJointAnimation"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSKEL_API  TfType


"""
   result["PackedJointAnimation"].Define.func_doc = """**static** Define(stage, path) -> USDSKEL_API UsdSkelPackedJointAnimation

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
   result["MakeTransforms"].func_doc = """MakeTransforms(translations, rotations, scales, xforms) -> USDSKEL_API bool

translations : VtVec3fArray
rotations : VtQuatfArray
scales : VtVec3hArray
xforms : VtMatrix4dArray


Create transforms from arrays of components.


----------------------------------------------------------------------
MakeTransforms(translations, rotations, scales, xforms, count) -> USDSKEL_API bool

translations : GfVec3f
rotations : GfQuatf
scales : GfVec3h
xforms : GfMatrix4d
count : size_t


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
MakeTransforms(translations, rotations, scales, xforms) -> USDSKEL_API bool

translations : VtVec3fArray
rotations : VtQuatfArray
scales : VtVec3hArray
xforms : VtMatrix4dArray


Create transforms from arrays of components.


----------------------------------------------------------------------
MakeTransforms(translations, rotations, scales, xforms, count) -> USDSKEL_API bool

translations : GfVec3f
rotations : GfQuatf
scales : GfVec3h
xforms : GfMatrix4d
count : size_t


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""