def Execute(result):
   result["ShaderNode"].__doc__ = """
A specialized version of C{NdrNode} which holds shading information.

"""
   result["ShaderNode"].GetPropertyNamesForPage.im_func.func_doc = """GetPropertyNamesForPage(pageName) -> SDR_API NdrTokenVec

pageName : string


Gets the names of the properties on a certain page (one that was
returned by C{GetPages()} ).


To get properties that are not assigned to a page, an empty string can
be used for C{pageName}.

"""
   result["ShaderNode"].GetDepartments.im_func.func_doc = """GetDepartments() -> SDR_API  NdrTokenVec



The departments this node is associated with, if any.

"""
   result["ShaderNode"].GetPages.im_func.func_doc = """GetPages() -> SDR_API  NdrTokenVec



Gets the pages on which the node's properties reside (an aggregate of
the unique C{SdrShaderProperty::GetPage()} values for all of the
node's properties).


Nodes themselves do not reside on pages. In an example scenario,
properties might be divided into two pages, 'Simple' and 'Advanced'.

"""
   result["ShaderNode"].GetImplementationName.im_func.func_doc = """GetImplementationName() -> SDR_API  string



Returns the implementation name of this node.


The name of the node is how to refer to the node in shader networks.
The label is how to present this node to users. The implementation
name is the name of the function (or something) this node represents
in the implementation. Any client using the implementation B{must}
call this method to get the correct name; using C{getName()} is not
correct.

"""
   result["ShaderNode"].GetShaderOutput.im_func.func_doc = """GetShaderOutput(outputName) -> SDR_API SdrShaderPropertyConstPtr

outputName : TfToken


Get a shader output property by name.


C{nullptr} is returned if an output with the given name does not
exist.

"""
   result["ShaderNode"].GetPrimvars.im_func.func_doc = """GetPrimvars() -> SDR_API  NdrTokenVec



The list of primvars that this node uses (note that additional
primvars may also be present on specific input properties' values; the
properties that primvars are provided on can be determined via
C{GetAdditionalPrimvarProperties()} ).

"""
   result["ShaderNode"].GetAllVstructNames.im_func.func_doc = """GetAllVstructNames() -> SDR_API NdrTokenVec



Gets all vstructs that are present in the shader.

"""
   result["ShaderNode"].GetHelp.im_func.func_doc = """GetHelp() -> SDR_API  string



The help message assigned to this node, if any.

"""
   result["ShaderNode"].GetAdditionalPrimvarProperties.im_func.func_doc = """GetAdditionalPrimvarProperties() -> SDR_API  NdrTokenVec



The list of string input properties whose values provide the names of
additional primvars consumed by this node.

"""
   result["ShaderNode"].GetLabel.im_func.func_doc = """GetLabel() -> SDR_API  TfToken



The label assigned to this node, if any.


Distinct from the name returned from C{GetName()} . In the context of
a UI, the label value might be used as the display name for the node
instead of the name.

"""
   result["ShaderNode"].GetCategory.im_func.func_doc = """GetCategory() -> SDR_API  TfToken



The category assigned to this node, if any.


Distinct from the family returned from C{GetFamily()} .

"""
   result["ShaderNode"].GetShaderInput.im_func.func_doc = """GetShaderInput(inputName) -> SDR_API SdrShaderPropertyConstPtr

inputName : TfToken


Get a shader input property by name.


C{nullptr} is returned if an input with the given name does not exist.

"""
   result["Registry"].__doc__ = """
The shading-specialized version of C{NdrRegistry}.

"""
   result["Registry"].__init__.im_func.func_doc = """__init__()


"""
   result["Registry"].GetShaderNodeByIdentifierAndType.im_func.func_doc = """GetShaderNodeByIdentifierAndType(identifier, nodeType) -> SDR_API SdrShaderNodeConstPtr

identifier : NdrIdentifier
nodeType : TfToken


Exactly like C{NdrRegistry::GetNodeByIdentifierAndType()} , but
returns a C{SdrShaderNode} pointer instead of a C{NdrNode} pointer.

"""
   result["Registry"].GetShaderNodeByNameAndType.im_func.func_doc = """GetShaderNodeByNameAndType(name, nodeType, filter) -> SDR_API SdrShaderNodeConstPtr

name : string
nodeType : TfToken
filter : NdrVersionFilter


Exactly like C{NdrRegistry::GetNodeByNameAndType()} , but returns a
C{SdrShaderNode} pointer instead of a C{NdrNode} pointer.

"""
   result["Registry"].GetShaderNodesByFamily.im_func.func_doc = """GetShaderNodesByFamily(family, filter) -> SDR_API SdrShaderNodePtrVec

family : TfToken
filter : NdrVersionFilter


Exactly like C{NdrRegistry::GetNodesByFamily()} , but returns a vector
of C{SdrShaderNode} pointers instead of a vector of C{NdrNode}
pointers.

"""
   result["Registry"].GetShaderNodesByName.im_func.func_doc = """GetShaderNodesByName(name, filter) -> SDR_API SdrShaderNodePtrVec

name : string
filter : NdrVersionFilter


Exactly like C{NdrRegistry::GetNodesByName()} , but returns a vector
of C{SdrShaderNode} pointers instead of a vector of C{NdrNode}
pointers.

"""
   result["Registry"].GetShaderNodeByURI.im_func.func_doc = """GetShaderNodeByURI(uri) -> SDR_API SdrShaderNodeConstPtr

uri : string


Exactly like C{NdrRegistry::GetNodeByURI()} , but returns a
C{SdrShaderNode} pointer instead of a C{NdrNode} pointer.

"""
   result["Registry"].GetShaderNodeByIdentifier.im_func.func_doc = """GetShaderNodeByIdentifier(identifier, typePriority) -> SDR_API SdrShaderNodeConstPtr

identifier : NdrIdentifier
typePriority : NdrTokenVec


Exactly like C{NdrRegistry::GetNodeByIdentifier()} , but returns a
C{SdrShaderNode} pointer instead of a C{NdrNode} pointer.

"""
   result["Registry"].GetShaderNodeByName.im_func.func_doc = """GetShaderNodeByName(name, typePriority, filter) -> SDR_API SdrShaderNodeConstPtr

name : string
typePriority : NdrTokenVec
filter : NdrVersionFilter


Exactly like C{NdrRegistry::GetNodeByName()} , but returns a
C{SdrShaderNode} pointer instead of a C{NdrNode} pointer.

"""
   result["Registry"].GetShaderNodeFromSourceCode.im_func.func_doc = """GetShaderNodeFromSourceCode(sourceCode, sourceType, metadata) -> SDR_API SdrShaderNodeConstPtr

sourceCode : string
sourceType : TfToken
metadata : NdrTokenMap


Wrapper method for NdrRegistry::GetNodeFromSourceCode() .


Returns a valid SdrShaderNode pointer upon success.

"""
   result["Registry"].GetShaderNodesByIdentifier.im_func.func_doc = """GetShaderNodesByIdentifier(identifier) -> SDR_API SdrShaderNodePtrVec

identifier : NdrIdentifier


Exactly like C{NdrRegistry::GetNodesByIdentifier()} , but returns a
vector of C{SdrShaderNode} pointers instead of a vector of C{NdrNode}
pointers.

"""
   result["Registry"].GetShaderNodeFromAsset.im_func.func_doc = """GetShaderNodeFromAsset(shaderAsset, metadata) -> SDR_API SdrShaderNodeConstPtr

shaderAsset : SdfAssetPath
metadata : NdrTokenMap


Wrapper method for NdrRegistry::GetNodeFromAsset() .


Returns a valid SdrShaderNode pointer upon success.

"""
   result["Registry"].__doc__ = """Registry(arg1) -> Shader Definition

arg1 : SDR

"""
   result["ShaderProperty"].__doc__ = """
A specialized version of C{NdrProperty} which holds shading
information.

"""
   result["ShaderProperty"].IsVStructMember.im_func.func_doc = """IsVStructMember() -> SDR_API bool



Returns true if this field is part of a vstruct.

"""
   result["ShaderProperty"].GetVStructMemberOf.im_func.func_doc = """GetVStructMemberOf() -> SDR_API  TfToken



If this field is part of a vstruct, this is the name of the struct.

"""
   result["ShaderProperty"].IsAssetIdentifier.im_func.func_doc = """IsAssetIdentifier() -> SDR_API bool



Determines if the value held by this property is an asset identifier
(eg, a file path); the logic for this is left up to the parser.


Note: The type returned from C{GetTypeAsSdfType()} will be C{Asset} if
this method returns C{true} (even though its true underlying data type
is string).

"""
   result["ShaderProperty"].IsVStruct.im_func.func_doc = """IsVStruct() -> SDR_API bool



Returns true if the field is the head of a vstruct.

"""
   result["ShaderProperty"].GetPage.im_func.func_doc = """GetPage() -> SDR_API  TfToken



The page (group), eg "Advanced", this property appears on, if any.

"""
   result["ShaderProperty"].IsConnectable.im_func.func_doc = """IsConnectable() -> SDR_API bool



Whether this property can be connected to other properties.


If this returns C{true}, connectability to a specific property can be
tested via C{CanConnectTo()} .

"""
   result["ShaderProperty"].GetVStructMemberName.im_func.func_doc = """GetVStructMemberName() -> SDR_API  TfToken



If this field is part of a vstruct, this is its name in the struct.

"""
   result["ShaderProperty"].GetTypeAsSdfType.im_func.func_doc = """GetTypeAsSdfType() -> SDR_API  SdfTypeIndicator



Converts the property's type from C{GetType()} into a
C{SdfValueTypeName}.


Two scenarios can result: an exact mapping from property type to Sdf
type, and an inexact mapping. In the first scenario, the first element
in the pair will be the cleanly-mapped Sdf type, and the second
element, a TfToken, will be empty. In the second scenario, the Sdf
type will be set to C{Token} to indicate an unclean mapping, and the
second element will be set to the original type returned by
C{GetType()} .

"""
   result["ShaderProperty"].GetHelp.im_func.func_doc = """GetHelp() -> SDR_API  string



The help message assigned to this property, if any.

"""
   result["ShaderProperty"].GetValidConnectionTypes.im_func.func_doc = """GetValidConnectionTypes() -> SDR_API  NdrTokenVec



Gets the list of valid connection types for this property.


This value comes from shader metadata, and may not be specified. The
value from C{NdrProperty::GetType()} can be used as a fallback, or you
can use the connectability test in C{CanConnectTo()} .

"""
   result["ShaderProperty"].GetLabel.im_func.func_doc = """GetLabel() -> SDR_API  TfToken



The label assigned to this property, if any.


Distinct from the name returned from C{GetName()} . In the context of
a UI, the label value might be used as the display name for the
property instead of the name.

"""
   result["ShaderProperty"].GetWidget.im_func.func_doc = """GetWidget() -> SDR_API  TfToken



The widget "hint" that indicates the widget that can best display the
type of data contained in this property, if any.


Examples of this value could include "number", "slider", etc.

"""
   result["ShaderProperty"].GetOptions.im_func.func_doc = """GetOptions() -> SDR_API  NdrOptionVec



If the property has a set of valid values that are pre-determined,
this will return the valid option names and corresponding string
values (if the option was specified with a value).

"""
   result["ShaderProperty"].GetImplementationName.im_func.func_doc = """GetImplementationName() -> SDR_API  string



Returns the implementation name of this property.


The name of the property is how to refer to the property in shader
networks. The label is how to present this property to users. The
implementation name is the name of the parameter this property
represents in the implementation. Any client using the implementation
B{must} call this method to get the correct name; using C{getName()}
is not correct.

"""
   result["ShaderProperty"].GetHints.im_func.func_doc = """GetHints() -> SDR_API  NdrTokenMap



Any UI "hints" that are associated with this property.


"Hints" are simple key/value pairs.

"""
   result["ShaderProperty"].CanConnectTo.im_func.func_doc = """CanConnectTo(other) -> SDR_API bool

other : NdrProperty


Determines if this property can be connected to the specified
property.

"""