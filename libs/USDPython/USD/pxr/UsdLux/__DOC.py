def Execute(result):
   result["ShadowAPI"].__doc__ = """
Controls to refine a light's shadow behavior.


These are non-physical controls that are valuable for visual lighting
work.

"""
   result["ShadowAPI"].CreateShadowColorAttr.im_func.func_doc = """CreateShadowColorAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShadowColorAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShadowAPI"].GetShadowFalloffGammaAttr.im_func.func_doc = """GetShadowFalloffGammaAttr() -> USDLUX_API UsdAttribute



A gamma (i.e., exponential) control over shadow strength with linear
distance within the falloff zone.


This requires the use of shadowDistance and shadowFalloff.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["ShadowAPI"].CreateShadowFalloffAttr.im_func.func_doc = """CreateShadowFalloffAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShadowFalloffAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShadowAPI"].GetShadowColorAttr.im_func.func_doc = """GetShadowColorAttr() -> USDLUX_API UsdAttribute



The color of shadows cast by the light.


This is a non-physical control. The default is to cast black shadows.

C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Color3f  Variability:
SdfVariabilityVarying  Fallback Value: (0, 0, 0)

"""
   result["ShadowAPI"].GetShadowExcludeRel.im_func.func_doc = """GetShadowExcludeRel() -> USDLUX_API UsdRelationship



Set of geometry to ignore for the purpose of casting shadows from a
light.


If this is not specified, all geometry is used for shadowing.

"""
   result["ShadowAPI"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxShadowAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxShadowAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxShadowAPI(stage->GetPrimAtPath(path));


"""
   result["ShadowAPI"].GetShadowEnableAttr.im_func.func_doc = """GetShadowEnableAttr() -> USDLUX_API UsdAttribute



Enables shadows to be cast by this light.


C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: True

"""
   result["ShadowAPI"].CreateShadowExcludeRel.im_func.func_doc = """CreateShadowExcludeRel() -> USDLUX_API UsdRelationship



See GetShadowExcludeRel() , and also Create vs Get Property Methods
for when to use Get vs Create.

"""
   result["ShadowAPI"].GetShadowIncludeRel.im_func.func_doc = """GetShadowIncludeRel() -> USDLUX_API UsdRelationship



Set of geometry to consider for the purpose of casting shadows from a
light.


If this is not specified, all geometry is used for shadowing.

"""
   result["ShadowAPI"].CreateShadowIncludeRel.im_func.func_doc = """CreateShadowIncludeRel() -> USDLUX_API UsdRelationship



See GetShadowIncludeRel() , and also Create vs Get Property Methods
for when to use Get vs Create.

"""
   result["ShadowAPI"].GetShadowDistanceAttr.im_func.func_doc = """GetShadowDistanceAttr() -> USDLUX_API UsdAttribute



The maximum distance shadows are cast.


There is no limit unless this attribute value is overridden.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["ShadowAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["ShadowAPI"].CreateShadowFalloffGammaAttr.im_func.func_doc = """CreateShadowFalloffGammaAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShadowFalloffGammaAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShadowAPI"].CreateShadowEnableAttr.im_func.func_doc = """CreateShadowEnableAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShadowEnableAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShadowAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxShadowAPI on UsdPrim C{prim}.


Equivalent to UsdLuxShadowAPI::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxShadowAPI on the prim held by C{schemaObj}.


Should be preferred over UsdLuxShadowAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["ShadowAPI"].GetShadowFalloffAttr.im_func.func_doc = """GetShadowFalloffAttr() -> USDLUX_API UsdAttribute



The near distance at which shadow falloff beings.


There is no falloff unless this attribute value is overridden.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["ShadowAPI"].CreateShadowDistanceAttr.im_func.func_doc = """CreateShadowDistanceAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShadowDistanceAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShadowAPI"].Apply.func_doc = """**static** Apply(prim) -> USDLUX_API UsdLuxShadowAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "ShadowAPI" to the token-valued,
listOp metadata *apiSchemas* on the prim.

A valid UsdLuxShadowAPI object is returned upon success. An invalid
(or empty) UsdLuxShadowAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["ShadowAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["Light"].__doc__ = """
Base class for all lights.


B{Linking}

Lights can be linked to geometry. Linking controls which geometry a
light illuminates, and which geometry casts shadows from the light.

Linking is specified as collections (UsdCollectionAPI) which can be
accessed via GetLightLinkCollection() and GetShadowLinkCollection().
Note however that there are extra semantics in how UsdLuxLight uses
its collections: if a collection is empty, the light is treated as
linked to *all* geometry for the respective purpose. UsdCollectionAPI
and UsdCollectionAPI::MembershipQuery are unaware of this light-
specific interpretation.

"""
   result["Light"].GetFiltersRel.im_func.func_doc = """GetFiltersRel() -> USDLUX_API UsdRelationship



Relationship to the light filters that apply to this light.

"""
   result["Light"].CreateEnableColorTemperatureAttr.im_func.func_doc = """CreateEnableColorTemperatureAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEnableColorTemperatureAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Light"].CreateDiffuseAttr.im_func.func_doc = """CreateDiffuseAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDiffuseAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Light"].CreateNormalizeAttr.im_func.func_doc = """CreateNormalizeAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetNormalizeAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Light"].GetLightLinkCollectionAPI.im_func.func_doc = """GetLightLinkCollectionAPI() -> USDLUX_API UsdCollectionAPI



Return the UsdCollectionAPI interface used for examining and modifying
the light-linking of this light.


Light-linking controls which geometry this light illuminates.

"""
   result["Light"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxLight

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxLight holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxLight(stage->GetPrimAtPath(path));


"""
   result["Light"].GetIntensityAttr.im_func.func_doc = """GetIntensityAttr() -> USDLUX_API UsdAttribute



Scales the power of the light linearly.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["Light"].GetColorTemperatureAttr.im_func.func_doc = """GetColorTemperatureAttr() -> USDLUX_API UsdAttribute



Color temperature, in degrees Kelvin, representing the white point.


The default is a common white point, D65. Lower values are warmer and
higher values are cooler. The valid range is from 1000 to 10000. Only
takes effect when enableColorTemperature is set to true. When active,
the computed result multiplies against the color attribute. See
UsdLuxBlackbodyTemperatureAsRgb() .

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 6500.0

"""
   result["Light"].CreateExposureAttr.im_func.func_doc = """CreateExposureAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetExposureAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Light"].CreateIntensityAttr.im_func.func_doc = """CreateIntensityAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetIntensityAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Light"].GetColorAttr.im_func.func_doc = """GetColorAttr() -> USDLUX_API UsdAttribute



The color of emitted light, in energy-linear terms.


C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Color3f  Variability:
SdfVariabilityVarying  Fallback Value: (1, 1, 1)

"""
   result["Light"].GetNormalizeAttr.im_func.func_doc = """GetNormalizeAttr() -> USDLUX_API UsdAttribute



Normalizes power by the surface area of the light.


This makes it easier to independently adjust the power and shape of
the light, by causing the power to not vary with the area or angular
size of the light.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["Light"].CreateFiltersRel.im_func.func_doc = """CreateFiltersRel() -> USDLUX_API UsdRelationship



See GetFiltersRel() , and also Create vs Get Property Methods for when
to use Get vs Create.

"""
   result["Light"].GetDiffuseAttr.im_func.func_doc = """GetDiffuseAttr() -> USDLUX_API UsdAttribute



A multiplier for the effect of this light on the diffuse response of
materials.


This is a non-physical control.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["Light"].ComputeBaseEmission.im_func.func_doc = """ComputeBaseEmission() -> USDLUX_API GfVec3f



Computes the base emission (aka radiant flux density, aka energy per
unit area), incorporating the parameters for intensity, exposure,
color, and colorTemperature attributes.


This "base" emission method exists solely as a reference example
implementation of how to interpret these parameters. It is expected
that most rendering backends will consume the parameter values
directly rather than call this method.

The base emission is only one step in the process of sampling light
radiance. It does not incorporate effects from:

   - textural/procedural modifications

   - normalization by area

   - specular/diffuse multipliers


"""
   result["Light"].CreateColorAttr.im_func.func_doc = """CreateColorAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetColorAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Light"].GetExposureAttr.im_func.func_doc = """GetExposureAttr() -> USDLUX_API UsdAttribute



Scales the power of the light exponentially as a power of 2 (similar
to an F-stop control over exposure).


The result is multiplied against the intensity.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["Light"].GetSpecularAttr.im_func.func_doc = """GetSpecularAttr() -> USDLUX_API UsdAttribute



A multiplier for the effect of this light on the specular response of
materials.


This is a non-physical control.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["Light"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Light"].CreateSpecularAttr.im_func.func_doc = """CreateSpecularAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSpecularAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Light"].GetShadowLinkCollectionAPI.im_func.func_doc = """GetShadowLinkCollectionAPI() -> USDLUX_API UsdCollectionAPI



Return the UsdCollectionAPI interface used for examining and modifying
the shadow-linking of this light.


Shadow-linking controls which geometry casts shadows from this light.

"""
   result["Light"].GetEnableColorTemperatureAttr.im_func.func_doc = """GetEnableColorTemperatureAttr() -> USDLUX_API UsdAttribute



Enables using colorTemperature.


C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["Light"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxLight on UsdPrim C{prim}.


Equivalent to UsdLuxLight::Get (prim.GetStage(), prim.GetPath()) for a
*valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxLight on the prim held by C{schemaObj}.


Should be preferred over UsdLuxLight (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Light"].CreateColorTemperatureAttr.im_func.func_doc = """CreateColorTemperatureAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetColorTemperatureAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Light"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["__doc__"] = """

Overview
========

UsdLux provides a representation for lights and related components
that are common to many graphics environments and therefore suitable
for interchange.

The goal of UsdLux is to serve as a basis for:

   - passing lighting setups from a creation environment to a renderer

   - best-effort portability of setups across environments, to the
     degree that they share capabilities

The UsdLux core includes:

   - common light types
   - UsdLuxDiskLight

   - UsdLuxDistantLight

   - UsdLuxDomeLight

   - UsdLuxGeometryLight

   - UsdLuxRectLight

   - UsdLuxSphereLight

   - common light attributes
   - *power*: intensity and exposure

   - *color*: as RGB components and/or color temperature

   - API classes embodying more complex behaviors
   - UsdLuxListAPI : light component enumeration and discovery

   - UsdCollectionAPI : light-object linking

   - UsdLuxShadowAPI : shadow-linking and falloff

   - UsdLuxShapingAPI : focus, cone angle, and IES profiles

   - associated components for adjusting behavior
   - UsdLuxLightFilter : a filter to modulate the effect of lights

   - UsdLuxLightPortal : a portal to guide sampling of a dome light

This core can be extended to add more types of lights, filters, or
other features.

For a comprehensive list of the types see the full class hierarchy.

Design Notes and Usage Guide
============================

By convention, lights with a primary axis emit along -Z. Area lights
are centered in the XY plane and are 1 unit in diameter.

UsdLux objects are UsdGeomXformable, so they use its set of transform
operators, and inherit transforms hierarchically. It is recommended
that only translation and rotations be used with lights, to avoid
introducing difficulties for light sampling and integration. Lights
have explicit attributes to adjust their size.

UsdLux includes both a light that uses arbitrary user-supplied
geometry, as well as lights for specific shapes: spheres, rectangles,
disks, and cylinders. The specific shapes exist because they can
support superior, analytic sampling methods.

UsdLux is designed primarily for physically-based cinematic lighting
with area lights. Accordingly, it does not include zero-area point or
line lights. However, some backends benefit from a point or line
approximation. This intent can be indicated using the treatAsPoint and
treatAsLine attributes on UsdSphereLight and UsdCylinderLight. These
attributes are hints that avoid the need for backends to use
heuristics (such as an arbitrary epsilon threshold) to determine the
approximation. These hints can be set at the time of creation (or
export) where the most information about the visual intent exists.

To support efficient sampling, these specialized types place
restrictions on their local-to-world transform. For example, a sphere
may only be scaled uniformly. Because arbitrary transforms may be
inherited from parent prims, it is necessary to explicitly compute the
"effective" transform for such lights using
UsdLuxLight::ComputeEffectiveTransform().

To clarify geometric semantics and aid pipeline integration, UsdLux
includes code to compute guide geometry for interactive viewport
visualization. This code is used in usdview.

UsdLux does not provide support for expressing live transform
constraints, such as to attach lights to moving geometry. This is
consistent with USD's policy of storing the computed result of
rigging, not the rigging itself.

Colors specified in attributes are in energy-linear terms, and obey
the USD convention for indicating their color space via
C{colorConfiguration} and C{colorSpace} metadata. See
UsdStage::SetColorConfiguration() for discussion of colorspace
management in USD.

UsdLux presumes a physically-based lighting model where falloff with
distance is a consequence of reduced visible solid angle. Environments
that do not measure the visible solid angle are expected to provide an
approximation, such as inverse-square falloff. Further artistic
control over attenuation can be modelled as light filters.

More complex behaviors are provided via a set of API classes. These
behaviors are common and well-defined but may not be supported in all
rendering environments. These API classes provide functions to specify
the relevant semantic behavior:

   - UsdLuxListAPI provides a "light list" relationship to enumerate
     locations of known lights in the scene. It can be useful to enumerate
     lights without requiring full scene traversal. For example, some
     systems require lights to be declared before the rest of the scene.
     UsdLuxListAPI provides a way to compute this result ahead of time and
     store the result in a well-defined place. Pipeline integration of
     UsdLux can use this API to discover and publish lights at an
     appropriate time  such as export from any system where lights may be
     created.

   - UsdCollectionAPI provides relationships to represent subsets of
     geometry to consider for illumination. These provide hierarchical
     inclusion and exclusion  for example, to illuminate a building but not
     a window within. UsdLux supports a concept of fractional illumination,
     allowing partial contribution from a light to a particular object, for
     rendering systems that support this.

   - UsdLuxShadowAPI provides controls to refine shadow behavior in
     non-physical ways, including shadow linking, tinting, and falloff.

   - UsdLuxShapingAPI provides controls to shape light emission,
     including focus, cone-angle falloff, and IES profiles.

Like other USD schemas, UsdLux core may be extended to address
features specific to certain environments. Possible renderer- or
pipeline-specific capabilities that could be addded as extensions
include:

   - specialized light types
   - point cloud lights

   - volumetric/voxel lights

   - procedural sky models

   - light probes, lightfields

   - renderer-specific configuration
   - arbitrary output variable images (AOV's) such as depth or normals

   - light path expressions (LPE's)

   - image post-processing effects

   - refraction and opacity approximations, such as thin shadows

   - sampling and optimization tweaks
   - light sample counts

   - importance multipliers

   - integrator path-depth limits

   - constraint rigging to attach a light to an object


"""
   result["LightPortal"].__doc__ = """
A rectangular portal in the local XY plane that guides sampling of a
dome light.


Transmits light in the -Z direction. The rectangle is 1 unit in
length.

"""
   result["LightPortal"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxLightPortal

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxLightPortal holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxLightPortal(stage->GetPrimAtPath(path));


"""
   result["LightPortal"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxLightPortal on UsdPrim C{prim}.


Equivalent to UsdLuxLightPortal::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxLightPortal on the prim held by C{schemaObj}.


Should be preferred over UsdLuxLightPortal (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["LightPortal"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["LightPortal"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["LightPortal"].Define.func_doc = """**static** Define(stage, path) -> USDLUX_API UsdLuxLightPortal

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
   result["DistantLight"].__doc__ = """
Light emitted from a distant source along the -Z axis.


Also known as a directional light.

"""
   result["DistantLight"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxDistantLight

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxDistantLight holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxDistantLight(stage->GetPrimAtPath(path));


"""
   result["DistantLight"].GetAngleAttr.im_func.func_doc = """GetAngleAttr() -> USDLUX_API UsdAttribute



Angular size of the light in degrees.


As an example, the Sun is approximately 0.53 degrees as seen from
Earth. Higher values broaden the light and therefore soften shadow
edges.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.52999997139

"""
   result["DistantLight"].GetIntensityAttr.im_func.func_doc = """GetIntensityAttr() -> USDLUX_API UsdAttribute



Scales the emission of the light linearly.


The DistantLight has a high default intensity to approximate the Sun.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 50000.0

"""
   result["DistantLight"].CreateIntensityAttr.im_func.func_doc = """CreateIntensityAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetIntensityAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["DistantLight"].CreateAngleAttr.im_func.func_doc = """CreateAngleAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAngleAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["DistantLight"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["DistantLight"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxDistantLight on UsdPrim C{prim}.


Equivalent to UsdLuxDistantLight::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxDistantLight on the prim held by C{schemaObj}.


Should be preferred over UsdLuxDistantLight (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["DistantLight"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["DistantLight"].Define.func_doc = """**static** Define(stage, path) -> USDLUX_API UsdLuxDistantLight

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
   result["ListAPI"].__doc__ = """
API schema to support discovery and publishing of lights in a scene.


Discovering Lights via Traversal
================================

To motivate this API, consider what is required to discover all lights
in a scene. We must load all payloads and traverse all prims: ::

  01  // Load everything on the stage so we can find all lights,
  02  // including those inside payloads
  03  stage->Load();
  04  
  05  // Traverse all prims, checking if they are of type UsdLuxLight
  06  // (Note: ignoring instancing and a few other things for simplicity)
  07  SdfPathVector lights;
  08  for (UsdPrim prim: stage->Traverse()) {
  09      if (prim.IsA<UsdLuxLight>()) {
  10          lights.push_back(i->GetPath());
  11      }
  12  }

This traversal  suitably elaborated to handle certain details  is the
first and simplest thing UsdLuxListAPI provides.
UsdLuxListAPI::ComputeLightList() performs this traversal and returns
all lights in the scene: ::

  01  UsdLuxListAPI listAPI(stage->GetPseudoRoot());
  02  SdfPathVector lights = listAPI.ComputeLightList();

Publishing a Cached Light List
==============================

Consider a USD client that needs to quickly discover lights but wants
to defer loading payloads and traversing the entire scene where
possible, and is willing to do up-front computation and caching to
achieve that.

UsdLuxListAPI provides a way to cache the computed light list, by
publishing the list of lights onto prims in the model hierarchy.
Consider a big set that contains lights: ::

  01  def Xform "BigSetWithLights" (
  02      kind = "assembly"
  03      payload = @BigSetWithLights.usd@   // Heavy payload
  04  ) {
  05      
// Pre-
computed, cached list of lights inside payload
  06      rel lightList = [
  07          <./Lights/light_1>,
  08          <./Lights/light_2>,
  09          ...
  10      ]
  11      token lightList:cacheBehavior = "consumeAndContinue";
  12  }

The lightList relationship encodes a set of lights, and the
lightList:cacheBehavior property provides fine-grained control over
how to use that cache. (See details below.)

The cache can be created by first invoking
ComputeLightList(ComputeModeIgnoreCache) to pre-compute the list and
then storing the result with UsdLuxListAPI::StoreLightList() .

To enable efficient retrieval of the cache, it should be stored on a
model hierarchy prim. Furthermore, note that while you can use a
UsdLuxListAPI bound to the pseudo-root prim to query the lights (as in
the example above) because it will perform a traversal over
descendants, you cannot store the cache back to the pseduo-root prim.

To consult the cached list, we invoke
ComputeLightList(ComputeModeConsultModelHierarchyCache): ::

  01  // Find and load all lights, using lightList cache where available
  02  UsdLuxListAPI list(stage->GetPseudoRoot());
  03  SdfPathSet lights = list.ComputeLightList(
  04      UsdLuxListAPI::ComputeModeConsultModelHierarchyCache);
  05  stage.LoadAndUnload(lights, SdfPathSet());

In this mode, ComputeLightList() will traverse the model hierarchy,
accumulating cached light lists.

Controlling Cache Behavior
==========================

The lightList:cacheBehavior property gives additional fine-grained
control over cache behavior:

   - The fallback value, "ignore", indicates that the lightList should
     be disregarded. This provides a way to invalidate cache entries. Note
     that unless "ignore" is specified, a lightList with an empty list of
     targets is considered a cache indicating that no lights are present.

   - The value "consumeAndContinue" indicates that the cache should be
     consulted to contribute lights to the scene, and that recursion should
     continue down the model hierarchy in case additional lights are added
     as descedants. This is the default value established when
     StoreLightList() is invoked. This behavior allows the lights within a
     large model, such as the BigSetWithLights example above, to be
     published outside the payload, while also allowing referencing and
     layering to add additional lights over that set.

   - The value "consumeAndHalt" provides a way to terminate recursive
     traversal of the scene for light discovery. The cache will be
     consulted but no descendant prims will be examined.

Instancing
==========

Where instances are present, UsdLuxListAPI::ComputeLightList() will
return the instance-unique paths to any lights discovered within those
instances. Lights within a UsdGeomPointInstancer will not be returned,
however, since they cannot be referred to solely via paths.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdLuxTokens. So to set an attribute to the value "rightHanded",
use UsdLuxTokens->rightHanded as the value.

"""
   result["ListAPI"].GetLightListCacheBehaviorAttr.im_func.func_doc = """GetLightListCacheBehaviorAttr() -> USDLUX_API UsdAttribute



Controls how the lightList should be interpreted.


Valid values are:
   - consumeAndHalt: The lightList should be consulted, and if it
     exists, treated as a final authoritative statement of any lights that
     exist at or below this prim, halting recursive discovery of lights.

   - consumeAndContinue: The lightList should be consulted, but
     recursive traversal over nameChildren should continue in case
     additional lights are added by descendants.

   - ignore: The lightList should be entirely ignored. This provides a
     simple way to temporarily invalidate an existing cache. This is the
     fallback behavior.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback  Allowed Values :
[consumeAndHalt, consumeAndContinue, ignore]

"""
   result["ListAPI"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxListAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxListAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxListAPI(stage->GetPrimAtPath(path));


"""
   result["ListAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxListAPI on UsdPrim C{prim}.


Equivalent to UsdLuxListAPI::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxListAPI on the prim held by C{schemaObj}.


Should be preferred over UsdLuxListAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["ListAPI"].ComputeMode.__doc__ = """
Runtime control over whether to consult stored lightList caches.

"""
   result["ListAPI"].CreateLightListRel.im_func.func_doc = """CreateLightListRel() -> USDLUX_API UsdRelationship



See GetLightListRel() , and also Create vs Get Property Methods for
when to use Get vs Create.

"""
   result["ListAPI"].InvalidateLightList.im_func.func_doc = """InvalidateLightList() -> USDLUX_API void



Mark any stored lightlist as invalid, by setting the
lightList:cacheBehavior attribute to ignore.

"""
   result["ListAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["ListAPI"].GetLightListRel.im_func.func_doc = """GetLightListRel() -> USDLUX_API UsdRelationship



Relationship to lights in the scene.

"""
   result["ListAPI"].CreateLightListCacheBehaviorAttr.im_func.func_doc = """CreateLightListCacheBehaviorAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetLightListCacheBehaviorAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ListAPI"].Apply.func_doc = """**static** Apply(prim) -> USDLUX_API UsdLuxListAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "ListAPI" to the token-valued,
listOp metadata *apiSchemas* on the prim.

A valid UsdLuxListAPI object is returned upon success. An invalid (or
empty) UsdLuxListAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["ListAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["ListAPI"].ComputeLightList.im_func.func_doc = """ComputeLightList(mode) -> USDLUX_API SdfPathSet

mode : ComputeMode


Computes and returns the list of lights and light filters in the
stage, optionally consulting a cached result.


In ComputeModeIgnoreCache mode, caching is ignored, and this does a
prim traversal looking for prims of type UsdLuxLight or
UsdLuxLightFilter.

In ComputeModeConsultModelHierarchyCache, this does a traversal only
of the model hierarchy. In this traversal, any lights that live as
model hierarchy prims are accumulated, as well as any paths stored in
lightList caches. The lightList:cacheBehavior attribute gives further
control over the cache behavior; see the class overview for details.

When instances are present, ComputeLightList(ComputeModeIgnoreCache)
will return the instance-uniqiue paths to any lights discovered within
those instances. Lights within a UsdGeomPointInstancer will not be
returned, however, since they cannot be referred to solely via paths.

"""
   result["ListAPI"].StoreLightList.im_func.func_doc = """StoreLightList(arg1) -> USDLUX_API void

arg1 : SdfPathSet


Store the given paths as the lightlist for this prim.


Paths that do not have this prim's path as a prefix will be silently
ignored. This will set the listList:cacheBehavior to
"consumeAndContinue".

"""
   result["CylinderLight"].__doc__ = """
Light emitted outward from a cylinder.


The cylinder is centered at the origin and has its major axis on the X
axis. The cylinder does not emit light from the flat end-caps.

"""
   result["CylinderLight"].CreateTreatAsLineAttr.im_func.func_doc = """CreateTreatAsLineAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTreatAsLineAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["CylinderLight"].CreateRadiusAttr.im_func.func_doc = """CreateRadiusAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRadiusAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["CylinderLight"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxCylinderLight on UsdPrim C{prim}.


Equivalent to UsdLuxCylinderLight::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxCylinderLight on the prim held by C{schemaObj}.


Should be preferred over UsdLuxCylinderLight (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["CylinderLight"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxCylinderLight

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxCylinderLight holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxCylinderLight(stage->GetPrimAtPath(path));


"""
   result["CylinderLight"].CreateLengthAttr.im_func.func_doc = """CreateLengthAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetLengthAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["CylinderLight"].GetLengthAttr.im_func.func_doc = """GetLengthAttr() -> USDLUX_API UsdAttribute



Width of the rectangle, in the local X axis.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["CylinderLight"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["CylinderLight"].GetRadiusAttr.im_func.func_doc = """GetRadiusAttr() -> USDLUX_API UsdAttribute



Radius of the cylinder.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.5

"""
   result["CylinderLight"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["CylinderLight"].GetTreatAsLineAttr.im_func.func_doc = """GetTreatAsLineAttr() -> USDLUX_API UsdAttribute



A hint that this light can be treated as a 'line' light (effectively,
a zero-radius cylinder) by renderers that benefit from non-area
lighting.


Renderers that only support area lights can disregard this.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["CylinderLight"].Define.func_doc = """**static** Define(stage, path) -> USDLUX_API UsdLuxCylinderLight

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
   result["DomeLight"].__doc__ = """
Light emitted inward from a distant external environment, such as a
sky or IBL light probe.


For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdLuxTokens. So to set an attribute to the value "rightHanded",
use UsdLuxTokens->rightHanded as the value.

"""
   result["DomeLight"].GetTextureFileAttr.im_func.func_doc = """GetTextureFileAttr() -> USDLUX_API UsdAttribute



A color texture to use on the dome, such as an HDR (high dynamic
range) texture intended for IBL (image based lighting).


C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["DomeLight"].GetTextureFormatAttr.im_func.func_doc = """GetTextureFormatAttr() -> USDLUX_API UsdAttribute



Specifies the parameterization of the color map file.


Valid values are:
   - automatic: Tries to determine the layout from the file itself.
     For example, Renderman texture files embed an explicit
     parameterization.

   - latlong: Latitude as X, longitude as Y.

   - mirroredBall: An image of the environment reflected in a sphere,
     using an implicitly orthogonal projection.

   - angular: Similar to mirroredBall but the radial dimension is
     mapped linearly to the angle, providing better sampling at the edges.

   - cubeMapVerticalCross: A cube map with faces laid out as a
     vertical cross.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: automatic  Allowed Values :
[automatic, latlong, mirroredBall, angular, cubeMapVerticalCross]

"""
   result["DomeLight"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxDomeLight

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxDomeLight holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxDomeLight(stage->GetPrimAtPath(path));


"""
   result["DomeLight"].GetPortalsRel.im_func.func_doc = """GetPortalsRel() -> USDLUX_API UsdRelationship



Optional portals to guide light sampling.

"""
   result["DomeLight"].CreateTextureFormatAttr.im_func.func_doc = """CreateTextureFormatAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureFormatAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["DomeLight"].CreateTextureFileAttr.im_func.func_doc = """CreateTextureFileAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureFileAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["DomeLight"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxDomeLight on UsdPrim C{prim}.


Equivalent to UsdLuxDomeLight::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxDomeLight on the prim held by C{schemaObj}.


Should be preferred over UsdLuxDomeLight (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["DomeLight"].CreatePortalsRel.im_func.func_doc = """CreatePortalsRel() -> USDLUX_API UsdRelationship



See GetPortalsRel() , and also Create vs Get Property Methods for when
to use Get vs Create.

"""
   result["DomeLight"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["DomeLight"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["DomeLight"].Define.func_doc = """**static** Define(stage, path) -> USDLUX_API UsdLuxDomeLight

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
   result["BlackbodyTemperatureAsRgb"].func_doc = """BlackbodyTemperatureAsRgb(colorTemp) -> USDLUX_API GfVec3f

colorTemp : float


Compute the RGB equivalent of the spectrum emitted by a blackbody with
the given temperature in degrees Kelvin, with normalized luminance.

"""
   result["DiskLight"].__doc__ = """
Light emitted from one side of a circular disk.


The disk is centered in the XY plane and emits light along the -Z
axis.

"""
   result["DiskLight"].CreateRadiusAttr.im_func.func_doc = """CreateRadiusAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRadiusAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["DiskLight"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxDiskLight

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxDiskLight holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxDiskLight(stage->GetPrimAtPath(path));


"""
   result["DiskLight"].GetRadiusAttr.im_func.func_doc = """GetRadiusAttr() -> USDLUX_API UsdAttribute



Radius of the disk.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.5

"""
   result["DiskLight"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["DiskLight"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxDiskLight on UsdPrim C{prim}.


Equivalent to UsdLuxDiskLight::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxDiskLight on the prim held by C{schemaObj}.


Should be preferred over UsdLuxDiskLight (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["DiskLight"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["DiskLight"].Define.func_doc = """**static** Define(stage, path) -> USDLUX_API UsdLuxDiskLight

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
   result["SphereLight"].__doc__ = """
Light emitted outward from a sphere.

"""
   result["SphereLight"].CreateRadiusAttr.im_func.func_doc = """CreateRadiusAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRadiusAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["SphereLight"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxSphereLight

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxSphereLight holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxSphereLight(stage->GetPrimAtPath(path));


"""
   result["SphereLight"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxSphereLight on UsdPrim C{prim}.


Equivalent to UsdLuxSphereLight::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxSphereLight on the prim held by C{schemaObj}.


Should be preferred over UsdLuxSphereLight (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["SphereLight"].CreateTreatAsPointAttr.im_func.func_doc = """CreateTreatAsPointAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTreatAsPointAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["SphereLight"].GetRadiusAttr.im_func.func_doc = """GetRadiusAttr() -> USDLUX_API UsdAttribute



Radius of the sphere.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.5

"""
   result["SphereLight"].GetTreatAsPointAttr.im_func.func_doc = """GetTreatAsPointAttr() -> USDLUX_API UsdAttribute



A hint that this light can be treated as a 'point' light (effectively,
a zero-radius sphere) by renderers that benefit from non-area
lighting.


Renderers that only support area lights can disregard this.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["SphereLight"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["SphereLight"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["SphereLight"].Define.func_doc = """**static** Define(stage, path) -> USDLUX_API UsdLuxSphereLight

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
   result["RectLight"].__doc__ = """
Light emitted from one side of a rectangle.


The rectangle is centered in the XY plane and emits light along the -Z
axis. The rectangle is 1 unit in length in the X and Y axis.

"""
   result["RectLight"].CreateHeightAttr.im_func.func_doc = """CreateHeightAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHeightAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RectLight"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxRectLight

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxRectLight holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxRectLight(stage->GetPrimAtPath(path));


"""
   result["RectLight"].GetTextureFileAttr.im_func.func_doc = """GetTextureFileAttr() -> USDLUX_API UsdAttribute



A color texture to use on the rectangle.


C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["RectLight"].CreateTextureFileAttr.im_func.func_doc = """CreateTextureFileAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureFileAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RectLight"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxRectLight on UsdPrim C{prim}.


Equivalent to UsdLuxRectLight::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxRectLight on the prim held by C{schemaObj}.


Should be preferred over UsdLuxRectLight (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["RectLight"].GetWidthAttr.im_func.func_doc = """GetWidthAttr() -> USDLUX_API UsdAttribute



Width of the rectangle, in the local X axis.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["RectLight"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["RectLight"].Define.func_doc = """**static** Define(stage, path) -> USDLUX_API UsdLuxRectLight

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
   result["RectLight"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["RectLight"].CreateWidthAttr.im_func.func_doc = """CreateWidthAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetWidthAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RectLight"].GetHeightAttr.im_func.func_doc = """GetHeightAttr() -> USDLUX_API UsdAttribute



Height of the rectangle, in the local Y axis.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["GeometryLight"].__doc__ = """
Light emitted outward from a geometric prim (UsdGeomGprim), which is
typically a mesh.

"""
   result["GeometryLight"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxGeometryLight

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxGeometryLight holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxGeometryLight(stage->GetPrimAtPath(path));


"""
   result["GeometryLight"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxGeometryLight on UsdPrim C{prim}.


Equivalent to UsdLuxGeometryLight::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxGeometryLight on the prim held by C{schemaObj}.


Should be preferred over UsdLuxGeometryLight (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["GeometryLight"].CreateGeometryRel.im_func.func_doc = """CreateGeometryRel() -> USDLUX_API UsdRelationship



See GetGeometryRel() , and also Create vs Get Property Methods for
when to use Get vs Create.

"""
   result["GeometryLight"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["GeometryLight"].Define.func_doc = """**static** Define(stage, path) -> USDLUX_API UsdLuxGeometryLight

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
   result["GeometryLight"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["GeometryLight"].GetGeometryRel.im_func.func_doc = """GetGeometryRel() -> USDLUX_API UsdRelationship



Relationship to the geometry to use as the light source.

"""
   result["LightFilter"].__doc__ = """
A light filter modifies the effect of a light.


Lights refer to filters via relationships so that filters may be
shared.

B{Linking}

Filters can be linked to geometry. Linking controls which geometry a
light-filter affects, when considering the light filters attached to a
light illuminating the geometry.

Linking is specified as a collection (UsdCollectionAPI) which can be
accessed via GetFilterLinkCollection(). Note however that there are
extra semantics in how UsdLuxLightFilter uses its collection: if a
collection is empty, the filter is treated as linked to *all* geometry
for the respective purpose. UsdCollectionAPI and
UsdCollectionAPI::MembershipQuery are unaware of this filter-specific
interpretation.

"""
   result["LightFilter"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxLightFilter on UsdPrim C{prim}.


Equivalent to UsdLuxLightFilter::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxLightFilter on the prim held by C{schemaObj}.


Should be preferred over UsdLuxLightFilter (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["LightFilter"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxLightFilter

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxLightFilter holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxLightFilter(stage->GetPrimAtPath(path));


"""
   result["LightFilter"].GetFilterLinkCollectionAPI.im_func.func_doc = """GetFilterLinkCollectionAPI() -> USDLUX_API UsdCollectionAPI



Return the UsdCollectionAPI interface used for examining and modifying
the filter-linking of this light filter.


Linking controls which geometry this light filter affects.

"""
   result["LightFilter"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["LightFilter"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["LightFilter"].Define.func_doc = """**static** Define(stage, path) -> USDLUX_API UsdLuxLightFilter

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
   result["ShapingAPI"].__doc__ = """
Controls for shaping a light's emission.

"""
   result["ShapingAPI"].GetShapingIesAngleScaleAttr.im_func.func_doc = """GetShapingIesAngleScaleAttr() -> USDLUX_API UsdAttribute



Rescales the angular distribution of the IES profile.


TODO: clarify semantics

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["ShapingAPI"].GetShapingConeAngleAttr.im_func.func_doc = """GetShapingConeAngleAttr() -> USDLUX_API UsdAttribute



Angular limit off the primary axis to restrict the light spread.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 90.0

"""
   result["ShapingAPI"].Apply.func_doc = """**static** Apply(prim) -> USDLUX_API UsdLuxShapingAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "ShapingAPI" to the token-valued,
listOp metadata *apiSchemas* on the prim.

A valid UsdLuxShapingAPI object is returned upon success. An invalid
(or empty) UsdLuxShapingAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["ShapingAPI"].GetShapingFocusAttr.im_func.func_doc = """GetShapingFocusAttr() -> USDLUX_API UsdAttribute



A control to shape the spread of light.


Higher focus values pull light towards the center and narrow the
spread. Implemented as an off-axis cosine power exponent. TODO:
clarify semantics

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["ShapingAPI"].GetShapingConeSoftnessAttr.im_func.func_doc = """GetShapingConeSoftnessAttr() -> USDLUX_API UsdAttribute



Controls the cutoff softness for cone angle.


TODO: clarify semantics

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["ShapingAPI"].CreateShapingFocusTintAttr.im_func.func_doc = """CreateShapingFocusTintAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShapingFocusTintAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShapingAPI"].Get.func_doc = """**static** Get(stage, path) -> USDLUX_API UsdLuxShapingAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdLuxShapingAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdLuxShapingAPI(stage->GetPrimAtPath(path));


"""
   result["ShapingAPI"].CreateShapingFocusAttr.im_func.func_doc = """CreateShapingFocusAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShapingFocusAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShapingAPI"].CreateShapingConeAngleAttr.im_func.func_doc = """CreateShapingConeAngleAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShapingConeAngleAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShapingAPI"].CreateShapingIesFileAttr.im_func.func_doc = """CreateShapingIesFileAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShapingIesFileAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShapingAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdLuxShapingAPI on UsdPrim C{prim}.


Equivalent to UsdLuxShapingAPI::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdLuxShapingAPI on the prim held by C{schemaObj}.


Should be preferred over UsdLuxShapingAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["ShapingAPI"].CreateShapingIesAngleScaleAttr.im_func.func_doc = """CreateShapingIesAngleScaleAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShapingIesAngleScaleAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShapingAPI"].GetShapingFocusTintAttr.im_func.func_doc = """GetShapingFocusTintAttr() -> USDLUX_API UsdAttribute



Off-axis color tint.


This tints the emission in the falloff region. The default tint is
black. TODO: clarify semantics

C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Color3f  Variability:
SdfVariabilityVarying  Fallback Value: (0, 0, 0)

"""
   result["ShapingAPI"].GetShapingIesFileAttr.im_func.func_doc = """GetShapingIesFileAttr() -> USDLUX_API UsdAttribute



An IES (Illumination Engineering Society) light profile describing the
angular distribution of light.


C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["ShapingAPI"].CreateShapingConeSoftnessAttr.im_func.func_doc = """CreateShapingConeSoftnessAttr(defaultValue, writeSparsely) -> USDLUX_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetShapingConeSoftnessAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ShapingAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDLUX_API  TfType


"""
   result["ShapingAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDLUX_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""