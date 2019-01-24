def Execute(result):
   result["VersionFilter"].__doc__ = """
Enumeration used to select nodes by version.

"""
   result["FsHelpersDiscoverNodes"].func_doc = """FsHelpersDiscoverNodes(searchPaths, allowedExtensions, followSymlinks, context) -> NDR_API NdrNodeDiscoveryResultVec

searchPaths : StringVec
allowedExtensions : StringVec
followSymlinks : bool
context : DiscoveryPluginContext


Walks the specified search paths, optionally following symlinks.


Paths are walked recursively, and each directory has
C{FsHelpersExamineFiles()} called on it. Only files that match one of
the provided extensions (case insensitive) are candidates for being
turned into C{NdrDiscoveryResult} s. Returns a vector of discovery
results that have been found while walking the search paths. In each
result the name and identifier will be the same, the version will be
invalid and default, and the family will be empty. The caller is
expected to adjust these as appropriate. A naive client with no
versions and no family will work correctly.

"""
   result["Node"].__doc__ = """
Represents an abstract node.


Describes information like the name of the node, what its inputs and
outputs are, and any associated metadata.

In almost all cases, this class will not be used directly. More
specialized nodes can be created that derive from C{NdrNode}; those
specialized nodes can add their own domain-specific data and methods.

"""
   result["Node"].GetFamily.im_func.func_doc = """GetFamily() -> TfToken



Gets the name of the family that the node belongs to.


An empty token will be returned if the node does not belong to a
family.

"""
   result["Node"].GetSourceURI.im_func.func_doc = """GetSourceURI() -> string



Gets the URI to the resource that this node originated from.


Could be a path to a file, or some other resource identifier.

"""
   result["Node"].GetMetadata.im_func.func_doc = """GetMetadata() -> NDR_API  NdrTokenMap



All metadata that came from the parse process.


Specialized nodes may isolate values in the metadata (with possible
manipulations and/or additional parsing) and expose those values in
their API.

"""
   result["Node"].IsValid.im_func.func_doc = """IsValid() -> NDR_API bool



Whether or not this node is valid.


A node that is valid indicates that the parser plugin was able to
successfully parse the contents of this node.

Note that if a node is not valid, some data like its name, URI, source
code etc. could still be available (data that was obtained during the
discovery process). However, other data that must be gathered from the
parsing process will NOT be available (eg, inputs and outputs).

"""
   result["Node"].GetName.im_func.func_doc = """GetName() -> string



Gets the name of the node.

"""
   result["Node"].GetInputNames.im_func.func_doc = """GetInputNames() -> NDR_API  NdrTokenVec



Get an ordered list of all the input names on this node.

"""
   result["Node"].GetInfoString.im_func.func_doc = """GetInfoString() -> NDR_API string



Gets a string with basic information about this node.


Helpful for things like adding this node to a log.

"""
   result["Node"].GetContext.im_func.func_doc = """GetContext() -> TfToken



Gets the context of the node.


The context is the context that the node declares itself as having
(or, if a particular node does not declare a context, it will be
assigned a default context by the parser).

As a concrete example from the C{Sdr} module, a shader with a
specific source type may perform different duties vs. another shader
with the same source type. For example, one shader with a source type
of C{SdrArgsParser::SourceType} may declare itself as having a context
of 'pattern', while another shader of the same source type may say it
is used for lighting, and thus has a context of 'light'.

"""
   result["Node"].GetInput.im_func.func_doc = """GetInput(inputName) -> NDR_API NdrPropertyConstPtr

inputName : TfToken


Get an input property by name.


C{nullptr} is returned if an input with the given name does not exist.

"""
   result["Node"].GetOutput.im_func.func_doc = """GetOutput(outputName) -> NDR_API NdrPropertyConstPtr

outputName : TfToken


Get an output property by name.


C{nullptr} is returned if an output with the given name does not
exist.

"""
   result["Node"].GetSourceType.im_func.func_doc = """GetSourceType() -> TfToken



Gets the type of source that this node originated from.


Note that this is distinct from C{GetContext()} , which is the type
that the node declares itself as having.

As a concrete example from the C{Sdr} module, several shader parsers
exist and operate on different types of shaders. In this scenario,
each distinct type of shader (OSL, Args, etc) is considered a
different *source*, even though they are all shaders. In addition, the
shaders under each source type may declare themselves as having a
specific context (shaders can serve different roles). See
C{GetContext()} for more information on this.

"""
   result["Node"].GetOutputNames.im_func.func_doc = """GetOutputNames() -> NDR_API  NdrTokenVec



Get an ordered list of all the output names on this node.

"""
   result["Node"].GetIdentifier.im_func.func_doc = """GetIdentifier() -> Identifier



Return the identifier of the node.

"""
   result["Node"].GetVersion.im_func.func_doc = """GetVersion() -> Version



Return the version of the node.

"""
   result["Node"].GetSourceCode.im_func.func_doc = """GetSourceCode() -> string



Returns the source code for this node.


This will be empty for most nodes. It will be non-empty only for the
nodes that are constructed using NdrRegistry::GetNodeFromSourceCode()
, in which case, the source code has not been parsed (or even
compiled) yet.

An unparsed node with non-empty source-code but no properties is
considered to be invalid. Once the node is parsed and the relevant
properties and metadata are extracted from the source code, the node
becomes valid.

NdrNode::IsValid

"""
   result["DiscoveryPlugin"].__doc__ = """
Interface for discovery plugins.


Discovery plugins, like the name implies, find nodes. Where the plugin
searches is up to the plugin that implements this interface. Examples
of discovery plugins could include plugins that look for nodes on the
filesystem, another that finds nodes in a cloud service, and another
that searches a local database. Multiple discovery plugins that search
the filesystem in specific locations/ways could also be created. All
discovery plugins are executed as soon as the registry is
instantiated.

These plugins simply report back to the registry what nodes they found
in a generic way. The registry doesn't know much about the innards of
the nodes yet, just that the nodes exist. Understanding the nodes is
the responsibility of another set of plugins defined by the
C{NdrParserPlugin} interface.

Discovery plugins report back to the registry via
C{NdrNodeDiscoveryResult} s. These are small, lightweight classes that
contain the information for a single node that was found during
discovery. The discovery result only includes node information that
can be gleaned pre-parse, so the data is fairly limited; to see
exactly what's included, and what is expected to be populated, see the
documentation for C{NdrNodeDiscoveryResult}.

How to Create a Discovery Plugin
================================

There are three steps to creating a discovery plugin:
   - Implement the discovery plugin interface, C{NdrDiscoveryPlugin}

   - Register your new plugin with the registry. The registration
     macro must be called in your plugin's implementation file: ::

  NDR_REGISTER_DISCOVERY_PLUGIN(YOUR_DISCOVERY_PLUGIN_CLASS_NAME)

 This macro is available in discoveryPlugin.h.

   - In the same folder as your plugin, create a C{plugInfo.json}
     file. This file must be formatted like so, substituting
     C{YOUR_LIBRARY_NAME}, C{YOUR_CLASS_NAME}, and C{YOUR_DISPLAY_NAME} :
     ::

  {
      "Plugins": [{
          "Type": "module",
          "Name": "YOUR_LIBRARY_NAME",
          "Root": "@PLUG_INFO_ROOT@",
          "LibraryPath": "@PLUG_INFO_LIBRARY_PATH@",
          "ResourcePath": "@PLUG_INFO_RESOURCE_PATH@",
          "Info": {
              "Types": {
                  "YOUR_CLASS_NAME" : {
                      "bases": ["NdrDiscoveryPlugin"],
                      "displayName": "YOUR_DISPLAY_NAME"
                  }
              }
          }
      }]
  }

The NDR ships with one discovery plugin, the
C{_NdrFilesystemDiscoveryPlugin}. Take a look at NDR's plugInfo.json
file for example values for C{YOUR_LIBRARY_NAME}, C{YOUR_CLASS_NAME},
and C{YOUR_DISPLAY_NAME}. If multiple discovery plugins exist in the
same folder, you can continue adding additional plugins under the
C{Types} key in the JSON. More detailed information about the
plugInfo.json format can be found in the documentation for the C{plug}
module (in pxr/base).


"""
   result["DiscoveryPlugin"].DiscoverNodes.im_func.func_doc = """DiscoverNodes(arg1) -> NDR_API NdrNodeDiscoveryResultVec

arg1 : Context


Finds and returns all nodes that the implementing plugin should be
aware of.

"""
   result["DiscoveryPlugin"].GetSearchURIs.im_func.func_doc = """GetSearchURIs() -> NDR_API  NdrStringVec



Gets the URIs that this plugin is searching for nodes in.

"""
   result["DiscoveryPluginContext"].__doc__ = """
A context for discovery.


Discovery plugins can use this to get a limited set of non-local
information without direct coupling between plugins.

"""
   result["DiscoveryPluginContext"].GetSourceType.im_func.func_doc = """GetSourceType(discoveryType) -> NDR_API TfToken

discoveryType : TfToken


Returns the source type associated with the discovery type.


This may return an empty token if there is no such association.

"""
   result["Property"].__doc__ = """
Represents a property (input or output) that is part of a C{NdrNode}
instance.


A property must have a name and type, but may also specify a host of
additional metadata. Instances can also be queried to determine if
another C{NdrProperty} instance can be connected to it.

In almost all cases, this class will not be used directly. More
specialized properties can be created that derive from C{NdrProperty};
those specialized properties can add their own domain-specific data
and methods.

"""
   result["Property"].IsArray.im_func.func_doc = """IsArray() -> NDR_API bool



Whether this property's type is an array type.

"""
   result["Property"].IsConnectable.im_func.func_doc = """IsConnectable() -> NDR_API bool



Whether this property can be connected to other properties.

"""
   result["Property"].GetDefaultValue.im_func.func_doc = """GetDefaultValue() -> NDR_API  VtValue



Gets this property's default value.

"""
   result["Property"].GetMetadata.im_func.func_doc = """GetMetadata() -> NDR_API  NdrTokenMap



All of the metadata that came from the parse process.

"""
   result["Property"].GetName.im_func.func_doc = """GetName() -> NDR_API  TfToken



Gets the name of the property.

"""
   result["Property"].GetType.im_func.func_doc = """GetType() -> NDR_API  TfToken



Gets the type of the property.

"""
   result["Property"].GetInfoString.im_func.func_doc = """GetInfoString() -> NDR_API string



Gets a string with basic information about this property.


Helpful for things like adding this property to a log.

"""
   result["Property"].IsDynamicArray.im_func.func_doc = """IsDynamicArray() -> NDR_API bool



Whether this property's array type is dynamically-sized.

"""
   result["Property"].CanConnectTo.im_func.func_doc = """CanConnectTo(other) -> NDR_API bool

other : Property


Determines if this property can be connected to the specified
property.

"""
   result["Property"].GetArraySize.im_func.func_doc = """GetArraySize() -> NDR_API int



Gets this property's array size.


If this property is a fixed-size array type, the array size is
returned. In the case of a dynamically-sized array, this method
returns the array size that the parser reports, and should not be
relied upon to be accurate. A parser may report -1 for the array size,
for example, to indicate a dynamically-sized array. For types that are
not a fixed-size array or dynamic array, this returns 0.

"""
   result["Property"].GetTypeAsSdfType.im_func.func_doc = """GetTypeAsSdfType() -> NDR_API  SdfTypeIndicator



Converts the property's type from C{GetType()} into a
C{SdfValueTypeName}.


Two scenarios can result: an exact mapping from property type to Sdf
type, and an inexact mapping. In the first scenario, the first element
in the pair will be the cleanly-mapped Sdf type, and the second
element, a TfToken, will be empty. In the second scenario, the Sdf
type will be set to C{Token} to indicate an unclean mapping, and the
second element will be set to the original type returned by
C{GetType()} .

This base property class is generic and cannot know ahead of time how
to perform this mapping reliably, thus it will always fall into the
second scenario. It is up to specialized properties to perform the
mapping.

"""
   result["Property"].IsOutput.im_func.func_doc = """IsOutput() -> NDR_API bool



Whether this property is an output.

"""
   result["Registry"].__doc__ = """Registry(arg1) -> Node Definition

arg1 : NDR

"""
   result["NodeDiscoveryResult"].__doc__ = """
Represents the raw data of a node, and some other bits of metadata,
that were determined via a C{NdrDiscoveryPlugin}.

"""
   result["NodeDiscoveryResult"].__init__.im_func.func_doc = """__init__(identifier, version, name, family, discoveryType, sourceType, uri, resolvedUri, sourceCode, metadata, blindData)

identifier : Identifier
version : Version
name : string
family : TfToken
discoveryType : TfToken
sourceType : TfToken
uri : string
resolvedUri : string
sourceCode : string
metadata : TokenMap
blindData : string


Constructor.

"""
   result["Version"].__doc__ = """"""
   result["Version"].GetStringSuffix.im_func.func_doc = """GetStringSuffix() -> NDR_API string



Return the version as a identifier suffix.

"""
   result["Version"].__init__.im_func.func_doc = """__init__() -> NDR_API



Create an invalid version.


----------------------------------------------------------------------
__init__(major, minor) -> NDR_API

major : int
minor : int


Create a version with the given major and minor numbers.


Numbers must be non-negative, and at least one must be non-zero.  On
failure generates an error and yields an invalid version.


----------------------------------------------------------------------
__init__(x) -> NDR_API

x : string


Create a version from a string.


On failure generates an error and yields an invalid version.


----------------------------------------------------------------------
__init__(x, arg2)

x : Version
arg2 : bool

"""
   result["Version"].GetMinor.im_func.func_doc = """GetMinor() -> NDR_API int



Return the minor version number or zero for an invalid version.

"""
   result["Version"].GetAsDefault.im_func.func_doc = """GetAsDefault() -> NDR_API NdrVersion



Return an equal version marked as default.


It's permitted to mark an invalid version as the default.

"""
   result["Version"].GetMajor.im_func.func_doc = """GetMajor() -> NDR_API int



Return the major version number or zero for an invalid version.

"""
   result["Version"].IsDefault.im_func.func_doc = """IsDefault() -> NDR_API bool



Return true iff this version is marked as default.

"""
   result["Registry"].__doc__ = """
The registry provides access to node information.


"Discovery Plugins" are responsible for finding the nodes that should
be included in the registry.

Discovery plugins are found through the plugin system. If additional
discovery plugins need to be specified, a client can pass them to
C{SetExtraDiscoveryPlugins()} .

When the registry is first told about the discovery plugins, the
plugins will be asked to discover nodes. These plugins will generate
C{NdrNodeDiscoveryResult} instances, which only contain basic
metadata. Once the client asks for information that would require the
node's contents to be parsed (eg, what its inputs and outputs are),
the registry will begin the parsing process on an as-needed basis. See
C{NdrNodeDiscoveryResult} for the information that can be retrieved
without triggering a parse.

Some methods in this module may allow for a "family" to be provided.
A family is simply a generic grouping which is optional.

"""
   result["Registry"].GetNodeByIdentifier.im_func.func_doc = """GetNodeByIdentifier(identifier, typePriority) -> NDR_API NdrNodeConstPtr

identifier : Identifier
typePriority : TokenVec


Get the node with the specified identifier, and an optional priority
list specifying the set of node SOURCE types (see
C{NdrNode::GetSourceType()} ) that should be searched.


Nodes of the same identifier but different source type can exist in
the registry. If a node 'Foo' with source types 'abc' and 'xyz' exist
in the registry, and you want to make sure the 'abc' version is
fetched before the 'xyz' version, the priority list would be specified
as ['abc', 'xyz']. If the 'abc' version did not exist in the registry,
then the 'xyz' version would be returned.

Note that this *will* run the parsing routine. However, unlike some
other methods that run parsing, this will only parse the node(s) that
matches the specified identifier and type(s).

Returns C{nullptr} if a node matching the arguments can't be found.

"""
   result["Registry"].GetSearchURIs.im_func.func_doc = """GetSearchURIs() -> NDR_API NdrStringVec



Get the locations where the registry is searching for nodes.


Depending on which discovery plugins were used, this may include non-
filesystem paths.

"""
   result["Registry"].GetNodesByName.im_func.func_doc = """GetNodesByName(name, filter) -> NDR_API NdrNodeConstPtrVec

name : string
filter : VersionFilter


Get all nodes matching the specified name.


Only nodes matching the specified name will be parsed. Optionally, a
filter can be specified to get just the default version (the default)
or all versions of the node. If no nodes match an empty vector is
returned.

"""
   result["Registry"].GetNodesByIdentifier.im_func.func_doc = """GetNodesByIdentifier(identifier) -> NDR_API NdrNodeConstPtrVec

identifier : Identifier


Get all nodes matching the specified identifier (multiple nodes of the
same identifier, but different source types, may exist).


Only nodes matching the specified identifier will be parsed. If no
nodes match the identifier, an empty vector is returned.

"""
   result["Registry"].GetNodeByIdentifierAndType.im_func.func_doc = """GetNodeByIdentifierAndType(identifier, nodeType) -> NDR_API NdrNodeConstPtr

identifier : Identifier
nodeType : TfToken


A convenience wrapper around C{GetNodeByIdentifier()} .


Instead of providing a priority list, an exact type is specified, and
C{nullptr} is returned if a node with the exact identifier and type
does not exist.

"""
   result["Registry"].GetNodeByNameAndType.im_func.func_doc = """GetNodeByNameAndType(name, nodeType, filter) -> NDR_API NdrNodeConstPtr

name : string
nodeType : TfToken
filter : VersionFilter


A convenience wrapper around C{GetNodeByName()} .


Instead of providing a priority list, an exact type is specified, and
C{nullptr} is returned if a node with the exact identifier and type
does not exist.

Optionally, a filter can be specified to consider just the default
versions of nodes matching C{name} (the default) or all versions of
the nodes.

"""
   result["Registry"].GetNodeIdentifiers.im_func.func_doc = """GetNodeIdentifiers(family, filter) -> NDR_API NdrIdentifierVec

family : TfToken
filter : VersionFilter


Get the identifiers of all the nodes that the registry is aware of.


This will not run the parsing plugins on the nodes that have been
discovered, so this method is relatively quick. Optionally, a "family"
name can be specified to only get the identifiers of nodes that belong
to that family and a filter can be specified to get just the default
version (the default) or all versions of the node.

"""
   result["Registry"].__init__.im_func.func_doc = """__init__(arg1)

arg1 : Registry


----------------------------------------------------------------------
__init__() -> NDR_API


"""
   result["Registry"].GetNodeByName.im_func.func_doc = """GetNodeByName(name, typePriority, filter) -> NDR_API NdrNodeConstPtr

name : string
typePriority : TokenVec
filter : VersionFilter


Get the node with the specified name.


An optional priority list specifies the set of node SOURCE types (

NdrNode::GetSourceType() ) that should be searched and in what order.
Optionally, a filter can be specified to consider just the default
versions of nodes matching C{name} (the default) or all versions of
the nodes.

GetNodeByIdentifier() .

"""
   result["Registry"].GetNodeFromSourceCode.im_func.func_doc = """GetNodeFromSourceCode(sourceCode, sourceType, metadata) -> NDR_API NdrNodeConstPtr

sourceCode : string
sourceType : TfToken
metadata : TokenMap


Parses the given C{sourceCode} string, constructs a NdrNode from it
and adds it to the registry.


The parser to be used is determined by the specified C{sourceType}.

Nodes created from source code using this API can be looked up by the
unique identifier and sourceType of the returned node.

C{metadata} contains additional metadata needed for parsing and
compiling the source code correctly. This metadata supplements the
metadata available in C{sourceCode} and overrides it cases where there
are key collisions.

Returns a valid node if the given source code is parsed successfully
using the parser plugins that is registered for the specified
C{sourceType}.

"""
   result["Registry"].SetExtraDiscoveryPlugins.im_func.func_doc = """SetExtraDiscoveryPlugins(plugins) -> NDR_API void

plugins : DiscoveryPluginPtrVec


Allows the client to set any additional discovery plugins that would
otherwise NOT be found through the plugin system.


Runs the discovery process for the specified plugins immediately.

Note that this method cannot be called after any nodes in the registry
have been parsed (eg, through GetNode*()), otherwise an error will
result.

"""
   result["Registry"].GetNodesByFamily.im_func.func_doc = """GetNodesByFamily(family, filter) -> NDR_API NdrNodeConstPtrVec

family : TfToken
filter : VersionFilter


Get all nodes from the registry, optionally restricted to the nodes
that fall under a specified family and/or the default version.


Note that this will parse *all* nodes that the registry is aware of
(unless a family is specified), so this may take some time to run the
first time it is called.

"""
   result["Registry"].GetNodeByURI.im_func.func_doc = """GetNodeByURI(uri) -> NDR_API NdrNodeConstPtr

uri : string


Gets the node matching the specified URI (eg, a filesystem path).


The URI specified here must match the node's URI *exactly* (eg, a
relative filesystem path would not match an absolute path). Only runs
the parsing process for the single node matching the specified URI.
Returns C{nullptr} if a node matching the URI does not exist.

"""
   result["Registry"].GetAllNodeSourceTypes.im_func.func_doc = """GetAllNodeSourceTypes() -> NDR_API  NdrTokenVec



Get a list of all node source types that may be present on the nodes
in the registry.


Source types originate from the parser plugins that have been
registered, so the types here depend on the parsers that are
available. Also note that some parser plugins may not advertise a
source type.

See the documentation for C{NdrParserPlugin} and
C{NdrNode::GetSourceType()} for more information.

"""
   result["Registry"].GetNodeFromAsset.im_func.func_doc = """GetNodeFromAsset(asset, metadata) -> NDR_API NdrNodeConstPtr

asset : SdfAssetPath
metadata : TokenMap


Parses the given C{asset}, constucts a NdrNode from it and adds it to
the registry.


Nodes created from an asset using this API can be looked up by the
unique identifier and sourceType of the returned node, or by URI,
which will be set to the unresolved asset path value.

C{metadata} contains additional metadata needed for parsing and
compiling the source code in the file pointed to by C{asset}
correctly. This metadata supplements the metadata available in the
asset and overrides it in cases where there are key collisions.

Returns a valid node if the asset is parsed successfully using one of
the registered parser plugins.

"""
   result["Registry"].GetNodeNames.im_func.func_doc = """GetNodeNames(family) -> NDR_API NdrStringVec

family : TfToken


Get the names of all the nodes that the registry is aware of.


This will not run the parsing plugins on the nodes that have been
discovered, so this method is relatively quick. Optionally, a "family"
name can be specified to only get the names of nodes that belong to
that family.

"""