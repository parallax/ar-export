def Execute(result):
   result["StitchClipsTemplate"].func_doc = """StitchClipsTemplate(resultLayer, topologyLayer, clipPath, templatePath, startTime, endTime, stride, activeOffset, clipSet) -> USDUTILS_API bool

resultLayer : SdfLayerHandle
topologyLayer : SdfLayerHandle
clipPath : SdfPath
templatePath : string
startTime : double
endTime : double
stride : double
activeOffset : double
clipSet : TfToken


A function which authors clip template metadata on a particular prim
in a result layer, as well as adding the topologyLayer to the list of
subLayers on the C{resultLayer}.


It will clear the C{resultLayer} and create a prim at C{clipPath}.
Specifically, this will author clipPrimPath, clipTemplateAssetPath,
clipTemplateStride, clipTemplateStartTime,  clipTemplateEndTime, and
clipManifestAssetPath.

C{resultLayer} The layer in which we will author the metadata.

C{topologyLayer} The layer containing the aggregate topology of the
clipLayers which the metadata refers to.

C{clipPath} The path at which to author the metadata in C{resultLayer}

C{templatePath} The template string to be authored at the
clipTemplateAssetPath metadata key.

C{startTime} The start time to be authored at the
clipTemplateStartTime metadata key.

C{endTime} The end time to be authored at the clipTemplateEndTime
metadata key.

C{stride} The stride to be authored at the clipTemplateStride metadata
key.

C{activeOffset} The offset to be authored at the
clipTemplateActiveOffset metadata key.

If this parameter is omitted, no value will be authored as the
metadata is optional. C{clipSet} The name of the clipSet in which the
aforementioned metadata will be authored.

If this parameter is omitted, the default clipSet name("default") will
be authored. For further information on these metadatum, see Advanced
Scenegraph Scalability Features

"""
   result["StitchInfo"].func_doc = """StitchInfo(strongObj, weakObj, stitchValueFn) -> USDUTILS_API void

strongObj : SdfSpecHandle
weakObj : SdfSpecHandle
stitchValueFn : StitchValueFn


Advanced version of UsdUtilsStitchInfo that accepts a C{stitchValueFn}
callback to customize how fields in C{strongObj} and C{weakObj} are
stitched together.


See documentation on UsdUtilsStitchValueFn for more details.


----------------------------------------------------------------------
StitchInfo(strongObj, weakObj) -> USDUTILS_API void

strongObj : SdfSpecHandle
weakObj : SdfSpecHandle


Merge the scene description for C{weakObj} into C{strongObj}.


See documentation on UsdUtilsStitchLayers for a description of the
merging behavior.

"""
   result["StageCache"].__doc__ = """
The UsdUtilsStageCache class provides a simple interface for handling
a singleton usd stage cache for use by all USD clients.


This way code from any location can make use of the same cache to
maximize stage reuse.

"""
   result["StageCache"].GetSessionLayerForVariantSelections.func_doc = """**static** GetSessionLayerForVariantSelections(modelName, variantSelections) -> USDUTILS_API SdfLayerRefPtr

modelName : TfToken
variantSelections : sequence<pair<string, string>>


Given variant selections as a vector of pairs (vector in case order
matters to the client), constructs a session layer with overs on the
given root modelName with the variant selections, or returns a cached
session layer with those opinions.

"""
   result["StageCache"].Get.func_doc = """**static** Get() -> USDUTILS_API UsdStageCache



Returns the singleton stage cache.

"""
   result["AuthorCollection"].func_doc = """AuthorCollection(collectionName, usdPrim, pathsToInclude, pathsToExclude) -> USDUTILS_API UsdCollectionAPI

collectionName : TfToken
usdPrim : UsdPrim
pathsToInclude : SdfPathVector
pathsToExclude : SdfPathVector


Authors a collection named C{collectionName} on the given prim,
C{usdPrim} with the given set of included paths ( C{pathsToInclude})
and excluded paths ( C{pathsToExclude}).


If a collection with the specified name already exists on C{usdPrim},
its data is appended to. The resulting collection will contain both
the old paths and the newly included paths.

"""
   result["CoalescingDiagnosticDelegateUnsharedItem"].__doc__ = """
The unshared component in a coalesced result.

"""
   result["CoalescingDiagnosticDelegateSharedItem"].__doc__ = """
The shared component in a coalesced result This type can be thought of
as the key by which we coalesce our diagnostics.

"""
   result["CoalescingDiagnosticDelegate"].__doc__ = """
A class which collects warnings and statuses from the Tf diagnostic
manager system in a thread safe manner.


This class allows clients to get both the unfiltered results, as well
as a compressed view which deduplicates diagnostic events by their
source line number, function and file from which they occurred.

"""
   result["CoalescingDiagnosticDelegate"].TakeCoalescedDiagnostics.im_func.func_doc = """TakeCoalescedDiagnostics() -> USDUTILS_API UsdUtilsCoalescingDiagnosticDelegateVector



Get all pending diagnostics in a coalesced form.



This method clears the pending diagnostics.

"""
   result["CoalescingDiagnosticDelegate"].TakeUncoalescedDiagnostics.im_func.func_doc = """TakeUncoalescedDiagnostics() -> USDUTILS_API sequence<unique_ptr< TfDiagnosticBase >>



Get all pending diagnostics without any coalescing.



This method clears the pending diagnostics.

"""
   result["CoalescingDiagnosticDelegate"].DumpUncoalescedDiagnostics.im_func.func_doc = """DumpUncoalescedDiagnostics(ostr) -> USDUTILS_API void

ostr : ostream


Print all pending diagnostics without any coalescing to C{ostr}.



This method clears the pending diagnostics.

"""
   result["CoalescingDiagnosticDelegate"].__init__.im_func.func_doc = """__init__() -> USDUTILS_API


"""
   result["CreateCollections"].func_doc = """CreateCollections(assignments, usdPrim, minInclusionRatio, maxNumExcludesBelowInclude, minIncludeExcludeCollectionSize) -> USDUTILS_API sequence< UsdCollectionAPI >

assignments : sequence<pair< TfToken , SdfPathSet>>
usdPrim : UsdPrim
minInclusionRatio : double
maxNumExcludesBelowInclude : unsigned int
minIncludeExcludeCollectionSize : unsigned int


Given a vector of (collection-name, path-set) pairs, C{assignments},
creates and returns a vector of collections that include subtrees of
prims rooted at the included paths.


The collections are created on the given prim, C{usdPrim}.

Based on the paths included in the various collections, this function
computes a compact representation for each collection in parallel
using UsdUtilsGetCollectionIncludesExcludes(). So, it takes the same
set of parameters as that function: C{minInclusionRatio},
C{maxNumExcludesBelowInclude} and C{minIncludeExcludeCollectionSize}.

It is valid for the paths or subtrees specified in C{assignments} to
have overlapping subtrees. In this case the overlapping bits will
belong to multiple collections. C{assignments} is a vector of pairs
representing collection names and paths to be included in the
collection in each collection. C{usdPrim} is the prim on which the
collections are created. C{minInclusionRatio} is the minimum value of
the ratio between the number of included paths and the sum of the
number of included and excluded paths below an ancestor path, at or
above which the ancestor path is included in the collection. For
example, if an ancestor prim has four children and three out of the
four are included in the collection, the inclusion ratio at the
ancestor is 0.75. This value should be in the range (0,1), if not,
it's clamped to the range. C{maxNumExcludesBelowInclude} is the
maximum number of paths that we exclude below any ancestor path that
we include in a collection. This parameter only affects paths that
have already passed the min-inclusion-ratio test. Setting this to 0
will cause all collections to have includes only (and no excludes).
Setting it to a higher number will cause ancestor paths that are
higher up in the namespace hierarchy to be included in collections.
C{minIncludeExcludeCollectionSize} is the minimum size of a collection
(i.e. the number of subtree-root paths included in it), at or above
which the algorithm chooses to make a collection with both included
and excluded paths, instead of creating a collection with only
includes (containing the specified set of paths). UsdCollectionAPI

Returns the vector of UsdCollectionAPI objects that were created. If a
collection is empty (i.e. includes no paths), then an empty collection
is created for it with the default expansionRule. Hence, the size of
the returned vector should match the size of C{assignments}.

"""
   result["GetRegisteredVariantSets"].func_doc = """GetRegisteredVariantSets() -> USDUTILS_API  set< UsdUtilsRegisteredVariantSet >



Certain variant sets can be registered with the system.



UsdUtilsRegisteredVariantSetReturns the set of
UsdUtilsRegisteredVariantSet objects that are registered with the
pipeline. This list will be empty until one or more plugInfo.json
files discoverable by your USD installation contain an entry in the
UsdUtilsPipeline group like the following: ::

  "UsdUtilsPipeline": {
      "RegisteredVariantSets": [
          "modelingVariant": {
              "selectionExportPolicy": {
                  "always"
              }
          },
          "standin": {
              "selectionExportPolicy": {
                  "never"
              }
          }
      ]
  }


"""
   result["UninstancePrimAtPath"].func_doc = """UninstancePrimAtPath(stage, path) -> USDUTILS_API UsdPrim

stage : UsdStagePtr
path : SdfPath


Given a path, uninstances all the instanced prims in the namespace
chain and returns the resulting prim at the requested path.


Returns a None prim if the given path doesn't exist and does not
correspond to a valid prim inside a master.

"""
   result["StitchClipsTopology"].func_doc = """StitchClipsTopology(topologyLayer, clipLayerFiles) -> USDUTILS_API bool

topologyLayer : SdfLayerHandle
clipLayerFiles : sequence<string>


A function which aggregates the topology of a set of C{clipLayerFiles}
for use in USD's Value Clips system.


This aggregated scene topology will only include non-time-varying
data, as it is for use in conjunction with the value clip metadata in
a manifest layer.

C{topologyLayer} The layer in which topology of the C{clipLayerFiles}
will be aggregated and inserted.

C{clipLayerFiles} The files containing the time varying data.

"""
   result["StitchLayers"].func_doc = """StitchLayers(strongLayer, weakLayer, stitchValueFn) -> USDUTILS_API void

strongLayer : SdfLayerHandle
weakLayer : SdfLayerHandle
stitchValueFn : StitchValueFn


Advanced version of UsdUtilsStitchLayers that accepts a
C{stitchValueFn} callback to customize how fields in C{strongLayer}
and C{weakLayer} are stitched together.


See documentation on UsdUtilsStitchValueFn for more details.


----------------------------------------------------------------------
StitchLayers(strongLayer, weakLayer) -> USDUTILS_API void

strongLayer : SdfLayerHandle
weakLayer : SdfLayerHandle


Merge all scene description in C{weakLayer} into C{strongLayer}.


Prims and properties in C{weakLayer} that do not exist in
C{strongLayer} will be copied into C{strongLayer}. Prims and
properties that do exist in C{strongLayer} will be merged with the
existing scene description.

Merging prims and properties is done on a field-by-field basis. In
general, if a field has a value in C{strongLayer}, the value from
C{weakLayer} will be ignored. However, certain fields have special
rules for merging values together:

   - For map and dictionary-valued fields (including time samples), a
     dictionary merge is performed; values in the weaker dictionary are
     copied into the stronger dictionary only if the key does not already
     exist.

   - For listOp-valued fields, the listOps will be combined into a
     single listOp. The historical "add" and "reorder" list op operations
     cannot be combined in this way; "add" will be converted to "append",
     and "reorder" will be discarded.

   - The minimum startTimeCode value and maximum endTimeCode value
     will be used.


"""
   result["RegisteredVariantSet"].SelectionExportPolicy.__doc__ = """
This specifies how the variantSet should be treated during export.


Note, in the plugInfo.json, the values for these enum's are
lowerCamelCase.

"""
   result["StitchClips"].func_doc = """StitchClips(resultLayer, clipLayerFiles, clipPath, startTimeCode, endTimeCode, clipSet) -> USDUTILS_API bool

resultLayer : SdfLayerHandle
clipLayerFiles : sequence<string>
clipPath : SdfPath
startTimeCode : double
endTimeCode : double
clipSet : TfToken


A function that creates layers that use USD Value Clips to effectively
merge the time samples in the given C{clipLayers} under C{clipPath}
without copying the samples into a separate layer.


C{resultLayer} The layer to which clip meta data and frame data will
be written. The layer representing the static scene topology will be
authored as a sublayer on this layer as well; it will be authored as
the first sublayer in the list(strongest).

C{clipLayerFiles} The files containing the time varying data.

C{clipPath} The path at which we will put the clip meta data.

C{startTimeCode} The first time coordinate for the rootLayer to point
to. If none is provided, it will be the lowest startTimeCode available
from the C{clipLayers}.

C{endTimeCode} The last time coordinate for the rootLayer to point to.
If none is provided, it will be the highest endTimeCode authored from
the C{clipLayers}.

C{clipSet} The name of the clipSet in which the aforementioned
metadata will be authored.

If this parameter is omitted, the default clipSet name will be
authored. Details on how this is accomplished can be found below:

Pre-existing opinions will be wiped away upon success. Upon failure,
the original topology layer, if it was pre-existing, will be
preserved. Topology layers will be named/looked up via the following
scheme: topologyLayerName =<resultIdWithoutExt>.topology.<resultExt>

For example: if the resultLayerFile's name is foo.usd the expected
topology layer will be foo.topology.usd.

This layer contains the aggregated topology of the set of
C{clipLayers}. This process will merge prims and properties, save for
time varying properties, those will be accessed from the original clip
files.

The aggregation of topology works by merging a clipLayer at a time
with the topologyLayer. If a prim already exists in the topologyLayer,
its attributes will be merged.

For example, if we have a layer, clipA with attributes
/World/fx/foo.bar and a second layer with /World/fx/foo.baz. Our
aggregate topology layer will contain both /World/fx/foo.bar,
/World/fx/foo.baz.

The C{resultLayer} will contain clip meta data: clipTimes,
clipPrimPath clipManifestAssetPath, clipActive etc. at the specified
C{clipPath}. The resultLayer will also have timeCode range data, such
as start and end timeCodes written to it, with the starting position
being provided by C{startTimeCode} and the ending provided by
C{endTimeCode}.

Note: an invalid clip path(because the prim doesn't exist in the
aggregate topologyLayer) will result in a TF_CODING_ERROR.

"""
   result["CoalescingDiagnosticDelegateItem"].__doc__ = """
An item used in coalesced results, containing a shared component: the
file/function/line number, and a set of unshared components: the call
context and commentary.

"""
   result["GetAlphaAttributeNameForColor"].func_doc = """GetAlphaAttributeNameForColor(colorAttrName) -> USDUTILS_API TfToken

colorAttrName : TfToken


Define the shading pipeline's convention for naming a companion
alpha/opacity attribute and primvarnames given the full name of a
color-valued attribute.

"""
   result["CopyLayerMetadata"].func_doc = """CopyLayerMetadata(source, destination, skipSublayers, bakeUnauthoredFallbacks) -> USDUTILS_API bool

source : SdfLayerHandle
destination : SdfLayerHandle
skipSublayers : bool
bakeUnauthoredFallbacks : bool


Given two layers C{source} and C{destination}, copy the authored
metadata from one to the other.


By default, copy B{all} authored metadata; however, you can skip
certain classes of metadata with the parameter C{skipSublayers}, which
will prevent copying subLayers or subLayerOffsets

Makes no attempt to clear metadata that may already be authored in
C{destination}, but any fields that are already in C{destination} but
also in C{source} will be replaced.

Certain bits of layer metadata (eg. colorConfiguration and
colorManagementSystem) can have their fallback values specified in the
plugInfo.json files of plugins. When such metadata is unauthored in
the source layer, if C{bakeUnauthoredFallbacks} is set to true, then
the fallback values are baked intothe destination layer.

C{true} on success, C{false} on error.

"""
   result["GetPrimaryUVSetName"].func_doc = """GetPrimaryUVSetName() -> USDUTILS_API TfToken



Returns the name of the primary UV set used on meshes and nurbs.


By default the name is "st".

"""
   result["GetModelNameFromRootLayer"].func_doc = """GetModelNameFromRootLayer(rootLayer) -> USDUTILS_API TfToken

rootLayer : SdfLayerHandle


Returns the model name associated with a given root layer.


In order, it looks for defaultPrim metadata, a prim matching the
filename, and then the first concrete root prim.

"""
   result["ExtractExternalReferences"].func_doc = """ExtractExternalReferences(filePath, subLayers, references, payloads) -> USDUTILS_API void

filePath : string
subLayers : sequence<string>
references : sequence<string>
payloads : sequence<string>


Parses the file at C{filePath}, identifying external references, and
sorting them into separate type-based buckets.


Sublayers are returned in the C{sublayers} vector, references, whether
prim references, value clip references or values from asset path
attributes, are returned in the C{references} vector. Payload paths
are returned in C{payloads}.

No recursive chasing of dependencies is performed; that is the
client's responsibility, if desired.

Not all returned references are actually authored explicitly in the
layer. For example, templated clip asset paths are resolved and
expanded to include all available clip files that match the specified
pattern.

"""
   result["ComputeUsdStageStats"].func_doc = """ComputeUsdStageStats(rootLayerPath, stats) -> USDUTILS_API UsdStageRefPtr

rootLayerPath : string
stats : VtDictionary


Opens the given layer on a USD stage and collects various stats.


The stats are populated in the dictionary-valued output param
C{stats}.

The set of stats include:
   - approxMemoryInMb - approximate memory allocated when opening the
     stage with all the models loaded.

   - totalPrimCount - total number of prims

   - modelCount - number of models

   - instancedModelCount - number of instanced models

   - assetCount - number of assets

   - masterCount - number of masters

   - totalInstanceCount - total number of instances (including nested
     instances)

   - two sub-dictionaries, 'primary' and 'masters' for the "primary"
     prim tree and for all the master subtrees respectively, containing the
     following stats:

   - primCounts - a sub-dictionary containing the following
   - totalPrimCount - number of prims

   - activePrimCount - number of active prims

   - inactivePrimCount - number of inactive prims

   - pureOverCount - number of pure overs

   - instanceCount - number of instances

   - primCountsByType - a sub-dictionary containing prim counts keyed
     by the prim type.

Returns the stage that was opened.

The "masters" subdictionary is populated only if the stage has one ore
more instanced models.

The approximate memory allocated when opening the stage is computed
and reported *only* if the TfMallocTag system has already been
initialized by the client, and the number will represent only
*additional* consumed memory, so if some of the layers the stage uses
are already open, the true memory consumption for the stage may be
higher than reported.

TfMallocTag::IsInitialized()

Only component models are included in 'modelCount' and
'instancedModelCount'.


----------------------------------------------------------------------
ComputeUsdStageStats(stage, stats) -> USDUTILS_API size_t

stage : UsdStageWeakPtr
stats : VtDictionary


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Computes stats on an already opened USD stage.


Returns the total number of prims on the stage, including active,
inactive. pure overs, prims inside masters etc.

"""
   result["ComputeAllDependencies"].func_doc = """ComputeAllDependencies(assetPath, layers, assets, unresolvedPaths) -> USDUTILS_API bool

assetPath : SdfAssetPath
layers : sequence<SdfLayerRefPtr>
assets : sequence<string>
unresolvedPaths : sequence<string>


Recursively computes all the dependencies of the given asset and
populates C{layers} with all the dependencies that can be opened as an
SdfLayer.


All of the resolved non-layer dependencies are populated in C{assets}.
Any unresolved (layer and non-layer) asset paths are populated in
C{unresolvedPaths}.

The input vectors to be populated with the results are are *cleared*
before any results are added to them.

Returns true if the given asset was resolved correctly.

"""
   result["GetDirtyLayers"].func_doc = """GetDirtyLayers(stage, includeClipLayers) -> USDUTILS_API SdfLayerHandleVector

stage : UsdStagePtr
includeClipLayers : bool


Retrieve a list of all dirty layers from the stage's UsedLayers.

"""
   result["CreateNewUsdzPackage"].func_doc = """CreateNewUsdzPackage(assetPath, usdzFilePath, firstLayerName) -> USDUTILS_API bool

assetPath : SdfAssetPath
usdzFilePath : string
firstLayerName : string


Creates a USDZ package containing the specified asset, identified by
its C{assetPath}.


The created package will include a localized version of the asset
itself and all of its external dependencies. Due to localization, the
packaged layers might be modified to have different asset paths.

You can optionally specify a different package-internal name for the
first layer of the asset by specifying C{firstLayerName}. By default,
C{firstLayerName} is empty, meaning that the original name is
preserved.

Returns true if the package was created successfully.

Clients of this function must take care of configuring the asset
resolver context before invoking the function. To create a default
resolver context, use CreateDefaultContextForAsset() with the asset
path.

If the given asset has a dependency on a directory (i.e. an external
reference to a directory path), the dependency is ignored and the
contents of the directory are not included in the created package.

"""
   result["GenerateClipTopologyName"].func_doc = """GenerateClipTopologyName(rootLayerName) -> USDUTILS_API string

rootLayerName : string


Generates a topology file name based on an input file name.


For example, if given 'foo.usd', it generates 'foo.topology.usd'

Note: this will not strip preceding paths off of a file name so
/bar/baz/foo.usd will produce /bar/baz/foo.topology.usd

C{rootLayerName} The filepath used as a basis for generating our
topology layer name.

"""
   result["ComputeCollectionIncludesAndExcludes"].func_doc = """ComputeCollectionIncludesAndExcludes(includedRootPaths, usdStage, pathsToInclude, pathsToExclude, minInclusionRatio, maxNumExcludesBelowInclude, minIncludeExcludeCollectionSize, pathsToIgnore) -> USDUTILS_API bool

includedRootPaths : SdfPathSet
usdStage : UsdStageWeakPtr
pathsToInclude : SdfPathVector
pathsToExclude : SdfPathVector
minInclusionRatio : double
maxNumExcludesBelowInclude : unsigned int
minIncludeExcludeCollectionSize : unsigned int
pathsToIgnore : PathHashSet


Computes the optimal set of paths to include and the set of paths to
exclude below includes paths, in order to encode an "expandPrims"
collection that contains the subtrees of prims rooted at
C{includedRootPaths}.


The algorithm used to determine a compact representation is driven by
the following three parameters: C{minInclusionRatio},
C{maxNumExcludesBelowInclude} and C{minIncludeExcludeCollectionSize}.
See below for their descriptions.

C{usdStage} is the USD stage to which the paths in
C{includedRootPaths} belong. C{pathsToInclude} is populated with the
set of paths to include. Any existing paths in the set are cleared
before adding paths to it. C{pathsToExclude} is populated with the set
of paths to exclude. Any existing paths in the set are cleared before
adding paths to it. C{minInclusionRatio} is the minimum value of the
ratio between the number of included paths and the sum of the number
of included and excluded paths below an ancestor path, at or above
which the ancestor path is included in the collection. For example, if
an ancestor prim has four children and three out of the four are
included in the collection, the inclusion ratio at the ancestor is
0.75. This value should be in the range (0,1), if not, it's clamped to
the range. C{maxNumExcludesBelowInclude} is the maximum number of
paths that we exclude below any ancestor path that we include in a
collection. This parameter only affects paths that have already passed
the min-inclusion-ratio test. Setting this to 0 will cause all
collections to have includes only (and no excludes). Setting it to a
higher number will cause ancestor paths that are higher up in the
namespace hierarchy to be included in collections.
C{minIncludeExcludeCollectionSize} is the minimum size of a collection
(i.e. the number of subtree-root paths included in it), at or above
which the algorithm chooses to make a collection with both included
and excluded paths, instead of creating a collection with only
includes (containing the specified set of paths). UsdCollectionAPI
C{pathsToIgnore} is the list of paths to be ignored by the algorithm
used to determine the included and excluded paths for each collection.
If non-empty, the paths in the hash set don't contribute towards the
counts and ratios computed by the algorithm.

Returns false if paths in C{includedRootPaths} (or their common
ancestor) can't be found on the given C{usdStage}. parameters has an
invalid value.

The python version of this function returns a tuple containing the two
lists (pathsToInclude, pathsToExclude).

"""
   result["CreateNewARKitUsdzPackage"].func_doc = """CreateNewARKitUsdzPackage(assetPath, usdzFilePath, firstLayerName) -> USDUTILS_API bool

assetPath : SdfAssetPath
usdzFilePath : string
firstLayerName : string


Similar to UsdUtilsCreateNewUsdzPackage, this function packages all of
the dependencies of the given asset.


Assets targeted at the initial usdz implementation in ARKit operate
under greater constraints than usdz files for more general 'in house'
uses, and this option attempts to ensure that these constraints are
honored; this may involve more transformations to the data, which may
cause loss of features such as VariantSets.

If C{firstLayerName} is specified, it is modified to have the ".usdc"
extension, as required by the initial usdz implementation in ARKit.

Returns true if the package was created successfully.

Clients of this function must take care of configuring the asset
resolver context before invoking the function. To create a default
resolver context, use CreateDefaultContextForAsset() with the asset
path.

If the given asset has a dependency on a directory (i.e. an external
reference to a directory path), the dependency is ignored and the
contents of the directory are not included in the created package.

"""
   result["GetPrimAtPathWithForwarding"].func_doc = """GetPrimAtPathWithForwarding(stage, path) -> USDUTILS_API UsdPrim

stage : UsdStagePtr
path : SdfPath


If a valid UsdPrim already exists at C{path} on the USD stage
C{stage}, returns it.


It not, it checks to see if the path belongs to a prim underneath an
instance and returns the corresponding master prim.

This returns an invalid UsdPrim if no corresponding master prim can be
found and if no prim exists at the path.

This method is similar to UsdStage::GetPrimAtPath() , in that it will
never author scene description, and therefore is safe to use as a
"reader" in the Usd multi-threading model.

"""
   result["GetPrefName"].func_doc = """GetPrefName() -> USDUTILS_API TfToken



Returns the name of the reference position used on meshes and nurbs.


By default the name is "pref".

"""
   result["SparseValueWriter"].__doc__ = """
Utility class that manages sparse authoring of a set of UsdAttributes.


It does this by maintaining a map of UsdAttributes to their
corresponding UsdUtilsSparseAttrValueWriter objects.

To use this class, simply instantiate an instance of it and invoke the
SetAttribute() method with various attributes and their associated
time-samples.

If the attribute has a default value, SetAttribute() must be called
with time=Default first (multiple times, if necessary), followed by
calls to author time-samples in sequentially increasing time order.

This class is not threadsafe. In general, authoring to a single USD
layer from multiple threads isn't threadsafe. Hence, there is little
value in making this class threadsafe. Example c++ usage: ::

  UsdGeomCylinder cylinder = UsdGeomCylinder::Define(stage, SdfPath("/Cylinder"));
  UsdAttribute radius = cylinder.CreateRadiusAttr();
  UsdAttribute height = cylinder.CreateHeightAttr();
  UsdUtilsSparseValueWriter valueWriter;
  valueWriter.SetAttribute(radius, 2.0, UsdTimeCode::Default());
  valueWriter.SetAttribute(height, 2.0, UsdTimeCode::Default());
  
  valueWriter.SetAttribute(radius, 10.0, UsdTimeCode(1.0));
  valueWriter.SetAttribute(radius, 20.0, UsdTimeCode(2.0));
  valueWriter.SetAttribute(radius, 20.0, UsdTimeCode(3.0));
  valueWriter.SetAttribute(radius, 20.0, UsdTimeCode(4.0));
  
  valueWriter.SetAttribute(height, 2.0, UsdTimeCode(1.0));
  valueWriter.SetAttribute(height, 2.0, UsdTimeCode(2.0));
  valueWriter.SetAttribute(height, 3.0, UsdTimeCode(3.0));
  valueWriter.SetAttribute(height, 3.0, UsdTimeCode(4.0));

Equivalent python code: ::

  cylinder = UsdGeom.Cylinder.Define(stage, Sdf.Path("/Cylinder"))
  radius = cylinder.CreateRadiusAttr()
  height = cylinder.CreateHeightAttr()
  valueWriter = UsdUtils.SparseValueWriter()
  valueWriter.SetAttribute(radius, 2.0, Usd.TimeCode.Default())
  valueWriter.SetAttribute(height, 2.0, Usd.TimeCode.Default())
  
  valueWriter.SetAttribute(radius, 10.0, 1.0)
  valueWriter.SetAttribute(radius, 20.0, 2.0)
  valueWriter.SetAttribute(radius, 20.0, 3.0)
  valueWriter.SetAttribute(radius, 20.0, 4.0)
  
  valueWriter.SetAttribute(height, 2.0, 1.0)
  valueWriter.SetAttribute(height, 2.0, 2.0)
  valueWriter.SetAttribute(height, 3.0, 3.0)
  valueWriter.SetAttribute(height, 3.0, 4.0)

In the above example,
   - The default value of the "height" attribute is not authored into
     scene description since it matches the fallback value.

   - Time-samples at time=3.0 and time=4.0 will be skipped for the
     radius attribute.

   - For the "height" attribute, the first timesample at time=1.0 will
     be skipped since it matches the default value.

   - The last time-sample at time=4.0 will also be skipped for
     "height" since it matches the previously written value at time=3.0.


"""
   result["SparseValueWriter"].SetAttribute.im_func.func_doc = """SetAttribute(attr, value, time) -> USDUTILS_API bool

attr : UsdAttribute
value : VtValue
time : UsdTimeCode


Sets the value of C{attr} to C{value} at time C{time}.


The value is written sparsely, i.e., the default value is authored
only if it is different from the fallback value or the existing
default value, and any redundant time-samples are skipped when the
attribute value does not change significantly between consecutive
time-samples.


----------------------------------------------------------------------
SetAttribute(attr, value, time) -> USDUTILS_API bool

attr : UsdAttribute
value : VtValue
time : UsdTimeCode


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
For efficiency, this function swaps out the given C{value}, leaving it
empty.


The value will be held in memory at least until the next time-sample
is written or until the SparseAttrValueWriter instance is destroyed.


----------------------------------------------------------------------
SetAttribute(attr, value, time) -> bool

attr : UsdAttribute
value : T
time : UsdTimeCode


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["SparseAttrValueWriter"].__doc__ = """
A utility class for authoring time-varying attribute values with
simple run-length encoding, by skipping any redundant time-samples.


Time-samples that are close enough to each other, with relative
difference smaller than a fixed epsilon value are considered to be
equivalent. This is to avoid unnecessary authoring of time-samples
caused by numerical fuzz in certain computations.

For vectors, matrices, and other composite types (like quaternions and
arrays), each component is compared with the corresponding component
for closeness. The chosen epsilon value for double precision floating
point numbers is 1e-12. For single-precision, it is 1e-6 and for half-
precision, it is 1e-2.

Example c++ usage: ::

  UsdGeomSphere sphere = UsdGeomSphere::Define(stage, SdfPath("/Sphere"));
  UsdAttribute radius = sphere.CreateRadiusAttr();
  UsdUtilsSparseAttrValueWriter attrValueWriter(radius, 
          /*defaultValue*/ VtValue(1.0));
  attrValueWriter.SetTimeSample(VtValue(10.0), UsdTimeCode(1.0));
  attrValueWriter.SetTimeSample(VtValue(10.0), UsdTimeCode(2.0));
  attrValueWriter.SetTimeSample(VtValue(10.0), UsdTimeCode(3.0));
  attrValueWriter.SetTimeSample(VtValue(20.0), UsdTimeCode(4.0));

Equivalent python example: ::

  sphere = UsdGeom.Sphere.Define(stage, Sdf.Path("/Sphere"))
  radius = sphere.CreateRadiusAttr()
  attrValueWriter = UsdUtils.SparseAttrValueWriter(radius, defaultValue=1.0)
  attrValueWriter.SetTimeSample(10.0, 1.0)
  attrValueWriter.SetTimeSample(10.0, 2.0)
  attrValueWriter.SetTimeSample(10.0, 3.0)
  attrValueWriter.SetTimeSample(20.0, 4.0)

In the above examples, the specified default value of radius (1.0)
will not be authored into scene description since it matches the
fallback value. Additionally, the time-sample authored at time=2.0
will be skipped since it is redundant. Also note that for correct
behavior, the calls to SetTimeSample() must be made with sequentially
increasing time values. If not, a coding error is issued and the
authored animation may be incorrect.

"""
   result["SparseAttrValueWriter"].__init__.im_func.func_doc = """__init__(attr, defaultValue) -> USDUTILS_API

attr : UsdAttribute
defaultValue : VtValue


The constructor initializes the data required for run-length encoding
of time-samples.


It also sets the default value of C{attr} to C{defaultValue}, if
C{defaultValue} is non-empty and different from the existing default
value of C{attr}.

C{defaultValue} can be unspecified (or left empty) if you don't care
about authoring a default value. In this case, the sparse authoring
logic is initialized with the existing authored default value or the
fallback value, if C{attr} has one.


----------------------------------------------------------------------
__init__(attr, defaultValue) -> USDUTILS_API

attr : UsdAttribute
defaultValue : VtValue


The constructor initializes the data required for run-length encoding
of time-samples.


It also sets the default value of C{attr} to C{defaultValue}, if
C{defaultValue} is non-empty and different from the existing default
value of C{attr}.

It C{defaultValue} is null or points to an empty VtValue, the sparse
authoring logic is intialized with the existing authored default value
or the fallback value, if C{attr} has one.

For efficiency, this function swaps out the given C{defaultValue},
leaving it empty.

"""
   result["SparseAttrValueWriter"].SetTimeSample.im_func.func_doc = """SetTimeSample(value, time) -> USDUTILS_API bool

value : VtValue
time : UsdTimeCode


Sets a new time-sample on the attribute with given C{value} at the
given C{time}.


The time-sample is only authored if it's different from the previously
set time-sample, in which case the previous time-sample is also
authored, in order to to end the previous run of contiguous identical
values and start a new run.

This incurs a copy of C{value}. Also, the value will be held in memory
at least until the next time-sample is written or until the
SparseAttrValueWriter instance is destroyed.


----------------------------------------------------------------------
SetTimeSample(value, time) -> USDUTILS_API bool

value : VtValue
time : UsdTimeCode


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

For efficiency, this function swaps out the given C{value}, leaving it
empty.


The value will be held in memory at least until the next time-sample
is written or until the SparseAttrValueWriter instance is destroyed.

"""
   result["FlattenLayerStack"].func_doc = """FlattenLayerStack(stage, tag) -> USDUTILS_API SdfLayerRefPtr

stage : UsdStagePtr
tag : string


Flatten the root layer stack of the given C{stage} into a single layer
with the given optional C{tag}.


The result layer can be substituted for the original layer stack while
producing the same composed UsdStage.

Unlike UsdStage::Export() , this function does not flatten composition
arcs, such as references, payloads, inherits, specializes, or
variants.

Sublayer time offsets on the sublayers will be applied to remap any
time-keyed scene description, such as timeSamples and clips.

Asset paths will be resolved to absolute form, to ensure that they
continue to identify the same asset from the output layer.

A few historical scene description features cannot be flattened into a
single opinion because they unfortunately encode operations that are
not closed under composition. Specifically, the SdfListOp operations
"add" and "reorder" cannot be flattened. Instead, "add" will be
converted to "append", and "reorder" will be discarded.

"""