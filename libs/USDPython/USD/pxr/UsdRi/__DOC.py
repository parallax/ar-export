def Execute(result):
   result["TextureAPI"].__doc__ = """
RiTextureAPI is an API schema that provides an interface to add
Renderman-specific attributes to adjust textures.

"""
   result["TextureAPI"].GetRiTextureGammaAttr.im_func.func_doc = """GetRiTextureGammaAttr() -> USDRI_API UsdAttribute



Gamma-correct the texture.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["TextureAPI"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiTextureAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdRiTextureAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiTextureAPI(stage->GetPrimAtPath(path));


"""
   result["TextureAPI"].CreateRiTextureGammaAttr.im_func.func_doc = """CreateRiTextureGammaAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiTextureGammaAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["TextureAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiTextureAPI on UsdPrim C{prim}.


Equivalent to UsdRiTextureAPI::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiTextureAPI on the prim held by C{schemaObj}.


Should be preferred over UsdRiTextureAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["TextureAPI"].CreateRiTextureSaturationAttr.im_func.func_doc = """CreateRiTextureSaturationAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiTextureSaturationAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["TextureAPI"].Apply.func_doc = """**static** Apply(prim) -> USDRI_API UsdRiTextureAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "RiTextureAPI" to the token-
valued, listOp metadata *apiSchemas* on the prim.

A valid UsdRiTextureAPI object is returned upon success. An invalid
(or empty) UsdRiTextureAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["TextureAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["TextureAPI"].GetRiTextureSaturationAttr.im_func.func_doc = """GetRiTextureSaturationAttr() -> USDRI_API UsdAttribute



Adjust the texture's saturation.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["TextureAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["RisObject"].__doc__ = """
Deprecated

Specialized RIS shader schemas have been deprecated in favor of all
shader prims being simple UsdShadeShader. Represents a ris object with
connectable parameters.

"""
   result["RisObject"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiRisObject

stage : UsdStagePtr
path : SdfPath


Return a UsdRiRisObject holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiRisObject(stage->GetPrimAtPath(path));


"""
   result["RisObject"].CreateArgsPathAttr.im_func.func_doc = """CreateArgsPathAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetArgsPathAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RisObject"].GetArgsPathAttr.im_func.func_doc = """GetArgsPathAttr() -> USDRI_API UsdAttribute



C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["RisObject"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["RisObject"].CreateFilePathAttr.im_func.func_doc = """CreateFilePathAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFilePathAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RisObject"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiRisObject on UsdPrim C{prim}.


Equivalent to UsdRiRisObject::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiRisObject on the prim held by C{schemaObj}.


Should be preferred over UsdRiRisObject (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["RisObject"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["RisObject"].GetFilePathAttr.im_func.func_doc = """GetFilePathAttr() -> USDRI_API UsdAttribute



C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["RisObject"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiRisObject

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
   result["LightAPI"].__doc__ = """
RiLightAPI is an API schema that provides an interface to add
Renderman-specific attributes to lights.

"""
   result["LightAPI"].GetRiLightGroupAttr.im_func.func_doc = """GetRiLightGroupAttr() -> USDRI_API UsdAttribute



Specify the light group name used for light group LPEs.


This is useful to generate per-light AOVs for later adjustment in
compositing.

C++ Type: std::string  Usd Type: SdfValueTypeNames->String
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightAPI"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiLightAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdRiLightAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiLightAPI(stage->GetPrimAtPath(path));


"""
   result["LightAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiLightAPI on UsdPrim C{prim}.


Equivalent to UsdRiLightAPI::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiLightAPI on the prim held by C{schemaObj}.


Should be preferred over UsdRiLightAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["LightAPI"].GetRiTraceLightPathsAttr.im_func.func_doc = """GetRiTraceLightPathsAttr() -> USDRI_API UsdAttribute



Enable light and photon tracing from this light.


This value enforces a physically-based light and as a side-effect
disables the above Shadows controls. Users may use this feature to
selectively decide which lights emit photons when using the PxrVCM or
PxrUPBP Integrators.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightAPI"].GetRiIntensityNearDistAttr.im_func.func_doc = """GetRiIntensityNearDistAttr() -> USDRI_API UsdAttribute



Near distance between the point being illuminated and the light at
which the sample doesn't get brighter.


This may help you avoid hot spots and sampling issues where a light is
near a surface.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightAPI"].CreateRiSamplingFixedSampleCountAttr.im_func.func_doc = """CreateRiSamplingFixedSampleCountAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiSamplingFixedSampleCountAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightAPI"].CreateRiShadowThinShadowAttr.im_func.func_doc = """CreateRiShadowThinShadowAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiShadowThinShadowAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightAPI"].GetRiShadowThinShadowAttr.im_func.func_doc = """GetRiShadowThinShadowAttr() -> USDRI_API UsdAttribute



Enable thin shadow and disable refraction caustics for this light.


This parameter will ignored if Trace Light Paths is enabled. This is a
non-physical control that creates "fake" colored shadows for
transmissive objects without needing to generate photons for caustics.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightAPI"].GetRiSamplingImportanceMultiplierAttr.im_func.func_doc = """GetRiSamplingImportanceMultiplierAttr() -> USDRI_API UsdAttribute



Importance of this light for noise control.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["LightAPI"].GetRiSamplingFixedSampleCountAttr.im_func.func_doc = """GetRiSamplingFixedSampleCountAttr() -> USDRI_API UsdAttribute



Specifies an override of the number of light samples to be taken for
this light source.


If set to something other than zero, it will override the sampling
performed by the integrator and can result in a performance impact.
For scenes that have lots of lights, resulting in some lights that are
under-sampled, you may want to set it to non-zero.

C++ Type: int  Usd Type: SdfValueTypeNames->Int  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightAPI"].CreateRiSamplingImportanceMultiplierAttr.im_func.func_doc = """CreateRiSamplingImportanceMultiplierAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiSamplingImportanceMultiplierAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightAPI"].CreateRiTraceLightPathsAttr.im_func.func_doc = """CreateRiTraceLightPathsAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiTraceLightPathsAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightAPI"].Apply.func_doc = """**static** Apply(prim) -> USDRI_API UsdRiLightAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "RiLightAPI" to the token-valued,
listOp metadata *apiSchemas* on the prim.

A valid UsdRiLightAPI object is returned upon success. An invalid (or
empty) UsdRiLightAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["LightAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["LightAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["LightAPI"].CreateRiIntensityNearDistAttr.im_func.func_doc = """CreateRiIntensityNearDistAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiIntensityNearDistAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightAPI"].CreateRiLightGroupAttr.im_func.func_doc = """CreateRiLightGroupAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiLightGroupAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["ConvertToRManFaceVaryingLinearInterpolation"].func_doc = """ConvertToRManFaceVaryingLinearInterpolation(token) -> USDRI_API int

token : TfToken


Given a C{token} representing a UsdGeom face-varying interpolate
boundary value, returns corresponding rman enum (converted to int).

"""
   result["ConvertFromRManFaceVaryingLinearInterpolation"].func_doc = """ConvertFromRManFaceVaryingLinearInterpolation(i) -> USDRI_API  TfToken

i : int


Given the integer C{i} that corresponds to an rman enum for face-
varying interpolate boundary condition, returns the equivalent UsdGeom
token.

"""
   result["MaterialAPI"].__doc__ = """
This API provides outputs that connect a material prim to prman
shaders and RIS objects.


For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdRiTokens. So to set an attribute to the value "rightHanded", use
UsdRiTokens->rightHanded as the value.

"""
   result["MaterialAPI"].GetDisplacementOutput.im_func.func_doc = """GetDisplacementOutput() -> USDRI_API UsdShadeOutput



Returns the "displacement" output associated with the material.

"""
   result["MaterialAPI"].GetInterfaceInputs.im_func.func_doc = """GetInterfaceInputs() -> USDRI_API sequence< UsdShadeInput >



Returns all the interface inputs belonging to the material.

"""
   result["MaterialAPI"].SetSurfaceSource.im_func.func_doc = """SetSurfaceSource(surfacePath) -> USDRI_API bool

surfacePath : SdfPath

"""
   result["MaterialAPI"].SetVolumeSource.im_func.func_doc = """SetVolumeSource(volumePath) -> USDRI_API bool

volumePath : SdfPath

"""
   result["MaterialAPI"].CreateDisplacementAttr.im_func.func_doc = """CreateDisplacementAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDisplacementAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["MaterialAPI"].GetVolume.im_func.func_doc = """GetVolume(ignoreBaseMaterial) -> USDRI_API UsdShadeShader

ignoreBaseMaterial : bool


Returns a valid shader object if the "volume" output on the material
is connected to one.


If C{ignoreBaseMaterial} is true and if the "volume" shader source is
specified in the base-material of this material, then this returns an
invalid shader object.

"""
   result["MaterialAPI"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiMaterialAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdRiMaterialAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiMaterialAPI(stage->GetPrimAtPath(path));


"""
   result["MaterialAPI"].GetSurfaceAttr.im_func.func_doc = """GetSurfaceAttr() -> USDRI_API UsdAttribute



C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["MaterialAPI"].GetVolumeAttr.im_func.func_doc = """GetVolumeAttr() -> USDRI_API UsdAttribute



C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["MaterialAPI"].ComputeInterfaceInputConsumersMap.im_func.func_doc = """ComputeInterfaceInputConsumersMap(computeTransitiveConsumers) -> USDRI_API UsdShadeNodeGraph.InterfaceInputConsumersMap

computeTransitiveConsumers : bool


Walks the namespace subtree below the material and computes a map
containing the list of all inputs on the material and the associated
vector of consumers of their values.


The consumers can be inputs on shaders within the material or on node-
graphs under it.

"""
   result["MaterialAPI"].GetVolumeOutput.im_func.func_doc = """GetVolumeOutput() -> USDRI_API UsdShadeOutput



Returns the "volume" output associated with the material.

"""
   result["MaterialAPI"].SetInterfaceInputConsumer.im_func.func_doc = """SetInterfaceInputConsumer(interfaceInput, consumer) -> USDRI_API bool

interfaceInput : UsdShadeInput
consumer : UsdShadeInput


Set the input consumer of the given C{interfaceInput} to the specified
input, C{consumer}.


This sets the connected source of C{consumer} to C{interfaceInput}.

"""
   result["MaterialAPI"].SetDisplacementSource.im_func.func_doc = """SetDisplacementSource(displacementPath) -> USDRI_API bool

displacementPath : SdfPath

"""
   result["MaterialAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiMaterialAPI on UsdPrim C{prim}.


Equivalent to UsdRiMaterialAPI::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiMaterialAPI on the prim held by C{schemaObj}.


Should be preferred over UsdRiMaterialAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.


----------------------------------------------------------------------
__init__(material)

material : UsdShadeMaterial


A constructor for creating a MaterialAPI object from a material prim.

"""
   result["MaterialAPI"].GetSurfaceOutput.im_func.func_doc = """GetSurfaceOutput() -> USDRI_API UsdShadeOutput



Returns the "surface" output associated with the material.

"""
   result["MaterialAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["MaterialAPI"].GetDisplacement.im_func.func_doc = """GetDisplacement(ignoreBaseMaterial) -> USDRI_API UsdShadeShader

ignoreBaseMaterial : bool


Returns a valid shader object if the "displacement" output on the
material is connected to one.


If C{ignoreBaseMaterial} is true and if the "displacement" shader
source is specified in the base-material of this material, then this
returns an invalid shader object.

"""
   result["MaterialAPI"].CreateVolumeAttr.im_func.func_doc = """CreateVolumeAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVolumeAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["MaterialAPI"].CreateSurfaceAttr.im_func.func_doc = """CreateSurfaceAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSurfaceAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["MaterialAPI"].GetSurface.im_func.func_doc = """GetSurface(ignoreBaseMaterial) -> USDRI_API UsdShadeShader

ignoreBaseMaterial : bool


Returns a valid shader object if the "surface" output on the material
is connected to one.


If C{ignoreBaseMaterial} is true and if the "surface" shader source is
specified in the base-material of this material, then this returns an
invalid shader object.

"""
   result["MaterialAPI"].GetDisplacementAttr.im_func.func_doc = """GetDisplacementAttr() -> USDRI_API UsdAttribute



C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["MaterialAPI"].Apply.func_doc = """**static** Apply(prim) -> USDRI_API UsdRiMaterialAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "RiMaterialAPI" to the token-
valued, listOp metadata *apiSchemas* on the prim.

A valid UsdRiMaterialAPI object is returned upon success. An invalid
(or empty) UsdRiMaterialAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["MaterialAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["PxrAovLight"].__doc__ = """"""
   result["PxrAovLight"].CreateUseThroughputAttr.im_func.func_doc = """CreateUseThroughputAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetUseThroughputAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrAovLight"].CreateAovNameAttr.im_func.func_doc = """CreateAovNameAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAovNameAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrAovLight"].CreateInvertAttr.im_func.func_doc = """CreateInvertAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetInvertAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrAovLight"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PxrAovLight"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiPxrAovLight

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
   result["PxrAovLight"].CreateInPrimaryHitAttr.im_func.func_doc = """CreateInPrimaryHitAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetInPrimaryHitAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrAovLight"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiPxrAovLight

stage : UsdStagePtr
path : SdfPath


Return a UsdRiPxrAovLight holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiPxrAovLight(stage->GetPrimAtPath(path));


"""
   result["PxrAovLight"].GetInvertAttr.im_func.func_doc = """GetInvertAttr() -> USDRI_API UsdAttribute



If this is on, it inverts the signal for the AOV.


C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrAovLight"].GetUseThroughputAttr.im_func.func_doc = """GetUseThroughputAttr() -> USDRI_API UsdAttribute



If this is on, the values in the mask for the reflected or refracted
rays will be affected by the strength of the reflection or refraction.


This can lead to values below and above 1.0. Turn this off if you want
a more solid mask.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: True

"""
   result["PxrAovLight"].GetOnVolumeBoundariesAttr.im_func.func_doc = """GetOnVolumeBoundariesAttr() -> USDRI_API UsdAttribute



If this is on, the bounding box or shape of volumes will appear in the
mask.


Since this is not always desirable, this can be turned off.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: True

"""
   result["PxrAovLight"].CreateInReflectionAttr.im_func.func_doc = """CreateInReflectionAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetInReflectionAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrAovLight"].GetInPrimaryHitAttr.im_func.func_doc = """GetInPrimaryHitAttr() -> USDRI_API UsdAttribute



If this is on, the usual mask of the illuminated objects is generated.


If this is off, you can get a mask of only in the refraction or
reflection.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: True

"""
   result["PxrAovLight"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiPxrAovLight on UsdPrim C{prim}.


Equivalent to UsdRiPxrAovLight::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiPxrAovLight on the prim held by C{schemaObj}.


Should be preferred over UsdRiPxrAovLight (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["PxrAovLight"].CreateOnVolumeBoundariesAttr.im_func.func_doc = """CreateOnVolumeBoundariesAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetOnVolumeBoundariesAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrAovLight"].GetInReflectionAttr.im_func.func_doc = """GetInReflectionAttr() -> USDRI_API UsdAttribute



If this is on, the rays are traced through the specular reflections to
get the masking signal.


Warning: this will require some amount of samples to get a clean mask.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrAovLight"].GetUseColorAttr.im_func.func_doc = """GetUseColorAttr() -> USDRI_API UsdAttribute



If this is on, it outputs a RGB color image instead of a float image
for the AOV.


C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrAovLight"].CreateUseColorAttr.im_func.func_doc = """CreateUseColorAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetUseColorAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrAovLight"].GetAovNameAttr.im_func.func_doc = """GetAovNameAttr() -> USDRI_API UsdAttribute



The name of the AOV to write to.


C++ Type: std::string  Usd Type: SdfValueTypeNames->String
Variability: SdfVariabilityVarying  Fallback Value:

"""
   result["PxrAovLight"].CreateInRefractionAttr.im_func.func_doc = """CreateInRefractionAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetInRefractionAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrAovLight"].GetInRefractionAttr.im_func.func_doc = """GetInRefractionAttr() -> USDRI_API UsdAttribute



If this is on, the rays are traced through the glass refractions to
get the masking signal.


Warning: this will require some amount of samples to get a clean mask.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrAovLight"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["PxrBarnLightFilter"].__doc__ = """
Simulated geometric barn doors that control the spread of light.


For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdRiTokens. So to set an attribute to the value "rightHanded", use
UsdRiTokens->rightHanded as the value.

"""
   result["PxrBarnLightFilter"].CreateHeightAttr.im_func.func_doc = """CreateHeightAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHeightAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetAnalyticShearXAttr.im_func.func_doc = """GetAnalyticShearXAttr() -> USDRI_API UsdAttribute



Shear the projection along the X axis.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].GetBarnModeAttr.im_func.func_doc = """GetBarnModeAttr() -> USDRI_API UsdAttribute



Chooses a physical or analytic evaluation model for the barn.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: physical  Allowed Values :
[physical, analytic]

"""
   result["PxrBarnLightFilter"].GetAnalyticDensityExponentAttr.im_func.func_doc = """GetAnalyticDensityExponentAttr() -> USDRI_API UsdAttribute



Power exponent of the density interpolation.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].GetEdgeRightAttr.im_func.func_doc = """GetEdgeRightAttr() -> USDRI_API UsdAttribute



Additional adjustment to the left region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].GetEdgeThicknessAttr.im_func.func_doc = """GetEdgeThicknessAttr() -> USDRI_API UsdAttribute



Thickness of the edge region.


Larger values will soften the edge shape.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["PxrBarnLightFilter"].CreateBarnModeAttr.im_func.func_doc = """CreateBarnModeAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetBarnModeAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateAnalyticUseLightDirectionAttr.im_func.func_doc = """CreateAnalyticUseLightDirectionAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticUseLightDirectionAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateRefineTopAttr.im_func.func_doc = """CreateRefineTopAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineTopAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetRadiusAttr.im_func.func_doc = """GetRadiusAttr() -> USDRI_API UsdAttribute



Radius of the corners of the inner barn square.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.5

"""
   result["PxrBarnLightFilter"].CreateAnalyticShearYAttr.im_func.func_doc = """CreateAnalyticShearYAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticShearYAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetScaleWidthAttr.im_func.func_doc = """GetScaleWidthAttr() -> USDRI_API UsdAttribute



Scale the width of the inner barn shape.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrBarnLightFilter"].GetAnalyticDensityFarDistanceAttr.im_func.func_doc = """GetAnalyticDensityFarDistanceAttr() -> USDRI_API UsdAttribute



Distance from the barn where the density interpolation ends.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].GetScaleHeightAttr.im_func.func_doc = """GetScaleHeightAttr() -> USDRI_API UsdAttribute



Scale the height of the inner barn shape.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrBarnLightFilter"].CreateEdgeThicknessAttr.im_func.func_doc = """CreateEdgeThicknessAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeThicknessAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetRefineLeftAttr.im_func.func_doc = """GetRefineLeftAttr() -> USDRI_API UsdAttribute



Additional adjustment to the left region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].CreateRadiusAttr.im_func.func_doc = """CreateRadiusAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRadiusAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetAnalyticDensityNearValueAttr.im_func.func_doc = """GetAnalyticDensityNearValueAttr() -> USDRI_API UsdAttribute



Density multiplier where the density interpolation starts.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiPxrBarnLightFilter

stage : UsdStagePtr
path : SdfPath


Return a UsdRiPxrBarnLightFilter holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiPxrBarnLightFilter(stage->GetPrimAtPath(path));


"""
   result["PxrBarnLightFilter"].GetEdgeLeftAttr.im_func.func_doc = """GetEdgeLeftAttr() -> USDRI_API UsdAttribute



Additional adjustment to the left region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].GetRefineBottomAttr.im_func.func_doc = """GetRefineBottomAttr() -> USDRI_API UsdAttribute



Additional adjustment to the top region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].GetEdgeTopAttr.im_func.func_doc = """GetEdgeTopAttr() -> USDRI_API UsdAttribute



Additional adjustment to the top region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].CreateAnalyticDensityNearDistanceAttr.im_func.func_doc = """CreateAnalyticDensityNearDistanceAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityNearDistanceAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetPreBarnEffectAttr.im_func.func_doc = """GetPreBarnEffectAttr() -> USDRI_API UsdAttribute



The effect on light before it reaches the barn geometry.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: noEffect  Allowed Values :
[noEffect, cone, noLight]

"""
   result["PxrBarnLightFilter"].CreateEdgeBottomAttr.im_func.func_doc = """CreateEdgeBottomAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeBottomAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateScaleWidthAttr.im_func.func_doc = """CreateScaleWidthAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetScaleWidthAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateEdgeRightAttr.im_func.func_doc = """CreateEdgeRightAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeRightAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiPxrBarnLightFilter

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
   result["PxrBarnLightFilter"].GetAnalyticDirectionalAttr.im_func.func_doc = """GetAnalyticDirectionalAttr() -> USDRI_API UsdAttribute



When this is on, the texture projects along a direction using the
orthographic projection.


When it is off, the texture projects using a focal point specified by
the analytic:apex.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrBarnLightFilter"].GetHeightAttr.im_func.func_doc = """GetHeightAttr() -> USDRI_API UsdAttribute



Height of the inner region of the barn (Y axis).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrBarnLightFilter"].CreateAnalyticDensityExponentAttr.im_func.func_doc = """CreateAnalyticDensityExponentAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityExponentAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateAnalyticShearXAttr.im_func.func_doc = """CreateAnalyticShearXAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticShearXAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetAnalyticUseLightDirectionAttr.im_func.func_doc = """GetAnalyticUseLightDirectionAttr() -> USDRI_API UsdAttribute



When this is on, If this is on, the projection direction is determined
by the position of the center of the light source.


Otherwise, it only follows the orientation of the barn. WARNING: This
does not work with dome and mesh lights.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrBarnLightFilter"].CreateRefineRightAttr.im_func.func_doc = """CreateRefineRightAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineRightAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateAnalyticDensityFarValueAttr.im_func.func_doc = """CreateAnalyticDensityFarValueAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityFarValueAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateRefineLeftAttr.im_func.func_doc = """CreateRefineLeftAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineLeftAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateAnalyticDirectionalAttr.im_func.func_doc = """CreateAnalyticDirectionalAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDirectionalAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetRefineRightAttr.im_func.func_doc = """GetRefineRightAttr() -> USDRI_API UsdAttribute



Additional adjustment to the left region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].CreateAnalyticDensityFarDistanceAttr.im_func.func_doc = """CreateAnalyticDensityFarDistanceAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityFarDistanceAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PxrBarnLightFilter"].CreateEdgeLeftAttr.im_func.func_doc = """CreateEdgeLeftAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeLeftAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetEdgeBottomAttr.im_func.func_doc = """GetEdgeBottomAttr() -> USDRI_API UsdAttribute



Additional adjustment to the top region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].CreateAnalyticApexAttr.im_func.func_doc = """CreateAnalyticApexAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticApexAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetRefineTopAttr.im_func.func_doc = """GetRefineTopAttr() -> USDRI_API UsdAttribute



Additional adjustment to the top region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].CreateEdgeTopAttr.im_func.func_doc = """CreateEdgeTopAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeTopAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiPxrBarnLightFilter on UsdPrim C{prim}.


Equivalent to UsdRiPxrBarnLightFilter::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiPxrBarnLightFilter on the prim held by C{schemaObj}.


Should be preferred over UsdRiPxrBarnLightFilter
(schemaObj.GetPrim()), as it preserves SchemaBase state.

"""
   result["PxrBarnLightFilter"].GetAnalyticDensityFarValueAttr.im_func.func_doc = """GetAnalyticDensityFarValueAttr() -> USDRI_API UsdAttribute



Density multiplier at the end of interpolation.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].GetAnalyticShearYAttr.im_func.func_doc = """GetAnalyticShearYAttr() -> USDRI_API UsdAttribute



Shear the projection along the Y axis.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].CreateScaleHeightAttr.im_func.func_doc = """CreateScaleHeightAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetScaleHeightAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetAnalyticApexAttr.im_func.func_doc = """GetAnalyticApexAttr() -> USDRI_API UsdAttribute



Shear the projection along the Y axis.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrBarnLightFilter"].CreateAnalyticDensityNearValueAttr.im_func.func_doc = """CreateAnalyticDensityNearValueAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityNearValueAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetWidthAttr.im_func.func_doc = """GetWidthAttr() -> USDRI_API UsdAttribute



Width of the inner region of the barn (X axis).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrBarnLightFilter"].CreatePreBarnEffectAttr.im_func.func_doc = """CreatePreBarnEffectAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetPreBarnEffectAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateRefineBottomAttr.im_func.func_doc = """CreateRefineBottomAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineBottomAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].CreateWidthAttr.im_func.func_doc = """CreateWidthAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetWidthAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrBarnLightFilter"].GetAnalyticDensityNearDistanceAttr.im_func.func_doc = """GetAnalyticDensityNearDistanceAttr() -> USDRI_API UsdAttribute



Distance from the barn where the density interpolation starts.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["RslShader"].__doc__ = """"""
   result["RslShader"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiRslShader

stage : UsdStagePtr
path : SdfPath


Return a UsdRiRslShader holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiRslShader(stage->GetPrimAtPath(path));


"""
   result["RslShader"].GetSloPathAttr.im_func.func_doc = """GetSloPathAttr() -> USDRI_API UsdAttribute



C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["RslShader"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["RslShader"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiRslShader on UsdPrim C{prim}.


Equivalent to UsdRiRslShader::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiRslShader on the prim held by C{schemaObj}.


Should be preferred over UsdRiRslShader (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["RslShader"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["RslShader"].CreateSloPathAttr.im_func.func_doc = """CreateSloPathAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSloPathAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RslShader"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiRslShader

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
   result["RisIntegrator"].__doc__ = """
Integrator.


Only one can be declared in a rib scene.

"""
   result["RisIntegrator"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiRisIntegrator on UsdPrim C{prim}.


Equivalent to UsdRiRisIntegrator::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiRisIntegrator on the prim held by C{schemaObj}.


Should be preferred over UsdRiRisIntegrator (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["RisIntegrator"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiRisIntegrator

stage : UsdStagePtr
path : SdfPath


Return a UsdRiRisIntegrator holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiRisIntegrator(stage->GetPrimAtPath(path));


"""
   result["RisIntegrator"].CreateArgsPathAttr.im_func.func_doc = """CreateArgsPathAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetArgsPathAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RisIntegrator"].GetArgsPathAttr.im_func.func_doc = """GetArgsPathAttr() -> USDRI_API UsdAttribute



C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["RisIntegrator"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["RisIntegrator"].CreateFilePathAttr.im_func.func_doc = """CreateFilePathAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFilePathAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RisIntegrator"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["RisIntegrator"].GetFilePathAttr.im_func.func_doc = """GetFilePathAttr() -> USDRI_API UsdAttribute



C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["RisIntegrator"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiRisIntegrator

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
   result["PxrEnvDayLight"].__doc__ = """"""
   result["PxrEnvDayLight"].GetHourAttr.im_func.func_doc = """GetHourAttr() -> USDRI_API UsdAttribute



hour: Hours since midnight, local standard time.


May be fractional to include minutes and seconds. If daylight saving
time is in effect, subtract 1 to correct to standard time. This is
ignored if month is 0.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 14.6333332062

"""
   result["PxrEnvDayLight"].CreateSunTintAttr.im_func.func_doc = """CreateSunTintAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSunTintAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].CreateYearAttr.im_func.func_doc = """CreateYearAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetYearAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].CreateLongitudeAttr.im_func.func_doc = """CreateLongitudeAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetLongitudeAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiPxrEnvDayLight on UsdPrim C{prim}.


Equivalent to UsdRiPxrEnvDayLight::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiPxrEnvDayLight on the prim held by C{schemaObj}.


Should be preferred over UsdRiPxrEnvDayLight (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["PxrEnvDayLight"].GetSkyTintAttr.im_func.func_doc = """GetSkyTintAttr() -> USDRI_API UsdAttribute



skyTint: Tweak the sky's contribution and color.


The default, white (1,1,1), gives results based on measured physical
values.

C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Color3f  Variability:
SdfVariabilityVarying  Fallback Value: (1, 1, 1)

"""
   result["PxrEnvDayLight"].CreateMonthAttr.im_func.func_doc = """CreateMonthAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetMonthAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].CreateHourAttr.im_func.func_doc = """CreateHourAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHourAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiPxrEnvDayLight

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
   result["PxrEnvDayLight"].GetSunTintAttr.im_func.func_doc = """GetSunTintAttr() -> USDRI_API UsdAttribute



sunTint: Tweak the sun's contribution and color.


The default, white (1,1,1), gives results based on measured physical
values. Setting this to black removes the sun contribution.

C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Color3f  Variability:
SdfVariabilityVarying  Fallback Value: (1, 1, 1)

"""
   result["PxrEnvDayLight"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiPxrEnvDayLight

stage : UsdStagePtr
path : SdfPath


Return a UsdRiPxrEnvDayLight holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiPxrEnvDayLight(stage->GetPrimAtPath(path));


"""
   result["PxrEnvDayLight"].GetZoneAttr.im_func.func_doc = """GetZoneAttr() -> USDRI_API UsdAttribute



zone: Standard time zone offset from GMT/UTC in hours.


Positive for east, negative for west. For example, this would be -8
for Pacific time. This is ignored if month is 0.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: -8.0

"""
   result["PxrEnvDayLight"].CreateZoneAttr.im_func.func_doc = """CreateZoneAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetZoneAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].GetLatitudeAttr.im_func.func_doc = """GetLatitudeAttr() -> USDRI_API UsdAttribute



latitude: Latitude in degrees.


Positive for north, negative for south. Ranges frmo -90 to +90
degrees. This is ignored if month is 0.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 47.6020011902

"""
   result["PxrEnvDayLight"].GetSunDirectionAttr.im_func.func_doc = """GetSunDirectionAttr() -> USDRI_API UsdAttribute



sunDirection: The *apparent* direction towards the center of the sun.


The zenith is at +Y (for noon light) and the horizon is in the XZ
plane (for sunrise/set). Note that the Y component must non- negative.
Ignored if a month is given.

C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Vector3f  Variability:
SdfVariabilityVarying  Fallback Value: (0, 0, 1)

"""
   result["PxrEnvDayLight"].GetYearAttr.im_func.func_doc = """GetYearAttr() -> USDRI_API UsdAttribute



year: Four-digit year.


This is ignored if month is 0.

C++ Type: int  Usd Type: SdfValueTypeNames->Int  Variability:
SdfVariabilityVarying  Fallback Value: 2015

"""
   result["PxrEnvDayLight"].CreateSkyTintAttr.im_func.func_doc = """CreateSkyTintAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSkyTintAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].GetSunSizeAttr.im_func.func_doc = """GetSunSizeAttr() -> USDRI_API UsdAttribute



sunSize: Scale the apparent size of the sun in the sky.


Leave at 1 for a realistic sun size with an 0.55 degree angular
diameter.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrEnvDayLight"].GetDayAttr.im_func.func_doc = """GetDayAttr() -> USDRI_API UsdAttribute



day: Day of the month, 1 through 31.


This is ignored if month is 0.

C++ Type: int  Usd Type: SdfValueTypeNames->Int  Variability:
SdfVariabilityVarying  Fallback Value: 1

"""
   result["PxrEnvDayLight"].GetLongitudeAttr.im_func.func_doc = """GetLongitudeAttr() -> USDRI_API UsdAttribute



longitude: Longitude in degrees.


Positive for east, negative for west. Ranges frmo -180 to +180
degrees. This is ignored if month is 0.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: -122.332000732

"""
   result["PxrEnvDayLight"].GetHazinessAttr.im_func.func_doc = """GetHazinessAttr() -> USDRI_API UsdAttribute



haziness: The turbidity of the sky.


The lower limit of the model is 1.7 for an exceptionally clear sky,
and 10, for an nversion, is the upper limit.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 2.0

"""
   result["PxrEnvDayLight"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PxrEnvDayLight"].CreateLatitudeAttr.im_func.func_doc = """CreateLatitudeAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetLatitudeAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].CreateSunDirectionAttr.im_func.func_doc = """CreateSunDirectionAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSunDirectionAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].CreateDayAttr.im_func.func_doc = """CreateDayAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDayAttr() , and also Create vs Get Property Methods for when to
use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].CreateSunSizeAttr.im_func.func_doc = """CreateSunSizeAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSunSizeAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].CreateHazinessAttr.im_func.func_doc = """CreateHazinessAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHazinessAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrEnvDayLight"].GetMonthAttr.im_func.func_doc = """GetMonthAttr() -> USDRI_API UsdAttribute



month: Month of the year, 1 through 12.


The default, 0, means to use the explicitly given sun direction
instead of automatically computing it.

C++ Type: int  Usd Type: SdfValueTypeNames->Int  Variability:
SdfVariabilityVarying  Fallback Value: 0

"""
   result["PxrEnvDayLight"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["ConvertToRManInterpolateBoundary"].func_doc = """ConvertToRManInterpolateBoundary(token) -> USDRI_API int

token : TfToken


Given a C{token} representing a UsdGeom interpolate boundary value,
returns corresponding rman enum (converted to int).

"""
   result["LightPortalAPI"].__doc__ = """
Renderman-specific attributes for light portals.

"""
   result["LightPortalAPI"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiLightPortalAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdRiLightPortalAPI holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiLightPortalAPI(stage->GetPrimAtPath(path));


"""
   result["LightPortalAPI"].CreateRiPortalTintAttr.im_func.func_doc = """CreateRiPortalTintAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiPortalTintAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightPortalAPI"].GetRiPortalTintAttr.im_func.func_doc = """GetRiPortalTintAttr() -> USDRI_API UsdAttribute



tint: This parameter tints the color from the dome texture.


C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Color3f  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightPortalAPI"].GetRiPortalIntensityAttr.im_func.func_doc = """GetRiPortalIntensityAttr() -> USDRI_API UsdAttribute



Intensity adjustment relative to the light intensity.


This gets multiplied by the light's intensity and power

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightPortalAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiLightPortalAPI on UsdPrim C{prim}.


Equivalent to UsdRiLightPortalAPI::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiLightPortalAPI on the prim held by C{schemaObj}.


Should be preferred over UsdRiLightPortalAPI (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["LightPortalAPI"].Apply.func_doc = """**static** Apply(prim) -> USDRI_API UsdRiLightPortalAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "RiLightPortalAPI" to the token-
valued, listOp metadata *apiSchemas* on the prim.

A valid UsdRiLightPortalAPI object is returned upon success. An
invalid (or empty) UsdRiLightPortalAPI object is returned upon
failure. See UsdAPISchemaBase::_ApplyAPISchema() for conditions
resulting in failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["LightPortalAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["LightPortalAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["LightPortalAPI"].CreateRiPortalIntensityAttr.im_func.func_doc = """CreateRiPortalIntensityAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiPortalIntensityAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].__doc__ = """
A textured surface that filters light.


For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdRiTokens. So to set an attribute to the value "rightHanded", use
UsdRiTokens->rightHanded as the value.

"""
   result["PxrCookieLightFilter"].CreateAnalyticBlurTMultAttr.im_func.func_doc = """CreateAnalyticBlurTMultAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurTMultAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateTextureFillColorAttr.im_func.func_doc = """CreateTextureFillColorAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureFillColorAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticUseLightDirectionAttr.im_func.func_doc = """CreateAnalyticUseLightDirectionAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticUseLightDirectionAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetTextureOffsetVAttr.im_func.func_doc = """GetTextureOffsetVAttr() -> USDRI_API UsdAttribute



Offsets the texture in the V direction.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PxrCookieLightFilter"].CreateAnalyticBlurMidpointAttr.im_func.func_doc = """CreateAnalyticBlurMidpointAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurMidpointAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetColorTintAttr.im_func.func_doc = """GetColorTintAttr() -> USDRI_API UsdAttribute



Tint of the resulting color after saturation, contrast and clamp.


C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Color3f  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PxrCookieLightFilter"].GetTextureScaleUAttr.im_func.func_doc = """GetTextureScaleUAttr() -> USDRI_API UsdAttribute



Scales the U dimension.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrCookieLightFilter"].CreateAnalyticBlurExponentAttr.im_func.func_doc = """CreateAnalyticBlurExponentAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurExponentAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurTMultAttr.im_func.func_doc = """GetAnalyticBlurTMultAttr() -> USDRI_API UsdAttribute



Blur multiplier in the T direction.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetCookieModeAttr.im_func.func_doc = """GetCookieModeAttr() -> USDRI_API UsdAttribute



Chooses a physical or analytic evaluation model for the cookie:



   - physical: The cookie behaves like a stained glass window through
     which light falls. The falloff and blur are determined by the size of
     the light, the distance to the light and distance from the cookie.

   - analytic: The cookie has a fixed projection and manual blur and
     falloff controls.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: physical  Allowed Values :
[physical, analytic]

"""
   result["PxrCookieLightFilter"].GetTextureScaleVAttr.im_func.func_doc = """GetTextureScaleVAttr() -> USDRI_API UsdAttribute



Scales the V dimension.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrCookieLightFilter"].GetColorContrastAttr.im_func.func_doc = """GetColorContrastAttr() -> USDRI_API UsdAttribute



Contrast control (less than 1 = contrast reduction, larger than 1 =
contrast increase).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurFarValueAttr.im_func.func_doc = """GetAnalyticBlurFarValueAttr() -> USDRI_API UsdAttribute



Blur multiplier at the end of interpolation.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetAnalyticDirectionalAttr.im_func.func_doc = """GetAnalyticDirectionalAttr() -> USDRI_API UsdAttribute



When this is on, the texture projects along a direction using the
orthographic projection.


When it is off, the texture projects using a focal point specified by
the analytic:apex.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrCookieLightFilter"].CreateAnalyticBlurMidValueAttr.im_func.func_doc = """CreateAnalyticBlurMidValueAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurMidValueAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetAnalyticShearYAttr.im_func.func_doc = """GetAnalyticShearYAttr() -> USDRI_API UsdAttribute



Shear the projection along the Y axis.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetAnalyticApexAttr.im_func.func_doc = """GetAnalyticApexAttr() -> USDRI_API UsdAttribute



Shear the projection along the Y axis.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetWidthAttr.im_func.func_doc = """GetWidthAttr() -> USDRI_API UsdAttribute



Width of the rect the light is shining through.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurFarDistanceAttr.im_func.func_doc = """GetAnalyticBlurFarDistanceAttr() -> USDRI_API UsdAttribute



Distance from the cookie where the blur interpolation ends.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].CreateWidthAttr.im_func.func_doc = """CreateWidthAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetWidthAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateHeightAttr.im_func.func_doc = """CreateHeightAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHeightAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurMidpointAttr.im_func.func_doc = """GetAnalyticBlurMidpointAttr() -> USDRI_API UsdAttribute



Distance between near and far where midValue is located.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].CreateTextureOffsetVAttr.im_func.func_doc = """CreateTextureOffsetVAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureOffsetVAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetTextureMapAttr.im_func.func_doc = """GetTextureMapAttr() -> USDRI_API UsdAttribute



A color texture to use on the cookie.


May use alpha.

C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PxrCookieLightFilter"].GetTextureInvertUAttr.im_func.func_doc = """GetTextureInvertUAttr() -> USDRI_API UsdAttribute



Flips the texture from left to right.


By default, the orientation of the texture as seen from the light
source matches the orientation as it is viewed in an image viewer.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrCookieLightFilter"].CreateAnalyticShearYAttr.im_func.func_doc = """CreateAnalyticShearYAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticShearYAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetColorMidpointAttr.im_func.func_doc = """GetColorMidpointAttr() -> USDRI_API UsdAttribute



Midpoint for the contrast control.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.180000007153

"""
   result["PxrCookieLightFilter"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiPxrCookieLightFilter

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
   result["PxrCookieLightFilter"].CreateAnalyticBlurNearDistanceAttr.im_func.func_doc = """CreateAnalyticBlurNearDistanceAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurNearDistanceAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurSMultAttr.im_func.func_doc = """GetAnalyticBlurSMultAttr() -> USDRI_API UsdAttribute



Blur multiplier in the S direction.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].CreateTextureInvertUAttr.im_func.func_doc = """CreateTextureInvertUAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureInvertUAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticBlurFarValueAttr.im_func.func_doc = """CreateAnalyticBlurFarValueAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurFarValueAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticDensityMidpointAttr.im_func.func_doc = """CreateAnalyticDensityMidpointAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityMidpointAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateColorContrastAttr.im_func.func_doc = """CreateColorContrastAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetColorContrastAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticDensityExponentAttr.im_func.func_doc = """CreateAnalyticDensityExponentAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityExponentAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateTextureInvertVAttr.im_func.func_doc = """CreateTextureInvertVAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureInvertVAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticShearXAttr.im_func.func_doc = """CreateAnalyticShearXAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticShearXAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticDirectionalAttr.im_func.func_doc = """CreateAnalyticDirectionalAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDirectionalAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateColorTintAttr.im_func.func_doc = """CreateColorTintAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetColorTintAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetColorWhitepointAttr.im_func.func_doc = """GetColorWhitepointAttr() -> USDRI_API UsdAttribute



White point for the contrast control if (contrast>1.0).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrCookieLightFilter"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiPxrCookieLightFilter on UsdPrim C{prim}.


Equivalent to UsdRiPxrCookieLightFilter::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiPxrCookieLightFilter on the prim held by
C{schemaObj}.


Should be preferred over UsdRiPxrCookieLightFilter
(schemaObj.GetPrim()), as it preserves SchemaBase state.

"""
   result["PxrCookieLightFilter"].GetAnalyticDensityFarValueAttr.im_func.func_doc = """GetAnalyticDensityFarValueAttr() -> USDRI_API UsdAttribute



Density multiplier at the end of interpolation.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].CreateTextureWrapModeAttr.im_func.func_doc = """CreateTextureWrapModeAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureWrapModeAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetAnalyticDensityExponentAttr.im_func.func_doc = """GetAnalyticDensityExponentAttr() -> USDRI_API UsdAttribute



Power exponent of the density interpolation.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].CreateTextureScaleVAttr.im_func.func_doc = """CreateTextureScaleVAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureScaleVAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticBlurSMultAttr.im_func.func_doc = """CreateAnalyticBlurSMultAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurSMultAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetAnalyticDensityNearValueAttr.im_func.func_doc = """GetAnalyticDensityNearValueAttr() -> USDRI_API UsdAttribute



Density multiplier where the density interpolation starts.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiPxrCookieLightFilter

stage : UsdStagePtr
path : SdfPath


Return a UsdRiPxrCookieLightFilter holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiPxrCookieLightFilter(stage->GetPrimAtPath(path));


"""
   result["PxrCookieLightFilter"].GetTextureFillColorAttr.im_func.func_doc = """GetTextureFillColorAttr() -> USDRI_API UsdAttribute



If the texture is not repeating, this specifies the color for the
region outside of and behind the projected rectangle.


C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Color3f  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["PxrCookieLightFilter"].CreateColorMidpointAttr.im_func.func_doc = """CreateColorMidpointAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetColorMidpointAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetTextureOffsetUAttr.im_func.func_doc = """GetTextureOffsetUAttr() -> USDRI_API UsdAttribute



Offsets the texture in the U direction.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurNearDistanceAttr.im_func.func_doc = """GetAnalyticBlurNearDistanceAttr() -> USDRI_API UsdAttribute



Distance from the cookie where the blur interpolation starts.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].CreateAnalyticDensityFarValueAttr.im_func.func_doc = """CreateAnalyticDensityFarValueAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityFarValueAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurMidValueAttr.im_func.func_doc = """GetAnalyticBlurMidValueAttr() -> USDRI_API UsdAttribute



Blur multiplier in the middle of interpolation.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].CreateCookieModeAttr.im_func.func_doc = """CreateCookieModeAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetCookieModeAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetAnalyticDensityMidpointAttr.im_func.func_doc = """GetAnalyticDensityMidpointAttr() -> USDRI_API UsdAttribute



Distance between near and far where midValue is located.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurNearValueAttr.im_func.func_doc = """GetAnalyticBlurNearValueAttr() -> USDRI_API UsdAttribute



Blur multiplier where the blur interpolation starts.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurExponentAttr.im_func.func_doc = """GetAnalyticBlurExponentAttr() -> USDRI_API UsdAttribute



Power exponent of the blur interpolation.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].CreateAnalyticBlurFarDistanceAttr.im_func.func_doc = """CreateAnalyticBlurFarDistanceAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurFarDistanceAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateTextureScaleUAttr.im_func.func_doc = """CreateTextureScaleUAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureScaleUAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetHeightAttr.im_func.func_doc = """GetHeightAttr() -> USDRI_API UsdAttribute



Height of the rect the light is shining through.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrCookieLightFilter"].GetAnalyticShearXAttr.im_func.func_doc = """GetAnalyticShearXAttr() -> USDRI_API UsdAttribute



Shear the projection along the X axis.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetAnalyticUseLightDirectionAttr.im_func.func_doc = """GetAnalyticUseLightDirectionAttr() -> USDRI_API UsdAttribute



When this is on, If this is on, the projection direction is determined
by the position of the center of the light source.


Otherwise, it only follows the orientation of the filter. WARNING:
This does not work with dome and mesh lights.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrCookieLightFilter"].GetColorSaturationAttr.im_func.func_doc = """GetColorSaturationAttr() -> USDRI_API UsdAttribute



Saturation of the result (0=greyscale, 1=normal,>1=boosted colors).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrCookieLightFilter"].GetAnalyticDensityFarDistanceAttr.im_func.func_doc = """GetAnalyticDensityFarDistanceAttr() -> USDRI_API UsdAttribute



Distance from the cookie where the density interpolation ends.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].GetAnalyticBlurAmountAttr.im_func.func_doc = """GetAnalyticBlurAmountAttr() -> USDRI_API UsdAttribute



Specify the blur of projected texture from 0-1.


This gets multiplied by the blurNear/blurFar interpolation. This blurs
between the projected color and the fill color when the texture is not
repeating.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"].CreateTextureOffsetUAttr.im_func.func_doc = """CreateTextureOffsetUAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureOffsetUAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticDensityNearDistanceAttr.im_func.func_doc = """CreateAnalyticDensityNearDistanceAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityNearDistanceAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetTextureInvertVAttr.im_func.func_doc = """GetTextureInvertVAttr() -> USDRI_API UsdAttribute



Flips the texture from top to bottom.


By default, the orientation of the texture as seen from the light
source matches the orientation as it is viewed in an image viewer.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: False

"""
   result["PxrCookieLightFilter"].CreateAnalyticBlurNearValueAttr.im_func.func_doc = """CreateAnalyticBlurNearValueAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurNearValueAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateTextureMapAttr.im_func.func_doc = """CreateTextureMapAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetTextureMapAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateColorSaturationAttr.im_func.func_doc = """CreateColorSaturationAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetColorSaturationAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticDensityNearValueAttr.im_func.func_doc = """CreateAnalyticDensityNearValueAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityNearValueAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticDensityFarDistanceAttr.im_func.func_doc = """CreateAnalyticDensityFarDistanceAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityFarDistanceAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateColorWhitepointAttr.im_func.func_doc = """CreateColorWhitepointAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetColorWhitepointAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticDensityMidValueAttr.im_func.func_doc = """CreateAnalyticDensityMidValueAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticDensityMidValueAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].CreateAnalyticApexAttr.im_func.func_doc = """CreateAnalyticApexAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticApexAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetTextureWrapModeAttr.im_func.func_doc = """GetTextureWrapModeAttr() -> USDRI_API UsdAttribute



Specifies what value to use outside the texture's domain:



   - off: no repeat

   - repeat: repeats in X and Y

   - clamp: uses the value from the nearest edge

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: off  Allowed Values : [off,
repeat, clamp]

"""
   result["PxrCookieLightFilter"].CreateAnalyticBlurAmountAttr.im_func.func_doc = """CreateAnalyticBlurAmountAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetAnalyticBlurAmountAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrCookieLightFilter"].GetAnalyticDensityMidValueAttr.im_func.func_doc = """GetAnalyticDensityMidValueAttr() -> USDRI_API UsdAttribute



Density multiplier in the middle of interpolation.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrCookieLightFilter"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["PxrCookieLightFilter"].GetAnalyticDensityNearDistanceAttr.im_func.func_doc = """GetAnalyticDensityNearDistanceAttr() -> USDRI_API UsdAttribute



Distance from the cookie where the density interpolation starts.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].__doc__ = """
Simulates a rod or capsule-shaped region to modulate light.

"""
   result["PxrRodLightFilter"].CreateHeightAttr.im_func.func_doc = """CreateHeightAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetHeightAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetRefineBottomAttr.im_func.func_doc = """GetRefineBottomAttr() -> USDRI_API UsdAttribute



Additional adjustment to the top region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].GetColorRampAPI.im_func.func_doc = """GetColorRampAPI() -> USDRI_API UsdRiSplineAPI



Return the UsdRiSplineAPI interface used for examining and modifying
the color ramp.


The values of the spline knots are of type GfVec3f, representing RGB
colors.

"""
   result["PxrRodLightFilter"].GetColorSaturationAttr.im_func.func_doc = """GetColorSaturationAttr() -> USDRI_API UsdAttribute



Saturation of the result (0=greyscale, 1=normal,>1=boosted colors).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrRodLightFilter"].GetDepthAttr.im_func.func_doc = """GetDepthAttr() -> USDRI_API UsdAttribute



Depth of the inner region of the rod (Z axis).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrRodLightFilter"].GetEdgeThicknessAttr.im_func.func_doc = """GetEdgeThicknessAttr() -> USDRI_API UsdAttribute



Thickness of the edge region.


Larger values will soften the edge shape.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["PxrRodLightFilter"].CreateRefineFrontAttr.im_func.func_doc = """CreateRefineFrontAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineFrontAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].CreateEdgeBackAttr.im_func.func_doc = """CreateEdgeBackAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeBackAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetRadiusAttr.im_func.func_doc = """GetRadiusAttr() -> USDRI_API UsdAttribute



Radius of the corners of the inner rod box.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.5

"""
   result["PxrRodLightFilter"].CreateEdgeTopAttr.im_func.func_doc = """CreateEdgeTopAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeTopAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetScaleWidthAttr.im_func.func_doc = """GetScaleWidthAttr() -> USDRI_API UsdAttribute



Scale the width of the inner rod shape.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrRodLightFilter"].GetRefineFrontAttr.im_func.func_doc = """GetRefineFrontAttr() -> USDRI_API UsdAttribute



Additional adjustment to the front region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].GetScaleHeightAttr.im_func.func_doc = """GetScaleHeightAttr() -> USDRI_API UsdAttribute



Scale the height of the inner rod shape.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrRodLightFilter"].GetEdgeLeftAttr.im_func.func_doc = """GetEdgeLeftAttr() -> USDRI_API UsdAttribute



Additional adjustment to the left region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].CreateRadiusAttr.im_func.func_doc = """CreateRadiusAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRadiusAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiPxrRodLightFilter

stage : UsdStagePtr
path : SdfPath


Return a UsdRiPxrRodLightFilter holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiPxrRodLightFilter(stage->GetPrimAtPath(path));


"""
   result["PxrRodLightFilter"].GetRefineBackAttr.im_func.func_doc = """GetRefineBackAttr() -> USDRI_API UsdAttribute



Additional adjustment to the back region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].CreateEdgeFrontAttr.im_func.func_doc = """CreateEdgeFrontAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeFrontAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetEdgeTopAttr.im_func.func_doc = """GetEdgeTopAttr() -> USDRI_API UsdAttribute



Additional adjustment to the top region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].GetRefineLeftAttr.im_func.func_doc = """GetRefineLeftAttr() -> USDRI_API UsdAttribute



Additional adjustment to the left region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].GetEdgeBackAttr.im_func.func_doc = """GetEdgeBackAttr() -> USDRI_API UsdAttribute



Additional adjustment to the back region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].CreateScaleDepthAttr.im_func.func_doc = """CreateScaleDepthAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetScaleDepthAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetEdgeFrontAttr.im_func.func_doc = """GetEdgeFrontAttr() -> USDRI_API UsdAttribute



Additional adjustment to the front region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].CreateScaleWidthAttr.im_func.func_doc = """CreateScaleWidthAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetScaleWidthAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].CreateEdgeRightAttr.im_func.func_doc = """CreateEdgeRightAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeRightAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetFalloffRampAPI.im_func.func_doc = """GetFalloffRampAPI() -> USDRI_API UsdRiSplineAPI



Return the UsdRiSplineAPI interface used for examining and modifying
the falloff ramp.


The values of the spline knots are of type float.

"""
   result["PxrRodLightFilter"].GetHeightAttr.im_func.func_doc = """GetHeightAttr() -> USDRI_API UsdAttribute



Height of the inner region of the rod (Y axis).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrRodLightFilter"].CreateColorSaturationAttr.im_func.func_doc = """CreateColorSaturationAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetColorSaturationAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetEdgeRightAttr.im_func.func_doc = """GetEdgeRightAttr() -> USDRI_API UsdAttribute



Additional adjustment to the left region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].CreateEdgeThicknessAttr.im_func.func_doc = """CreateEdgeThicknessAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeThicknessAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].CreateRefineBackAttr.im_func.func_doc = """CreateRefineBackAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineBackAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetScaleDepthAttr.im_func.func_doc = """GetScaleDepthAttr() -> USDRI_API UsdAttribute



Scale the depth of the inner rod shape.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrRodLightFilter"].CreateRefineRightAttr.im_func.func_doc = """CreateRefineRightAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineRightAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].CreateRefineLeftAttr.im_func.func_doc = """CreateRefineLeftAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineLeftAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].CreateEdgeLeftAttr.im_func.func_doc = """CreateEdgeLeftAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeLeftAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].CreateScaleHeightAttr.im_func.func_doc = """CreateScaleHeightAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetScaleHeightAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetRefineRightAttr.im_func.func_doc = """GetRefineRightAttr() -> USDRI_API UsdAttribute



Additional adjustment to the left region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PxrRodLightFilter"].GetEdgeBottomAttr.im_func.func_doc = """GetEdgeBottomAttr() -> USDRI_API UsdAttribute



Additional adjustment to the top region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].GetRefineTopAttr.im_func.func_doc = """GetRefineTopAttr() -> USDRI_API UsdAttribute



Additional adjustment to the top region.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRodLightFilter"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiPxrRodLightFilter on UsdPrim C{prim}.


Equivalent to UsdRiPxrRodLightFilter::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiPxrRodLightFilter on the prim held by C{schemaObj}.


Should be preferred over UsdRiPxrRodLightFilter (schemaObj.GetPrim()),
as it preserves SchemaBase state.

"""
   result["PxrRodLightFilter"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiPxrRodLightFilter

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

The given *path* must be an absolute prim path that doesnot contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not specify this schema class, in case a stronger typeName opinion
overrides the opinion at the current EditTarget.

"""
   result["PxrRodLightFilter"].CreateRefineTopAttr.im_func.func_doc = """CreateRefineTopAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineTopAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].CreateDepthAttr.im_func.func_doc = """CreateDepthAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDepthAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].CreateEdgeBottomAttr.im_func.func_doc = """CreateEdgeBottomAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetEdgeBottomAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].GetWidthAttr.im_func.func_doc = """GetWidthAttr() -> USDRI_API UsdAttribute



Width of the inner region of the rod (X axis).


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 1.0

"""
   result["PxrRodLightFilter"].CreateRefineBottomAttr.im_func.func_doc = """CreateRefineBottomAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRefineBottomAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRodLightFilter"].CreateWidthAttr.im_func.func_doc = """CreateWidthAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetWidthAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrIntMultLightFilter"].__doc__ = """
Multiplies the intensity of a given light.

"""
   result["PxrIntMultLightFilter"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiPxrIntMultLightFilter

stage : UsdStagePtr
path : SdfPath


Return a UsdRiPxrIntMultLightFilter holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiPxrIntMultLightFilter(stage->GetPrimAtPath(path));


"""
   result["PxrIntMultLightFilter"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PxrIntMultLightFilter"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiPxrIntMultLightFilter on UsdPrim C{prim}.


Equivalent to UsdRiPxrIntMultLightFilter::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiPxrIntMultLightFilter on the prim held by
C{schemaObj}.


Should be preferred over UsdRiPxrIntMultLightFilter
(schemaObj.GetPrim()), as it preserves SchemaBase state.

"""
   result["PxrIntMultLightFilter"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["PxrIntMultLightFilter"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiPxrIntMultLightFilter

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
   result["SplineAPI"].__doc__ = """
RiSplineAPI is a general purpose API schema used to describe a named
spline stored as a set of attributes on a prim.


It is an add-on schema that can be applied many times to a prim with
different spline names. All the attributes authored by the schema are
namespaced under "$NAME:spline:", with the name of the spline
providing a namespace for the attributes.

The spline describes a 2D piecewise cubic curve with a position and
value for each knot. This is chosen to give straightforward artistic
control over the shape. The supported basis types are:

   - linear (UsdRiTokens->linear)

   - bspline (UsdRiTokens->bspline)

   - Catmull-Rom (UsdRiTokens->catmullRom)


"""
   result["SplineAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["SplineAPI"].GetValuesAttr.im_func.func_doc = """GetValuesAttr() -> USDRI_API UsdAttribute



Values of the knots.


C++ Type: See GetValuesTypeName()  Usd Type: See GetValuesTypeName()
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["SplineAPI"].GetInterpolationAttr.im_func.func_doc = """GetInterpolationAttr() -> USDRI_API UsdAttribute



Interpolation method for the spline.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: linear  Allowed Values :
[linear, constant, bspline, catmullRom]

"""
   result["SplineAPI"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiSplineAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdRiSplineAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiSplineAPI(stage->GetPrimAtPath(path));


"""
   result["SplineAPI"].CreateInterpolationAttr.im_func.func_doc = """CreateInterpolationAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetInterpolationAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["SplineAPI"].GetPositionsAttr.im_func.func_doc = """GetPositionsAttr() -> USDRI_API UsdAttribute



Positions of the knots.


C++ Type: VtArray<float>  Usd Type: SdfValueTypeNames->FloatArray
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["SplineAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["SplineAPI"].GetValuesTypeName.im_func.func_doc = """GetValuesTypeName() -> USDRI_API SdfValueTypeName



Returns the intended typename of the values attribute of the spline.

"""
   result["SplineAPI"].CreateValuesAttr.im_func.func_doc = """CreateValuesAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetValuesAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["SplineAPI"].CreatePositionsAttr.im_func.func_doc = """CreatePositionsAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetPositionsAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["SplineAPI"].Apply.func_doc = """**static** Apply(prim) -> USDRI_API UsdRiSplineAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "RiSplineAPI" to the token-
valued, listOp metadata *apiSchemas* on the prim.

A valid UsdRiSplineAPI object is returned upon success. An invalid (or
empty) UsdRiSplineAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["SplineAPI"].Validate.im_func.func_doc = """Validate(reason) -> USDRI_API bool

reason : string


Validates the attribute values belonging to the spline.


Returns true if the spline has all valid attribute values. Returns
false and populates the C{reason} output argument if the spline has
invalid attribute values.

Here's the list of validations performed by this method:
   - the SplineAPI must be fully initialized

   - interpolation attribute must exist and use an allowed value

   - the positions array must be a float array

   - the positions array must be sorted by increasing value

   - the values array must use the correct value type

   - the positions and values array must have the same size


"""
   result["SplineAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiSplineAPI on UsdPrim C{prim}.


Equivalent to UsdRiSplineAPI::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiSplineAPI on the prim held by C{schemaObj}.


Should be preferred over UsdRiSplineAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.


----------------------------------------------------------------------
__init__(prim, splineName, valuesTypeName, doesDuplicateBSplineEndpoints)

prim : UsdPrim
splineName : TfToken
valuesTypeName : SdfValueTypeName
doesDuplicateBSplineEndpoints : bool


Construct a UsdRiSplineAPI with the given C{splineName} on the UsdPrim
C{prim}.


----------------------------------------------------------------------
__init__(schemaObj, splineName, valuesTypeName, doesDuplicateBSplineEndpoints)

schemaObj : UsdSchemaBase
splineName : TfToken
valuesTypeName : SdfValueTypeName
doesDuplicateBSplineEndpoints : bool


Construct a UsdRiSplineAPI with the given C{splineName} on the prim
held by C{schemaObj}.

"""
   result["RisBxdf"].__doc__ = """
Deprecated

Specialized RIS shader schemas have been deprecated in favor of all
shader prims being simple UsdShadeShader. Represents a ris bxdf
object. One of these is assigned at one time.

"""
   result["RisBxdf"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiRisBxdf

stage : UsdStagePtr
path : SdfPath


Return a UsdRiRisBxdf holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiRisBxdf(stage->GetPrimAtPath(path));


"""
   result["RisBxdf"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiRisBxdf on UsdPrim C{prim}.


Equivalent to UsdRiRisBxdf::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiRisBxdf on the prim held by C{schemaObj}.


Should be preferred over UsdRiRisBxdf (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["RisBxdf"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["RisBxdf"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["RisBxdf"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiRisBxdf

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
   result["StatementsAPI"].__doc__ = """
Container namespace schema for all renderman statements.



The longer term goal is for clients to go directly to primvar or
render-attribute API's, instead of using UsdRi StatementsAPI for
inherited attributes. Anticpating this, StatementsAPI can smooth the
way via a few environment variables:
   - USDRI_STATEMENTS_WRITE_NEW_ENCODING: Causes StatementsAPI to
     write attributes to primvars in the "ri:" namespace.

   - USDRI_STATEMENTS_READ_OLD_ENCODING: Causes StatementsAPI to read
     old-style attributes instead of primvars in the "ri:" namespace.


"""
   result["StatementsAPI"].MakeRiAttributePropertyName.func_doc = """**static** MakeRiAttributePropertyName(attrName) -> USDRI_API string

attrName : string


Returns the given C{attrName} prefixed with the full Ri attribute
namespace, creating a name suitable for an RiAttribute UsdProperty.


This handles conversion of common separator characters used in other
packages, such as periods and underscores.

Will return empty string if attrName is not a valid property
identifier; otherwise, will return a valid property name that
identifies the property as an RiAttribute, according to the following
rules:
   - If C{attrName} is already a properly constructed RiAttribute
     property name, return it unchanged.

   - If C{attrName} contains two or more tokens separated by a
     *colon*, consider the first to be the namespace, and the rest the
     name, joined by underscores

   - If C{attrName} contains two or more tokens separated by a
     *period*, consider the first to be the namespace, and the rest the
     name, joined by underscores

   - If C{attrName} contains two or more tokens separated by an,
     *underscore* consider the first to be the namespace, and the rest the
     name, joined by underscores

   - else, assume C{attrName} is the name, and "user" is the namespace


"""
   result["StatementsAPI"].GetModelScopedCoordinateSystems.im_func.func_doc = """GetModelScopedCoordinateSystems(targets) -> USDRI_API bool

targets : SdfPathVector


Populates the output C{targets} with the authored
ri:modelScopedCoordinateSystems, if any.


Returns true if the query was successful.

"""
   result["StatementsAPI"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiStatementsAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdRiStatementsAPI holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiStatementsAPI(stage->GetPrimAtPath(path));


"""
   result["StatementsAPI"].CreateRiAttribute.im_func.func_doc = """CreateRiAttribute(name, riType, nameSpace) -> USDRI_API UsdAttribute

name : TfToken
riType : string
nameSpace : string


Create a rib attribute on the prim to which this schema is attached.


A rib attribute consists of an attribute *"nameSpace"* and an
attribute *"name"*. For example, the namespace "cull" may define
attributes "backfacing" and "hidden", and user-defined attributes
belong to the namespace "user".

This method makes no attempt to validate that the given C{nameSpace}
and *name* are actually meaningful to prman or any other renderer.

riType

should be a known RenderMan type definition, which can be array-
valued. For instance, both "color" and "float[3]" are valid values for
C{riType}.


----------------------------------------------------------------------
CreateRiAttribute(name, tfType, nameSpace) -> USDRI_API UsdAttribute

name : TfToken
tfType : TfType
nameSpace : string


Creates an attribute of the given C{tfType}.


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["StatementsAPI"].GetRiAttributeName.func_doc = """**static** GetRiAttributeName(prop) -> TfToken

prop : UsdProperty


Return the base, most-specific name of the rib attribute.


For example, the *name* of the rib attribute "cull:backfacing" is
"backfacing"

"""
   result["StatementsAPI"].SetCoordinateSystem.im_func.func_doc = """SetCoordinateSystem(coordSysName) -> USDRI_API void

coordSysName : string


Sets the "ri:coordinateSystem" attribute to the given string value,
creating the attribute if needed.


That identifies this prim as providing a coordinate system, which can
be retrieved via UsdGeomXformable::GetTransformAttr(). Also adds the
owning prim to the ri:modelCoordinateSystems relationship targets on
its parent leaf model prim, if it exists. If this prim is not under a
leaf model, no relationship targets will be authored.

"""
   result["StatementsAPI"].GetRiAttribute.im_func.func_doc = """GetRiAttribute(name, nameSpace) -> USDRI_API UsdAttribute

name : TfToken
nameSpace : string


Return a UsdAttribute representing the Ri attribute with the name
*name*, in the namespace *nameSpace*.


The attribute returned may or may not B{actually} exist so it must be
checked for validity.

"""
   result["StatementsAPI"].GetModelCoordinateSystems.im_func.func_doc = """GetModelCoordinateSystems(targets) -> USDRI_API bool

targets : SdfPathVector


Populates the output C{targets} with the authored
ri:modelCoordinateSystems, if any.


Returns true if the query was successful.

"""
   result["StatementsAPI"].GetCoordinateSystem.im_func.func_doc = """GetCoordinateSystem() -> USDRI_API string



Returns the value in the "ri:coordinateSystem" attribute if it exists.

"""
   result["StatementsAPI"].HasCoordinateSystem.im_func.func_doc = """HasCoordinateSystem() -> USDRI_API bool



Returns true if the underlying prim has a ri:coordinateSystem opinion.

"""
   result["StatementsAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiStatementsAPI on UsdPrim C{prim}.


Equivalent to UsdRiStatementsAPI::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiStatementsAPI on the prim held by C{schemaObj}.


Should be preferred over UsdRiStatementsAPI (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["StatementsAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["StatementsAPI"].GetRiAttributes.im_func.func_doc = """GetRiAttributes(nameSpace) -> USDRI_API sequence< UsdProperty >

nameSpace : string


Return all rib attributes on this prim, or under a specific namespace
(e.g. "user").


As noted above, rib attributes can be either UsdAttribute or
UsdRelationship, and like all UsdProperties, need not have a defined
value.

"""
   result["StatementsAPI"].HasScopedCoordinateSystem.im_func.func_doc = """HasScopedCoordinateSystem() -> USDRI_API bool



Returns true if the underlying prim has a ri:scopedCoordinateSystem
opinion.

"""
   result["StatementsAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["StatementsAPI"].GetScopedCoordinateSystem.im_func.func_doc = """GetScopedCoordinateSystem() -> USDRI_API string



Returns the value in the "ri:scopedCoordinateSystem" attribute if it
exists.

"""
   result["StatementsAPI"].SetScopedCoordinateSystem.im_func.func_doc = """SetScopedCoordinateSystem(coordSysName) -> USDRI_API void

coordSysName : string


Sets the "ri:scopedCoordinateSystem" attribute to the given string
value, creating the attribute if needed.


That identifies this prim as providing a coordinate system, which can
be retrieved via UsdGeomXformable::GetTransformAttr(). Such coordinate
systems are local to the RI attribute stack state, but does get
updated properly for instances when defined inside an object master.
Also adds the owning prim to the ri:modelScopedCoordinateSystems
relationship targets on its parent leaf model prim, if it exists. If
this prim is not under a leaf model, no relationship targets will be
authored.

"""
   result["StatementsAPI"].IsRiAttribute.func_doc = """**static** IsRiAttribute(prop) -> USDRI_API bool

prop : UsdProperty


Return true if the property is in the "ri:attributes" namespace.

"""
   result["StatementsAPI"].Apply.func_doc = """**static** Apply(prim) -> USDRI_API UsdRiStatementsAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "StatementsAPI" to the token-
valued, listOp metadata *apiSchemas* on the prim.

A valid UsdRiStatementsAPI object is returned upon success. An invalid
(or empty) UsdRiStatementsAPI object is returned upon failure. See
UsdAPISchemaBase::_ApplyAPISchema() for conditions resulting in
failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["StatementsAPI"].GetRiAttributeNameSpace.func_doc = """**static** GetRiAttributeNameSpace(prop) -> USDRI_API TfToken

prop : UsdProperty


Return the containing namespace of the rib attribute (e.g. "user").

"""
   result["ConvertFromRManInterpolateBoundary"].func_doc = """ConvertFromRManInterpolateBoundary(i) -> USDRI_API  TfToken

i : int


Given the integer C{i} that corresponds to an rman enum for
interpolate boundary condition, returns the equivalent UsdGeom token.

"""
   result["RisPattern"].__doc__ = """
Deprecated

Specialized RIS shader schemas have been deprecated in favor of all
shader prims being simple UsdShadeShader. Represents a ris pattern
object. Multiple of these can be assigned.

"""
   result["RisPattern"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiRisPattern on UsdPrim C{prim}.


Equivalent to UsdRiRisPattern::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiRisPattern on the prim held by C{schemaObj}.


Should be preferred over UsdRiRisPattern (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["RisPattern"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiRisPattern

stage : UsdStagePtr
path : SdfPath


Return a UsdRiRisPattern holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiRisPattern(stage->GetPrimAtPath(path));


"""
   result["RisPattern"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["RisPattern"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["RisPattern"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiRisPattern

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
   result["RisOslPattern"].__doc__ = """
Deprecated

Specialized RIS shader schemas have been deprecated in favor of all
shader prims being simple UsdShadeShader. Represents a ris osl pattern
object.

"""
   result["RisOslPattern"].GetOslPathAttr.im_func.func_doc = """GetOslPathAttr() -> USDRI_API UsdAttribute



C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["RisOslPattern"].CreateOslPathAttr.im_func.func_doc = """CreateOslPathAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetOslPathAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RisOslPattern"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiRisOslPattern

stage : UsdStagePtr
path : SdfPath


Return a UsdRiRisOslPattern holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiRisOslPattern(stage->GetPrimAtPath(path));


"""
   result["RisOslPattern"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["RisOslPattern"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiRisOslPattern on UsdPrim C{prim}.


Equivalent to UsdRiRisOslPattern::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiRisOslPattern on the prim held by C{schemaObj}.


Should be preferred over UsdRiRisOslPattern (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["RisOslPattern"].CreateFilePathAttr.im_func.func_doc = """CreateFilePathAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFilePathAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["RisOslPattern"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["RisOslPattern"].GetFilePathAttr.im_func.func_doc = """GetFilePathAttr() -> USDRI_API UsdAttribute



C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityVarying  Fallback Value: @

"""
   result["RisOslPattern"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiRisOslPattern

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
   result["__doc__"] = """

Overview
========

This module provides schemas and utilities for authoring USD that
encodes Renderman-specific information, and for converting between USD
and Ri values and datatypes. There is no inclusion of Renderman
headers, so this schema module is compilable and useful regardless of
whether you have or use Renderman.

The primary classes are:

   - UsdRiStatements, which provides API for encoding most Renderman
     specific concepts, like Ri Attributes, and (scoped) coordinate
     systems.

   - UsdRiLookAPI, UsdRiRisBxdf and several other shading-schema-
     related classes for encoding Renderman shading interfaces and networks
     in the UsdShade shading model.

   - usdRi/rmanUtilities.h prvides usd/ri conversion utilities

   - The UsdRiPxr...LightFilter classes, representing extensions to
     the core UsdLight schemas specific to Renderman


"""
   result["PxrRampLightFilter"].__doc__ = """
A ramp to modulate how a light falls off with distance.


For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdRiTokens. So to set an attribute to the value "rightHanded", use
UsdRiTokens->rightHanded as the value.

"""
   result["PxrRampLightFilter"].GetFalloffRampEndDistanceAttr.im_func.func_doc = """GetFalloffRampEndDistanceAttr() -> USDRI_API UsdAttribute



C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 10.0

"""
   result["PxrRampLightFilter"].CreateRampModeAttr.im_func.func_doc = """CreateRampModeAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRampModeAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRampLightFilter"].GetColorRampAPI.im_func.func_doc = """GetColorRampAPI() -> USDRI_API UsdRiSplineAPI



Return the UsdRiSplineAPI interface used for examining and modifying
the color ramp.

"""
   result["PxrRampLightFilter"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiPxrRampLightFilter

stage : UsdStagePtr
path : SdfPath


Return a UsdRiPxrRampLightFilter holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiPxrRampLightFilter(stage->GetPrimAtPath(path));


"""
   result["PxrRampLightFilter"].GetFalloffRampBeginDistanceAttr.im_func.func_doc = """GetFalloffRampBeginDistanceAttr() -> USDRI_API UsdAttribute



C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["PxrRampLightFilter"].Define.func_doc = """**static** Define(stage, path) -> USDRI_API UsdRiPxrRampLightFilter

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
   result["PxrRampLightFilter"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""
   result["PxrRampLightFilter"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiPxrRampLightFilter on UsdPrim C{prim}.


Equivalent to UsdRiPxrRampLightFilter::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiPxrRampLightFilter on the prim held by C{schemaObj}.


Should be preferred over UsdRiPxrRampLightFilter
(schemaObj.GetPrim()), as it preserves SchemaBase state.

"""
   result["PxrRampLightFilter"].CreateFalloffRampEndDistanceAttr.im_func.func_doc = """CreateFalloffRampEndDistanceAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFalloffRampEndDistanceAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["PxrRampLightFilter"].GetRampModeAttr.im_func.func_doc = """GetRampModeAttr() -> USDRI_API UsdAttribute



Specifies the direction in which the ramp is applied.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: distanceToLight  Allowed Values
: [distanceToLight, linear, spherical, radial]

"""
   result["PxrRampLightFilter"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["PxrRampLightFilter"].GetFalloffRampAPI.im_func.func_doc = """GetFalloffRampAPI() -> USDRI_API UsdRiSplineAPI



Return the UsdRiSplineAPI interface used for examining and modifying
the falloff ramp.

"""
   result["PxrRampLightFilter"].CreateFalloffRampBeginDistanceAttr.im_func.func_doc = """CreateFalloffRampBeginDistanceAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetFalloffRampBeginDistanceAttr() , and also Create vs Get
Property Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightFilterAPI"].__doc__ = """
Renderman-specific attributes for light filters.


For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdRiTokens. So to set an attribute to the value "rightHanded", use
UsdRiTokens->rightHanded as the value.

"""
   result["LightFilterAPI"].CreateRiCombineModeAttr.im_func.func_doc = """CreateRiCombineModeAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiCombineModeAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightFilterAPI"].CreateRiDensityAttr.im_func.func_doc = """CreateRiDensityAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiDensityAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightFilterAPI"].GetRiDensityAttr.im_func.func_doc = """GetRiDensityAttr() -> USDRI_API UsdAttribute



Scales the strength of the filter.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightFilterAPI"].CreateRiExposureAttr.im_func.func_doc = """CreateRiExposureAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiExposureAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightFilterAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDRI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["LightFilterAPI"].Get.func_doc = """**static** Get(stage, path) -> USDRI_API UsdRiLightFilterAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdRiLightFilterAPI holding the prim adhering to this schema
at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdRiLightFilterAPI(stage->GetPrimAtPath(path));


"""
   result["LightFilterAPI"].CreateRiSpecularAttr.im_func.func_doc = """CreateRiSpecularAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiSpecularAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightFilterAPI"].CreateRiDiffuseAttr.im_func.func_doc = """CreateRiDiffuseAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiDiffuseAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightFilterAPI"].GetRiDiffuseAttr.im_func.func_doc = """GetRiDiffuseAttr() -> USDRI_API UsdAttribute



A multiplier for the effect of this light on the diffuse response of
materials.


This is a non-physical control.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightFilterAPI"].GetRiExposureAttr.im_func.func_doc = """GetRiExposureAttr() -> USDRI_API UsdAttribute



Exposure control for the multiplier.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: 0.0

"""
   result["LightFilterAPI"].GetRiInvertAttr.im_func.func_doc = """GetRiInvertAttr() -> USDRI_API UsdAttribute



When true, inverts the output of the light filter.


C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightFilterAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdRiLightFilterAPI on UsdPrim C{prim}.


Equivalent to UsdRiLightFilterAPI::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdRiLightFilterAPI on the prim held by C{schemaObj}.


Should be preferred over UsdRiLightFilterAPI (schemaObj.GetPrim()), as
it preserves SchemaBase state.

"""
   result["LightFilterAPI"].GetRiIntensityAttr.im_func.func_doc = """GetRiIntensityAttr() -> USDRI_API UsdAttribute



Multipier for the diffuse and specular result.


C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightFilterAPI"].GetRiCombineModeAttr.im_func.func_doc = """GetRiCombineModeAttr() -> USDRI_API UsdAttribute



Specifies how this filter combines with others.


Valid values are:

   - multiply: The results of filters are multiplied together

   - max: The maximum result of the filters is used. This works best
     for grey-scale filters.

   - min: The minimum result of the filters is used. This works best
     for grey-scale filters.

   - screen: Similar to max, but combines gradients in a smoother way
     by using a screen operation: screen(a,b) = 1-(1-a)(1-b) This works
     best for grey-scale filters.

Light filters on a light are grouped by their combine mode. Each group
is executed and combined using that mode. Then, the final results of
each group are multiplied together.

Fallback: multiply

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback  Allowed Values :
[multiply, max, min, screen]

"""
   result["LightFilterAPI"].GetRiSpecularAttr.im_func.func_doc = """GetRiSpecularAttr() -> USDRI_API UsdAttribute



A multiplier for the effect of this light on the specular response of
materials.


This is a non-physical control.

C++ Type: float  Usd Type: SdfValueTypeNames->Float  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["LightFilterAPI"].CreateRiIntensityAttr.im_func.func_doc = """CreateRiIntensityAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiIntensityAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightFilterAPI"].Apply.func_doc = """**static** Apply(prim) -> USDRI_API UsdRiLightFilterAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "RiLightFilterAPI" to the token-
valued, listOp metadata *apiSchemas* on the prim.

A valid UsdRiLightFilterAPI object is returned upon success. An
invalid (or empty) UsdRiLightFilterAPI object is returned upon
failure. See UsdAPISchemaBase::_ApplyAPISchema() for conditions
resulting in failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["LightFilterAPI"].CreateRiInvertAttr.im_func.func_doc = """CreateRiInvertAttr(defaultValue, writeSparsely) -> USDRI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetRiInvertAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["LightFilterAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDRI_API  TfType


"""