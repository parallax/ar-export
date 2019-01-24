def Execute(result):
   result["ErrorInternalAssetPath"].__doc__ = """
Error about an arc that is prohibited due to being internal to an
asset.

"""
   result["PrimIndex"].__doc__ = """
PcpPrimIndex is an index of the all sites of scene description that
contribute opinions to a specific prim, under composition semantics.


PcpComputePrimIndex() builds an index ("indexes") the given prim site.
At any site there may be scene description values expressing arcs that
represent instructions to pull in further scene description.
PcpComputePrimIndex() recursively follows these arcs, building and
ordering the results.

"""
   result["PrimIndex"].PrintStatistics.im_func.func_doc = """PrintStatistics() -> PCP_API void



Prints various statistics about this prim index.

"""
   result["PrimIndex"].DumpToDotGraph.im_func.func_doc = """DumpToDotGraph(filename, includeInheritOriginInfo, includeMaps) -> PCP_API void

filename : string
includeInheritOriginInfo : bool
includeMaps : bool


Dump the prim index in dot format to the file named C{filename}.


See Dump(...) for information regarding arguments.

"""
   result["PrimIndex"].DumpToString.im_func.func_doc = """DumpToString(includeInheritOriginInfo, includeMaps) -> PCP_API string

includeInheritOriginInfo : bool
includeMaps : bool


Dump the prim index contents to a string.


If C{includeInheritOriginInfo} is C{true}, output for implied inherit
nodes will include information about the originating inherit node. If
C{includeMaps} is C{true}, output for each node will include the
mappings to the parent and root node.

"""
   result["PrimIndex"].ComputePrimChildNames.im_func.func_doc = """ComputePrimChildNames(nameOrder, prohibitedNameSet) -> PCP_API void

nameOrder : TfTokenVector
prohibitedNameSet : TokenSet


Compute the prim child names for the given path.


C{errors} will contain any errors encountered while performing this
operation.

"""
   result["PrimIndex"].IsInstanceable.im_func.func_doc = """IsInstanceable() -> PCP_API bool



Returns true if this prim index is instanceable.


Instanceable prim indexes with the same instance key are guaranteed to
have the same set of opinions, but may not have local opinions about
name children.

PcpInstanceKey

"""
   result["PrimIndex"].ComposeAuthoredVariantSelections.im_func.func_doc = """ComposeAuthoredVariantSelections() -> PCP_API SdfVariantSelectionMap



Compose the authored prim variant selections.


These are the variant selections expressed in scene description. Note
that these selections may not have actually been applied, if they are
invalid.

This result is not cached, but computed each time.

"""
   result["PrimIndex"].IsValid.im_func.func_doc = """IsValid() -> bool



Return true if this index is valid.


A default-constructed index is invalid.

"""
   result["PrimIndex"].ComputePrimPropertyNames.im_func.func_doc = """ComputePrimPropertyNames(nameOrder) -> PCP_API void

nameOrder : TfTokenVector


Compute the prim property names for the given path.


C{errors} will contain any errors encountered while performing this
operation. The C{nameOrder} vector must not contain any duplicate
entries.

"""
   result["PrimIndex"].GetSelectionAppliedForVariantSet.im_func.func_doc = """GetSelectionAppliedForVariantSet(variantSet) -> PCP_API string

variantSet : string


Return the variant selection applied for the named variant set.


If none was applied, this returns an empty string. This can be
different from the authored variant selection; for example, if the
authored selection is invalid.

"""
   result["PayloadContext"].__doc__ = """
Context object that allows PcpPayloadDecorator subclasses to examine
the prim index being constructed.



PcpPayloadDecorator

"""
   result["PayloadContext"].ComposeValue.im_func.func_doc = """ComposeValue(field, fn) -> PCP_API bool

field : TfToken
fn : ComposeFunction


Compose the value of the scene description C{field} using the given
composition function C{fn} from strongest to weakest available
opinion.

"""
   result["ErrorPropertyPermissionDenied"].__doc__ = """
Layers with illegal opinions about private properties.

"""
   result["ErrorOpinionAtRelocationSource"].__doc__ = """
Opinions were found at a relocation source path.

"""
   result["ErrorSublayerCycle"].__doc__ = """
Layers that recursively sublayer themselves.

"""
   result["ErrorInvalidPrimPath"].__doc__ = """
Invalid prim paths used by references or payloads.

"""
   result["ErrorMutedAssetPath"].__doc__ = """
Muted asset paths used by references or payloads.

"""
   result["InstanceKey"].__doc__ = """
A PcpInstanceKey identifies instanceable prim indexes that share the
same set of opinions.


Instanceable prim indexes with equal instance keys are guaranteed to
have the same opinions for name children and properties beneath those
name children. They are NOT guaranteed to have the same opinions for
direct properties of the prim indexes themselves.

"""
   result["InstanceKey"].__init__.im_func.func_doc = """__init__() -> PCP_API



----------------------------------------------------------------------
__init__(primIndex) -> PCP_API

primIndex : PrimIndex


Create an instance key for the given prim index.

"""
   result["ErrorUnresolvedPrimPath"].__doc__ = """
Asset paths that could not be both resolved and loaded.

"""
   result["LayerStack"].__doc__ = """
Represents a stack of layers that contribute opinions to composition.


Each PcpLayerStack is identified by a PcpLayerStackIdentifier. This
identifier contains all of the parameters needed to construct a layer
stack, such as the root layer, session layer, and path resolver
context.

PcpLayerStacks are constructed and managed by a
Pcp_LayerStackRegistry.

"""
   result["ErrorInvalidExternalTargetPath"].__doc__ = """
Invalid target or connection path in some scope that points to an
object outside of that scope.

"""
   result["ErrorType"].__doc__ = """
Enum to indicate the type represented by a Pcp error.

"""
   result["ErrorInconsistentAttributeType"].__doc__ = """
Attributes that have specs with conflicting definitions.

"""
   result["ErrorInconsistentAttributeVariability"].__doc__ = """
Attributes that have specs with conflicting variability.

"""
   result["ErrorInvalidSublayerOwnership"].__doc__ = """
Sibling layers that have the same owner.

"""
   result["__doc__"] = """

Introduction
============

Pcp implements the core scenegraph composition semantics  the behavior
informally referred to as *Layering & Referencing*.

Pcp specializes in providing low-level composition services on behalf
of higher-level scenegraph modules (Usd, Csd, Mf) that instantiate
scenegraph objects based on the results. Most clients will typically
use one of those modules, rather than consulting Pcp directly. The
name "Pcp" stands for *Prim Cache Population*, a historical term for
this area of the system.

Motivation
==========

Objects in the scenegraph are backed by scene description  authored
data describing those objects.

A single file of scene description is sufficient to describe a
hierarchy of objects. However, it is also useful to organize that data
across multiple files. For one thing, this provides a way for multiple
people (such as in different departments) to collaborate while keeping
their contributions distinct. For another, this provides a means of
re-use: an asset like a rig or model can be built once, then used many
times as needed.

This instancing is expressed as a "reference arc" that points at the
external file. The Pcp runtime detects and interprets these arcs to
bring together the disparate files into a single combined set of
opinions. By using a reference arc, the underlying external asset can
be continually worked on, with improvements automatically being picked
up in downstream assets.

There are other kinds of arcs that provide variations of this
behavior. Pcp provides the service of identifying and interpreting
these composition arcs.

Capabilities
============

Pcp implements the following composition semantics:

   - sublayers

   - list-editing

   - references

   - payloads

   - inherits / classes

   - variants

   - "standin" variant preferences

   - relocates

   - permissions

In support of this, the runtime provides these features:

   - caching and cache invalidation

   - change processing

   - dependency tracking

   - namespace editing support

   - path translation

   - error detection

   - payload inclusion control

   - diagnostic output
     Pcp is all about finding sources of opinions that contribute to
     objects. It has little to do with the interpretation of those
     opinions. As a result, there are some higher-level features which are
     sometimes thought of as part of composition, but which are not part of
     Pcp:

   - model hierarchy

   - scenegraph structure, objects and their identity

   - value resolution

   - symmetry

Usage
=====

The main entrypoint to the Pcp algorithm is the PcpCache. It provides
a context to specify the key parameters that configure how composition
should be performed. It also provides storage for caching the results
of composition queries.

The input parameters to the composition algorithm are:

   - a root layer

   - a session layer (optional)

   - a path resolver context

   - standin preferences (ex: render, anim, etc.)

   - payload inclusion set  paths for which payloads should be
     included
     Most of these are fixed when a PcpCache is created. The payload
     inclusion set can be modified at runtime to bring payloads into and
     out of the working set.

Once a cache has been created, it can service composition queries.
These apply composition algorithms to the underlying scene description
data. See the ComputeXXX methods on PcpCache. The most fundamental
queries are PcpCache::ComputeLayerStack() and
PcpCache::ComputePrimIndex() . These two provide the majority of the
composition semantics and are the basis for the other queries.
Different queries return different types of result values.

The process of composition may discover errors in the structure of the
scene. For example, a reference arc might target a file that cannot be
found (resolved), or it might create a reference cycle.

These errors get first-class treatment in Pcp. That is, errors are not
a side-effect; they are treated as a formal output of the composition
algorithms and returned alongside the primary results describing the
structure of the scene. Pcp does not embed any error handling or
reporting policy. It is entirely up to Pcp clients to dispatch errors.

Pcp B{does} participate in the TfError reporting system when it
encounters API misuse (coding errors), as do the lower-level modules
it uses. Pcp only treats errors in authored scene description
specially. Errors are represented as instances of a PcpErrorBase base
class. Each error sub-type contains semantic information about the
source and exact details of the error, as would be required to report
the error to the user, check if the error still applies, or
programmatically address it.

Each Pcp computation stores a "local" set of errors that are specific
to that computation. If one computation requires recursive computation
such as one prim needing to compute a layer stack across a reference
arc  the errors for the nested computation will be stored locally with
that nested computation. Each Pcp result provides a GetLocalErrors()
API to examine its local errors. Since errors are first-class results
of Pcp and stored as part of the primary composition outputs, they are
cached along with those outputs.

Clients of Pcp typically want to report errors when they are first
discovered. They want to do this without needing knowledge about the
cache hit/miss behavior or the recursive nature of composition
queries. To facilitate this common usage, Pcp API provides an
"allErrors" output argument that will accumulate any newly discovered
errors. In the case of cache hits, existing errors will not be
reported.

For simple cases where you just want to raise Pcp errors as Tf runtime
errors, see PcpRaiseErrors().

In addition to the primary result and errors, computations also
internally retain the dependencies discovered by a cached computation
result. For example, computing a PcpPrimIndex that contains a
reference will internally record a dependency representing that
reference. This dependency internally retains the scene description
layer across the reference. Dependencies also provide a means to
analyze and propagate changes to the scene, as well as to implement
namespace editing (rename, reparent, and delete operations), which
want to fix up dependent scene opinions accordingly. PcpCache has API
to query dependencies; for example, see PcpCache::GetPathsUsingSite().

The phrase "namespace editing" means operations that edit namespace:
renaming, reparenting, or removing composed objects. Although Pcp does
not maintain a scenegraph of composed objects, it does provide
utilities for such a module to implement these operations, making use
of the Pcp dependencies to build a list of necessary edits to the
underlying layers that keep them consistent with one another. See
PcpCache::ComputeNamespaceEdits().

Pcp caches computation results derived from the underlying scene
description data. When that underlying data changes, those
computations are no longer valid. Pcp provides assistance to determine
which computations have been invalidated, and to re-compute them as
desired. PcpChanges represents the effect that a set of changes to
scene description have on a PcpCache. Processing changes has two
phases: the first is to build up the list of changes, (including
chasing dependencies to find all the affected caches); the second is
to apply those changes, invalidating the internal caches. It is up to
the client to re-pull on any affected caches. Since dependencies are
dropped when the cached computations that yielded them are
invalidated, PcpLifeboat provides a way to retain the underlying
referenced data for the duration of time until the client can re-pull
on the cached computations.

Every PcpChanges object requested by a scenegraph client contains a
PcpLifeboat, so clients should rarely need to interact with one
directly.

Composition arcs pull together scene description from different places
in layers. Part of this process requires rebinding those opinions to
new paths. For example, a model at the path
C{</World/anim/chars/MeridaGroup/Merida>} may reference a model at the
source path C{</Merida>} . Now imagine a relationship authored within
C{</Merida/rig/FaceRig>} to C{</Merida/anim/Face>.} To resolve that
relationship path, composition needs to transform the authored values
flowing across the arc so that they re-bind to the new namespace
position of Merida, in
C{</World/anim/chars/MeridaGroup/Merida/anim/Face>} . This process is
known as "path translation", and is one of the more subtle and
important behaviors of Pcp. See PcpTranslatePathFromNodeToRoot() and
PcpTranslatePathFromRootToNode() .

Composition is a large subsystem and have can have complicated
results. To help analyze the system we provide a few features:

   - PcpPrimIndex::DumpToString() - to dump out a prim's structure

   - PcpPrimIndex::PrintStatistics() - to analyze a prim's structure

   - PcpCache::PrintStatistics() - to analyze a cache's overall
     footprint

   - TF_DEBUG runtime debugging flags  see pcp/debugCodes.h

   - Optional additional runtime validation that must be compiled in:
     C{PCP_DIAGNOSTIC_VALIDATION}


"""
   result["ArcType"].__doc__ = """
Describes the type of arc connecting two nodes in the prim index.

"""
   result["Dependency"].__doc__ = """
Description of a dependency.

"""
   result["Cache"].__doc__ = """
PcpCache is the context required to make requests of the Pcp
composition algorithm and cache the results.


Because the algorithms are recursive  making a request typically makes
other internal requests to solve subproblems  caching subproblem
results is required for reasonable performance, and so this cache is
the only entrypoint to the algorithms.

There is a set of parameters that affect the composition results:

   - variant fallbacks: per named variant set, an ordered list of
     fallback values to use when composing a prim that defines a variant
     set but does not specify a selection

   - payload inclusion set: an SdfPath set used to identify which
     prims should have their payloads included during composition; this is
     the basis for explicit control over the "working set" of composition

   - target schema: the target schema that Pcp will request when
     opening scene description layers

   - "USD mode" configures the Pcp composition algorithm to provide
     only a custom, lighter subset of the full feature set, as needed by
     the Universal Scene Description system
     There are a number of different computations that can be requested.
     These include computing a layer stack from a PcpLayerStackIdentifier,
     computing a prim index or prim stack, and computing a property index.

"""
   result["Cache"].PrintStatistics.im_func.func_doc = """PrintStatistics() -> PCP_API void



Prints various statistics about the data stored in this cache.

"""
   result["Cache"].FindPropertyIndex.im_func.func_doc = """FindPropertyIndex(propPath) -> PCP_API  PcpPropertyIndex

propPath : SdfPath


Returns a pointer to the cached computed property index for the given
path, or None if it has not been computed.

"""
   result["Cache"].ComputePrimIndex.im_func.func_doc = """ComputePrimIndex(primPath, allErrors) -> PCP_API  PcpPrimIndex

primPath : SdfPath
allErrors : ErrorVector


Compute and return a reference to the cached result for the prim index
for the given path.


C{allErrors} will contain any errors encountered while performing this
operation.

"""
   result["Cache"].GetLayerStackIdentifier.im_func.func_doc = """GetLayerStackIdentifier() -> PCP_API PcpLayerStackIdentifier



Get the identifier of the layerStack used for composition.

"""
   result["Cache"].IsPayloadIncluded.im_func.func_doc = """IsPayloadIncluded(path) -> PCP_API bool

path : SdfPath


Return true if the payload is included for the given path.

"""
   result["Cache"].IsLayerMuted.im_func.func_doc = """IsLayerMuted(layerIdentifier) -> PCP_API bool

layerIdentifier : string


Returns true if the layer specified by C{layerIdentifier} is muted in
this cache, false otherwise.


If C{layerIdentifier} is relative, it is assumed to be relative to
this cache's root layer. See documentation on RequestLayerMuting for
more details.


----------------------------------------------------------------------
IsLayerMuted(anchorLayer, layerIdentifier, canonicalMutedLayerIdentifier) -> PCP_API bool

anchorLayer : SdfLayerHandle
layerIdentifier : string
canonicalMutedLayerIdentifier : string


Returns true if the layer specified by C{layerIdentifier} is muted in
this cache, false otherwise.


If C{layerIdentifier} is relative, it is assumed to be relative to
C{anchorLayer}. If C{canonicalMutedLayerIdentifier} is supplied, it
will be populated with the canonical identifier of the muted layer if
this function returns true. See documentation on RequestLayerMuting
for more details.

"""
   result["Cache"].FindAllLayerStacksUsingLayer.im_func.func_doc = """FindAllLayerStacksUsingLayer(layer) -> PCP_API  PcpLayerStackPtrVector

layer : SdfLayerHandle


Returns every computed & cached layer stack that includes C{layer}.

"""
   result["Cache"].GetMutedLayers.im_func.func_doc = """GetMutedLayers() -> PCP_API  sequence<string>



Returns the list of canonical identifiers for muted layers in this
cache.


See documentation on RequestLayerMuting for more details.

"""
   result["Cache"].FindSiteDependencies.im_func.func_doc = """FindSiteDependencies(siteLayerStack, sitePath, depMask, recurseOnSite, recurseOnIndex, filterForExistingCachesOnly) -> PCP_API PcpDependencyVector

siteLayerStack : LayerStackPtr
sitePath : SdfPath
depMask : DependencyFlags
recurseOnSite : bool
recurseOnIndex : bool
filterForExistingCachesOnly : bool


Returns dependencies on the given site of scene description, as
discovered by the cached index computations.


depMask

specifies what classes of dependency to include; see
PcpDependencyFlags for details recurseOnSite

includes incoming dependencies on children of sitePath recurseOnIndex

extends the result to include all PcpCache child indexes below
discovered results filterForExistingCachesOnly

filters the results to only paths representing computed prim and
property index caches; otherwise a recursively-expanded result can
include un-computed paths that are expected to depend on the site


----------------------------------------------------------------------
FindSiteDependencies(siteLayer, sitePath, depMask, recurseOnSite, recurseOnIndex, filterForExistingCachesOnly) -> PCP_API PcpDependencyVector

siteLayer : SdfLayerHandle
sitePath : SdfPath
depMask : DependencyFlags
recurseOnSite : bool
recurseOnIndex : bool
filterForExistingCachesOnly : bool


Returns dependencies on the given site of scene description, as
discovered by the cached index computations.


This method overload takes a site layer rather than a layer stack. It
will check every layer stack using that layer, and apply any relevant
sublayer offsets to the map functions in the returned
PcpDependencyVector.

See the other method for parameter details.

"""
   result["Cache"].IsInvalidSublayerIdentifier.im_func.func_doc = """IsInvalidSublayerIdentifier(identifier) -> PCP_API bool

identifier : string


Returns true if C{identifier} was used as a sublayer path in a layer
stack but did not identify a valid layer.


This is functionally equivalent to examining the values in the vector
returned by GetInvalidSublayerIdentifiers, but more efficient.

"""
   result["Cache"].ComputePropertyIndex.im_func.func_doc = """ComputePropertyIndex(propPath, allErrors) -> PCP_API  PcpPropertyIndex

propPath : SdfPath
allErrors : ErrorVector


Compute and return a reference to the cached result for the property
index for the given path.


C{allErrors} will contain any errors encountered while performing this
operation.

"""
   result["Cache"].RequestLayerMuting.im_func.func_doc = """RequestLayerMuting(layersToMute, layersToUnmute, changes) -> PCP_API void

layersToMute : sequence<string>
layersToUnmute : sequence<string>
changes : Changes


Request layers to be muted or unmuted in this cache.


Muted layers are ignored during composition and do not appear in any
layer stacks. The root layer of this stage may not be muted;
attempting to do so will generate a coding error. If the root layer of
a reference or payload layer stack is muted, the behavior is as if the
muted layer did not exist, which means a composition error will be
generated.

A canonical identifier for each layer in C{layersToMute} will be
computed using ArResolver::ComputeRepositoryPath. Any layer
encountered during composition with the same repository path will be
considered muted and ignored. Relative paths will be assumed to be
relative to the cache's root layer. Search paths are immediately
resolved and the result is used for computing the canonical path.

Note that muting a layer will cause this cache to release all
references to that layer. If no other client is holding on to
references to that layer, it will be unloaded. In this case, if there
are unsaved edits to the muted layer, those edits are lost.  Since
anonymous layers are not serialized, muting an anonymous layer will
cause that layer and its contents to be lost in this case.

If C{changes} is not C{nullptr}, it is adjusted to reflect the changes
necessary to see the change in muted layers. Otherwise, those changes
are applied immediately.

"""
   result["Cache"].FindPrimIndex.im_func.func_doc = """FindPrimIndex(primPath) -> PCP_API  PcpPrimIndex

primPath : SdfPath


Returns a pointer to the cached computed prim index for the given
path, or None if it has not been computed.

"""
   result["Cache"].ComputeAttributeConnectionPaths.im_func.func_doc = """ComputeAttributeConnectionPaths(attributePath, paths, localOnly, stopProperty, includeStopProperty, allErrors) -> PCP_API void

attributePath : SdfPath
paths : SdfPathVector
localOnly : bool
stopProperty : SdfSpecHandle
includeStopProperty : bool
allErrors : ErrorVector


Compute the attribute connection paths for the attribute at
C{attributePath} into C{paths}.


If C{localOnly} is C{true} then this will compose attribute
connections from local nodes only. If C{stopProperty} is not C{None}
then this will stop composing attribute connections at
C{stopProperty}, including C{stopProperty} iff C{includeStopProperty}
is C{true}. C{allErrors} will contain any errors encountered while
performing this operation.

"""
   result["Cache"].GetUsedLayers.im_func.func_doc = """GetUsedLayers() -> PCP_API SdfLayerHandleSet



Returns set of all layers used by this cache.

"""
   result["Cache"].__init__.im_func.func_doc = """__init__(arg1)

arg1 : Cache


----------------------------------------------------------------------
__init__(layerStackIdentifier, targetSchema, usd, payloadDecorator) -> PCP_API

layerStackIdentifier : LayerStackIdentifier
targetSchema : string
usd : bool
payloadDecorator : PayloadDecoratorRefPtr


Construct a PcpCache to compose results for the layer stack identified
by *layerStackIdentifier*.


If C{targetSchema} is specified, Pcp will require all scene
description layers it encounters to adhere to the identified schema.
When searching for or opening a layer, Pcp will specify
C{targetSchema} as the layer's target.

If C{payloadDecorator} is specified, it will be used when computing
any prim index. See documentation for C{PcpPayloadDecorator} for more
details.

If C{usd} is true, computation of prim indices and composition of prim
child names are performed without relocates, inherits, permissions,
symmetry, or payloads, and without populating the prim stack and
gathering its dependencies.

"""
   result["Cache"].Reload.im_func.func_doc = """Reload(changes) -> PCP_API void

changes : Changes


Reload the layers of the layer stack, except session layers and
sublayers of session layers.


This will also try to load sublayers in this cache's layer stack that
could not be loaded previously. It will also try to load any
referenced or payloaded layer that could not be loaded previously.
Clients should subsequently C{Apply()} C{changes} to use any now-valid
layers.

"""
   result["Cache"].SetVariantFallbacks.im_func.func_doc = """SetVariantFallbacks(map, changes) -> PCP_API void

map : VariantFallbackMap
changes : Changes


Set the list of fallbacks to attempt to use when evaluating variant
sets that lack an authored selection.


If C{changes} is not C{None} then it's adjusted to reflect the changes
necessary to see the change in standin preferences, otherwise those
changes are applied immediately.

"""
   result["Cache"].RequestPayloads.im_func.func_doc = """RequestPayloads(pathsToInclude, pathsToExclude, changes) -> PCP_API void

pathsToInclude : SdfPathSet
pathsToExclude : SdfPathSet
changes : Changes


Request payloads to be included or excluded from composition.


pathsToInclude

is a set of paths to add to the set for payload inclusion.
pathsToExclude

is a set of paths to remove from the set for payload inclusion.
changes

if not C{None}, is adjusted to reflect the changes necessary to see
the change in payloads; otherwise those changes are applied
immediately.

If a path is listed in both pathsToInclude and pathsToExclude, it will
be treated as an inclusion only.

"""
   result["Cache"].IsInvalidAssetPath.im_func.func_doc = """IsInvalidAssetPath(resolvedAssetPath) -> PCP_API bool

resolvedAssetPath : string


Returns true if C{resolvedAssetPath} was used by a prim (e.g.


in a reference) but did not resolve to a valid asset. This is
functionally equivalent to examining the values in the map returned by
GetInvalidAssetPaths, but more efficient.

"""
   result["Cache"].GetVariantFallbacks.im_func.func_doc = """GetVariantFallbacks() -> PCP_API PcpVariantFallbackMap



Get the list of fallbacks to attempt to use when evaluating variant
sets that lack an authored selection.

"""
   result["Cache"].ComputeRelationshipTargetPaths.im_func.func_doc = """ComputeRelationshipTargetPaths(relationshipPath, paths, localOnly, stopProperty, includeStopProperty, allErrors) -> PCP_API void

relationshipPath : SdfPath
paths : SdfPathVector
localOnly : bool
stopProperty : SdfSpecHandle
includeStopProperty : bool
allErrors : ErrorVector


Compute the relationship target paths for the relationship at
C{relationshipPath} into C{paths}.


If C{localOnly} is C{true} then this will compose relationship targets
from local nodes only. If C{stopProperty} is not C{None} then this
will stop composing relationship targets at C{stopProperty}, including
C{stopProperty} iff C{includeStopProperty} is C{true}. C{allErrors}
will contain any errors encountered while performing this operation.

"""
   result["Cache"].ComputeLayerStack.im_func.func_doc = """ComputeLayerStack(identifier, allErrors) -> PCP_API PcpLayerStackRefPtr

identifier : LayerStackIdentifier
allErrors : ErrorVector


Returns the layer stack for C{identifier} if it exists, otherwise
creates a new layer stack for C{identifier}.


This returns C{None} if C{identifier} is invalid (i.e. its root layer
is C{None}). C{allErrors} will contain any errors encountered while
creating a new layer stack. It'll be unchanged if the layer stack
already existed.

"""
   result["ErrorTargetPermissionDenied"].__doc__ = """
Paths with illegal opinions about private targets.

"""
   result["TranslatePathFromNodeToRoot"].func_doc = """TranslatePathFromNodeToRoot(sourceNode, pathInNodeNamespace, pathWasTranslated) -> PCP_API SdfPath

sourceNode : NodeRef
pathInNodeNamespace : SdfPath
pathWasTranslated : bool


Translates C{pathInNodeNamespace} from the namespace of the prim index
node C{sourceNode} to the namespace of the prim index's root node.


This applies all necessary namespace translations.

If the path is successfully translated and C{pathWasTranslated} is
supplied, it will be set to C{true}. In some cases, paths may fail to
translate because they fall outside the set of paths that are allowed
by nodes in the prim index. For instance, for a referenced model,
paths referring to locations outside that model will not be
translated. In these cases, this function will return an empty SdfPath
and C{pathWasTranslated} will be set to C{false}.

In Sd/Csd terminology, this is forward path translation from the
namespace of the prim spec represented by C{sourceNode} to the
composed scene namespace.

"""
   result["ErrorInvalidInstanceTargetPath"].__doc__ = """
Invalid target or connection path authored in an inherited class that
points to an instance of that class.

"""
   result["PayloadDecorator"].__doc__ = """
PcpPayloadDecorator provides a way to specify additional information
to the prim indexing algorithm when it loads payload layers.


If a decorator has been specified as an prim indexing input, it will
be invoked whenever a payload arc is encountered. The decorator can
then fill in an SdfLayer::FileFormatArguments object with any
information it wants. This information will be passed to
SdfLayer::FindOrOpen when the layer is ultimately opened.

When processing a payload, the decorator can examine scene description
values from stronger nodes in the index via the supplied
PcpPayloadContext object. For instance, a decorator might use the
PcpPayloadContext to find the strongest available metadata value
authored on a prim, and use that to control its behavior.

Since decoration happens before the payload is actually loaded it
cannot examine locations introduced inside the payload. For example,
if a payload introduces a class inherit, the context will not be able
to see values from class overrides that are stronger than the payload.

"""
   result["PayloadDecorator"]._IsFieldChangeRelevantForDecoration.im_func.func_doc = """_IsFieldChangeRelevantForDecoration(primIndexPath, siteLayer, sitePath, field, oldAndNewValues) -> bool

primIndexPath : SdfPath
siteLayer : SdfLayerHandle
sitePath : SdfPath
field : TfToken
oldAndNewValues : pair< VtValue , VtValue >

"""
   result["PayloadDecorator"].__init__.im_func.func_doc = """__init__() -> PCP_API


"""
   result["PayloadDecorator"].IsFieldChangeRelevantForDecoration.im_func.func_doc = """IsFieldChangeRelevantForDecoration(primIndexPath, siteLayer, sitePath, field, oldAndNewValues) -> PCP_API bool

primIndexPath : SdfPath
siteLayer : SdfLayerHandle
sitePath : SdfPath
field : TfToken
oldAndNewValues : pair< VtValue , VtValue >


Return true if the change to scene description field C{field} on the
prim spec at C{sitePath} in the layer C{siteLayer} may affect the
decoration of payloads when composing the index at C{primIndexPath},
false otherwise.


C{oldAndNewValues} contain the old and new values of the field.

This is used during change processing to determine whether a scene
description change affects a prim's payload arcs and requires the prim
to be recomposed.

"""
   result["PayloadDecorator"].DecoratePayload.im_func.func_doc = """DecoratePayload(primIndexPath, payload, context, args) -> PCP_API void

primIndexPath : SdfPath
payload : SdfPayload
context : PayloadContext
args : SdfLayer.FileFormatArguments


Decorate the SdfLayer arguments C{args} with additional arguments that
will be used when opening the layer specified in the payload
C{payload} when composing the index at C{primIndexPath}.

"""
   result["PayloadDecorator"].IsFieldRelevantForDecoration.im_func.func_doc = """IsFieldRelevantForDecoration(field) -> PCP_API bool

field : TfToken


Return true if changes to the scene description field C{field} may
affect the decoration of payloads, false otherwise.


If a change is made to a field for which this function returns true,
IsFieldChangeRelevantForDecoration will be called during change
processing to allow the decorator to determine if the change is
relevant and requires affected prims to be recomposed.

"""
   result["PayloadDecorator"]._DecoratePayload.im_func.func_doc = """_DecoratePayload(primIndexPath, payload, context, args)

primIndexPath : SdfPath
payload : SdfPayload
context : PayloadContext
args : SdfLayer.FileFormatArguments


Virtual implementation functions.


See corresponding public API for documentation.

"""
   result["ErrorPrimPermissionDenied"].__doc__ = """
Layers with illegal opinions about private prims.

"""
   result["MapFunction"].__doc__ = """
A function that maps values from one namespace (and time domain) to
another.


It represents the transformation that an arc such as a reference arc
applies as it incorporates values across the arc.

Take the example of a reference arc, where a source path</Model>is
referenced as a target path,</Model_1>. The source path</Model>is the
source of the opinions; the target path</Model_1>is where they are
incorporated in the scene. Values in the model that refer to paths
relative to</Model>must be transformed to be relative
to</Model_1>instead. The PcpMapFunction for the arc provides this
service.

Map functions have a specific *domain*, or set of values they can
operate on. Any values outside the domain cannot be mapped. The domain
precisely tracks what areas of namespace can be referred to across
various forms of arcs.

Map functions can be chained to represent a series of map operations
applied in sequence. The map function represent the cumulative effect
as efficiently as possible. For example, in the case of a chained
reference from</Model>to</Model>to</Model>to</Model_1>, this is
effectively the same as a mapping directly from</Model>to</Model_1>.
Representing the cumulative effect of arcs in this way is important
for handling larger scenes efficiently.

Map functions can be *inverted*. Formally, map functions are
bijections (one-to-one and onto), which ensures that they can be
inverted. Put differently, no information is lost by applying a map
function to set of values within its domain; they retain their
distinct identities and can always be mapped back.

One analogy that may or may not be helpful: In the same way a
geometric transform maps a model's points in its rest space into the
world coordinates for a particular instance, a PcpMapFunction maps
values about a referenced model into the composed scene for a
particular instance of that model. But rather than translating and
rotating points, the map function shifts the values in namespace (and
time).

Map functions are flyweighted, so they can be passed around by value
relatively cheaply.

"""
   result["MapFunction"].Compose.im_func.func_doc = """Compose(f) -> PCP_API PcpMapFunction

f : MapFunction


Compose this map over the given map function.


The result will represent the application of f followed by the
application of this function.

"""
   result["MapFunction"].__init__.im_func.func_doc = """__init__() -> PCP_API



Construct a null function.


----------------------------------------------------------------------
__init__(map) -> PCP_API

map : MapFunction


Copy-construct the map.


----------------------------------------------------------------------
__init__(sourceToTarget, offset)

sourceToTarget : PathPairVector
offset : SdfLayerOffset


----------------------------------------------------------------------
__init__(fn)

fn : _DataFlyweight

"""
   result["MapFunction"].Identity.func_doc = """**static** Identity() -> PCP_API  PcpMapFunction



Construct an identity map function.

"""
   result["MapFunction"].GetInverse.im_func.func_doc = """GetInverse() -> PCP_API PcpMapFunction



Return the inverse of this map function.


This returns a true inverse C{inv:} for any path p in this function's
domain that it maps to p', inv(p') ->p.

"""
   result["MapFunction"].MapSourceToTarget.im_func.func_doc = """MapSourceToTarget(path) -> PCP_API SdfPath

path : SdfPath


Map a path in the source namespace to the target.


If the path is not in the domain, returns an empty path.

"""
   result["MapFunction"].IdentityPathMap.func_doc = """**static** IdentityPathMap() -> PCP_API  PathMap



Returns an identity path mapping.

"""
   result["MapFunction"].MapTargetToSource.im_func.func_doc = """MapTargetToSource(path) -> PCP_API SdfPath

path : SdfPath


Map a path in the target namespace to the source.


If the path is not in the co-domain, returns an empty path.

"""
   result["Site"].__doc__ = """
A site specifies a path in a layer stack of scene description.

"""
   result["DependencyType"].__doc__ = """
A classification of PcpPrimIndex-> PcpSite dependencies by composition
structure.

"""
   result["MapExpression"].__doc__ = """
An expression that yields a PcpMapFunction value.


Expressions comprise constant values, variables, and operators applied
to sub-expressions. Expressions cache their computed values
internally. Assigning a new value to a variable automatically
invalidates the cached values of dependent expressions. Common
(sub-)expressions are automatically detected and shared.

PcpMapExpression exists solely to support efficient incremental
handling of relocates edits. It represents a tree of the namespace
mapping operations and their inputs, so we can narrowly redo the
computation when one of the inputs changes.

"""
   result["MapExpression"].Inverse.func_doc = """Inverse() -> PCP_API PcpMapExpression



Create a new PcpMapExpression representing the inverse of f.

"""
   result["MapExpression"].Constant.func_doc = """**static** Constant(constValue) -> PCP_API PcpMapExpression

constValue : Value


Create a new constant.

"""
   result["MapExpression"].Evaluate.im_func.func_doc = """Evaluate() -> PCP_API  Value



Evaluate this expression, yielding a PcpMapFunction value.


The computed result is cached. The return value is a reference to the
internal cached value. The cache is automatically invalidated as
needed.

"""
   result["MapExpression"].__init__.im_func.func_doc = """__init__() -> PCP_API



Default-construct a None expression.


----------------------------------------------------------------------
__init__(node)

node : _NodeRefPtr

"""
   result["MapExpression"].MapTargetToSource.im_func.func_doc = """MapTargetToSource(path) -> SdfPath

path : SdfPath


Map a path in the target namespace to the source.


If the path is not in the co-domain, returns an empty path.

"""
   result["MapExpression"].Compose.im_func.func_doc = """Compose(f) -> PCP_API PcpMapExpression

f : MapExpression


Create a new PcpMapExpression representing the application of f's
value, followed by the application of this expression's value.

"""
   result["MapExpression"].AddRootIdentity.im_func.func_doc = """AddRootIdentity() -> PCP_API PcpMapExpression



Return a new expression representing this expression with an added (if
necessary) mapping from</>to</>.

"""
   result["MapExpression"].MapSourceToTarget.im_func.func_doc = """MapSourceToTarget(path) -> SdfPath

path : SdfPath


Map a path in the source namespace to the target.


If the path is not in the domain, returns an empty path.

"""
   result["MapExpression"].Identity.func_doc = """**static** Identity() -> PCP_API PcpMapExpression



Return an expression representing PcpMapFunction::Identity() .

"""
   result["ErrorInvalidSublayerOffset"].__doc__ = """
Sublayers that use invalid layer offsets.

"""
   result["PropertyIndex"].__doc__ = """
PcpPropertyIndex is an index of all sites in scene description that
contribute opinions to a specific property, under composition
semantics.

"""
   result["ErrorInvalidSublayerPath"].__doc__ = """
Asset paths that could not be both resolved and loaded.

"""
   result["ErrorInvalidTargetPath"].__doc__ = """
Invalid target or connection path.

"""
   result["NodeRef"].__doc__ = """
PcpNode represents a node in an expression tree for compositing scene
description.


A node represents the opinions from a particular site. In addition, it
may have child nodes, representing nested expressions that are
composited over/under this node.

Child nodes are stored and composited in strength order.

Each node holds information about the arc to its parent. This captures
both the relative strength of the sub-expression as well as any value-
mapping needed, such as to rename opinions from a model to use in a
particular instance.

"""
   result["NodeRef"].CanContributeSpecs.im_func.func_doc = """CanContributeSpecs() -> PCP_API bool



Returns true if this node is allowed to contribute opinions for
composition, false otherwise.

"""
   result["NodeRef"].GetDepthBelowIntroduction.im_func.func_doc = """GetDepthBelowIntroduction() -> PCP_API int



Return the number of levels of namespace this node's site is below the
level at which it was introduced by an arc.

"""
   result["NodeRef"].GetRootNode.im_func.func_doc = """GetRootNode() -> PCP_API PcpNodeRef



Walk up to the root node of this expression.

"""
   result["NodeRef"].GetPathAtIntroduction.im_func.func_doc = """GetPathAtIntroduction() -> PCP_API SdfPath



Returns the path for this node's site when it was introduced.

"""
   result["NodeRef"].IsDueToAncestor.im_func.func_doc = """IsDueToAncestor() -> PCP_API bool



Returns true if this node is due to an ancestral opinion.

"""
   result["NodeRef"].IsDirect.im_func.func_doc = """IsDirect() -> PCP_API bool



Returns true if this node is a source of direct opinions.


There should only be one direct node per prim index.

"""
   result["NodeRef"].GetOriginRootNode.im_func.func_doc = """GetOriginRootNode() -> PCP_API PcpNodeRef



Walk up to the root origin node for this node.


This is the very first node that caused this node to be added to the
graph. For instance, the root origin node of an implied inherit is the
original inherit node.

"""
   result["NodeRef"].GetIntroPath.im_func.func_doc = """GetIntroPath() -> PCP_API SdfPath



Get the path that introduced this node.


Specifically, this is the path the parent node had at the level of
namespace where this node was added as a child. For a root node, this
returns the absolute root path. See also GetDepthBelowIntroduction() .

"""
   result["ErrorInvalidReferenceOffset"].__doc__ = """
Sublayers that use invalid layer offsets.

"""
   result["ErrorInvalidAssetPath"].__doc__ = """
Invalid asset paths used by references or payloads.

"""
   result["ErrorTargetPathBase"].__doc__ = """
Base class for composition errors related to target or connection
paths.

"""
   result["ErrorBase"].__doc__ = """
Base class for all error types.

"""
   result["ErrorInconsistentPropertyType"].__doc__ = """
Properties that have specs with conflicting definitions.

"""
   result["ErrorArcPermissionDenied"].__doc__ = """
Arcs that were not made between PcpNodes because of permission
restrictions.

"""
   result["ErrorInvalidVariantSelection"].__doc__ = """
Invalid variant selections.

"""
   result["TranslatePathFromRootToNode"].func_doc = """TranslatePathFromRootToNode(destNode, pathInRootNamespace, pathWasTranslated) -> PCP_API SdfPath

destNode : NodeRef
pathInRootNamespace : SdfPath
pathWasTranslated : bool


Translates C{pathInRootNamespace} from the namespace of the root of
the prim index that C{destNode} belongs to to the namespace of
C{destNode} itself.


This applies all necessary namespace translations.

If the path is successfully translated and C{pathWasTranslated} is
supplied, it will be set to C{true}. In some cases, paths may fail to
translate because they fall outside the set of paths that are allowed
by nodes in the prim index. For instance, for a referenced model,
paths referring to locations outside that model will not be
translated. In these cases, this function will return an empty SdfPath
and C{pathWasTranslated} will be set to C{false}.

In Sd/Csd terminology, this is reverse path translation from the
namespace of the composed scene to the namespace of the prim spec
represented by C{destNode}.

"""
   result["ErrorInvalidAssetPathBase"].__doc__ = """"""
   result["LayerStackIdentifier"].__doc__ = """
Arguments used to identify a layer stack.


Objects of this type are immutable.

"""
   result["LayerStackIdentifier"].__init__.im_func.func_doc = """__init__() -> PCP_API



Construct with all empty pointers.


----------------------------------------------------------------------
__init__(rootLayer_, sessionLayer_, pathResolverContext_) -> PCP_API

rootLayer_ : SdfLayerHandle
sessionLayer_ : SdfLayerHandle
pathResolverContext_ : ArResolverContext


Construct with given pointers.


If all arguments are C{TfNullPtr} then the result is identical to the
default constructed object.

"""
   result["LayerStackSite"].__doc__ = """
A site specifies a path in a layer stack of scene description.

"""
   result["ErrorArcCycle"].__doc__ = """
Arcs between PcpNodes that form a cycle.

"""
   result["NodeRef"].mapToRoot = property(result["NodeRef"].mapToRoot.fget, result["NodeRef"].mapToRoot.fset, result["NodeRef"].mapToRoot.fdel, """type : PCP_API  PcpMapExpression


Returns mapping function used to translate paths and values from this
node directly to the root node.

""")
   result["MapFunction"].sourceToTargetMap = property(result["MapFunction"].sourceToTargetMap.fget, result["MapFunction"].sourceToTargetMap.fset, result["MapFunction"].sourceToTargetMap.fdel, """type : PCP_API PathMap


The set of path mappings, from source to target.

""")
   result["MapExpression"].timeOffset = property(result["MapExpression"].timeOffset.fget, result["MapExpression"].timeOffset.fset, result["MapExpression"].timeOffset.fdel, """type : SdfLayerOffset


The time offset of the mapping.

""")
   result["NodeRef"].isInert = property(result["NodeRef"].isInert.fget, result["NodeRef"].isInert.fset, result["NodeRef"].isInert.fdel, """type : PCP_API bool

""")
   result["PropertyIndex"].localErrors = property(result["PropertyIndex"].localErrors.fget, result["PropertyIndex"].localErrors.fset, result["PropertyIndex"].localErrors.fdel, """type : ErrorVector


Return the list of errors local to this property.

""")
   result["Cache"].targetSchema = property(result["Cache"].targetSchema.fget, result["Cache"].targetSchema.fset, result["Cache"].targetSchema.fdel, """type : PCP_API  string


Returns the target schema this cache is configured for.

""")
   result["LayerStack"].layerTree = property(result["LayerStack"].layerTree.fget, result["LayerStack"].layerTree.fset, result["LayerStack"].layerTree.fdel, """type : PCP_API  SdfLayerTreeHandle


Returns the layer tree representing the structure of this layer stack.

""")
   result["MapExpression"].isNull = property(result["MapExpression"].isNull.fget, result["MapExpression"].isNull.fset, result["MapExpression"].isNull.fdel, """type : PCP_API bool


Return true if this is a null expression.

""")
   result["LayerStack"].incrementalRelocatesTargetToSource = property(result["LayerStack"].incrementalRelocatesTargetToSource.fget, result["LayerStack"].incrementalRelocatesTargetToSource.fset, result["LayerStack"].incrementalRelocatesTargetToSource.fdel, """type : PCP_API  SdfRelocatesMap


Returns incremental relocation target-to-source mapping for this layer
stack.


See GetIncrementalRelocatesTargetToSource for more details.

""")
   result["MapExpression"].isIdentity = property(result["MapExpression"].isIdentity.fget, result["MapExpression"].isIdentity.fset, result["MapExpression"].isIdentity.fdel, """type : bool


Return true if the evaluated map function is the identity function.


For identity, MapSourceToTarget() always returns the path unchanged.

""")
   result["NodeRef"].arcType = property(result["NodeRef"].arcType.fget, result["NodeRef"].arcType.fset, result["NodeRef"].arcType.fdel, """type : PCP_API PcpArcType


Returns the type of arc connecting this node to its parent node.

""")
   result["NodeRef"].isRestricted = property(result["NodeRef"].isRestricted.fget, result["NodeRef"].isRestricted.fset, result["NodeRef"].isRestricted.fdel, """type : PCP_API bool

""")
   result["NodeRef"].permission = property(result["NodeRef"].permission.fget, result["NodeRef"].permission.fset, result["NodeRef"].permission.fdel, """type : PCP_API SdfPermission

----------------------------------------------------------------------type : PCP_API void


Get/set the permission for this node.


This indicates whether specs on this node can be accessed from other
nodes.

""")
   result["LayerStack"].incrementalRelocatesSourceToTarget = property(result["LayerStack"].incrementalRelocatesSourceToTarget.fget, result["LayerStack"].incrementalRelocatesSourceToTarget.fset, result["LayerStack"].incrementalRelocatesSourceToTarget.fdel, """type : PCP_API  SdfRelocatesMap


Returns incremental relocation source-to-target mapping for this layer
stack.


This map contains the individual relocation entries found across all
layers in this layer stack; it does not combine ancestral entries with
descendant entries. For instance, if this layer stack contains
relocations { /A: /B} and { /A/C: /A/D}, this map will contain { /A:
/B} and { /A/C: /A/D}.

""")
   result["LayerStack"].resolvedAssetPaths = property(result["LayerStack"].resolvedAssetPaths.fget, result["LayerStack"].resolvedAssetPaths.fset, result["LayerStack"].resolvedAssetPaths.fdel, """type : PCP_API  set<string>


Returns the set of asset paths resolved while building the layer
stack.

""")
   result["LayerStack"].localErrors = property(result["LayerStack"].localErrors.fget, result["LayerStack"].localErrors.fset, result["LayerStack"].localErrors.fdel, """type : ErrorVector


Return the list of errors local to this layer stack.

""")
   result["NodeRef"].path = property(result["NodeRef"].path.fget, result["NodeRef"].path.fset, result["NodeRef"].path.fdel, """type : PCP_API  SdfPath


Returns the path for the site this node represents.

""")
   result["MapFunction"].isNull = property(result["MapFunction"].isNull.fget, result["MapFunction"].isNull.fset, result["MapFunction"].isNull.fdel, """type : PCP_API bool


Return true if this map function is the null function.


For a null function, MapSourceToTarget() always returns an empty path.

""")
   result["LayerStack"].layers = property(result["LayerStack"].layers.fget, result["LayerStack"].layers.fset, result["LayerStack"].layers.fdel, """type : PCP_API  SdfLayerRefPtrVector


Returns the layers in this layer stack in strong-to-weak order.


Note that this is only the *local* layer stack  it does not include
any layers brought in by references inside prims.

""")
   result["MapFunction"].timeOffset = property(result["MapFunction"].timeOffset.fget, result["MapFunction"].timeOffset.fset, result["MapFunction"].timeOffset.fdel, """type : SdfLayerOffset


The time offset of the mapping.

""")
   result["NodeRef"].layerStack = property(result["NodeRef"].layerStack.fget, result["NodeRef"].layerStack.fset, result["NodeRef"].layerStack.fdel, """type : PCP_API  PcpLayerStackRefPtr


Returns the layer stack for the site this node represents.

""")
   result["NodeRef"].mapToParent = property(result["NodeRef"].mapToParent.fget, result["NodeRef"].mapToParent.fset, result["NodeRef"].mapToParent.fdel, """type : PCP_API  PcpMapExpression


Returns mapping function used to translate paths and values from this
node to its parent node.

""")
   result["LayerStack"].relocatesTargetToSource = property(result["LayerStack"].relocatesTargetToSource.fget, result["LayerStack"].relocatesTargetToSource.fset, result["LayerStack"].relocatesTargetToSource.fdel, """type : PCP_API  SdfRelocatesMap


Returns relocation target-to-source mapping for this layer stack.


See GetRelocatesSourceToTarget for more details.

""")
   result["Cache"].layerStack = property(result["Cache"].layerStack.fget, result["Cache"].layerStack.fset, result["Cache"].layerStack.fdel, """type : PCP_API PcpLayerStackPtr


Get the layer stack for GetLayerStackIdentifier() .


Note that this will neither compute the layer stack nor report errors.
So if the layer stack has not been computed yet this will return
C{None}. Use ComputeLayerStack() if you need to compute the layer
stack if it hasn't been computed already and/or get errors caused by
computing the layer stack.

""")
   result["NodeRef"].namespaceDepth = property(result["NodeRef"].namespaceDepth.fget, result["NodeRef"].namespaceDepth.fset, result["NodeRef"].namespaceDepth.fdel, """type : PCP_API int


Returns the absolute namespace depth of the node that introduced this
node.


Note that this does *not* count any variant selections.

""")
   result["MapFunction"].isIdentity = property(result["MapFunction"].isIdentity.fget, result["MapFunction"].isIdentity.fset, result["MapFunction"].isIdentity.fdel, """type : PCP_API bool


Return true if the map function is the identity function.


For identity, MapSourceToTarget() always returns the path unchanged.

""")
   result["PrimIndex"].localErrors = property(result["PrimIndex"].localErrors.fget, result["PrimIndex"].localErrors.fset, result["PrimIndex"].localErrors.fdel, """type : ErrorVector


Return the list of errors local to this prim.

""")
   result["NodeRef"].hasSymmetry = property(result["NodeRef"].hasSymmetry.fget, result["NodeRef"].hasSymmetry.fset, result["NodeRef"].hasSymmetry.fdel, """type : PCP_API void


Get/set whether this node provides any symmetry opinions, either
directly or from a namespace ancestor.

""")
   result["LayerStack"].pathsToPrimsWithRelocates = property(result["LayerStack"].pathsToPrimsWithRelocates.fget, result["LayerStack"].pathsToPrimsWithRelocates.fset, result["LayerStack"].pathsToPrimsWithRelocates.fdel, """type : PCP_API  SdfPathVector


Returns a list of paths to all prims across all layers in this layer
stack that contained relocates.

""")
   result["NodeRef"].siblingNumAtOrigin = property(result["NodeRef"].siblingNumAtOrigin.fget, result["NodeRef"].siblingNumAtOrigin.fset, result["NodeRef"].siblingNumAtOrigin.fdel, """type : PCP_API int


Returns this node's index among siblings with the same arc type at
this node's origin.

""")
   result["LayerStack"].relocatesSourceToTarget = property(result["LayerStack"].relocatesSourceToTarget.fget, result["LayerStack"].relocatesSourceToTarget.fset, result["LayerStack"].relocatesSourceToTarget.fdel, """type : PCP_API  SdfRelocatesMap


Returns relocation source-to-target mapping for this layer stack.


This map combines the individual relocation entries found across all
layers in this layer stack; multiple entries that affect a single prim
will be combined into a single entry. For instance, if this layer
stack contains relocations { /A: /B} and { /A/C: /A/D}, this map will
contain { /A: /B} and { /B/C: /B/D}. This allows consumers to go from
unrelocated namespace to relocated namespace in a single step.

""")
   result["PrimIndex"].rootNode = property(result["PrimIndex"].rootNode.fget, result["PrimIndex"].rootNode.fset, result["PrimIndex"].rootNode.fdel, """type : PCP_API PcpNodeRef


Returns the root node of the prim index graph.

""")
   result["NodeRef"].hasSpecs = property(result["NodeRef"].hasSpecs.fget, result["NodeRef"].hasSpecs.fset, result["NodeRef"].hasSpecs.fdel, """type : PCP_API void


Returns true if this node has opinions authored for composition, false
otherwise.

""")
   result["NodeRef"].isCulled = property(result["NodeRef"].isCulled.fget, result["NodeRef"].isCulled.fset, result["NodeRef"].isCulled.fdel, """type : PCP_API bool

""")
   result["LayerStack"].identifier = property(result["LayerStack"].identifier.fget, result["LayerStack"].identifier.fset, result["LayerStack"].identifier.fdel, """type : PCP_API  PcpLayerStackIdentifier


Returns the identifier for this layer stack.

""")
   result["NodeRef"].site = property(result["NodeRef"].site.fget, result["NodeRef"].site.fset, result["NodeRef"].site.fdel, """type : PCP_API PcpLayerStackSite


Get the site this node represents.

""")