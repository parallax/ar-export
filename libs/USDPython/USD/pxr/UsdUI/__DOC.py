def Execute(result):
   result["SceneGraphPrimAPI"].__doc__ = """
Utility schema for display properties of a prim.


For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdUITokens. So to set an attribute to the value "rightHanded", use
UsdUITokens->rightHanded as the value.

"""
   result["SceneGraphPrimAPI"].GetDisplayNameAttr.im_func.func_doc = """GetDisplayNameAttr() -> USDUI_API UsdAttribute



When publishing a nodegraph or a material, it can be useful to provide
an optional display name, for readability.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["SceneGraphPrimAPI"].Get.func_doc = """**static** Get(stage, path) -> USDUI_API UsdUISceneGraphPrimAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdUISceneGraphPrimAPI holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdUISceneGraphPrimAPI(stage->GetPrimAtPath(path));


"""
   result["SceneGraphPrimAPI"].CreateDisplayNameAttr.im_func.func_doc = """CreateDisplayNameAttr(defaultValue, writeSparsely) -> USDUI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDisplayNameAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["SceneGraphPrimAPI"].CreateDisplayGroupAttr.im_func.func_doc = """CreateDisplayGroupAttr(defaultValue, writeSparsely) -> USDUI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDisplayGroupAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["SceneGraphPrimAPI"].GetDisplayGroupAttr.im_func.func_doc = """GetDisplayGroupAttr() -> USDUI_API UsdAttribute



When publishing a nodegraph or a material, it can be useful to provide
an optional display group, for organizational purposes and
readability.


This is because often the usd shading hierarchy is rather flat while
we want to display it in organized groups.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["SceneGraphPrimAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdUISceneGraphPrimAPI on UsdPrim C{prim}.


Equivalent to UsdUISceneGraphPrimAPI::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdUISceneGraphPrimAPI on the prim held by C{schemaObj}.


Should be preferred over UsdUISceneGraphPrimAPI (schemaObj.GetPrim()),
as it preserves SchemaBase state.

"""
   result["SceneGraphPrimAPI"].Apply.func_doc = """**static** Apply(prim) -> USDUI_API UsdUISceneGraphPrimAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "SceneGraphPrimAPI" to the token-
valued, listOp metadata *apiSchemas* on the prim.

A valid UsdUISceneGraphPrimAPI object is returned upon success. An
invalid (or empty) UsdUISceneGraphPrimAPI object is returned upon
failure. See UsdAPISchemaBase::_ApplyAPISchema() for conditions
resulting in failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["SceneGraphPrimAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDUI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["SceneGraphPrimAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDUI_API  TfType


"""
   result["NodeGraphNodeAPI"].__doc__ = """
This api helps storing information about nodes in node graphs.


For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdUITokens. So to set an attribute to the value "rightHanded", use
UsdUITokens->rightHanded as the value.

"""
   result["NodeGraphNodeAPI"].CreateSizeAttr.im_func.func_doc = """CreateSizeAttr(defaultValue, writeSparsely) -> USDUI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSizeAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NodeGraphNodeAPI"].GetDisplayColorAttr.im_func.func_doc = """GetDisplayColorAttr() -> USDUI_API UsdAttribute



This hint defines what tint the node should have in the node graph.


C++ Type: GfVec3f  Usd Type: SdfValueTypeNames->Color3f  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["NodeGraphNodeAPI"].GetExpansionStateAttr.im_func.func_doc = """GetExpansionStateAttr() -> USDUI_API UsdAttribute



The current expansionState of the node in the ui.


'open' = fully expanded 'closed' = fully collapsed 'minimized' =
should take the least space possible

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback  Allowed Values :
[open, closed, minimized]

"""
   result["NodeGraphNodeAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdUINodeGraphNodeAPI on UsdPrim C{prim}.


Equivalent to UsdUINodeGraphNodeAPI::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdUINodeGraphNodeAPI on the prim held by C{schemaObj}.


Should be preferred over UsdUINodeGraphNodeAPI (schemaObj.GetPrim()),
as it preserves SchemaBase state.

"""
   result["NodeGraphNodeAPI"].CreateDisplayColorAttr.im_func.func_doc = """CreateDisplayColorAttr(defaultValue, writeSparsely) -> USDUI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDisplayColorAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NodeGraphNodeAPI"].CreateStackingOrderAttr.im_func.func_doc = """CreateStackingOrderAttr(defaultValue, writeSparsely) -> USDUI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetStackingOrderAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NodeGraphNodeAPI"].Get.func_doc = """**static** Get(stage, path) -> USDUI_API UsdUINodeGraphNodeAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdUINodeGraphNodeAPI holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdUINodeGraphNodeAPI(stage->GetPrimAtPath(path));


"""
   result["NodeGraphNodeAPI"].GetSizeAttr.im_func.func_doc = """GetSizeAttr() -> USDUI_API UsdAttribute



Optional size hint for a node in a node graph.


X is the width. Y is the height.

This value is optional, because node size is often determined based on
the number of in- and outputs of a node.

C++ Type: GfVec2f  Usd Type: SdfValueTypeNames->Float2  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["NodeGraphNodeAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDUI_API  TfType


"""
   result["NodeGraphNodeAPI"].GetStackingOrderAttr.im_func.func_doc = """GetStackingOrderAttr() -> USDUI_API UsdAttribute



This optional value is a useful hint when an application cares about
the visibility of a node and whether each node overlaps another.


Nodes with lower stacking order values are meant to be drawn below
higher ones. Negative values are meant as background. Positive values
are meant as foreground. Undefined values should be treated as 0.

There are no set limits in these values.

C++ Type: int  Usd Type: SdfValueTypeNames->Int  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["NodeGraphNodeAPI"].CreatePosAttr.im_func.func_doc = """CreatePosAttr(defaultValue, writeSparsely) -> USDUI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetPosAttr() , and also Create vs Get Property Methods for when to
use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NodeGraphNodeAPI"].CreateExpansionStateAttr.im_func.func_doc = """CreateExpansionStateAttr(defaultValue, writeSparsely) -> USDUI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetExpansionStateAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NodeGraphNodeAPI"].GetIconAttr.im_func.func_doc = """GetIconAttr() -> USDUI_API UsdAttribute



This points to an image that should be displayed on the node.


C++ Type: SdfAssetPath  Usd Type: SdfValueTypeNames->Asset
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["NodeGraphNodeAPI"].CreateIconAttr.im_func.func_doc = """CreateIconAttr(defaultValue, writeSparsely) -> USDUI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetIconAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["NodeGraphNodeAPI"].Apply.func_doc = """**static** Apply(prim) -> USDUI_API UsdUINodeGraphNodeAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "NodeGraphNodeAPI" to the token-
valued, listOp metadata *apiSchemas* on the prim.

A valid UsdUINodeGraphNodeAPI object is returned upon success. An
invalid (or empty) UsdUINodeGraphNodeAPI object is returned upon
failure. See UsdAPISchemaBase::_ApplyAPISchema() for conditions
resulting in failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["NodeGraphNodeAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDUI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["NodeGraphNodeAPI"].GetPosAttr.im_func.func_doc = """GetPosAttr() -> USDUI_API UsdAttribute



Declared relative position to the parent in a node graph.


X is the horizontal position. Y is the vertical position. Higher
numbers correspond to lower positions (coordinates are Qt style, not
cartesian).

These positions are not explicitly meant in pixel space, but rather
assume that the size of a node is approximately 1.0x1.0. Where size-x
is the node width and size-y height of the node. Depending on graph UI
implementation, the size of a node may vary in each direction.

Example: If a node's width is 300 and it is position is at 1000, we
store for x-position: 1000 * (1.0/300)

C++ Type: GfVec2f  Usd Type: SdfValueTypeNames->Float2  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["Backdrop"].__doc__ = """
Provides a 'group-box' for the purpose of node graph organization.


Unlike containers, backdrops do not store the Shader nodes inside of
them. Backdrops are an organizational tool that allows Shader nodes to
be visually grouped together in a node-graph UI, but there is no
direct relationship between a Shader node and a Backdrop.

The guideline for a node-graph UI is that a Shader node is considered
part of a Backdrop when the Backdrop is the smallest Backdrop a Shader
node's bounding-box fits inside.

Backdrop objects are contained inside a NodeGraph, similar to how
Shader objects are contained inside a NodeGraph.

Backdrops have no shading inputs or outputs that influence the
rendered results of a NodeGraph. Therefore they can be safely ignored
during import.

Like Shaders and NodeGraphs, Backdrops subscribe to the
NodeGraphNodeAPI to specify position and size.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdUITokens. So to set an attribute to the value "rightHanded", use
UsdUITokens->rightHanded as the value.

"""
   result["Backdrop"].GetDescriptionAttr.im_func.func_doc = """GetDescriptionAttr() -> USDUI_API UsdAttribute



The text label that is displayed on the backdrop in the node graph.


This help-description explains what the nodes in a backdrop do.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["Backdrop"].Get.func_doc = """**static** Get(stage, path) -> USDUI_API UsdUIBackdrop

stage : UsdStagePtr
path : SdfPath


Return a UsdUIBackdrop holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdUIBackdrop(stage->GetPrimAtPath(path));


"""
   result["Backdrop"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDUI_API  TfType


"""
   result["Backdrop"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdUIBackdrop on UsdPrim C{prim}.


Equivalent to UsdUIBackdrop::Get (prim.GetStage(), prim.GetPath()) for
a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdUIBackdrop on the prim held by C{schemaObj}.


Should be preferred over UsdUIBackdrop (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Backdrop"].CreateDescriptionAttr.im_func.func_doc = """CreateDescriptionAttr(defaultValue, writeSparsely) -> USDUI_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDescriptionAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Backdrop"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDUI_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Backdrop"].Define.func_doc = """**static** Define(stage, path) -> USDUI_API UsdUIBackdrop

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