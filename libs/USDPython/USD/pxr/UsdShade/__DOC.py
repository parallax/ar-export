def Execute(result):
   result["ConnectableAPI"].__doc__ = """
UsdShadeConnectableAPI is an API schema that provides a common
interface for creating outputs and making connections between shading
parameters and outputs.


The interface is common to all UsdShade schemas that support Inputs
and Outputs, which currently includes UsdShadeShader,
UsdShadeNodeGraph, and UsdShadeMaterial.

One can construct a UsdShadeConnectableAPI directly from a UsdPrim, or
from objects of any of the schema classes listed above. If it seems
onerous to need to construct a secondary schema object to interact
with Inputs and Outputs, keep in mind that any function whose purpose
is either to walk material/shader networks via their connections, or
to create such networks, can typically be written entirely in terms of
UsdShadeConnectableAPI objects, without needing to care what the
underlying prim type is.

Additionally, the most common UsdShadeConnectableAPI behaviors
(creating Inputs and Outputs, and making connections) are wrapped as
convenience methods on the prim schema classes (creation) and
UsdShadeInput and UsdShadeOutput.

"""
   result["ConnectableAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdShadeConnectableAPI on UsdPrim C{prim}.


Equivalent to UsdShadeConnectableAPI::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdShadeConnectableAPI on the prim held by C{schemaObj}.


Should be preferred over UsdShadeConnectableAPI (schemaObj.GetPrim()),
as it preserves SchemaBase state.


----------------------------------------------------------------------
__init__(shader)

shader : Shader


Constructor that takes a UsdShadeShader.


Allow implicit (auto) conversion of UsdShadeShader to
UsdShadeConnectableAPI, so that a shader can be passed into any
function that accepts a ConnectableAPI.


----------------------------------------------------------------------
__init__(nodeGraph)

nodeGraph : NodeGraph


Constructor that takes a UsdShadeNodeGraph.


Allow implicit (auto) conversion of UsdShadeNodeGraph to
UsdShadeConnectableAPI, so that a nodegraph can be passed into any
function that accepts a ConnectableAPI.

"""
   result["ConnectableAPI"].GetOutputs.im_func.func_doc = """GetOutputs() -> USDSHADE_API sequence< UsdShadeOutput >



Returns all outputs on the connectable prim (i.e.


shader or node-graph). Outputs are represented by attributes in the
"outputs:" namespace.

"""
   result["ConnectableAPI"].ConnectToSource.func_doc = """**static** ConnectToSource(shadingProp, source, sourceName, sourceType, typeName) -> USDSHADE_API bool

shadingProp : UsdProperty
source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType
typeName : SdfValueTypeName


Authors a connection for a given shading property C{shadingProp}.


C{shadingProp} can represent a parameter, an interface attribute, an
input or an output. C{sourceName} is the name of the shading property
that is the target of the connection. This excludes any namespace
prefix that determines the type of the source (eg, output or interface
attribute). C{sourceType} is used to indicate the type of the shading
property that is the target of the connection. The source type is used
to determine the namespace prefix that must be attached to
C{sourceName} to determine the source full property name. C{typeName}
if specified, is the typename of the attribute to create on the source
if it doesn't exist. It is also used to validate whether the types of
the source and consumer of the connection are compatible. C{source} is
the connectable prim that produces or contains a value for the given
shading property.

C{true} if a connection was created successfully. C{false} if
C{shadingProp} or C{source} is invalid.

This method does not verify the connectability of the shading property
to the source. Clients must invoke CanConnect() themselves to ensure
compatibility.

The source shading property is created if it doesn't exist already.


----------------------------------------------------------------------
ConnectToSource(input, source, sourceName, sourceType, typeName) -> USDSHADE_API bool

input : Input
source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType
typeName : SdfValueTypeName


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ConnectToSource(output, source, sourceName, sourceType, typeName) -> USDSHADE_API bool

output : Output
source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType
typeName : SdfValueTypeName


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ConnectToSource(shadingProp, sourcePath) -> USDSHADE_API bool

shadingProp : UsdProperty
sourcePath : SdfPath


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

Connect the given shading property to the source at path,
C{sourcePath}.


C{sourcePath} should be the fully namespaced property path.

This overload is provided for convenience, for use in contexts where
the prim types are unknown or unavailable.


----------------------------------------------------------------------
ConnectToSource(input, sourcePath) -> USDSHADE_API bool

input : Input
sourcePath : SdfPath


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ConnectToSource(output, sourcePath) -> USDSHADE_API bool

output : Output
sourcePath : SdfPath


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ConnectToSource(shadingProp, sourceInput) -> USDSHADE_API bool

shadingProp : UsdProperty
sourceInput : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

Connect the given shading property to the given source input.


----------------------------------------------------------------------
ConnectToSource(input, sourceInput) -> USDSHADE_API bool

input : Input
sourceInput : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ConnectToSource(output, sourceInput) -> USDSHADE_API bool

output : Output
sourceInput : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ConnectToSource(shadingProp, sourceOutput) -> USDSHADE_API bool

shadingProp : UsdProperty
sourceOutput : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

Connect the given shading property to the given source output.


----------------------------------------------------------------------
ConnectToSource(input, sourceOutput) -> USDSHADE_API bool

input : Input
sourceOutput : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ConnectToSource(output, sourceOutput) -> USDSHADE_API bool

output : Output
sourceOutput : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ConnectableAPI"].Get.func_doc = """**static** Get(stage, path) -> USDSHADE_API UsdShadeConnectableAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdShadeConnectableAPI holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdShadeConnectableAPI(stage->GetPrimAtPath(path));


"""
   result["ConnectableAPI"].GetOutput.im_func.func_doc = """GetOutput(name) -> USDSHADE_API UsdShadeOutput

name : TfToken


Return the requested output if it exists.


C{name} is the unnamespaced base name.

"""
   result["ConnectableAPI"].GetInput.im_func.func_doc = """GetInput(name) -> USDSHADE_API UsdShadeInput

name : TfToken


Return the requested input if it exists.


C{name} is the unnamespaced base name.

"""
   result["ConnectableAPI"].IsSourceConnectionFromBaseMaterial.func_doc = """**static** IsSourceConnectionFromBaseMaterial(shadingProp) -> USDSHADE_API bool

shadingProp : UsdProperty


Returns true if the connection to the given shading property's source,
as returned by UsdShadeConnectableAPI::GetConnectedSource() , is
authored across a specializes arc, which is used to denote a base
material.


----------------------------------------------------------------------
IsSourceConnectionFromBaseMaterial(input) -> USDSHADE_API bool

input : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
IsSourceConnectionFromBaseMaterial(output) -> USDSHADE_API bool

output : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ConnectableAPI"].CreateInput.im_func.func_doc = """CreateInput(name, typeName) -> USDSHADE_API UsdShadeInput

name : TfToken
typeName : SdfValueTypeName


Create an input which can both have a value and be connected.


The attribute representing the input is created in the "inputs:"
namespace.

"""
   result["ConnectableAPI"].HasConnectedSource.func_doc = """**static** HasConnectedSource(shadingProp) -> USDSHADE_API bool

shadingProp : UsdProperty


Returns true if and only if the shading property is currently
connected to a valid (defined) source.


If you will be calling GetConnectedSource() afterwards anyways, it
will be *much* faster to instead guard like so: ::

  if (UsdShadeConnectableAPI::GetConnectedSource(property, 
&
source, 
          
& sourceName,  &
sourceType)){
       // process connected property
  } else {
       // process unconnected property
  }



----------------------------------------------------------------------
HasConnectedSource(input) -> USDSHADE_API bool

input : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
HasConnectedSource(output) -> USDSHADE_API bool

output : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ConnectableAPI"].DisconnectSource.func_doc = """**static** DisconnectSource(shadingProp) -> USDSHADE_API bool

shadingProp : UsdProperty


Disconnect source for this shading property.


This may author more scene description than you might expect - we
define the behavior of disconnect to be that, even if a shading
property becomes connected in a weaker layer than the current
UsdEditTarget, the property will *still* be disconnected in the
composition, therefore we must "block" it (see for e.g.
UsdRelationship::BlockTargets() ) in the current UsdEditTarget.

ConnectToSource() .


----------------------------------------------------------------------
DisconnectSource(input) -> USDSHADE_API bool

input : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
DisconnectSource(output) -> USDSHADE_API bool

output : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ConnectableAPI"].GetConnectedSource.func_doc = """**static** GetConnectedSource(shadingProp, source, sourceName, sourceType) -> USDSHADE_API bool

shadingProp : UsdProperty
source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType


Finds the source of a connection for the given shading property.


C{shadingProp} is the input shading property which is typically an
attribute, but can be a relationship in the case of a terminal on a
material. C{source} is an output parameter which will be set to the
source connectable prim. C{sourceName} will be set to the name of the
source shading property, which could be the parameter name, output
name or the interface attribute name. This does not include the
namespace prefix associated with the source type. C{sourceType} will
have the type of the source shading property.

C{true} if the shading property is connected to a valid, defined
source. C{false} if the shading property is not connected to a single,
valid source.

The python wrapping for this method returns a (source, sourceName,
sourceType) tuple if the parameter is connected, else C{None}


----------------------------------------------------------------------
GetConnectedSource(input, source, sourceName, sourceType) -> USDSHADE_API bool

input : Input
source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
GetConnectedSource(output, source, sourceName, sourceType) -> USDSHADE_API bool

output : Output
source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ConnectableAPI"].GetRawConnectedSourcePaths.func_doc = """**static** GetRawConnectedSourcePaths(shadingProp, sourcePaths) -> USDSHADE_API bool

shadingProp : UsdProperty
sourcePaths : SdfPathVector


Returns the "raw" (authored) connected source paths for the given
shading property.


----------------------------------------------------------------------
GetRawConnectedSourcePaths(input, sourcePaths) -> USDSHADE_API bool

input : Input
sourcePaths : SdfPathVector


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
GetRawConnectedSourcePaths(output, sourcePaths) -> USDSHADE_API bool

output : Output
sourcePaths : SdfPathVector


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ConnectableAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSHADE_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["ConnectableAPI"].ClearSource.func_doc = """**static** ClearSource(shadingProp) -> USDSHADE_API bool

shadingProp : UsdProperty


Clears source for this shading property in the current UsdEditTarget.


Most of the time, what you probably want is DisconnectSource() rather
than this function.

DisconnectSource()


----------------------------------------------------------------------
ClearSource(input) -> USDSHADE_API bool

input : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
ClearSource(output) -> USDSHADE_API bool

output : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ConnectableAPI"].IsNodeGraph.im_func.func_doc = """IsNodeGraph() -> USDSHADE_API bool



Returns true if the prim is a node-graph.

"""
   result["ConnectableAPI"].CanConnect.func_doc = """**static** CanConnect(input, source) -> USDSHADE_API bool

input : Input
source : UsdAttribute


Determines whether the given input can be connected to the given
source attribute, which can be an input or an output.


The result depends on the "connectability" of the input and the source
attributes.

UsdShadeInput::SetConnectability

UsdShadeInput::GetConnectability


----------------------------------------------------------------------
CanConnect(input, sourceInput) -> USDSHADE_API bool

input : Input
sourceInput : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CanConnect(input, sourceOutput) -> USDSHADE_API bool

input : Input
sourceOutput : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CanConnect(output, source) -> USDSHADE_API bool

output : Output
source : UsdAttribute


Determines whether the given output can be connected to the given
source attribute, which can be an input or an output.


An output is considered to be connectable only if it belongs to a
node-graph. Shader outputs are not connectable.

C{source} is an optional argument. If a valid UsdAttribute is supplied
for it, this method will return true only if the source attribute is
owned by a descendant of the node-graph owning the output.


----------------------------------------------------------------------
CanConnect(output, sourceInput) -> USDSHADE_API bool

output : Output
sourceInput : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CanConnect(output, sourceOutput) -> USDSHADE_API bool

output : Output
sourceOutput : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["ConnectableAPI"].IsShader.im_func.func_doc = """IsShader() -> USDSHADE_API bool



Returns true if the prim is a shader.

"""
   result["ConnectableAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSHADE_API  TfType


"""
   result["ConnectableAPI"].GetInputs.im_func.func_doc = """GetInputs() -> USDSHADE_API sequence< UsdShadeInput >



Returns all inputs on the connectable prim (i.e.


shader or node-graph). Inputs are represented by attributes in the
"inputs:" namespace.

"""
   result["ConnectableAPI"].CreateOutput.im_func.func_doc = """CreateOutput(name, typeName) -> USDSHADE_API UsdShadeOutput

name : TfToken
typeName : SdfValueTypeName


Create an output, which represents and externally computed, typed
value.


Outputs on node-graphs can be connected.

The attribute representing an output is created in the "outputs:"
namespace.

"""
   result["Output"].__doc__ = """
This class encapsulates a shader or node-graph output, which is a
connectable property representing a typed, externally computed value.

"""
   result["Output"].GetProperty.im_func.func_doc = """GetProperty() -> UsdProperty



Explicit UsdProperty extractor.

"""
   result["Output"].SetRenderType.im_func.func_doc = """SetRenderType(renderType) -> USDSHADE_API bool

renderType : TfToken


Specify an alternative, renderer-specific type to use when
emitting/translating this output, rather than translating based on its
GetTypeName()


For example, we set the renderType to "struct" for outputs that are of
renderman custom struct types.

true on success

"""
   result["Output"].GetPrim.im_func.func_doc = """GetPrim() -> UsdPrim



Get the prim that the output belongs to.

"""
   result["Output"].GetTypeName.im_func.func_doc = """GetTypeName() -> USDSHADE_API SdfValueTypeName



Get the "scene description" value type name of the attribute
associated with the output.



If this is an output belonging to a terminal on a material, which does
not have an associated attribute, we return 'Token' as the type.

"""
   result["Output"].ConnectToSource.im_func.func_doc = """ConnectToSource(source, sourceName, sourceType, typeName) -> USDSHADE_API bool

source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType
typeName : SdfValueTypeName


Authors a connection for this Output to the source described by the
following three elements: C{source}, the connectable owning the
source, C{sourceName}, the name of the source and C{sourceType}, the
value type of the source shading attribute.


C{typeName} if specified, is the typename of the attribute to create
on the source if it doesn't exist. It is also used to validate whether
the types of the source and consumer of the connection are compatible.

UsdShadeConnectableAPI::ConnectToSource


----------------------------------------------------------------------
ConnectToSource(sourcePath) -> USDSHADE_API bool

sourcePath : SdfPath


Authors a connection for this Output to the source at the given path.



UsdShadeConnectableAPI::ConnectToSource


----------------------------------------------------------------------
ConnectToSource(sourceInput) -> USDSHADE_API bool

sourceInput : Input


Connects this Output to the given input, C{sourceInput}.



UsdShadeConnectableAPI::ConnectToSource


----------------------------------------------------------------------
ConnectToSource(sourceOutput) -> USDSHADE_API bool

sourceOutput : Output


Connects this Output to the given output, C{sourceOutput}.



UsdShadeConnectableAPI::ConnectToSource

"""
   result["Output"].__init__.im_func.func_doc = """__init__(attr) -> USDSHADE_API

attr : UsdAttribute


Speculative constructor that will produce a valid UsdShadeOutput when
C{attr} already represents a shade Output, and produces an *invalid*
UsdShadeOutput otherwise (i.e.


unspecified-bool-type() will return false).


----------------------------------------------------------------------
__init__()



Default constructor returns an invalid Output.


Exists for container classes


----------------------------------------------------------------------
__init__(prim, name, typeName)

prim : UsdPrim
name : TfToken
typeName : SdfValueTypeName


----------------------------------------------------------------------
__init__(rel) -> USDSHADE_API

rel : UsdRelationship


----------------------------------------------------------------------
__init__(prop)

prop : UsdProperty

"""
   result["Output"].GetAttr.im_func.func_doc = """GetAttr() -> UsdAttribute



Explicit UsdAttribute extractor.

"""
   result["Output"].GetRel.im_func.func_doc = """GetRel() -> UsdRelationship



Explicit UsdRelationship extractor.

"""
   result["Output"].IsSourceConnectionFromBaseMaterial.im_func.func_doc = """IsSourceConnectionFromBaseMaterial() -> USDSHADE_API bool



Returns true if the connection to this Output's source, as returned by
GetConnectedSource() , is authored across a specializes arc, which is
used to denote a base material.



UsdShadeConnectableAPI::IsSourceConnectionFromBaseMaterial

"""
   result["Output"].GetRenderType.im_func.func_doc = """GetRenderType() -> USDSHADE_API TfToken



Return this output's specialized renderType, or an empty token if none
was authored.



SetRenderType()

"""
   result["Output"].HasConnectedSource.im_func.func_doc = """HasConnectedSource() -> USDSHADE_API bool



Returns true if and only if this Output is currently connected to a
valid (defined) source.



UsdShadeConnectableAPI::HasConnectedSource

"""
   result["Output"].DisconnectSource.im_func.func_doc = """DisconnectSource() -> USDSHADE_API bool



Disconnect source for this Output.



UsdShadeConnectableAPI::DisconnectSource

"""
   result["Output"].GetConnectedSource.im_func.func_doc = """GetConnectedSource(source, sourceName, sourceType) -> USDSHADE_API bool

source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType


Finds the source of a connection for this Output.


C{source} is an output parameter which will be set to the source
connectable prim. C{sourceName} will be set to the name of the source
shading property, which could be the parameter name, output name or
the interface attribute name. This does not include the namespace
prefix associated with the source type. C{sourceType} will have the
value type of the source shading property.

C{true} if this Input is connected to a valid, defined source.
C{false} if this Input is not connected to a single, valid source.

The python wrapping for this method returns a (source, sourceName,
sourceType) tuple if the parameter is connected, else C{None}

UsdShadeConnectableAPI::GetConnectedSource

"""
   result["Output"].GetRawConnectedSourcePaths.im_func.func_doc = """GetRawConnectedSourcePaths(sourcePaths) -> USDSHADE_API bool

sourcePaths : SdfPathVector


Returns the "raw" (authored) connected source paths for this Output.



UsdShadeConnectableAPI::GetRawConnectedSourcePaths

"""
   result["Output"].ClearSource.im_func.func_doc = """ClearSource() -> USDSHADE_API bool



Clears source for this shading property in the current UsdEditTarget.


Most of the time, what you probably want is DisconnectSource() rather
than this function.

UsdShadeConnectableAPI::ClearSource

"""
   result["Output"].Set.im_func.func_doc = """Set(value, time) -> USDSHADE_API bool

value : VtValue
time : UsdTimeCode


Set a value for the output.


It's unusual to be setting a value on an output since it represents an
externally computed value. The Set API is provided here just for the
sake of completeness and uniformity with other property schema.


----------------------------------------------------------------------
Set(value, time) -> bool

value : T
time : UsdTimeCode


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Set the attribute value of the Output at C{time}.

"""
   result["Output"].CanConnect.im_func.func_doc = """CanConnect(source) -> USDSHADE_API bool

source : UsdAttribute


Determines whether this Output can be connected to the given source
attribute, which can be an input or an output.


An output is considered to be connectable only if it belongs to a
node-graph. Shader outputs are not connectable.

UsdShadeConnectableAPI::CanConnect


----------------------------------------------------------------------
CanConnect(sourceInput) -> USDSHADE_API bool

sourceInput : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CanConnect(sourceOutput) -> USDSHADE_API bool

sourceOutput : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Output"].GetBaseName.im_func.func_doc = """GetBaseName() -> USDSHADE_API TfToken



Returns the name of the output.


We call this the base name since it strips off the "outputs:"
namespace prefix from the attribute name, and returns it.

This simply returns the full property name if the Output represents a
terminal on a material.

"""
   result["Output"].HasRenderType.im_func.func_doc = """HasRenderType() -> USDSHADE_API bool



Return true if a renderType has been specified for this output.



SetRenderType()

"""
   result["Output"].GetFullName.im_func.func_doc = """GetFullName() -> TfToken



Get the name of the attribute associated with the output.



Returns the relationship name if it represents a terminal on a
material.

"""
   result["AttributeType"].__doc__ = """
Specifies the type of a shading attribute.


"Parameter" and "InterfaceAttribute" are deprecated shading attribute
types.

"""
   result["Material"].__doc__ = """
A Material provides a container into which multiple "render targets"
can add data that defines a "shading material" for a renderer.


Typically this consists of one or more UsdRelationship properties that
target other prims of type *Shader* - though a target/client is free
to add any data that is suitable. We B{strongly advise} that all
targets adopt the convention that all properties be prefixed with a
namespace that identifies the target, e.g. "rel ri:surface
=</Shaders/mySurf>".

Binding Materials
=================

In the UsdShading model, geometry expresses a binding to a single
Material or to a set of Materials partitioned by UsdGeomSubsets
defined beneath the geometry; it is legal to bind a Material at the
root (or other sub-prim) of a model, and then bind a different
Material to individual gprims, but the meaning of inheritance and
"ancestral overriding" of Material bindings is left to each render-
target to determine. Since UsdGeom has no concept of shading, we
provide the API for binding and unbinding geometry on the API schema
UsdShadeMaterialBindingAPI.

Material Variation
==================

The entire power of USD VariantSets and all the other composition
operators can leveraged when encoding shading variation.
UsdShadeMaterial provides facilities for a particular way of building
"Material variants" in which neither the identity of the Materials
themselves nor the geometry Material-bindings need to change - instead
we vary the targeted networks, interface values, and even parameter
values within a single variantSet.  See Authoring Material Variations
for more details.

Materials Encapsulate their Networks in Namespace
=================================================

UsdShade requires that all of the shaders that "belong" to the
Material live under the Material in namespace. This supports powerful,
easy reuse of Materials, because it allows us to *reference* a
Material from one asset (the asset might be a module of Materials)
into another asset: USD references compose all descendant prims of the
reference target into the referencer's namespace, which means that all
of the referenced Material's shader networks will come along with the
Material. When referenced in this way, Materials can also be
instanced, for ease of deduplication and compactness. Finally,
Material encapsulation also allows us to specialize child materials
from parent materials.

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdShadeTokens. So to set an attribute to the value "rightHanded",
use UsdShadeTokens->rightHanded as the value.

"""
   result["Material"].Get.func_doc = """**static** Get(stage, path) -> USDSHADE_API UsdShadeMaterial

stage : UsdStagePtr
path : SdfPath


Return a UsdShadeMaterial holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdShadeMaterial(stage->GetPrimAtPath(path));


"""
   result["Material"].GetBaseMaterial.im_func.func_doc = """GetBaseMaterial() -> USDSHADE_API UsdShadeMaterial



Get the path to the base Material of this Material.


If there is no base Material, an empty Material is returned

"""
   result["Material"].GetDisplacementOutput.im_func.func_doc = """GetDisplacementOutput(renderContext) -> USDSHADE_API UsdShadeOutput

renderContext : TfToken


Returns the "displacement" output of this material for the specified
renderContext.


The returned output will always have the requested renderContext.

An invalid output is returned if an output corresponding to the
requested specific-renderContext does not exist.

UsdShadeMaterial::ComputeDisplacementSource()

"""
   result["Material"].CreateMaterialBindSubset.func_doc = """**static** CreateMaterialBindSubset(geom, subsetName, indices, elementType) -> USDSHADE_API UsdGeomSubset

geom : UsdGeomImageable
subsetName : TfToken
indices : VtIntArray
elementType : TfToken


Deprecated

Creates a GeomSubset named C{subsetName} with element type,
C{elementType} and familyName B{materialBind B{below the given
imageable prim, C{geom}.}}

If a GeomSubset named C{subsetName} already exists, then its
"familyName" is updated to be UsdShadeTokens->materialBind and its
indices (at *default* timeCode) are updated with the provided
C{indices} value before returning.

This method forces the familyType of the "materialBind" family of
subsets to UsdGeomTokens->nonOverlapping if it's unset or explicitly
set to UsdGeomTokens->unrestricted.

The default value C{elementType} is UsdGeomTokens->face, as we expect
materials to be bound most often to subsets of faces on meshes.

"""
   result["Material"].GetVolumeOutput.im_func.func_doc = """GetVolumeOutput(renderContext) -> USDSHADE_API UsdShadeOutput

renderContext : TfToken


Returns the "volume" output of this material for the specified
renderContext.


The returned output will always have the requested renderContext.

An invalid output is returned if an output corresponding to the
requested specific-renderContext does not exist.

UsdShadeMaterial::ComputeVolumeSource()

"""
   result["Material"].CreateDisplacementOutput.im_func.func_doc = """CreateDisplacementOutput(renderContext) -> USDSHADE_API UsdShadeOutput

renderContext : TfToken


Creates and returns the "displacement" output on this material for the
specified C{renderContext}.


If the output already exists on the material, it is returned and no
authoring is performed. The returned output will always have the
requested renderContext.

"""
   result["Material"].CreateMaterialFaceSet.func_doc = """**static** CreateMaterialFaceSet(prim) -> USDSHADE_API UsdGeomFaceSetAPI

prim : UsdPrim


Deprecated

Creates a "Material" face-set on the given prim. The Material face-set
is a partition of faces, since no face can be bound to more than one
Material.

If a "Material" face-set already exists, it is returned. If not, it
creates one and returns it.

"""
   result["Material"].ComputeSurfaceSource.im_func.func_doc = """ComputeSurfaceSource(renderContext, sourceName, sourceType) -> USDSHADE_API UsdShadeShader

renderContext : TfToken
sourceName : TfToken
sourceType : AttributeType


Computes the resolved "surface" output source for the given
C{renderContext}.


If a "surface" output corresponding to the specific renderContext does
not exist B{or} is not connected to a valid source, then this checks
the *universal* surface output.

Returns an empty Shader object if there is no valid *surface* output
source for the requested C{renderContext}. The python version of this
method returns a tuple containing three elements (the source surface
shader, sourceName, sourceType).

"""
   result["Material"].CreateSurfaceOutput.im_func.func_doc = """CreateSurfaceOutput(renderContext) -> USDSHADE_API UsdShadeOutput

renderContext : TfToken


Creates and returns the "surface" output on this material for the
specified C{renderContext}.


If the output already exists on the material, it is returned and no
authoring is performed. The returned output will always have the
requested renderContext.

"""
   result["Material"].HasMaterialFaceSet.func_doc = """**static** HasMaterialFaceSet(prim) -> USDSHADE_API bool

prim : UsdPrim


Deprecated

Returns true if the given prim has a "Material" face-set. A "Material"
face-set must be a partition for it to be considered valid.

"""
   result["Material"].ComputeDisplacementSource.im_func.func_doc = """ComputeDisplacementSource(renderContext, sourceName, sourceType) -> USDSHADE_API UsdShadeShader

renderContext : TfToken
sourceName : TfToken
sourceType : AttributeType


Computes the resolved "displacement" output source for the given
C{renderContext}.


If a "displacement" output corresponding to the specific renderContext
does not exist B{or} is not connected to a valid source, then this
checks the *universal* displacement output.

Returns an empty Shader object if there is no valid *displacement*
output source for the requested C{renderContext}. The python version
of this method returns a tuple containing three elements (the source
displacement shader, sourceName, sourceType).

"""
   result["Material"].GetEditContextForVariant.im_func.func_doc = """GetEditContextForVariant(MaterialVariantName, layer) -> USDSHADE_API pair<UsdStagePtr, UsdEditTarget >

MaterialVariantName : TfToken
layer : SdfLayerHandle


Helper function for configuring a UsdStage 's UsdEditTarget to author
Material variations.


Takes care of creating the Material variantSet and specified variant,
if necessary.

Let's assume that we are authoring Materials into the Stage's current
UsdEditTarget, and that we are iterating over the variations of a
UsdShadeMaterial *clothMaterial*, and *currVariant* is the variant we
are processing (e.g. "denim").

In C++, then, we would use the following pattern: ::

  {
      UsdEditContext ctxt(clothMaterial.GetEditContextForVariant(currVariant));
  
      // All USD mutation of the UsdStage on which clothMaterial sits will
      // now go "inside" the currVariant of the "MaterialVariant" variantSet
  }

In python, the pattern is: ::

  with clothMaterial.GetEditContextForVariant(currVariant):
      # Now sending mutations to currVariant

If C{layer} is specified, then we will use it, rather than the stage's
current UsdEditTarget 's layer as the destination layer for the edit
context we are building. If C{layer} does not actually contribute to
the Material prim's definition, any editing will have no effect on
this Material.

B{Note:} As just stated, using this method involves authoring a
selection for the MaterialVariant in the stage's current EditTarget.
When client is done authoring variations on this prim, they will
likely want to either UsdVariantSet::SetVariantSelection() to the
appropriate default selection, or possibly
UsdVariantSet::ClearVariantSelection() on the
UsdShadeMaterial::GetMaterialVariant() UsdVariantSet.

UsdVariantSet::GetVariantEditContext()

"""
   result["Material"].SetBaseMaterialPath.im_func.func_doc = """SetBaseMaterialPath(baseMaterialPath) -> USDSHADE_API void

baseMaterialPath : SdfPath


Set the path to the base Material of this Material.


An empty path is equivalent to clearing the base Material.

"""
   result["Material"].Define.func_doc = """**static** Define(stage, path) -> USDSHADE_API UsdShadeMaterial

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
   result["Material"].CreateMasterMaterialVariant.func_doc = """**static** CreateMasterMaterialVariant(masterPrim, MaterialPrims, masterVariantSetName) -> USDSHADE_API bool

masterPrim : UsdPrim
MaterialPrims : sequence< UsdPrim >
masterVariantSetName : TfToken


Create a variantSet on C{masterPrim} that will set the MaterialVariant
on each of the given *MaterialPrims*.


The variantSet, whose name can be specified with
C{masterVariantSetName} and defaults to the same MaterialVariant name
created on Materials by GetEditContextForVariant() , will have the
same variants as the Materials, and each Master variant will set every
C{MaterialPrims'} MaterialVariant selection to the same variant as the
master. Thus, it allows all Materials to be switched with a single
variant selection, on C{masterPrim}.

If C{masterPrim} is an ancestor of any given member of
C{MaterialPrims}, then we will author variant selections directly on
the MaterialPrims. However, it is often preferable to create a master
MaterialVariant in a separately rooted tree from the MaterialPrims, so
that it can be layered more strongly on top of the Materials.
Therefore, for any MaterialPrim in a different tree than masterPrim,
we will create "overs" as children of masterPrim that recreate the
path to the MaterialPrim, substituting masterPrim's full path for the
MaterialPrim's root path component.

Upon successful completion, the new variantSet we created on
C{masterPrim} will have its variant selection authored to the "last"
variant (determined lexicographically). It is up to the calling client
to either UsdVariantSet::ClearVariantSelection() on C{masterPrim}, or
set the selection to the desired default setting.

Return C{true} on success. It is an error if any of C{Materials} have
a different set of variants for the MaterialVariant than the others.

"""
   result["Material"].CreateVolumeOutput.im_func.func_doc = """CreateVolumeOutput(renderContext) -> USDSHADE_API UsdShadeOutput

renderContext : TfToken


Creates and returns the "volume" output on this material for the
specified C{renderContext}.


If the output already exists on the material, it is returned and no
authoring is performed. The returned output will always have the
requested renderContext.

"""
   result["Material"].GetBaseMaterialPath.im_func.func_doc = """GetBaseMaterialPath() -> USDSHADE_API SdfPath



Get the base Material of this Material.


If there is no base Material, an empty path is returned

"""
   result["Material"].GetSurfaceAttr.im_func.func_doc = """GetSurfaceAttr() -> USDSHADE_API UsdAttribute



Represents the universal "surface" output terminal of a material.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Material"].ClearBaseMaterial.im_func.func_doc = """ClearBaseMaterial() -> USDSHADE_API void



Clear the base Material of this Material.

"""
   result["Material"].CreateDisplacementAttr.im_func.func_doc = """CreateDisplacementAttr(defaultValue, writeSparsely) -> USDSHADE_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetDisplacementAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Material"].HasBaseMaterial.im_func.func_doc = """HasBaseMaterial() -> USDSHADE_API bool


"""
   result["Material"].Unbind.func_doc = """**static** Unbind(prim) -> USDSHADE_API bool

prim : UsdPrim


Deprecated

Ensure that, when resolved up to and including the current
UsdEditTarget in composition strength, the given prim has no binding
to a UsdShadeMaterial

Note that this constitutes an assertion that there be no binding - it
does *not* simply remove any binding at the current EditTarget such
that a weaker binding will "shine through". For that behavior, use
GetBindingRel() .ClearTargets()

true on success

"""
   result["Material"].Bind.im_func.func_doc = """Bind(prim) -> USDSHADE_API bool

prim : UsdPrim


Deprecated

Create a Material-binding relationship on C{prim} and target it to
this Material prim

Any UsdPrim can have a binding to at most a *single* UsdShadeMaterial.

true on success

"""
   result["Material"].GetMaterialBindSubsetsFamilyType.func_doc = """**static** GetMaterialBindSubsetsFamilyType(geom) -> USDSHADE_API TfToken

geom : UsdGeomImageable


Deprecated

Returns the familyType of the family of "materialBind" subsets under
C{geom}.

By default materialBind subsets have familyType="nonOverlapping", but
their can also be tagged as a "partition", using
SetMaterialBindFaceSubsetsFamilyType().

UsdGeomSubset::SetFamilyType

UsdGeomSubset::GetFamilyNameAttr

"""
   result["Material"].GetSurfaceOutput.im_func.func_doc = """GetSurfaceOutput(renderContext) -> USDSHADE_API UsdShadeOutput

renderContext : TfToken


Returns the "surface" output of this material for the specified
C{renderContext}.


The returned output will always have the requested renderContext.

An invalid output is returned if an output corresponding to the
requested specific-renderContext does not exist.

UsdShadeMaterial::ComputeSurfaceSource()

"""
   result["Material"].GetBindingRel.func_doc = """**static** GetBindingRel(prim) -> USDSHADE_API UsdRelationship

prim : UsdPrim


Deprecated

Direct access to the binding relationship for C{prim}, if it has
already been created.

This is how clients discover the Material to which a prim is bound,
and also how one would add metadata or customData.

Care should be exercized when manipulating this relationship's targets
directly, rather than via Bind() and Unbind() , since it will then be
the client's responsibility to ensure that only a single Material prim
is targetted. In general, use UsdRelationship::SetTargets() rather
than UsdRelationship::AddTarget()

"""
   result["Material"].GetMaterialFaceSet.func_doc = """**static** GetMaterialFaceSet(prim) -> USDSHADE_API UsdGeomFaceSetAPI

prim : UsdPrim


Deprecated

Returns the "Material" face-set if it exists on the given prim. If
not, returns an invalid UsdGeomFaceSetAPI object.

"""
   result["Material"].GetBoundMaterial.func_doc = """**static** GetBoundMaterial(prim) -> USDSHADE_API UsdShadeMaterial

prim : UsdPrim


Deprecated

Follows the relationship returned by GetBindingRel and returns a valid
UsdShadeMaterial if the relationship targets exactly one such prim.

"""
   result["Material"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSHADE_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Material"].SetBaseMaterial.im_func.func_doc = """SetBaseMaterial(baseMaterial) -> USDSHADE_API void

baseMaterial : Material


Set the base Material of this Material.


An empty Material is equivalent to clearing the base Material.

"""
   result["Material"].GetMaterialVariant.im_func.func_doc = """GetMaterialVariant() -> USDSHADE_API UsdVariantSet



Return a UsdVariantSet object for interacting with the Material
variant variantSet.

"""
   result["Material"].ComputeVolumeSource.im_func.func_doc = """ComputeVolumeSource(renderContext, sourceName, sourceType) -> USDSHADE_API UsdShadeShader

renderContext : TfToken
sourceName : TfToken
sourceType : AttributeType


Computes the resolved "volume" output source for the given
C{renderContext}.


If a "volume" output corresponding to the specific renderContext does
not exist B{or} is not connected to a valid source, then this checks
the *universal* volume output.

Returns an empty Shader object if there is no valid *volume* output
source for the requested C{renderContext}. The python version of this
method returns a tuple containing three elements (the source volume
shader, sourceName, sourceType).

"""
   result["Material"].CreateSurfaceAttr.im_func.func_doc = """CreateSurfaceAttr(defaultValue, writeSparsely) -> USDSHADE_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetSurfaceAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Material"].CreateVolumeAttr.im_func.func_doc = """CreateVolumeAttr(defaultValue, writeSparsely) -> USDSHADE_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetVolumeAttr() , and also Create vs Get Property Methods for when
to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Material"].GetMaterialBindSubsets.func_doc = """**static** GetMaterialBindSubsets(geom) -> USDSHADE_API sequence< UsdGeomSubset >

geom : UsdGeomImageable


Deprecated

Returns all the existing GeomSubsets with
familyName=UsdShadeTokens->materialBind below the given imageable
prim, C{geom}.

"""
   result["Material"].GetDisplacementAttr.im_func.func_doc = """GetDisplacementAttr() -> USDSHADE_API UsdAttribute



Represents the universal "displacement" output terminal of a material.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Material"].GetVolumeAttr.im_func.func_doc = """GetVolumeAttr() -> USDSHADE_API UsdAttribute



Represents the universal "volume" output terminal of a material.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityVarying  Fallback Value: No Fallback

"""
   result["Material"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdShadeMaterial on UsdPrim C{prim}.


Equivalent to UsdShadeMaterial::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdShadeMaterial on the prim held by C{schemaObj}.


Should be preferred over UsdShadeMaterial (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Material"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSHADE_API  TfType


"""
   result["Material"].SetMaterialBindSubsetsFamilyType.func_doc = """**static** SetMaterialBindSubsetsFamilyType(geom, familyType) -> USDSHADE_API bool

geom : UsdGeomImageable
familyType : TfToken


Deprecated

Encodes whether the family of "materialBind" subsets form a valid
partition of the set of all faces on the imageable prim, C{geom}.

"""
   result["__doc__"] = """
UsdShade provides schemas and behaviors for creating and binding
materials, which encapsulate shading networks.

UsdShade Networks
=================

UsdShade provides schemas and behaviors for creating shading networks
(UsdShadeNodeGraph) and materials (UsdShadeMaterial). The networks are
composed of UsdShadeShader objects, as well as other
UsdShadeNodeGraph.

Objects in a network are connected together and to their encapsulating
Material using the UsdShadeConnectableAPI schema, which allows one to
create UsdShadeInput and UsdShadeOutput (which are UsdAttribute
schemas), and *connect* them using UsdAttribute connections.

Here's a python example. ::

  # create material
  materialPath = Sdf.Path('/Model/Materials/MyMaterial')
  material = UsdShade.Material.Define(stage, materialPath)
  
  # create shaders
  downStreamShader = UsdShade.Shader.Define(
      stage, materialPath.AppendChild('Upstream'))
  upstreamShader = UsdShade.Shader.Define(
      stage, materialPath.AppendChild('Downstream'))
  
  # Connect
  inputPort = downStreamShader.CreateInput(
      'DownstreamInput', Sdf.ValueTypeNames.Float)
  inputPort.ConnectToSource(upstreamShader, 'UpstreamOutput')

This will yield a material with two connected nodes. ::

  #usda 1.0
  
  def "Model"
  {
      def "Materials"
      {
          def Material "MyMaterial"
          {
              def Shader "Upstream"
              {
                  float inputs:DownstreamInput.connect = 
                      </Model/Materials/MyMaterial/Downstream.outputs:UpstreamOutput>
              }
  
              def Shader "Downstream"
              {
                  float outputs:UpstreamOutput
              }
          }
      }
  }

Encapsulation and Sharing
=========================

In UsdShade, all shaders are UsdPrims or just "prims". However, in
deference to the larger body of technical discourse on shading, we
will refer to them as "nodes" in this discussion. Shading nodes should
be encapsulated in a containing object, and are not generally used in
isolation.

Shading networks can be organized into coherent packaged units
(UsdShadeNodeGraph), with their own public parameters exposed and
connected to the internal nodes. In this scenario, the
UsdShadeNodeGraph is a parent or ancestor prim to all of the
UsdShadeShader prims in the network, and serves as the point of
encapsulation - the UsdShadeNodeGraph prim can then be referenced*
into other, larger networks as a building block, with its entire
network intact. When referenced into larger networks, NodeGraphs can
also be instanced so that they appear as a single prim in the network,
and can be processed more efficiently when referenced from multiple
locations.

If the network of shading nodes is directly consumable as a "shader"
of a type known to some client renderer (e.g. a *surface shader*),
then the encapsulating parent/ancestor should be declared as a
UsdShadeMaterial, which is a container that can also be bound to
geometries or collections. Materials can also be reused and instanced,
retaining the same network but allowing top-level "Material Interface"
parameter to be authored uniquely.

To expose a parameter to the container, we use the same mechanism that
connects nodes. ::

  # Expose a parameter to the public interface
  internalPort = upstreamShader.CreateInput(
      'internalPort', Sdf.ValueTypeNames.Float)
  exposedPort = material.CreateInput(
      'ExposedPort', Sdf.ValueTypeNames.Float)
  exposedPort.Set(1.0)
  internalPort.ConnectToSource(exposedPort)

Which will yield a public interface parameter called 'ExposedPort' on
the UsdShadeMaterial called 'MyMaterial', and set its default value to
1.0 ::

  #usda 1.0
  
  def "Model"
  {
      def "Materials"
      {
          def Material "MyMaterial"
          {
              float inputs:ExposedPort = 1
  
              def Shader "Upstream"
              {
                  float inputs:DownstreamInput.connect = 
                      </Model/Materials/MyMaterial/Downstream.outputs:UpstreamOutput>
              }
  
              def Shader "Downstream"
              {
                  float inputs:internalPort.connect = 
                      </Model/Materials/MyMaterial.inputs:ExposedPort>
                  float outputs:UpstreamOutput
              }
          }
      }
  }

To expose an output of a node network as an output of a NodeGraph, or
as a "terminal output" of a Material, we again use the same connection
API, except that now we are connecting an Output to another Output (in
effect, *forwarding* the Output from a node to its encapsulating
container): ::

  # The output represents the result of the shader's computation. For
  # complex types like "surface illumination" we use the type Token as
  # a standin for the type specific to the renderer
  outPort = surfaceShader.CreateOutput(
      'out', Sdf.ValueTypeNames.Token)
  surfaceTerminal = material.CreateOutput(
      'surface', Sdf.ValueTypeNames.Token)
  # For outputs, it is the container's Output that connect's to the Node's
  # output
  surfaceTerminal.ConnectToSource(outPort)

Which will yield a public interface parameter called 'ExposedPort' on
the UsdShadeMaterial called 'MyMaterial', and set its default value to
1.0 ::

  #usda 1.0
  
  def "Model"
  {
      def "Materials"
      {
          def Material "MyMaterial"
          {
              token outputs:surface.connect = 
                  </Model/Materials/MyMaterial/Surface.outputs:out>
  
              def Shader "Surface"
              {
                  token outputs:out
              }
          }
      }
  }


"""
   result["Input"].__doc__ = """
This class encapsulates a shader or node-graph input, which is a
connectable property representing a typed value.

"""
   result["Input"].IsInterfaceInputName.func_doc = """**static** IsInterfaceInputName(name) -> USDSHADE_API bool

name : string


Test if this name has a namespace that indicates it could be an input.

"""
   result["Input"].SetConnectability.im_func.func_doc = """SetConnectability(connectability) -> USDSHADE_API bool

connectability : TfToken


Set the connectability of the Input.


In certain shading data models, there is a need to distinguish which
inputs B{can} vary over a surface from those that must be B{uniform}.
This is accomplished in UsdShade by limiting the connectability of the
input. This is done by setting the "connectability" metadata on the
associated attribute.

Connectability of an Input can be set to UsdShadeTokens->full or
UsdShadeTokens->interfaceOnly.

   - B{full} implies that the Input can be connected to any other
     Input or Output.

   - B{interfaceOnly} implies that the Input can only be connected to
     a NodeGraph Input (which represents an interface override, not a
     render-time dataflow connection), or another Input whose
     connectability is also "interfaceOnly".
     The default connectability of an input is UsdShadeTokens->full.

SetConnectability()

"""
   result["Input"].SetRenderType.im_func.func_doc = """SetRenderType(renderType) -> USDSHADE_API bool

renderType : TfToken


Specify an alternative, renderer-specific type to use when
emitting/translating this Input, rather than translating based on its
GetTypeName()


For example, we set the renderType to "struct" for Inputs that are of
renderman custom struct types.

true on success.

"""
   result["Input"].GetPrim.im_func.func_doc = """GetPrim() -> UsdPrim



Get the prim that the input belongs to.

"""
   result["Input"].GetTypeName.im_func.func_doc = """GetTypeName() -> USDSHADE_API SdfValueTypeName



Get the "scene description" value type name of the attribute
associated with the Input.

"""
   result["Input"].ConnectToSource.im_func.func_doc = """ConnectToSource(source, sourceName, sourceType, typeName) -> USDSHADE_API bool

source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType
typeName : SdfValueTypeName


Authors a connection for this Input to the source described by the
following three elements: C{source}, the connectable owning the
source, C{sourceName}, the name of the source and C{sourceType}, the
value type of the source shading attribute.


C{typeName} if specified, is the typename of the attribute to create
on the source if it doesn't exist. It is also used to validate whether
the types of the source and consumer of the connection are compatible.

UsdShadeConnectableAPI::ConnectToSource


----------------------------------------------------------------------
ConnectToSource(sourcePath) -> USDSHADE_API bool

sourcePath : SdfPath


Authors a connection for this Input to the source at the given path.



UsdShadeConnectableAPI::ConnectToSource


----------------------------------------------------------------------
ConnectToSource(sourceInput) -> USDSHADE_API bool

sourceInput : Input


Connects this Input to the given input, C{sourceInput}.



UsdShadeConnectableAPI::ConnectToSource


----------------------------------------------------------------------
ConnectToSource(sourceOutput) -> USDSHADE_API bool

sourceOutput : Output


Connects this Input to the given output, C{sourceOutput}.



UsdShadeConnectableAPI::ConnectToSource

"""
   result["Input"].Get.im_func.func_doc = """Get(value, time) -> bool

value : T
time : UsdTimeCode


Convenience wrapper for the templated UsdAttribute::Get() .


----------------------------------------------------------------------
Get(value, time) -> USDSHADE_API bool

value : VtValue
time : UsdTimeCode


Convenience wrapper for VtValue version of UsdAttribute::Get() .

"""
   result["Input"].GetConnectability.im_func.func_doc = """GetConnectability() -> USDSHADE_API TfToken



Returns the connectability of the Input.



SetConnectability()

"""
   result["Input"].GetAttr.im_func.func_doc = """GetAttr() -> UsdAttribute



Explicit UsdAttribute extractor.

"""
   result["Input"].__init__.im_func.func_doc = """__init__(attr) -> USDSHADE_API

attr : UsdAttribute


Speculative constructor that will produce a valid UsdShadeInput when
C{attr} already represents a shade Input, and produces an *invalid*
UsdShadeInput otherwise (i.e.


unspecified-bool-type() will return false).


----------------------------------------------------------------------
__init__()



Default constructor returns an invalid Input.


Exists for the sake of container classes


----------------------------------------------------------------------
__init__(prim, name, typeName)

prim : UsdPrim
name : TfToken
typeName : SdfValueTypeName

"""
   result["Input"].IsSourceConnectionFromBaseMaterial.im_func.func_doc = """IsSourceConnectionFromBaseMaterial() -> USDSHADE_API bool



Returns true if the connection to this Input's source, as returned by
GetConnectedSource() , is authored across a specializes arc, which is
used to denote a base material.



UsdShadeConnectableAPI::IsSourceConnectionFromBaseMaterial

"""
   result["Input"].GetRenderType.im_func.func_doc = """GetRenderType() -> USDSHADE_API TfToken



Return this Input's specialized renderType, or an empty token if none
was authored.



SetRenderType()

"""
   result["Input"].SetDisplayGroup.im_func.func_doc = """SetDisplayGroup(displayGroup) -> USDSHADE_API bool

displayGroup : string


Set the displayGroup metadata for this Input, i.e.


hinting for the location and nesting of the attribute.

UsdProperty::SetDisplayGroup() , UsdProperty::SetNestedDisplayGroup()

"""
   result["Input"].HasConnectedSource.im_func.func_doc = """HasConnectedSource() -> USDSHADE_API bool



Returns true if and only if this Input is currently connected to a
valid (defined) source.



UsdShadeConnectableAPI::HasConnectedSource

"""
   result["Input"].DisconnectSource.im_func.func_doc = """DisconnectSource() -> USDSHADE_API bool



Disconnect source for this Input.



UsdShadeConnectableAPI::DisconnectSource

"""
   result["Input"].GetConnectedSource.im_func.func_doc = """GetConnectedSource(source, sourceName, sourceType) -> USDSHADE_API bool

source : ConnectableAPI
sourceName : TfToken
sourceType : AttributeType


Finds the source of a connection for this Input.


C{source} is an output parameter which will be set to the source
connectable prim. C{sourceName} will be set to the name of the source
shading property, which could be the parameter name, output name or
the interface attribute name. This does not include the namespace
prefix associated with the source type. C{sourceType} will have the
value type of the source shading property.

C{true} if this Input is connected to a valid, defined source.
C{false} if this Input is not connected to a single, valid source.

The python wrapping for this method returns a (source, sourceName,
sourceType) tuple if the parameter is connected, else C{None}

UsdShadeConnectableAPI::GetConnectedSource

"""
   result["Input"].GetRawConnectedSourcePaths.im_func.func_doc = """GetRawConnectedSourcePaths(sourcePaths) -> USDSHADE_API bool

sourcePaths : SdfPathVector


Returns the "raw" (authored) connected source paths for this Input.



UsdShadeConnectableAPI::GetRawConnectedSourcePaths

"""
   result["Input"].IsInput.func_doc = """**static** IsInput(attr) -> USDSHADE_API bool

attr : UsdAttribute


Test whether a given UsdAttribute represents a valid Input, which
implies that creating a UsdShadeInput from the attribute will succeed.


Success implies that C{attr.IsDefined()} is true.

"""
   result["Input"].ClearSource.im_func.func_doc = """ClearSource() -> USDSHADE_API bool



Clears source for this shading property in the current UsdEditTarget.


Most of the time, what you probably want is DisconnectSource() rather
than this function.

UsdShadeConnectableAPI::ClearSource

"""
   result["Input"].Set.im_func.func_doc = """Set(value, time) -> USDSHADE_API bool

value : VtValue
time : UsdTimeCode


Set a value for the Input at C{time}.


----------------------------------------------------------------------
Set(value, time) -> bool

value : T
time : UsdTimeCode


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Set a value of the Input at C{time}.

"""
   result["Input"].ClearConnectability.im_func.func_doc = """ClearConnectability() -> USDSHADE_API bool



Clears any authored connectability on the Input.

"""
   result["Input"].CanConnect.im_func.func_doc = """CanConnect(source) -> USDSHADE_API bool

source : UsdAttribute


Determines whether this Input can be connected to the given source
attribute, which can be an input or an output.



UsdShadeConnectableAPI::CanConnect


----------------------------------------------------------------------
CanConnect(sourceInput) -> USDSHADE_API bool

sourceInput : Input


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CanConnect(sourceOutput) -> USDSHADE_API bool

sourceOutput : Output


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Input"].GetBaseName.im_func.func_doc = """GetBaseName() -> USDSHADE_API TfToken



Returns the name of the input.


We call this the base name since it strips off the "inputs:" namespace
prefix from the attribute name, and returns it.

"""
   result["Input"].HasRenderType.im_func.func_doc = """HasRenderType() -> USDSHADE_API bool



Return true if a renderType has been specified for this Input.



SetRenderType()

"""
   result["Input"].GetDocumentation.im_func.func_doc = """GetDocumentation() -> USDSHADE_API string



Get documentation string for this Input.



UsdObject::GetDocumentation()

"""
   result["Input"].SetDocumentation.im_func.func_doc = """SetDocumentation(docs) -> USDSHADE_API bool

docs : string


Set documentation string for this Input.



UsdObject::SetDocumentation()

"""
   result["Input"].GetDisplayGroup.im_func.func_doc = """GetDisplayGroup() -> USDSHADE_API string



Get the displayGroup metadata for this Input, i.e.


hint for the location and nesting of the attribute.

UsdProperty::GetDisplayGroup() , UsdProperty::GetNestedDisplayGroup()

"""
   result["Input"].GetFullName.im_func.func_doc = """GetFullName() -> TfToken



Get the name of the attribute associated with the Input.

"""
   result["Shader"].__doc__ = """
Base class for all USD shaders.


Shaders are the building blocks of shading networks. While
UsdShadeShader objects are not target specific, each renderer or
application target may derive its own renderer-specific shader object
types from this base, if needed.

Objects of this class generally represent a single shading object,
whether it exists in the target renderer or not. For example, a
texture, a fractal, or a mix node.

The main property of this class is the info:id token, which uniquely
identifies the type of this node. The id resolution into a renderable
shader target is deferred to the consuming application.

The purpose of representing them in Usd is two-fold:
   - To represent, via "connections" the topology of the shading
     network that must be reconstructed in the renderer. Facilities for
     authoring and manipulating connections are encapsulated in the Has-A
     schema UsdShadeConnectableAPI.

   - To present a (partial or full) interface of typed input
     parameters whose values can be set and overridden in Usd, to be
     provided later at render-time as parameter values to the actual render
     shader objects. Shader input parameters are encapsulated in the
     property schema UsdShadeInput.
     For any described attribute *Fallback* *Value* or *Allowed* *Values*
     below that are text/tokens, the actual token is published and defined
     in UsdShadeTokens. So to set an attribute to the value "rightHanded",
     use UsdShadeTokens->rightHanded as the value.

"""
   result["Shader"].GetShaderMetadataByKey.im_func.func_doc = """GetShaderMetadataByKey(key) -> USDSHADE_API string

key : TfToken


Returns the value corresponding to C{key} in the composed
B{shaderMetadata} dictionary.

"""
   result["Shader"].GetOutputs.im_func.func_doc = """GetOutputs() -> USDSHADE_API sequence< UsdShadeOutput >



Outputs are represented by attributes in the "outputs:" namespace.

"""
   result["Shader"].SetShaderMetadata.im_func.func_doc = """SetShaderMetadata(shaderMetadata) -> USDSHADE_API void

shaderMetadata : NdrTokenMap


Authors the given C{shaderMetadata} on this shader at the current
EditTarget.

"""
   result["Shader"].CreateIdAttr.im_func.func_doc = """CreateIdAttr(defaultValue, writeSparsely) -> USDSHADE_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetIdAttr() , and also Create vs Get Property Methods for when to
use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Shader"].GetSourceCode.im_func.func_doc = """GetSourceCode(sourceCode, sourceType) -> USDSHADE_API bool

sourceCode : string
sourceType : TfToken


Fetches the shader's source code for the specified C{sourceType} value
by reading the B{info: *sourceType*: sourceCode} attribute, if the
shader's *info:implementationSource* is B{sourceCode}.


If the *sourceCode* attribute corresponding to the requested
*sourceType* isn't present on the shader, then the *universal* or
*fallback* sourceCode attribute (i.e. *info:sourceCode*) is consulted,
if present, to get the source code.

Returns B{true} if the shader's implementation source is B{sourceCode}
and the source code string was fetched successfully into
C{sourceCode}. Returns false otherwise.

GetImplementationSource()

"""
   result["Shader"].Define.func_doc = """**static** Define(stage, path) -> USDSHADE_API UsdShadeShader

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
   result["Shader"].GetShaderNodeForSourceType.im_func.func_doc = """GetShaderNodeForSourceType(sourceType) -> USDSHADE_API SdrShaderNodeConstPtr

sourceType : TfToken


This method attempts to ensure that there is a ShaderNode in the
shader registry (i.e.


SdrRegistry) representing this shader for the given C{sourceType}. It
may return a null pointer if none could be found or created.

"""
   result["Shader"].Get.func_doc = """**static** Get(stage, path) -> USDSHADE_API UsdShadeShader

stage : UsdStagePtr
path : SdfPath


Return a UsdShadeShader holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdShadeShader(stage->GetPrimAtPath(path));


"""
   result["Shader"].GetOutput.im_func.func_doc = """GetOutput(name) -> USDSHADE_API UsdShadeOutput

name : TfToken


Return the requested output if it exists.

"""
   result["Shader"].GetSourceAsset.im_func.func_doc = """GetSourceAsset(sourceAsset, sourceType) -> USDSHADE_API bool

sourceAsset : SdfAssetPath
sourceType : TfToken


Fetches the shader's source asset value for the specified
C{sourceType} value from the B{info: *sourceType*: sourceAsset}
attribute, if the shader's *info:implementationSource* is
B{sourceAsset}.


If the *sourceAsset* attribute corresponding to the requested
*sourceType* isn't present on the shader, then the *universal*
*fallback* sourceAsset attribute, i.e. *info:sourceAsset* is
consulted, if present, to get the source asset path.

Returns B{true} if the shader's implementation source is
B{sourceAsset} and the source asset path value was fetched
successfully into C{sourceAsset}. Returns false otherwise.

GetImplementationSource()

"""
   result["Shader"].SetSourceAsset.im_func.func_doc = """SetSourceAsset(sourceAsset, sourceType) -> USDSHADE_API bool

sourceAsset : SdfAssetPath
sourceType : TfToken


Sets the shader's source-asset path value to C{sourceAsset} for the
given source type, C{sourceType}.


This also sets the *info:implementationSource* attribute on the shader
to B{UsdShadeTokens->sourceAsset}.

"""
   result["Shader"].GetInput.im_func.func_doc = """GetInput(name) -> USDSHADE_API UsdShadeInput

name : TfToken


Return the requested input if it exists.

"""
   result["Shader"].GetImplementationSourceAttr.im_func.func_doc = """GetImplementationSourceAttr() -> USDSHADE_API UsdAttribute



Specifies the attribute that should be consulted to get the shader's
implementation or its source code.



   - If set to "id", the "info:id" attribute's value is used to
     determine the shader source from the shader registry.

   - If set to "sourceAsset", the resolved value of the
     "info:sourceAsset" attribute corresponding to the desired
     implementation (or source-type) is used to locate the shader source.

   - If set to "sourceCode", the value of "info:sourceCode" attribute
     corresponding to the desired implementation (or source type) is used
     as the shader source.

C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: id  Allowed Values : [id,
sourceAsset, sourceCode]

"""
   result["Shader"].CreateImplementationSourceAttr.im_func.func_doc = """CreateImplementationSourceAttr(defaultValue, writeSparsely) -> USDSHADE_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetImplementationSourceAttr() , and also Create vs Get Property
Methods for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["Shader"].CreateInput.im_func.func_doc = """CreateInput(name, typeName) -> USDSHADE_API UsdShadeInput

name : TfToken
typeName : SdfValueTypeName


Create an input which can either have a value or can be connected.


The attribute representing the input is created in the "inputs:"
namespace. Inputs on both shaders and node-graphs are connectable.

"""
   result["Shader"].SetShaderId.im_func.func_doc = """SetShaderId(id) -> USDSHADE_API bool

id : TfToken


Sets the shader's ID value.


This also sets the *info:implementationSource* attribute on the shader
to B{UsdShadeTokens->id}, if the existing value is different.

"""
   result["Shader"].SetShaderMetadataByKey.im_func.func_doc = """SetShaderMetadataByKey(key, value) -> USDSHADE_API void

key : TfToken
value : string


Sets the value corresponding to C{key} to the given string C{value},
in the shader's "shaderMetadata" dictionary at the current EditTarget.

"""
   result["Shader"].GetIdAttr.im_func.func_doc = """GetIdAttr() -> USDSHADE_API UsdAttribute



The id is an identifier for the type or purpose of the shader.


E.g.: Texture or FractalFloat. The use of this id will depend on the
render target: some will turn it into an actual shader path, some will
use it to generate shader source code dynamically.

SetShaderId()  C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token
Variability: SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["Shader"].HasShaderMetadataByKey.im_func.func_doc = """HasShaderMetadataByKey(key) -> USDSHADE_API bool

key : TfToken


Returns true if there is a value corresponding to the given C{key} in
the composed "shaderMetadata" dictionary.

"""
   result["Shader"].ClearShaderMetadataByKey.im_func.func_doc = """ClearShaderMetadataByKey(key) -> USDSHADE_API void

key : TfToken


Clears the entry corresponding to the given C{key} in the
"shaderMetadata" dictionary authored in the current EditTarget.

"""
   result["Shader"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSHADE_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["Shader"].GetShaderId.im_func.func_doc = """GetShaderId(id) -> USDSHADE_API bool

id : TfToken


Fetches the shader's ID value from the *info:id* attribute, if the
shader's *info:implementationSource* is B{id}.


Returns B{true} if the shader's implementation source is B{id} and the
value was fetched properly into C{id}. Returns false otherwise.

GetImplementationSource()

"""
   result["Shader"].ClearShaderMetadata.im_func.func_doc = """ClearShaderMetadata() -> USDSHADE_API void



Clears any "shaderMetadata" value authored on the shader in the
current EditTarget.

"""
   result["Shader"].HasShaderMetadata.im_func.func_doc = """HasShaderMetadata() -> USDSHADE_API bool



Returns true if the shader has a non-empty composed "shaderMetadata"
dictionary value.

"""
   result["Shader"].GetImplementationSource.im_func.func_doc = """GetImplementationSource() -> USDSHADE_API TfToken



Reads the value of info:implementationSource attribute and returns a
token identifying the attribute that must be consulted to identify the
shader's source program.


This returns
   - B{id}, to indicate that the "info:id" attribute must be
     consulted.

   - B{sourceAsset} to indicate that the asset-valued
     "info:{sourceType}:sourceAsset" attribute associated with the desired
     B{sourceType} should be consulted to locate the asset with the
     shader's source.

   - B{sourceCode} to indicate that the string-valued
     "info:{sourceType}:sourceCode" attribute associated with the desired
     B{sourceType} should be read to get shader's source.

This issues a warning and returns B{id} if the
*info:implementationSource* attribute has an invalid value.

*{sourceType}* above is a place holder for a token that identifies the
type of shader source or its implementation. For example: osl, glslfx,
riCpp etc. This allows a shader to specify different sourceAsset (or
sourceCode) values for different sourceTypes. The sourceType tokens
usually correspond to the sourceType value of the NdrParserPlugin
that's used to parse the shader source ( NdrParserPlugin::SourceType).

When sourceType is empty, the corresponding sourceAsset or sourceCode
is considered to be "universal" (or fallback), which is represented by
the empty-valued token UsdShadeTokens->universalSourceType. When the
sourceAsset (or sourceCode) corresponding to a specific, requested
sourceType is unavailable, the universal sourceAsset (or sourceCode)
is returned by GetSourceAsset (and GetSourceCode} API, if present.

GetShaderId()

GetSourceAsset()

GetSourceCode()

"""
   result["Shader"].GetInputs.im_func.func_doc = """GetInputs() -> USDSHADE_API sequence< UsdShadeInput >



Inputs are represented by attributes in the "inputs:" namespace.

"""
   result["Shader"].SetSourceCode.im_func.func_doc = """SetSourceCode(sourceCode, sourceType) -> USDSHADE_API bool

sourceCode : string
sourceType : TfToken


Sets the shader's source-code value to C{sourceCode} for the given
source type, C{sourceType}.


This also sets the *info:implementationSource* attribute on the shader
to B{UsdShadeTokens->sourceCode}.

"""
   result["Shader"].ConnectableAPI.im_func.func_doc = """ConnectableAPI() -> USDSHADE_API UsdShadeConnectableAPI



Contructs and returns a UsdShadeConnectableAPI object with this
shader.


Note that most tasks can be accomplished without explicitly
constructing a UsdShadeConnectable API, since connection-related API
such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
and UsdShadeShader will auto-convert to a UsdShadeConnectableAPI when
passed to functions that want to act generically on a connectable
UsdShadeConnectableAPI object.

"""
   result["Shader"].GetShaderMetadata.im_func.func_doc = """GetShaderMetadata() -> USDSHADE_API NdrTokenMap



Returns this shader's composed "shaderMetadata" dictionary as a
NdrTokenMap.

"""
   result["Shader"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdShadeShader on UsdPrim C{prim}.


Equivalent to UsdShadeShader::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdShadeShader on the prim held by C{schemaObj}.


Should be preferred over UsdShadeShader (schemaObj.GetPrim()), as it
preserves SchemaBase state.


----------------------------------------------------------------------
__init__(connectable) -> USDSHADE_API

connectable : ConnectableAPI


Constructor that takes a ConnectableAPI object.


Allow implicit (auto) conversion of UsdShadeShader to
UsdShadeConnectableAPI, so that a shader can be passed into any
function that accepts a ConnectableAPI.

"""
   result["Shader"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSHADE_API  TfType


"""
   result["Shader"].CreateOutput.im_func.func_doc = """CreateOutput(name, typeName) -> USDSHADE_API UsdShadeOutput

name : TfToken
typeName : SdfValueTypeName


Create an output which can either have a value or can be connected.


The attribute representing the output is created in the "outputs:"
namespace. Outputs on a shader cannot be connected, as their value is
assumed to be computed externally.

"""
   result["NodeGraph"].__doc__ = """
A node-graph is a container for shading nodes, as well as other node-
graphs.


It has a public input interface and provides a list of public outputs.

B{Node Graph Interfaces}

One of the most important functions of a node-graph is to host the
"interface" with which clients of already-built shading networks will
interact. Please see Interface Inputs for a detailed explanation of
what the interface provides, and how to construct and use it, to
effectively share/instance shader networks.

B{Node Graph Outputs}

These behave like outputs on a shader and are typically connected to
an output on a shader inside the node-graph.

"""
   result["NodeGraph"].GetOutputs.im_func.func_doc = """GetOutputs() -> USDSHADE_API sequence< UsdShadeOutput >



Outputs are represented by attributes in the "outputs:" namespace.

"""
   result["NodeGraph"].GetInterfaceInputs.im_func.func_doc = """GetInterfaceInputs() -> USDSHADE_API sequence< UsdShadeInput >



Returns all the "Interface Inputs" of the node-graph.


This is the same as GetInputs() , but is provided as a convenience, to
allow clients to distinguish between inputs on shaders vs. interface-
inputs on node-graphs.

"""
   result["NodeGraph"].Define.func_doc = """**static** Define(stage, path) -> USDSHADE_API UsdShadeNodeGraph

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
   result["NodeGraph"].Get.func_doc = """**static** Get(stage, path) -> USDSHADE_API UsdShadeNodeGraph

stage : UsdStagePtr
path : SdfPath


Return a UsdShadeNodeGraph holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdShadeNodeGraph(stage->GetPrimAtPath(path));


"""
   result["NodeGraph"].GetOutput.im_func.func_doc = """GetOutput(name) -> USDSHADE_API UsdShadeOutput

name : TfToken


Return the requested output if it exists.

"""
   result["NodeGraph"].ComputeOutputSource.im_func.func_doc = """ComputeOutputSource(outputName, sourceName, sourceType) -> USDSHADE_API UsdShadeShader

outputName : TfToken
sourceName : TfToken
sourceType : AttributeType


Resolves the connection source of the requested output, identified by
C{outputName} to a shader output.


C{sourceName} is an output parameter that is set to the name of the
resolved output, if the node-graph output is connected to a valid
shader source.

C{sourceType} is an output parameter that is set to the type of the
resolved output, if the node-graph output is connected to a valid
shader source.

Returns a valid shader object if the specified output exists and is
connected to one. Return an empty shader object otherwise. The python
version of this method returns a tuple containing three elements (the
source shader, sourceName, sourceType).

"""
   result["NodeGraph"].GetInput.im_func.func_doc = """GetInput(name) -> USDSHADE_API UsdShadeInput

name : TfToken


Return the requested input if it exists.

"""
   result["NodeGraph"].ComputeInterfaceInputConsumersMap.im_func.func_doc = """ComputeInterfaceInputConsumersMap(computeTransitiveConsumers) -> USDSHADE_API InterfaceInputConsumersMap

computeTransitiveConsumers : bool


Walks the namespace subtree below the node-graph and computes a map
containing the list of all inputs on the node-graph and the associated
vector of consumers of their values.


The consumers can be inputs on shaders within the node-graph or on
nested node-graphs).

If C{computeTransitiveConsumers} is true, then value consumers
belonging to B{node-graphs} are resolved transitively to compute the
transitive mapping from inputs on the node-graph to inputs on shaders
inside the material. Note that inputs on node-graphs that don't have
value consumers will continue to be included in the result.

C{renderTarget} exists for backwards compatibility to allow retrieving
the input-consumers map when the shading network has old-style
interface attributes.

This API is provided for use by DCC's that want to present node-graph
interface / shader connections in the opposite direction than they are
encoded in USD.

"""
   result["NodeGraph"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdShadeNodeGraph on UsdPrim C{prim}.


Equivalent to UsdShadeNodeGraph::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdShadeNodeGraph on the prim held by C{schemaObj}.


Should be preferred over UsdShadeNodeGraph (schemaObj.GetPrim()), as
it preserves SchemaBase state.


----------------------------------------------------------------------
__init__(connectable) -> USDSHADE_API

connectable : ConnectableAPI


Constructor that takes a ConnectableAPI object.


Allow implicit (auto) conversion of UsdShadeNodeGraph to
UsdShadeConnectableAPI, so that a NodeGraph can be passed into any
function that accepts a ConnectableAPI.

"""
   result["NodeGraph"].CreateInput.im_func.func_doc = """CreateInput(name, typeName) -> USDSHADE_API UsdShadeInput

name : TfToken
typeName : SdfValueTypeName


Create an Input which can either have a value or can be connected.


The attribute representing the input is created in the "inputs:"
namespace.

"""
   result["NodeGraph"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSHADE_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["NodeGraph"].GetInputs.im_func.func_doc = """GetInputs() -> USDSHADE_API sequence< UsdShadeInput >



Returns all inputs present on the node-graph.


These are represented by attributes in the "inputs:" namespace.

"""
   result["NodeGraph"].ConnectableAPI.im_func.func_doc = """ConnectableAPI() -> USDSHADE_API UsdShadeConnectableAPI



Contructs and returns a UsdShadeConnectableAPI object with this node-
graph.


Note that most tasks can be accomplished without explicitly
constructing a UsdShadeConnectable API, since connection-related API
such as UsdShadeConnectableAPI::ConnectToSource() are static methods,
and UsdShadeNodeGraph will auto-convert to a UsdShadeConnectableAPI
when passed to functions that want to act generically on a connectable
UsdShadeConnectableAPI object.

"""
   result["NodeGraph"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSHADE_API  TfType


"""
   result["NodeGraph"].CreateOutput.im_func.func_doc = """CreateOutput(name, typeName) -> USDSHADE_API UsdShadeOutput

name : TfToken
typeName : SdfValueTypeName


Create an output which can either have a value or can be connected.


The attribute representing the output is created in the "outputs:"
namespace.

"""
   result["Utils"].__doc__ = """
This class contains a set of utility functions used when authoring and
querying shading networks.

"""
   result["Utils"].WriteNewEncoding.func_doc = """**static** WriteNewEncoding() -> USDSHADE_API bool



Whether the env-setting that enables the writing of new-style encoding
of shading networks is set to 'true'.

"""
   result["Utils"].ReadOldEncoding.func_doc = """**static** ReadOldEncoding() -> USDSHADE_API bool



Whether the env-setting that enables the reading of old-style encoding
of shading networks is set to 'true'.

"""
   result["Utils"].GetBaseNameAndType.func_doc = """**static** GetBaseNameAndType(fullName) -> USDSHADE_API pair< TfToken , UsdShadeAttributeType>

fullName : TfToken


Given the full name of a shading property, returns it's base name and
type.

"""
   result["Utils"].GetFullName.func_doc = """**static** GetFullName(baseName, type) -> USDSHADE_API TfToken

baseName : TfToken
type : AttributeType


Returns the full shading attribute name given the basename and the
type.


C{baseName} is the name of the input or output on the shading node.
C{type} is the UsdShadeAttributeType of the shading attribute.

"""
   result["Utils"].GetPrefixForAttributeType.func_doc = """**static** GetPrefixForAttributeType(sourceType) -> USDSHADE_API string

sourceType : AttributeType


Returns the namespace prefix of the USD attribute associated with the
given shading attribute type.

"""
   result["MaterialBindingAPI"].__doc__ = """
UsdShadeMaterialBindingAPI is an API schema that provides an interface
for binding materials to prims or collections of prims (represented by
UsdCollectionAPI objects).


In the USD shading model, each renderable gprim computes a single
B{resolved Material} that will be used to shade the gprim (exceptions,
of course, for gprims that possess UsdGeomSubsets, as each subset can
be shaded by a different Material). A gprim B{and each of its ancestor
prims} can possess, through the MaterialBindingAPI, both a B{direct}
binding to a Material, and any number of B{collection-based} bindings
to Materials; each binding can be generic or declared for a particular
B{purpose}, and given a specific B{binding strength}. It is the
process of "material resolution" (see
UsdShadeMaterialBindingAPI_MaterialResolution) that examines all of
these bindings, and selects the one Material that best matches the
client's needs.

The intent of B{purpose} is that each gprim should be able to resolve
a Material for any given purpose, which implies it can have
differently bound materials for different purposes. There are two
*special* values of B{purpose} defined in UsdShade, although the API
fully supports specifying arbitrary values for it, for the sake of
extensibility:
   - B{UsdShadeTokens->full} : to be used when the purpose of the
     render is entirely to visualize the truest representation of a scene,
     considering all lighting and material information, at highest
     fidelity.

   - B{UsdShadeTokens->preview} : to be used when the render is in
     service of a goal other than a high fidelity "full" render (such as
     scene manipulation, modeling, or realtime playback). Latency and speed
     are generally of greater concern for preview renders, therefore
     preview materials are generally designed to be "lighterweight"
     compared to full materials.
     A binding can also have no specific purpose at all, in which case, it
     is considered to be the fallback or all-purpose binding (denoted by
     the empty-valued token B{UsdShadeTokens->allPurpose}).

The B{purpose} of a material binding is encoded in the name of the
binding relationship.
   - In the case of a direct binding, the *allPurpose* binding is
     represented by the relationship named B{"material:binding"} . Special-
     purpose direct bindings are represented by relationships named
     B{"material:binding: *purpose*}. A direct binding relationship must
     have a single target path that points to a B{UsdShadeMaterial}.

   - In the case of a collection-based binding, the *allPurpose*
     binding is represented by a relationship named
     "material:binding:collection:<i>bindingName</i>", where B{bindingName}
     establishes an identity for the binding that is unique on the prim.
     Attempting to establish two collection bindings of the same name on
     the same prim will result in the first binding simply being
     overridden. A special-purpose collection-based binding is represented
     by a relationship named
     "material:binding:collection:<i>purpose:bindingName</i>". A
     collection-based binding relationship must have exacly two targets,
     one of which should be a collection-path (see ef
     UsdCollectionAPI::GetCollectionPath() ) and the other should point to
     a B{UsdShadeMaterial}. In the future, we may allow a single collection
     binding to target multiple collections, if we can establish a
     reasonable round-tripping pattern for applications that only allow a
     single collection to be associated with each Material.

B{Note:} Both B{bindingName} and B{purpose} must be non-namespaced
tokens. This allows us to know the role of a binding relationship
simply from the number of tokens in it.
   - B{Two tokens} : the fallback, "all purpose", direct binding,
     *material:binding*

   - B{Three tokens} : a purpose-restricted, direct, fallback binding,
     e.g. material:binding:preview

   - B{Four tokens} : an all-purpose, collection-based binding, e.g.
     material:binding:collection:metalBits

   - B{Five tokens} : a purpose-restricted, collection-based binding,
     e.g. material:binding:collection:full:metalBits

A B{binding-strength} value is used to specify whether a binding
authored on a prim should be weaker or stronger than bindings that
appear lower in namespace. We encode the binding strength with as
token-valued metadata B{'bindMaterialAs'} for future flexibility, even
though for now, there are only two possible values:
*UsdShadeTokens->weakerThanDescendants* and
*UsdShadeTokens->strongerThanDescendants*. When binding-strength is
not authored (i.e. empty) on a binding-relationship, the default
behavior matches UsdShadeTokens->weakerThanDescendants.

If a material binding relationship is a built-in property defined as
part of a typed prim's schema, a fallback value should not be provided
for it. This is because the "material resolution" algorithm only
conisders *authored* properties.

"""
   result["MaterialBindingAPI"].CreateMaterialBindSubset.func_doc = """CreateMaterialBindSubset(subsetName, indices, elementType) -> USDSHADE_API UsdGeomSubset

subsetName : TfToken
indices : VtIntArray
elementType : TfToken


Creates a GeomSubset named C{subsetName} with element type,
C{elementType} and familyName B{materialBind B{below this prim.}}


If a GeomSubset named C{subsetName} already exists, then its
"familyName" is updated to be UsdShadeTokens->materialBind and its
indices (at *default* timeCode) are updated with the provided
C{indices} value before returning.

This method forces the familyType of the "materialBind" family of
subsets to UsdGeomTokens->nonOverlapping if it's unset or explicitly
set to UsdGeomTokens->unrestricted.

The default value C{elementType} is UsdGeomTokens->face, as we expect
materials to be bound most often to subsets of faces on meshes.

"""
   result["MaterialBindingAPI"].GetCollectionBindingRel.im_func.func_doc = """GetCollectionBindingRel(bindingName, materialPurpose) -> USDSHADE_API UsdRelationship

bindingName : TfToken
materialPurpose : TfToken


Returns the collection-based material-binding relationship with the
given C{bindingName} and C{materialPurpose} on this prim.


For info on C{bindingName}, see UsdShadeMaterialBindingAPI::Bind() .
The material purpose of the relationship that's returned will match
the specified C{materialPurpose}.

"""
   result["MaterialBindingAPI"].DirectBinding.__doc__ = """
This class represents a direct material binding.

"""
   result["MaterialBindingAPI"].DirectBinding.GetBindingRel.im_func.func_doc = """GetBindingRel() -> UsdRelationship



Returns the binding-relationship that represents this direct binding.

"""
   result["MaterialBindingAPI"].DirectBinding.GetMaterialPurpose.im_func.func_doc = """GetMaterialPurpose() -> TfToken



Returns the purpose of the direct binding.

"""
   result["MaterialBindingAPI"].DirectBinding.GetMaterial.im_func.func_doc = """GetMaterial() -> USDSHADE_API UsdShadeMaterial



Gets the material object that this direct binding binds to.

"""
   result["MaterialBindingAPI"].DirectBinding.GetMaterialPath.im_func.func_doc = """GetMaterialPath() -> SdfPath



Returns the path to the material that is bound to by this direct
binding.

"""
   result["MaterialBindingAPI"].DirectBinding.__init__.im_func.func_doc = """__init__()



Default constructor initializes a DirectBinding object with invalid
material and bindingRel data members.


----------------------------------------------------------------------
__init__(bindingRel) -> USDSHADE_API

bindingRel : UsdRelationship

"""
   result["MaterialBindingAPI"].GetDirectBindingRel.im_func.func_doc = """GetDirectBindingRel(materialPurpose) -> USDSHADE_API UsdRelationship

materialPurpose : TfToken


Returns the direct material-binding relationship on this prim for the
given material purpose.


The material purpose of the relationship that's returned will match
the specified C{materialPurpose}.

"""
   result["MaterialBindingAPI"].GetCollectionBindingRels.im_func.func_doc = """GetCollectionBindingRels(materialPurpose) -> USDSHADE_API sequence< UsdRelationship >

materialPurpose : TfToken


Returns the list of collection-based material binding relationships on
this prim for the given material purpose, C{materialPurpose}.


The returned list of binding relationships will be in native property
order. See UsdPrim::GetPropertyOrder() , UsdPrim::SetPropertyOrder() .
Bindings that appear earlier in the property order are considered to
be stronger than the ones that come later. See rule #6 in
UsdShadeMaterialBindingAPI_MaterialResolution.

"""
   result["MaterialBindingAPI"].GetDirectBinding.im_func.func_doc = """GetDirectBinding(materialPurpose) -> USDSHADE_API DirectBinding

materialPurpose : TfToken


Computes and returns the direct binding for the given material purpose
on this prim.


The returned binding always has the specified C{materialPurpose} (i.e.
the all-purpose binding is not returned if a special purpose binding
is requested).

If the direct binding is to a prim that is not a Material, this does
not generate an error, but the returned Material will be invalid (i.e.
evaluate to false).

"""
   result["MaterialBindingAPI"].SetMaterialBindingStrength.func_doc = """**static** SetMaterialBindingStrength(bindingRel, bindingStrength) -> USDSHADE_API bool

bindingRel : UsdRelationship
bindingStrength : TfToken


Sets the 'bindMaterialAs' token-valued metadata on the given binding
relationship.


If C{bindingStrength} is *UsdShadeTokens->fallbackStrength*, the value
UsdShadeTokens->weakerThanDescendants is authored sparsely, i.e. only
when there is a different existing bindingStrength value. To stamp out
the bindingStrength value explicitly, clients can pass in
UsdShadeTokens->weakerThanDescendants or
UsdShadeTokens->strongerThanDescendants directly. Returns true on
success, false otherwise.

UsdShadeMaterialBindingAPI::GetMaterialBindingStrength()

"""
   result["MaterialBindingAPI"].CollectionBinding.__doc__ = """
This struct is used to represent a collection-based material binding,
which contains two objects - a collection and a bound material.

"""
   result["MaterialBindingAPI"].CollectionBinding.GetMaterial.im_func.func_doc = """GetMaterial() -> USDSHADE_API UsdShadeMaterial



Constructs and returns the material object that this collection-based
binding binds to.

"""
   result["MaterialBindingAPI"].CollectionBinding.IsValid.im_func.func_doc = """IsValid() -> bool



Returns true if the CollectionBinding points to a valid material and
collection.

"""
   result["MaterialBindingAPI"].CollectionBinding.GetCollectionPath.im_func.func_doc = """GetCollectionPath() -> SdfPath



Returns the path to the collection that is bound by this binding.

"""
   result["MaterialBindingAPI"].CollectionBinding.GetCollection.im_func.func_doc = """GetCollection() -> USDSHADE_API UsdCollectionAPI



Constructs and returns the CollectionAPI object for the collection
that is bound by this collection-binding.

"""
   result["MaterialBindingAPI"].CollectionBinding.GetBindingRel.im_func.func_doc = """GetBindingRel() -> UsdRelationship



Returns the binding-relationship that represents this collection-
based binding.

"""
   result["MaterialBindingAPI"].CollectionBinding.__init__.im_func.func_doc = """__init__()



Default constructor initializes a CollectionBinding object with
invalid collection, material and bindingRel data members.


----------------------------------------------------------------------
__init__(collBindingRel) -> USDSHADE_API

collBindingRel : UsdRelationship


Constructs a CollectionBinding object from the given collection-
binding relationship.


This inspects the targets of the relationship and determines the bound
collection and the target material that the collection is bound to.

"""
   result["MaterialBindingAPI"].CollectionBinding.GetMaterialPath.im_func.func_doc = """GetMaterialPath() -> SdfPath



Returns the path to the material that is bound to by this binding.

"""
   result["MaterialBindingAPI"].ComputeBoundMaterials.func_doc = """**static** ComputeBoundMaterials(prims, materialPurpose, bindingRels) -> USDSHADE_API sequence< UsdShadeMaterial >

prims : sequence< UsdPrim >
materialPurpose : TfToken
bindingRels : sequence< UsdRelationship >


Static API for efficiently and concurrently computing the resolved
material bindings for a vector of UsdPrims, C{prims} for the given
C{materialPurpose}.


The size of the returned vector always matches the size of the input
vector, C{prims}. If a prim is not bound to any material, an invalid
or empty UsdShadeMaterial is returned at the index corresponding to
it.

If the pointer C{bindingRels} points to a valid vector, then it is
populated with the set of all "winning" binding relationships.

The python version of this method returns a tuple containing two lists
- the bound materials and the corresponding "winning" binding
relationships.

"""
   result["MaterialBindingAPI"].GetMaterialBindingStrength.func_doc = """**static** GetMaterialBindingStrength(bindingRel) -> USDSHADE_API TfToken

bindingRel : UsdRelationship


Resolves the 'bindMaterialAs' token-valued metadata on the given
binding relationship and returns it.


If the resolved value is empty, this returns the fallback value
UsdShadeTokens->weakerThanDescendants.

UsdShadeMaterialBindingAPI::SetMaterialBindingStrength()

"""
   result["MaterialBindingAPI"].UnbindDirectBinding.im_func.func_doc = """UnbindDirectBinding(materialPurpose) -> USDSHADE_API bool

materialPurpose : TfToken


Unbinds the direct binding for the given material purpose (
C{materialPurpose}) on this prim.


It accomplishes this by blocking the targets of the binding
relationship in the current edit target.

"""
   result["MaterialBindingAPI"].GetCollectionBindings.im_func.func_doc = """GetCollectionBindings(materialPurpose) -> USDSHADE_API CollectionBindingVector

materialPurpose : TfToken


Returns all the collection-based bindings on this prim for the given
material purpose.


The returned CollectionBinding objects always have the specified
C{materialPurpose} (i.e. the all-purpose binding is not returned if a
special purpose binding is requested).

If one or more collection based bindings are to prims that are not
Materials, this does not generate an error, but the corresponding
Material(s) will be invalid (i.e. evaluate to false).

The python version of this API returns a tuple containing the vector
of CollectionBinding objects and the corresponding vector of binding
relationships.

The returned list of collection-bindings will be in native property
order of the associated binding relationships. See
UsdPrim::GetPropertyOrder() , UsdPrim::SetPropertyOrder() . Binding
relationships that come earlier in the list are considered to be
stronger than the ones that come later. See rule #6 in
UsdShadeMaterialBindingAPI_MaterialResolution.

"""
   result["MaterialBindingAPI"].Bind.im_func.func_doc = """Bind(material, bindingStrength, materialPurpose) -> USDSHADE_API bool

material : Material
bindingStrength : TfToken
materialPurpose : TfToken


Authors a direct binding to the given C{material} on this prim.


If C{bindingStrength} is UsdShadeTokens->fallbackStrength, the value
UsdShadeTokens->weakerThanDescendants is authored sparsely. To stamp
out the bindingStrength value explicitly, clients can pass in
UsdShadeTokens->weakerThanDescendants or
UsdShadeTokens->strongerThanDescendants directly.

If C{materialPurpose} is specified and isn't equal to
UsdShadeTokens->allPurpose, the binding only applies to the specified
material purpose.

Returns true on success, false otherwise.


----------------------------------------------------------------------
Bind(collection, material, bindingName, bindingStrength, materialPurpose) -> USDSHADE_API bool

collection : UsdCollectionAPI
material : Material
bindingName : TfToken
bindingStrength : TfToken
materialPurpose : TfToken


Authors a collection-based binding, which binds the given C{material}
to the given C{collection} on this prim.


C{bindingName} establishes an identity for the binding that is unique
on the prim. Attempting to establish two collection bindings of the
same name on the same prim will result in the first binding simply
being overridden. If C{bindingName} is empty, it is set to the base-
name of the collection being bound (which is the collection-name with
any namespaces stripped out). If there are multiple collections with
the same base-name being bound at the same prim, clients should pass
in a unique binding name per binding, in order to preserve all
bindings. The binding name used in constructing the collection-binding
relationship name shoud not contain namespaces. Hence, a coding error
is issued and no binding is authored if the provided value of
C{bindingName} is non-empty and contains namespaces.

If C{bindingStrength} is *UsdShadeTokens->fallbackStrength*, the value
UsdShadeTokens->weakerThanDescendants is authored sparsely, i.e. only
when there is an existing binding with a different bindingStrength. To
stamp out the bindingStrength value explicitly, clients can pass in
UsdShadeTokens->weakerThanDescendants or
UsdShadeTokens->strongerThanDescendants directly.

If C{materialPurpose} is specified and isn't equal to
UsdShadeTokens->allPurpose, the binding only applies to the specified
material purpose.

Returns true on success, false otherwise.

"""
   result["MaterialBindingAPI"].GetMaterialBindSubsetsFamilyType.func_doc = """GetMaterialBindSubsetsFamilyType() -> USDSHADE_API TfToken



Returns the familyType of the family of "materialBind" GeomSubsets on
this prim.


By default, materialBind subsets have familyType="nonOverlapping", but
they can also be tagged as a "partition", using
SetMaterialBindFaceSubsetsFamilyType().

UsdGeomSubset::GetFamilyNameAttr

"""
   result["MaterialBindingAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USDSHADE_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["MaterialBindingAPI"].ComputeBoundMaterial.im_func.func_doc = """ComputeBoundMaterial(bindingsCache, collectionQueryCache, materialPurpose, bindingRel) -> USDSHADE_API UsdShadeMaterial

bindingsCache : BindingsCache
collectionQueryCache : CollectionQueryCache
materialPurpose : TfToken
bindingRel : UsdRelationship


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the resolved bound material for this prim, for the given
material purpose.


This overload of ComputeBoundMaterial makes use of the BindingsCache (
C{bindingsCache}) and CollectionQueryCache ( C{collectionQueryCache})
that are passed in, to avoid redundant binding computations and
computations of MembershipQuery objects for collections. It would be
beneficial to make use of these when resolving bindings for a tree of
prims. These caches are populated lazily as more and more bindings are
resolved.

When the goal is to compute the bound material for a range (or list)
of prims, it is recommended to use this version of
ComputeBoundMaterial() . Here's how you could compute the bindings of
a range of prims efficiently in C++: ::

  std::vector<std::pair<UsdPrim, UsdShadeMaterial> primBindings; 
  UsdShadeMaterialBindingAPI::BindingsCache bindingsCache;
  UsdShadeMaterialBindingAPI::CollectionQueryCache collQueryCache;
  
  for (auto prim : UsdPrimRange(rootPrim)) {
      UsdShadeMaterial boundMaterial = 
            UsdShadeMaterialBindingAPI(prim).ComputeBoundMaterial(
            
& bindingsCache,  &
collQueryCache);
      if (boundMaterial) {
          primBindings.emplace_back({prim, boundMaterial});
      }
  }

If C{bindingRel} is not null, then it is set to the "winning" binding
relationship.

See Bound Material Resolution for details on the material resolution
process.

The python version of this method returns a tuple containing the bound
material and the "winning" binding relationship.


----------------------------------------------------------------------
ComputeBoundMaterial(materialPurpose, bindingRel) -> USDSHADE_API UsdShadeMaterial

materialPurpose : TfToken
bindingRel : UsdRelationship


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes the resolved bound material for this prim, for the given
material purpose.


This overload does not utilize cached MembershipQuery object. However,
it only computes the MembershipQuery of every collection that bound in
the ancestor chain at most once.

If C{bindingRel} is not null, then it is set to the winning binding
relationship.

See Bound Material Resolution for details on the material resolution
process.

The python version of this method returns a tuple containing the bound
material and the "winning" binding relationship.

"""
   result["MaterialBindingAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : UsdPrim


Construct a UsdShadeMaterialBindingAPI on UsdPrim C{prim}.


Equivalent to UsdShadeMaterialBindingAPI::Get (prim.GetStage(),
prim.GetPath()) for a *valid* C{prim}, but will not immediately throw
an error for an invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : UsdSchemaBase


Construct a UsdShadeMaterialBindingAPI on the prim held by
C{schemaObj}.


Should be preferred over UsdShadeMaterialBindingAPI
(schemaObj.GetPrim()), as it preserves SchemaBase state.

"""
   result["MaterialBindingAPI"].AddPrimToBindingCollection.im_func.func_doc = """AddPrimToBindingCollection(prim, bindingName, materialPurpose) -> USDSHADE_API bool

prim : UsdPrim
bindingName : TfToken
materialPurpose : TfToken


Adds the specified C{prim} to the collection targeted by the binding
relationship corresponding to given C{bindingName} and
C{materialPurpose}.


If the collection-binding relationship doesn't exist or if the
targeted collection already includes the C{prim}, then this does
nothing and returns true.

If the targeted collection does not include C{prim} (or excludes it
explicitly), then this modifies the collection by adding the prim to
it (by invoking UsdCollectionAPI::AddPrim()).

"""
   result["MaterialBindingAPI"].Get.func_doc = """**static** Get(stage, path) -> USDSHADE_API UsdShadeMaterialBindingAPI

stage : UsdStagePtr
path : SdfPath


Return a UsdShadeMaterialBindingAPI holding the prim adhering to this
schema at C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdShadeMaterialBindingAPI(stage->GetPrimAtPath(path));


"""
   result["MaterialBindingAPI"].RemovePrimFromBindingCollection.im_func.func_doc = """RemovePrimFromBindingCollection(prim, bindingName, materialPurpose) -> USDSHADE_API bool

prim : UsdPrim
bindingName : TfToken
materialPurpose : TfToken


Removes the specified C{prim} from the collection targeted by the
binding relationship corresponding to given C{bindingName} and
C{materialPurpose}.


If the collection-binding relationship doesn't exist or if the
targeted collection does not include the C{prim}, then this does
nothing and returns true.

If the targeted collection includes C{prim}, then this modifies the
collection by removing the prim from it (by invoking
UsdCollectionAPI::RemovePrim()). This method can be used in
conjunction with the Unbind*() methods (if desired) to guarantee that
a prim has no resolved material binding.

"""
   result["MaterialBindingAPI"].GetMaterialBindSubsets.func_doc = """GetMaterialBindSubsets() -> USDSHADE_API sequence< UsdGeomSubset >



Returns all the existing GeomSubsets with
familyName=UsdShadeTokens->materialBind below this prim.

"""
   result["MaterialBindingAPI"].Apply.func_doc = """**static** Apply(prim) -> USDSHADE_API UsdShadeMaterialBindingAPI

prim : UsdPrim


Applies this B{single-apply} API schema to the given C{prim}.


This information is stored by adding "MaterialBindingAPI" to the
token-valued, listOp metadata *apiSchemas* on the prim.

A valid UsdShadeMaterialBindingAPI object is returned upon success. An
invalid (or empty) UsdShadeMaterialBindingAPI object is returned upon
failure. See UsdAPISchemaBase::_ApplyAPISchema() for conditions
resulting in failure.

UsdPrim::GetAppliedSchemas()

UsdPrim::HasAPI()

"""
   result["MaterialBindingAPI"].UnbindAllBindings.im_func.func_doc = """UnbindAllBindings() -> USDSHADE_API bool



Unbinds all direct and collection-based bindings on this prim.

"""
   result["MaterialBindingAPI"].UnbindCollectionBinding.im_func.func_doc = """UnbindCollectionBinding(bindingName, materialPurpose) -> USDSHADE_API bool

bindingName : TfToken
materialPurpose : TfToken


Unbinds the collection-based binding with the given C{bindingName},
for the given C{materialPurpose} on this prim.


It accomplishes this by blocking the targets of the associated binding
relationship in the current edit target.

"""
   result["MaterialBindingAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USDSHADE_API  TfType


"""
   result["MaterialBindingAPI"].SetMaterialBindSubsetsFamilyType.func_doc = """SetMaterialBindSubsetsFamilyType(familyType) -> USDSHADE_API bool

familyType : TfToken


Author the *familyType* of the "materialBind" family of GeomSubsets on
this prim.


The default C{familyType} is *UsdGeomTokens->nonOverlapping *. It can
be set to *UsdGeomTokens->partition* to indicate that the entire
imageable prim is included in the union of all the "materialBind"
subsets. The family type should never be set to
UsdGeomTokens->unrestricted, since it is invalid for a single piece of
geometry (in this case, a subset) to be bound to more than one
material. Hence, a coding error is issued if C{familyType} is
UsdGeomTokens->unrestricted.**

**

UsdGeomSubset::SetFamilyType**

"""