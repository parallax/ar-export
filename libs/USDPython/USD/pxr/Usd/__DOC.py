def Execute(result):
   result["StageCacheContext"].__doc__ = """
A context object that lets the UsdStage::Open() API read from or read
from and write to a UsdStageCache instance during a scope of
execution.


Code examples illustrate typical use: ::

  {
      // A stage cache to work with.
      UsdStageCache stageCache;
  
      // Bind this cache.  UsdStage::Open() will attempt to find a matching
      // stage in the cache.  If none is found, it will open a new stage and
      // insert it into the cache.
      UsdStageCacheContext context(stageCache);
  
      // Since the cache is currently empty, this Open call will not find an
      // existing stage in the cache, but will insert the newly opened stage
      // in it.
      auto stage = UsdStage::Open(<args>);
  
      assert(stageCache.Contains(stage));
      
      // A subsequent Open() call with the same arguments will retrieve the
      // stage from cache.
      auto stage2 = UsdStage::Open(<args>);
      assert(stage2 == stage);
  }

The UsdStage::Open() API examines caches in UsdStageCacheContexts that
exist on the stack in the current thread in order starting with the
most recently created (deepest in the stack) to the least recently
created.

The UsdUseButDoNotPopulateCache() function makes a cache available for
UsdStage::Open() to find stages in, but newly opened stages will not
be published to it. This can be useful if you want to make use of a
cache but cannot or do not wish to mutate that cache.

Passing UsdBlockStageCaches disables cache use entirely (as if no
UsdStageCacheContexts exist on the stack), while
UsdBlockStageCachePopulation disables writing to all bound caches (as
if they were all established with UsdUseButDoNotPopulateCache()).

Threading note: Different threads have different call stacks, so
UsdStageCacheContext objects that exist in one thread's stack do not
influence calls to UsdStage::Open() from a different thread.

"""
   result["_PrimFlagsDisjunction"].__doc__ = """
Disjunction of prim flag predicate terms.


Usually clients will implicitly create disjunctions by ||-ing together
flag predicate terms. For example: ::

  // Get all deactivated or undefined children.
  prim.GetFilteredChildren(!UsdPrimIsActive || !UsdPrimIsDefined)

See primFlags.h for more details.

"""
   result["Notice"].__doc__ = """
Container class for Usd notices.

"""
   result["Notice"].StageNotice.__doc__ = """
Base class for UsdStage notices.

"""
   result["Notice"].StageNotice.GetStage.im_func.func_doc = """GetStage() -> StageWeakPtr



Return the stage associated with this notice.

"""
   result["Notice"].StageContentsChanged.__doc__ = """
Ultra-conservative notice sent when the given UsdStage 's contents
have changed in any way.


This notice is sent when *any* authoring is performed in any of the
stage's participatory layers, in the thread performing the authoring,
*after* the affected UsdStage has reconfigured itself in response to
the authored changes.

Receipt of this notice should cause clients to disregard any cached
values for properties or metadata. It does not *necessarily* imply
invalidation of UsdPrim s.

"""
   result["Notice"].StageEditTargetChanged.__doc__ = """
Notice sent when a stage's EditTarget has changed.


Sent in the thread that changed the target.

"""
   result["Notice"].ObjectsChanged.__doc__ = """
Notice sent in response to authored changes that affect UsdObjects.


The kinds of object changes are divided into two categories: "resync"
and "changed-info". "Resyncs" are potentially structural changes that
invalidate entire subtrees of UsdObjects (including prims and
properties). For example, if the path "/foo" is resynced, then all
subpaths like "/foo/bar" and "/foo/bar.baz" may be arbitrarily
changed. In contrast, "changed-info" means that a nonstructural change
has occurred, like an attribute value change or a value change to a
metadata field not related to composition.

When a prim is resynced, say "/foo/bar", it might have been created or
destroyed. In that case "/foo"'s list of children will have changed,
but we *do not* consider "/foo" to be resynced. If we did, it would
mean clients would have to consider all of "/foo/bar"'s siblings (and
their descendants) to be resynced which might be egregious
overinvalidation.

This notice provides API for two client use-cases. Clients interested
in testing whether specific objects are affected by the changes should
use the AffectedObject() method (and the ResyncedObject() and
ChangedInfoOnly() methods). Clients that wish to reason about all
changes as a whole should use the GetResyncedPaths() and
GetChangedInfoOnlyPaths() methods.

"""
   result["Notice"].ObjectsChanged.ChangedInfoOnly.im_func.func_doc = """ChangedInfoOnly(obj) -> USD_API bool

obj : Object


Return true if C{obj} was changed but not resynced by the layer
changes that generated this notice.

"""
   result["Notice"].ObjectsChanged.ResyncedObject.im_func.func_doc = """ResyncedObject(obj) -> USD_API bool

obj : Object


Return true if C{obj} was resynced by the layer changes that generated
this notice.


This is the case if the object's path or an ancestor path is present
in GetResyncedPrimPaths().

"""
   result["Notice"].ObjectsChanged.GetChangedInfoOnlyPaths.im_func.func_doc = """GetChangedInfoOnlyPaths() -> USD_API PathRange



Return the set of paths that have only info changes (those that do not
affect the structure of cached UsdPrims on a UsdStage) in
lexicographical order.


Info changes do not imply entire subtree invalidation, so this set is
not minimal regarding ancestors and descendants, as opposed to
GetResyncedPaths() . For example, both the paths '/foo' and '/foo/bar'
may appear in this set.

"""
   result["Notice"].ObjectsChanged.GetChangedFields.im_func.func_doc = """GetChangedFields(obj) -> USD_API TfTokenVector

obj : Object


Return the set of changed fields in layers that affected C{obj}.


This set will be empty for objects whose paths are not in
GetResyncedPaths() or GetChangedInfoOnlyPaths() .  If a field is
present in this set, it does not necessarily mean the composed value
of that field on C{obj} has changed. For example, if a metadata value
on C{obj} is overridden in a stronger layer and is changed in a weaker
layer, that field will appear in this set. However, since the value in
the stronger layer did not change, the composed value returned by
GetMetadata() will not have changed.


----------------------------------------------------------------------
GetChangedFields(path) -> USD_API TfTokenVector

path : SdfPath


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Notice"].ObjectsChanged.AffectedObject.im_func.func_doc = """AffectedObject(obj) -> bool

obj : Object


Return true if C{obj} was possibly affected by the layer changes that
generated this notice.


This is the case if either the object is subject to a resync or has
changed info. Equivalent to: ::

  ResyncedObject(obj) or ChangedInfoOnly(obj)


"""
   result["Notice"].ObjectsChanged.HasChangedFields.im_func.func_doc = """HasChangedFields(obj) -> USD_API bool

obj : Object


Return true if there are any changed fields that affected C{obj},
false otherwise.


See GetChangedFields for more details.


----------------------------------------------------------------------
HasChangedFields(path) -> USD_API bool

path : SdfPath


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Notice"].ObjectsChanged.GetResyncedPaths.im_func.func_doc = """GetResyncedPaths() -> USD_API PathRange



Return the set of paths that are resynced in lexicographical order.


Resyncs imply entire subtree invalidation of all descendant prims and
properties, so this set is minimal regarding ancestors and
descendants. For example, if the path '/foo' appears in this set, the
entire subtree at '/foo' is resynced so the path '/foo/bar' will not
appear, but it should be considered resynced.

"""
   result["UseButDoNotPopulateCache"].func_doc = """UseButDoNotPopulateCache(cache) -> _NonPopulatingStageCacheWrapper

cache : StageCache


Indicate that a UsdStageCacheContext should be bound in a read-only
fashion.


Calls to UsdStage::Open() will attempt to find stages in C{cache} when
a UsdStageCacheContext is present on the stack. See
UsdStageCacheContext for more details and example use.

"""
   result["EditTarget"].__doc__ = """
Defines a mapping from scene graph paths to Sdf spec paths in a
SdfLayer where edits should be directed, or up to where to perform
partial composition.


A UsdEditTarget can represent an arbitrary point in a composition
graph for the purposes of placing edits and resolving values. This
enables editing and resolving across references, classes, variants,
and payloads.

In the simplest case, an EditTarget represents a single layer in a
stage's local LayerStack. In this case, the mapping that transforms
scene graph paths to spec paths in the layer is the identity function.
That is, the UsdAttribute path '/World/Foo.avar' would map to the
SdfPropertySpec path '/World/Foo.avar'.

For a more complex example, suppose '/World/Foo' in 'Shot.usda' is a
reference to '/Model' in 'Model.usda'. One can construct a
UsdEditTarget that maps scene graph paths from the 'Shot.usda' stage
across the reference to the appropriate paths in the 'Model.usda'
layer. For example, the UsdAttribute '/World/Foo.avar' would map to
the SdfPropertySpec '/Model.avar'. Paths in the stage composed at
'Shot.usda' that weren't prefixed by '/World/Foo' would not have a
valid mapping to 'Model.usda'.

EditTargets may also work for any other kind of arc or series of arcs.
This allows for editing across variants, classes, and payloads, or in
a variant on the far side of a reference, for example.

In addition to mapping scene paths to spec paths for editing,
EditTargets may also be used to identify points in the composition
graph for partial composition. Though it doesn't currently exist, a
UsdCompose API that takes UsdEditTarget arguments may someday be
provided.

For convenience and deployment ease, SdfLayerHandles will implicitly
convert to UsdEditTargets. A UsdEditTarget constructed in this way
means direct opinions in a layer in a stage's local LayerStack.

"""
   result["EditTarget"].GetSpecForScenePath.im_func.func_doc = """GetSpecForScenePath(scenePath) -> USD_API SdfSpecHandle

scenePath : SdfPath

"""
   result["EditTarget"].__init__.im_func.func_doc = """__init__() -> USD_API



Construct a null EditTarget.


A null EditTarget will return paths unchanged when asked to map paths.


----------------------------------------------------------------------
__init__(layer, offset) -> USD_API

layer : SdfLayerHandle
offset : SdfLayerOffset


Constructor.


Allow implicit conversion from SdfLayerHandle. EditTargets constructed
in this way specify layers in the scene's local LayerStack. This lets
clients pass layers directly in this common case without explicitly
having to construct a *UsdEditTarget* instance. To automatically
supply the appropriate layer offset for the given layer, see
UsdStage::GetEditTargetForLayer().


----------------------------------------------------------------------
__init__(layer, offset) -> USD_API

layer : SdfLayerRefPtr
offset : SdfLayerOffset


Convenience implicit conversion from SdfLayerRefPtr.


See above constructor for more information.


----------------------------------------------------------------------
__init__(layer, node) -> USD_API

layer : SdfLayerHandle
node : PcpNodeRef


Construct an EditTarget with *layer* and *node*.


The mapping will be used to map paths from the scene into the
*layer's* namespace given the *PcpNodeRef* *node's* mapping.


----------------------------------------------------------------------
__init__(layer, node) -> USD_API

layer : SdfLayerRefPtr
node : PcpNodeRef


Convenience constructor taking SdfLayerRefPtr.


See above constructor for more information.


----------------------------------------------------------------------
__init__(layer, mapping)

layer : SdfLayerHandle
mapping : PcpMapFunction

"""
   result["EditTarget"].ComposeOver.im_func.func_doc = """ComposeOver(weaker) -> USD_API UsdEditTarget

weaker : EditTarget


Return a new EditTarget composed over *weaker*.


This is typically used to make an EditTarget "explicit". For example,
an edit target with a layer but with no mapping and no LayerStack
identifier indicates a layer in the local LayerStack of a composed
scene. However, an EditTarget with the same layer but an explicit
identity mapping and the LayerStack identifier of the composed scene
may be desired. This can be obtained by composing a partial (e.g.
layer only) EditTarget over an explicit EditTarget with layer, mapping
and layer stack identifier.

"""
   result["EditTarget"].IsValid.im_func.func_doc = """IsValid() -> bool



Return true if this EditTarget is valid, false otherwise.


Edit targets are considered valid when they have a layer.

"""
   result["EditTarget"].GetMapFunction.im_func.func_doc = """GetMapFunction() -> PcpMapFunction



Returns the PcpMapFunction representing the map from source specs
(including any variant selections) to the stage.

"""
   result["EditTarget"].GetPropertySpecForScenePath.im_func.func_doc = """GetPropertySpecForScenePath(scenePath) -> USD_API SdfPropertySpecHandle

scenePath : SdfPath

"""
   result["EditTarget"].IsNull.im_func.func_doc = """IsNull() -> bool



Return true if this EditTarget is null.


Null EditTargets map paths unchanged, and have no layer or LayerStack
identifier.

"""
   result["EditTarget"].MapToSpecPath.im_func.func_doc = """MapToSpecPath(scenePath) -> USD_API SdfPath

scenePath : SdfPath


Map the provided *scenePath* into a SdfSpec path for the EditTarget's
layer, according to the EditTarget's mapping.


Null edit targets and EditTargets for which *IsLocalLayer* are true
return scenePath unchanged.

"""
   result["EditTarget"].GetLayer.im_func.func_doc = """GetLayer() -> SdfLayerHandle



Return the layer this EditTarget contains.

"""
   result["EditTarget"].GetPrimSpecForScenePath.im_func.func_doc = """GetPrimSpecForScenePath(scenePath) -> USD_API SdfPrimSpecHandle

scenePath : SdfPath


Convenience function for getting the PrimSpec in the edit target's
layer for *scenePath*.


This is equivalent to
target.GetLayer()->GetPrimAtPath(target.MapToSpecPath(scenePath)) if
target has a valid layer. If this target IsNull or there is no valid
mapping from *scenePath* to a SdfPrimSpec path in the layer, return
null.

"""
   result["EditTarget"].ForLocalDirectVariant.func_doc = """**static** ForLocalDirectVariant(layer, varSelPath) -> USD_API UsdEditTarget

layer : SdfLayerHandle
varSelPath : SdfPath


Convenience constructor for editing a direct variant in a local
LayerStack.


The C{varSelPath} must be a prim variant selection path (see
SdfPath::IsPrimVariantSelectionPath() ).

"""
   result["PrepLayerOffset"].func_doc = """PrepLayerOffset(offset) -> USD_API SdfLayerOffset

offset : SdfLayerOffset


Prepare the given offset for application to map layer time to stage
time, respecting the environment variable
USD_USE_INVERSE_LAYER_OFFSET.


Typically, the supplied SdfLayerOffset will come from Pcp  in a
PcpNodeRef or PcpLayerStack  and represent the cumulative offset to
transform data from a layer to the Usd stage.

Historically, USD applied the inverse of that offset, flipping the
intended semantics. To address this, this function provides a
temporary measure to control whether to take the inverse or not. Under
the new behavior this function will become a no-op, and can eventually
be phased out.

"""
   result["AttributeQuery"].__doc__ = """
Object for efficiently making repeated queries for attribute values.


Retrieving an attribute's value at a particular time requires
determining the source of strongest opinion for that value. Often
(i.e. unless the attribute is affected by Value Clips) this source
does not vary over time. UsdAttributeQuery uses this fact to speed up
repeated value queries by caching the source information for an
attribute. It is safe to use a UsdAttributeQuery for any attribute -
if the attribute *is* affected by Value Clips, the performance gain
will just be less.

safety
======

This object provides the basic thread-safety guarantee. Multiple
threads may call the value accessor functions simultaneously.

Invalidation
============

This object does not listen for change notification. If a consumer is
holding on to a UsdAttributeQuery, it is their responsibility to
dispose of it in response to a resync change to the associated
attribute. Failing to do so may result in incorrect values or crashes
due to dereferencing invalid objects.

"""
   result["AttributeQuery"].HasFallbackValue.im_func.func_doc = """HasFallbackValue() -> USD_API bool



Return true if the attribute associated with this query has a fallback
value provided by a registered schema.



UsdAttribute::HasFallbackValue

"""
   result["AttributeQuery"].Get.im_func.func_doc = """Get(value, time) -> bool

value : T
time : TimeCode


Perform value resolution to fetch the value of the attribute
associated with this query at the requested UsdTimeCode C{time}.



UsdAttribute::Get


----------------------------------------------------------------------
Get(value, time) -> USD_API bool

value : VtValue
time : TimeCode


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Type-erased access, often not as efficient as typed access.

"""
   result["AttributeQuery"].GetAttribute.im_func.func_doc = """GetAttribute() -> USD_API  UsdAttribute



Return the attribute associated with this query.

"""
   result["AttributeQuery"].IsValid.im_func.func_doc = """IsValid() -> bool



Return true if this query is valid (i.e.


it is associated with a valid attribute), false otherwise.

"""
   result["AttributeQuery"].HasValue.im_func.func_doc = """HasValue() -> USD_API bool



Return true if the attribute associated with this query has an
authored default value, authored time samples or a fallback value
provided by a registered schema.



UsdAttribute::HasValue

"""
   result["AttributeQuery"].__init__.im_func.func_doc = """__init__() -> USD_API



Construct an invalid query object.


----------------------------------------------------------------------
__init__(attr) -> USD_API

attr : Attribute


Construct a new query for the attribute C{attr}.


----------------------------------------------------------------------
__init__(prim, attrName) -> USD_API

prim : Prim
attrName : TfToken


Construct a new query for the attribute named C{attrName} under the
prim C{prim}.

"""
   result["AttributeQuery"].GetUnionedTimeSamples.func_doc = """**static** GetUnionedTimeSamples(attrQueries, times) -> USD_API bool

attrQueries : sequence< UsdAttributeQuery >
times : sequence<double>


Populates the given vector, C{times} with the union of all the
authored sample times on all of the given attribute-query objects,
C{attrQueries}.


Behaves identically to UsdAttribute::GetUnionedTimeSamples()

false if one or more attribute-queries in C{attrQueries} are invalid
or if there's an error fetching time-samples for any of the attribute-
query objects.

UsdAttribute::GetUnionedTimeSamples

UsdAttributeQuery::GetUnionedTimeSamplesInInterval

"""
   result["AttributeQuery"].GetBracketingTimeSamples.im_func.func_doc = """GetBracketingTimeSamples(desiredTime, lower, upper, hasTimeSamples) -> USD_API bool

desiredTime : double
lower : double
upper : double
hasTimeSamples : bool


Populate *lower* and *upper* with the next greater and lesser value
relative to the *desiredTime*.



UsdAttribute::GetBracketingTimeSamples

"""
   result["AttributeQuery"].CreateQueries.func_doc = """**static** CreateQueries(prim, attrNames) -> USD_API sequence< UsdAttributeQuery >

prim : Prim
attrNames : TfTokenVector


Construct new queries for the attributes named in C{attrNames} under
the prim C{prim}.


The objects in the returned vector will line up 1-to-1 with
C{attrNames}.

"""
   result["AttributeQuery"].GetTimeSamples.im_func.func_doc = """GetTimeSamples(times) -> USD_API bool

times : sequence<double>


Populates a vector with authored sample times.


Returns false only on error. Behaves identically to
UsdAttribute::GetTimeSamples()

UsdAttributeQuery::GetTimeSamplesInInterval

"""
   result["AttributeQuery"].GetUnionedTimeSamplesInInterval.func_doc = """**static** GetUnionedTimeSamplesInInterval(attrQueries, interval, times) -> USD_API bool

attrQueries : sequence< UsdAttributeQuery >
interval : GfInterval
times : sequence<double>


Populates the given vector, C{times} with the union of all the
authored sample times in the GfInterval, C{interval} on all of the
given attribute-query objects, C{attrQueries}.


Behaves identically to UsdAttribute::GetUnionedTimeSamplesInInterval()

false if one or more attribute-queries in C{attrQueries} are invalid
or if there's an error fetching time-samples for any of the attribute-
query objects.

UsdAttribute::GetUnionedTimeSamplesInInterval

"""
   result["AttributeQuery"].HasAuthoredValueOpinion.im_func.func_doc = """HasAuthoredValueOpinion() -> USD_API bool



Return true if the attribute associated with this query has either an
authored default value or authored time samples.



UsdAttribute::HasAuthoredValueOpinion

"""
   result["AttributeQuery"].ValueMightBeTimeVarying.im_func.func_doc = """ValueMightBeTimeVarying() -> USD_API bool



Return true if it is possible, but not certain, that this attribute's
value changes over time, false otherwise.



UsdAttribute::ValueMightBeTimeVarying

"""
   result["AttributeQuery"].GetNumTimeSamples.im_func.func_doc = """GetNumTimeSamples() -> USD_API size_t



Returns the number of time samples that have been authored.



UsdAttribute::GetNumTimeSamples

"""
   result["AttributeQuery"].GetTimeSamplesInInterval.im_func.func_doc = """GetTimeSamplesInInterval(interval, times) -> USD_API bool

interval : GfInterval
times : sequence<double>


Populates a vector with authored sample times in C{interval}.


Returns false only on an error.

Behaves identically to UsdAttribute::GetTimeSamplesInInterval()

"""
   result["EditContext"].__doc__ = """
A utility class to temporarily modify a stage's current EditTarget
during an execution scope.


This is an "RAII"-like object meant to be used as an automatic local
variable. Upon construction, it sets a given stage's EditTarget, and
upon destruction it restores the stage's EditTarget to what it was
previously.

Example usage, temporarily overriding a stage's EditTarget to direct
an edit to the stage's session layer. When the *ctx* object expires,
it restores the stage's EditTarget to whatever it was previously. ::

  void SetVisState(const UsdPrim  & prim, bool vis) {
      UsdEditContext ctx(prim.GetStage(),
                         prim.GetStage()->GetSessionLayer());
      prim.GetAttribute("visible").Set(vis);
  }

B{Threading Note}

When one thread is mutating a *UsdStage*, it is unsafe for any other
thread to either query or mutate it. Using this class with a stage in
such a way that it modifies the stage's EditTarget constitutes a
mutation.

"""
   result["EditContext"].__init__.im_func.func_doc = """__init__(arg1)

arg1 : EditContext


----------------------------------------------------------------------
__init__(stage) -> USD_API

stage : StagePtr


Construct without modifying *stage's* current EditTarget.


Save *stage's* current EditTarget to restore on destruction.


----------------------------------------------------------------------
__init__(stage, editTarget) -> USD_API

stage : StagePtr
editTarget : EditTarget


Construct and save *stage's* current EditTarget to restore on
destruction, then invoke stage->SetEditTarget(editTarget).


If *editTarget* is invalid, a coding error will be issued by the
*stage*, and its EditTarget will not be modified.


----------------------------------------------------------------------
__init__(stageTarget) -> USD_API

stageTarget : pair<UsdStagePtr, UsdEditTarget >


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This ctor is handy to construct an edit context from the return value
of another function (Cannot return a UsdEditContext since it needs to
be noncopyable).


If *editTarget* is invalid, a coding error will be issued by the
*stage*, and its EditTarget will not be modified.

"""
   result["TimeCode"].__doc__ = """
Represent a time value, which may be either numeric, holding a double
value, or a sentinel value UsdTimeCode::Default() .


A UsdTimeCode does *not* represent an SMPTE timecode, although we may,
in future, support conversion functions between the two. Instead,
UsdTimeCode is an abstraction that acknowledges that in the principal
domains of use for USD, there are many different ways of encoding
time, and USD must be able to capture and translate between all of
them for interchange, retaining as much intent of the authoring
application as possible.

A UsdTimeCode is therefore a unitless, generic time measurement that
serves as the ordinate for time-sampled data in USD files. A client of
USD relies on the UsdStage (which in turn consults metadata authored
in its root layer) to define the mapping of TimeCodes to units like
seconds and frames.

UsdStage::GetStartTimeCode()

UsdStage::GetEndTimeCode()

UsdStage::GetTimeCodesPerSecond()

UsdStage::GetFramesPerSecond() As described in TimeSamples, Defaults,
and Value Resolution, USD optionally provides an unvarying, 'default'
value for every attribute. UsdTimeCode embodies a time value that can
either be a floating-point sample time, or the default.

All UsdAttribute and derived API that requires a time parameter
defaults to UsdTimeCode::Default() if the parameter is left
unspecified, and auto-constructs from a floating-point argument.

UsdTimeCode::EarliestTime() is provided to aid clients who wish to
retrieve the first authored timesample for any attribute.

"""
   result["TimeCode"].Default.func_doc = """**static** Default() -> expr UsdTimeCode



Produce a UsdTimeCode representing the sentinel value for 'default'.



In inequality comparisons, Default() is considered less than any
numeric TimeCode, including EarliestTime() , indicative of the fact
that in UsdAttribute value resolution, the sample at Default() (if
any) is always weaker than any numeric timeSample in the same layer.
For more information, see TimeSamples, Defaults, and Value Resolution

"""
   result["TimeCode"].GetValue.im_func.func_doc = """GetValue() -> double



Return the numeric value for this time.


If this time *IsDefault()*, return a quiet NaN value.

"""
   result["TimeCode"].SafeStep.func_doc = """**static** SafeStep(maxValue, maxCompression) -> expr double

maxValue : double
maxCompression : double


Produce a safe step value such that for any numeric UsdTimeCode t in
[-maxValue, maxValue], t +/- (step / maxCompression) != t with a
safety factor of 2.


This is shorthand for std::numeric_limits<double>::epsilon() *
maxValue * maxCompression * 2.0. Such a step value is recommended for
simulating jump discontinuities in time samples. For example, author
value x at time t, and value y at time t + SafeStep() . This ensures
that as the sample times are shifted and scaled, t and t + SafeStep()
remain distinct so long as they adhere to the C{maxValue} and
C{maxCompression} limits.

"""
   result["TimeCode"].IsNumeric.im_func.func_doc = """IsNumeric() -> bool



Return true if this time represents a numeric value, false otherwise.


This is equivalent to !IsDefault().

"""
   result["TimeCode"].__init__.im_func.func_doc = """__init__(t) -> expr

t : double


Construct with optional time value. Impilicitly convert from double.

"""
   result["TimeCode"].EarliestTime.func_doc = """**static** EarliestTime() -> expr UsdTimeCode



Produce a UsdTimeCode representing the lowest/earliest possible
timeCode.


Thus, for any given timeSample *s*, its time ordinate *t* will obey:
t>= UsdTimeCode::EarliestTime()

This is useful for clients that wish to retrieve the first authored
timeSample for an attribute, as they can use
UsdTimeCode::EarliestTime() as the *time* argument to
UsdAttribute::Get() and UsdAttribute::GetBracketingTimeSamples()

"""
   result["TimeCode"].IsDefault.im_func.func_doc = """IsDefault() -> bool



Return true if this time represents the 'default' sentinel value,
false otherwise.


This is equivalent to !IsNumeric().

"""
   result["Prim"].__doc__ = """
UsdPrim is the sole persistent scenegraph object on a UsdStage, and is
the embodiment of a "Prim" as described in the *Universal Scene
Description Composition Compendium*


A UsdPrim is the principal container of other types of scene
description. It provides API for accessing and creating all of the
contained kinds of scene description, which include:
   - UsdVariantSets - all VariantSets on the prim ( GetVariantSets() ,
     GetVariantSet() )

   - UsdReferences - all references on the prim ( GetReferences() )

   - UsdInherits - all inherits on the prim ( GetInherits() )

   - UsdSpecializes - all specializes on the prim ( GetSpecializes() )
     As well as access to the API objects for properties contained within
     the prim - UsdPrim as well as all of the following classes are
     subclasses of UsdObject :
   - UsdProperty - generic access to all attributes and relationships.
     A UsdProperty can be queried and cast to a UsdAttribute or
     UsdRelationship using UsdObject::Is<>() and UsdObject::As<>() . (
     GetPropertyNames() , GetProperties() , GetPropertiesInNamespace() ,
     GetPropertyOrder() , SetPropertyOrder() )

   - UsdAttribute - access to default and timesampled attribute
     values, as well as value resolution information, and attribute-
     specific metadata ( CreateAttribute() , GetAttribute() ,
     GetAttributes() , HasAttribute() )

   - UsdRelationship - access to authoring and resolving relationships
     to other prims and properties ( CreateRelationship() ,
     GetRelationship() , GetRelationships() , HasRelationship() )
     UsdPrim also provides access to iteration through its prim children,
     optionally making use of the prim predicates facility ( GetChildren()
     , GetAllChildren() , GetFilteredChildren() ).

Management
==========

Clients acquire UsdPrim objects, which act like weak/guarded pointers
to persistent objects owned and managed by their originating UsdStage.
We provide the following guarantees for a UsdPrim acquired via
UsdStage::GetPrimAtPath() or UsdStage::OverridePrim() or
UsdStage::DefinePrim() :
   - As long as no further mutations to the structure of the UsdStage
     are made, the UsdPrim will still be valid. Loading and Unloading are
     considered structural mutations.

   - When the UsdStage 's structure *is* mutated, the thread
     performing the mutation will receive a UsdNotice::ObjectsChanged
     notice after the stage has been reconfigured, which provides details
     as to what prims may have been created or destroyed, and what prims
     may simply have changed in some structural way.
     Prim access in "reader" threads should be limited to GetPrimAtPath(),
     which will never cause a mutation to the Stage or its layers.

Please refer to UsdNotice for a listing of the events that could cause
UsdNotice::ObjectsChanged to be emitted.

"""
   result["Prim"].HasDefiningSpecifier.im_func.func_doc = """HasDefiningSpecifier() -> bool



Return true if this prim has a specifier of type SdfSpecifierDef or
SdfSpecifierClass.



SdfIsDefiningSpecifier

"""
   result["Prim"].SetSpecifier.im_func.func_doc = """SetSpecifier(specifier) -> bool

specifier : SdfSpecifier


Author an opinion for this Prim's specifier at the current edit
target.

"""
   result["Prim"].GetAuthoredPropertyNames.im_func.func_doc = """GetAuthoredPropertyNames(predicate) -> USD_API TfTokenVector

predicate : PropertyPredicateFunc


Return this prim's property names (attributes and relationships) that
have authored scene description, ordered according to the strongest
propertyOrder statement in scene description if one exists, otherwise
ordered according to TfDictionaryLessThan.


If a valid C{predicate} is passed in, then only the authored
properties whose names pass the predicate are included in the result.
This is useful if the client is interested only in a subset of
authored properties on the prim. For example, only the ones in a given
namespace or only the ones needed to compute a value.

GetPropertyNames()

UsdProperty::IsAuthored()

"""
   result["Prim"].IsAbstract.im_func.func_doc = """IsAbstract() -> bool



Return true if this prim or any of its ancestors is a class.

"""
   result["Prim"].HasRelationship.im_func.func_doc = """HasRelationship(relName) -> USD_API bool

relName : TfToken


Return true if this prim has a relationship named C{relName}, false
otherwise.

"""
   result["Prim"].GetAllChildren.im_func.func_doc = """GetAllChildren() -> SiblingRange



Return all this prim's children as an iterable range.

"""
   result["Prim"].GetChildren.im_func.func_doc = """GetChildren() -> SiblingRange



Return this prim's active, loaded, defined, non-abstract children as
an iterable range.


Equivalent to: ::

  GetFilteredChildren(UsdPrimDefaultPredicate)

See Prim predicate flags and UsdPrimDefaultPredicate for more
information.

"""
   result["Prim"].HasAuthoredActive.im_func.func_doc = """HasAuthoredActive() -> bool



Return true if this prim has an authored opinion for 'active', false
otherwise.

"""
   result["Prim"].IsModel.im_func.func_doc = """IsModel() -> bool



Return true if this prim is a model based on its kind metadata, false
otherwise.

"""
   result["Prim"].Unload.im_func.func_doc = """Unload() -> USD_API void



Unloads this prim and all its descendants.


See UsdStage::Unload for additional details.

"""
   result["Prim"].GetPrimStack.im_func.func_doc = """GetPrimStack() -> USD_API SdfPrimSpecHandleVector



Return a list of PrimSpecs that provide opinions for this prim (i.e.


the prim's metadata fields, including composition metadata). These
specs are ordered from strongest to weakest opinion.

The results returned by this method are meant for debugging and
diagnostic purposes. It is B{not} advisable to retain a PrimStack for
the purposes of expedited value resolution for prim metadata, since
not all metadata resolves with simple "strongestopinion wins"
semantics.

"""
   result["Prim"].GetRelationships.im_func.func_doc = """GetRelationships() -> USD_API sequence< UsdRelationship >



Like GetProperties() , but exclude all attributes from the result.

"""
   result["Prim"].SetActive.im_func.func_doc = """SetActive(active) -> bool

active : bool


Author 'active' metadata for this prim at the current EditTarget.

"""
   result["Prim"].IsInstanceable.im_func.func_doc = """IsInstanceable() -> bool



Return true if this prim has been marked as instanceable.


Note that this is not the same as IsInstance() . A prim may return
true for IsInstanceable() and false for IsInstance() if this prim is
not active or if it is marked as instanceable but contains no
instanceable data.

"""
   result["Prim"].GetSpecializes.im_func.func_doc = """GetSpecializes() -> USD_API UsdSpecializes



Return a UsdSpecializes object that allows one to add, remove, or
mutate specializes *at the currently set UsdEditTarget*.


There is currently no facility for *listing* the currently authored
specializes on a prim... the problem is somewhat ill-defined, and
requires some thought.

"""
   result["Prim"].GetAppliedSchemas.im_func.func_doc = """GetAppliedSchemas() -> USD_API TfTokenVector



Return a vector containing the names of API schemas which have been
applied to this prim, using the Apply() method on the particular
schema class.

"""
   result["Prim"].GetPropertyOrder.im_func.func_doc = """GetPropertyOrder() -> USD_API TfTokenVector



Return the strongest propertyOrder metadata value authored on this
prim.

"""
   result["Prim"].__init__.im_func.func_doc = """__init__()



Construct an invalid prim.


----------------------------------------------------------------------
__init__(primData, proxyPrimPath)

primData : _PrimDataHandle
proxyPrimPath : SdfPath


----------------------------------------------------------------------
__init__(objType, prim, proxyPrimPath, propName)

objType : ObjType
prim : _PrimDataHandle
proxyPrimPath : SdfPath
propName : TfToken

"""
   result["Prim"].HasAuthoredReferences.im_func.func_doc = """HasAuthoredReferences() -> USD_API bool



Return true if this prim has any authored references.

"""
   result["Prim"].GetPrimInMaster.im_func.func_doc = """GetPrimInMaster() -> Prim



If this prim is an instance proxy, return the UsdPrim for the
corresponding prim in the instance's master.


Otherwise, return an invalid UsdPrim.

"""
   result["Prim"].HasAuthoredInherits.im_func.func_doc = """HasAuthoredInherits() -> USD_API bool



Return true if this prim has any authored inherits.

"""
   result["Prim"].HasVariantSets.im_func.func_doc = """HasVariantSets() -> USD_API bool



Return true if this prim has any authored VariantSets.



this connotes only the *existence* of one of more VariantSets, *not*
that such VariantSets necessarily contain any variants or variant
opinions.

"""
   result["Prim"].GetVariantSet.im_func.func_doc = """GetVariantSet(variantSetName) -> USD_API UsdVariantSet

variantSetName : string


Retrieve a specifically named VariantSet for editing or constructing a
UsdEditTarget.


This is a shortcut for ::

  prim.GetVariantSets().GetVariantSet(variantSetName)


"""
   result["Prim"].IsInMaster.im_func.func_doc = """IsInMaster() -> bool



Return true if this prim is located in a subtree of prims rooted at a
master prim, false otherwise.


If this function returns true, this prim is either a master prim or a
descendent of a master prim.

"""
   result["Prim"].IsActive.im_func.func_doc = """IsActive() -> bool



Return true if this prim is active, meaning neither it nor any of its
ancestors have active=false.


Return false otherwise.

"""
   result["Prim"].IsMaster.im_func.func_doc = """IsMaster() -> bool



Return true if this prim is a master prim, false otherwise.

"""
   result["Prim"].GetParent.im_func.func_doc = """GetParent() -> Prim



Return this prim's parent prim.


Return an invalid UsdPrim if this is a root prim.

"""
   result["Prim"].GetNextSibling.im_func.func_doc = """GetNextSibling() -> USD_API UsdPrim



Return this prim's next active, loaded, defined, non-abstract sibling
if it has one, otherwise return an invalid UsdPrim.


Equivalent to: ::

  GetFilteredNextSibling(UsdPrimDefaultPredicate)

See Prim predicate flags and UsdPrimDefaultPredicate for more
information.

"""
   result["Prim"].ComputeExpandedPrimIndex.im_func.func_doc = """ComputeExpandedPrimIndex() -> USD_API PcpPrimIndex



Compute the prim index containing all sites that could contribute
opinions to this prim.


This function is similar to UsdPrim::GetPrimIndex. However, the
returned prim index includes all sites that could possibly contribute
opinions to this prim, not just the sites that currently do so. This
is useful in certain situations; for example, this could be used to
generate a list of sites where clients could make edits to affect this
prim, or for debugging purposes.

This function may be relatively slow, since it will recompute the prim
index on every call. Clients should prefer UsdPrim::GetPrimIndex
unless the additional site information is truly needed.

"""
   result["Prim"].GetProperties.im_func.func_doc = """GetProperties(predicate) -> USD_API sequence< UsdProperty >

predicate : PropertyPredicateFunc


Return all of this prim's properties (attributes and relationships),
including all builtin properties, ordered by name according to the
strongest propertyOrder statement in scene description if one exists,
otherwise ordered according to TfDictionaryLessThan.


If a valid C{predicate} is passed in, then only properties whose names
pass the predicate are included in the result. This is useful if the
client is interested only in a subset of properties on the prim. For
example, only the ones in a given namespace or only the ones needed to
compute a value.

To obtain only either attributes or relationships, use either
GetAttributes() or GetRelationships() .

To determine whether a property is either an attribute or a
relationship, use the UsdObject::As() and UsdObject::Is() methods in
C++: ::

  // Use As<>() to obtain a subclass instance.
  if (UsdAttribute attr = property.As<UsdAttribute>()) {
      // use attribute 'attr'.
  else if (UsdRelationship rel = property.As<UsdRelationship>()) {
      // use relationship 'rel'.
  }
  
  // Use Is<>() to discriminate only.
  if (property.Is<UsdAttribute>()) {
      // property is an attribute.
  }

In Python, use the standard isinstance() function: ::

  if isinstance(property, Usd.Attribute):
      # property is a Usd.Attribute.
  elif isinstance(property, Usd.Relationship):
      # property is a Usd.Relationship.

GetAuthoredProperties()

UsdProperty::IsAuthored()

"""
   result["Prim"].FindAllRelationshipTargetPaths.im_func.func_doc = """FindAllRelationshipTargetPaths(pred, recurseOnTargets) -> USD_API SdfPathVector

pred : function<bool( UsdRelationship )>
recurseOnTargets : bool


Search the prim subtree rooted at this prim for relationships for
which C{predicate} returns true, collect their target paths and return
them in an arbitrary order.


If C{recurseOnTargets} is true, act as if this function was invoked on
the targeted prims and owning prims of targeted properties also (but
not of forwarding relationships) and return the union.

"""
   result["Prim"].GetPrimIndex.im_func.func_doc = """GetPrimIndex() -> PcpPrimIndex



Return the cached prim index containing all sites that contribute
opinions to this prim.


The prim index can be used to examine the composition arcs and scene
description sites that contribute to this prim's property and metadata
values.

The prim index returned by this function is optimized and may not
include sites that do not contribute opinions to this prim. Use
UsdPrim::ComputeExpandedPrimIndex to compute a prim index that
includes all possible sites that could contribute opinions.

This prim index will be empty for master prims. This ensures that
these prims do not provide any attribute or metadata values. For all
other prims in masters, this is the prim index that was chosen to be
shared with all other instances. In either case, the prim index's path
will not be the same as the prim's path.

Prim indexes may be invalidated by changes to the UsdStage and cannot
detect if they are expired. Clients should avoid keeping copies of the
prim index across such changes, which include scene description
changes or changes to load state.

"""
   result["Prim"].HasAPI.im_func.func_doc = """HasAPI(instanceName) -> bool

instanceName : TfToken


Return true if the UsdPrim has had an API schema represented by the
C++ class type B{T} applied to it through the Apply() method provided
on the API schema class.


C{instanceName}, if non-empty is used to determine if a particular
instance of a multiple-apply API schema (eg. UsdCollectionAPI) has
been applied to the prim. A coding error is issued if a non-empty
C{instanceName} is passed in and B{T} represents a single-apply API
schema.

B{Using HasAPI in C++} ::

  UsdPrim prim = stage->OverridePrim("/path/to/prim");
  UsdModelAPI modelAPI = UsdModelAPI::Apply(prim);
  assert(prim.HasAPI<UsdModelAPI>());
  
  UsdCollectionAPI collAPI = UsdCollectionAPI::Apply(prim, 
          /*instanceName*/ TfToken("geom"))
  assert(prim.HasAPI<UsdCollectionAPI>()
  assert(prim.HasAPI<UsdCollectionAPI>(/*instanceName*/ TfToken("geom")))

The python version of this method takes as an argument the TfType of
the API schema class. Similar validation of the schema type is
performed in python at run-time and a coding error is issued if the
given type is not a valid applied API schema.

B{Using HasAPI in Python} ::

  prim = stage.OverridePrim("/path/to/prim")
  modelAPI = Usd.ModelAPI.Apply(prim)
  assert prim.HasAPI(Usd.ModelAPI)
  
  collAPI = Usd.CollectionAPI.Apply(prim, "geom")
  assert(prim.HasAPI(Usd.CollectionAPI))
  assert(prim.HasAPI(Usd.CollectionAPI, instanceName="geom"))


"""
   result["Prim"].IsLoaded.im_func.func_doc = """IsLoaded() -> bool



Return true if this prim is active, and *either* it is loadable and it
is loaded, *or* its nearest loadable ancestor is loaded, *or* it has
no loadable ancestor; false otherwise.

"""
   result["Prim"].IsInstanceProxy.im_func.func_doc = """IsInstanceProxy() -> bool



Return true if this prim is an instance proxy, false otherwise.


An instance proxy prim represents a descendent of an instance prim.

"""
   result["Prim"].IsPseudoRoot.im_func.func_doc = """IsPseudoRoot() -> USD_API bool



Returns true if the prim is the pseudo root.


Equivalent to ::

  prim.GetPath() == SdfPath::AbsoluteRootPath()


"""
   result["Prim"].HasAuthoredInstanceable.im_func.func_doc = """HasAuthoredInstanceable() -> bool



Return true if this prim has an authored opinion for 'instanceable',
false otherwise.

"""
   result["Prim"].GetSpecifier.im_func.func_doc = """GetSpecifier() -> SdfSpecifier



Return this prim's composed specifier.

"""
   result["Prim"].HasPayload.im_func.func_doc = """HasPayload() -> USD_API bool



Return true if a payload is present on this prim.



Payloads: Impact of Using and Not Using

"""
   result["Prim"].GetPropertiesInNamespace.im_func.func_doc = """GetPropertiesInNamespace(namespaces) -> USD_API sequence< UsdProperty >

namespaces : sequence<string>


Return this prim's properties that are inside the given property
namespace ordered according to the strongest propertyOrder statement
in scene description if one exists, otherwise ordered according to
TfDictionaryLessThan.


A C{namespaces} argument whose elements are ["ri", "attribute"] will
return all the properties under the namespace "ri:attribute", i.e.
"ri:attribute:*". An empty C{namespaces} argument is equivalent to
GetProperties() .

For details of namespaced properties, see Names, Namespace Ordering,
and Property Namespaces


----------------------------------------------------------------------
GetPropertiesInNamespace(namespaces) -> USD_API sequence< UsdProperty >

namespaces : string


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
C{namespaces} must be an already-concatenated ordered set of
namespaces, and may or may not terminate with the namespace-separator
character.


If C{namespaces} is empty, this method is equivalent to
GetProperties() .

"""
   result["Prim"].GetAuthoredRelationships.im_func.func_doc = """GetAuthoredRelationships() -> USD_API sequence< UsdRelationship >



Like GetRelationships() , but exclude relationships without authored
scene description from the result.


See UsdProperty::IsAuthored() .

"""
   result["Prim"].HasAuthoredTypeName.im_func.func_doc = """HasAuthoredTypeName() -> bool



Return true if a typeName has been authored.

"""
   result["Prim"].GetRelationship.im_func.func_doc = """GetRelationship(relName) -> USD_API UsdRelationship

relName : TfToken


Return a UsdRelationship with the name *relName*.


The relationship returned may or may not B{actually} exist so it must
be checked for validity. Suggested use: ::

  if (UsdRelationship myRel = prim.GetRelationship("myRel")) {
     // myRel is safe to use.
     // Edits to the owning stage requires subsequent validation.
  } else {
     // myRel was not defined/authored
  }


"""
   result["Prim"].GetAuthoredAttributes.im_func.func_doc = """GetAuthoredAttributes() -> USD_API sequence< UsdAttribute >



Like GetAttributes() , but exclude attributes without authored scene
description from the result.


See UsdProperty::IsAuthored() .

"""
   result["Prim"].GetVariantSets.im_func.func_doc = """GetVariantSets() -> USD_API UsdVariantSets



Return a UsdVariantSets object representing all the VariantSets
present on this prim.


The returned object also provides the API for adding new VariantSets
to the prim.

"""
   result["Prim"].GetPrimDefinition.im_func.func_doc = """GetPrimDefinition() -> USD_API SdfPrimSpecHandle



Return this prim's definition from the UsdSchemaRegistry based on the
prim's type if one exists, otherwise return null.

"""
   result["Prim"].SetPayload.im_func.func_doc = """SetPayload(payload) -> USD_API bool

payload : SdfPayload


Author payload metadata for this prim at the current edit target.


Return true on success, false if the value could not be set.

Payloads: Impact of Using and Not Using


----------------------------------------------------------------------
SetPayload(assetPath, primPath) -> USD_API bool

assetPath : string
primPath : SdfPath


Shorthand for SetPayload(SdfPayload(assetPath, primPath)).


----------------------------------------------------------------------
SetPayload(layer, primPath) -> USD_API bool

layer : SdfLayerHandle
primPath : SdfPath


Shorthand for SetPayload( SdfPayload (layer->GetIdentifier(),
primPath)).

"""
   result["Prim"].SetTypeName.im_func.func_doc = """SetTypeName(typeName) -> bool

typeName : TfToken


Author this Prim's typeName at the current EditTarget.

"""
   result["Prim"].GetMaster.im_func.func_doc = """GetMaster() -> USD_API UsdPrim



If this prim is an instance, return the UsdPrim for the corresponding
master.


Otherwise, return an invalid UsdPrim.

"""
   result["Prim"].FindAllAttributeConnectionPaths.im_func.func_doc = """FindAllAttributeConnectionPaths(pred, recurseOnSources) -> USD_API SdfPathVector

pred : function<bool( UsdAttribute )>
recurseOnSources : bool


Search the prim subtree rooted at this prim for attributes for which
C{predicate} returns true, collect their connection source paths and
return them in an arbitrary order.


If C{recurseOnSources} is true, act as if this function was invoked on
the connected prims and owning prims of connected properties also and
return the union.

"""
   result["Prim"].IsInstance.im_func.func_doc = """IsInstance() -> bool



Return true if this prim is an instance of a master, false otherwise.


If this prim is an instance, calling GetMaster() will return the
UsdPrim for the corresponding master prim.

"""
   result["Prim"].GetTypeName.im_func.func_doc = """GetTypeName() -> TfToken



Return this prim's composed type name.


Note that this value is cached and is efficient to query.

"""
   result["Prim"].SetInstanceable.im_func.func_doc = """SetInstanceable(instanceable) -> bool

instanceable : bool


Author 'instanceable' metadata for this prim at the current
EditTarget.

"""
   result["Prim"].IsGroup.im_func.func_doc = """IsGroup() -> bool



Return true if this prim is a model group based on its kind metadata,
false otherwise.


If this prim is a group, it is also necessarily a model.

"""
   result["Prim"].ClearActive.im_func.func_doc = """ClearActive() -> bool



Remove the authored 'active' opinion at the current EditTarget.


Do nothing if there is no authored opinion.

"""
   result["Prim"].HasProperty.im_func.func_doc = """HasProperty(propName) -> USD_API bool

propName : TfToken


Return true if this prim has an property named C{propName}, false
otherwise.

"""
   result["Prim"].GetPropertyNames.im_func.func_doc = """GetPropertyNames(predicate) -> USD_API TfTokenVector

predicate : PropertyPredicateFunc


Return all of this prim's property names (attributes and
relationships), including all builtin properties.


If a valid C{predicate} is passed in, then only properties whose names
pass the predicate are included in the result. This is useful if the
client is interested only in a subset of properties on the prim. For
example, only the ones in a given namespace or only the ones needed to
compute a value.

GetAuthoredPropertyNames()

UsdProperty::IsAuthored()

"""
   result["Prim"].ClearTypeName.im_func.func_doc = """ClearTypeName() -> bool



Clear the opinion for this Prim's typeName at the current edit target.

"""
   result["Prim"].Load.im_func.func_doc = """Load(policy) -> USD_API void

policy : LoadPolicy


Load this prim, all its ancestors, and by default all its descendants.


If C{loadPolicy} is UsdLoadWithoutDescendants, then load only this
prim and its ancestors.

See UsdStage::Load for additional details.

"""
   result["Prim"].ClearInstanceable.im_func.func_doc = """ClearInstanceable() -> bool



Remove the authored 'instanceable' opinion at the current EditTarget.


Do nothing if there is no authored opinion.

"""
   result["Prim"].GetAttributes.im_func.func_doc = """GetAttributes() -> USD_API sequence< UsdAttribute >



Like GetProperties() , but exclude all relationships from the result.

"""
   result["Prim"].GetReferences.im_func.func_doc = """GetReferences() -> USD_API UsdReferences



Return a UsdReferences object that allows one to add, remove, or
mutate references *at the currently set UsdEditTarget*.


There is currently no facility for *listing* the currently authored
references on a prim... the problem is somewhat ill-defined, and
requires some thought.

"""
   result["Prim"]._GetSourcePrimIndex.im_func.func_doc = """_GetSourcePrimIndex() -> PcpPrimIndex


"""
   result["Prim"].CreateRelationship.im_func.func_doc = """CreateRelationship(relName, custom) -> USD_API UsdRelationship

relName : TfToken
custom : bool


Author scene description for the relationship named *relName* at the
current EditTarget if none already exists.


Return a valid relationship if scene description was successfully
authored or if it already existed, return an invalid relationship
otherwise.

Suggested use: ::

  if (UsdRelationship myRel = prim.CreateRelationship(...)) {
     // success. 
  }

To call this, GetPrim() must return a valid prim.

   - If a spec for this relationship already exists at the current
     edit target, do nothing.

   - If a spec for *relName* of a different spec type (e.g. an
     attribute) exists at the current EditTarget, issue an error.

   - If *name* refers to a builtin relationship according to the
     prim's definition, author a relationship spec with required metadata
     from the definition.

   - If *name* refers to a builtin attribute, issue an error.

   - If there exists an absolute strongest authored relationship spec
     for *relName*, author a relationship spec at the current EditTarget by
     copying required metadata from that strongest spec.

   - If there exists an absolute strongest authored attribute spec for
     *relName*, issue an error.

   - Otherwise author a uniform relationship spec at the current
     EditTarget, honoring C{custom}.



----------------------------------------------------------------------
CreateRelationship(nameElts, custom) -> USD_API UsdRelationship

nameElts : sequence<string>
custom : bool


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This overload of CreateRelationship() accepts a vector of name
components used to construct a *namespaced* property name.


For details, see Names, Namespace Ordering, and Property Namespaces

"""
   result["Prim"].GetProperty.im_func.func_doc = """GetProperty(propName) -> USD_API UsdProperty

propName : TfToken


Return a UsdProperty with the name *propName*.


The property returned may or may not B{actually} exist so it must be
checked for validity. Suggested use: ::

  if (UsdProperty myProp = prim.GetProperty("myProp")) {
     // myProp is safe to use. 
     // Edits to the owning stage requires subsequent validation.
  } else {
     // myProp was not defined/authored
  }


"""
   result["Prim"].IsDefined.im_func.func_doc = """IsDefined() -> bool



Return true if this prim and all its ancestors have defining
specifiers, false otherwise.



SdfIsDefiningSpecifier.

"""
   result["Prim"].GetFilteredNextSibling.im_func.func_doc = """GetFilteredNextSibling(predicate) -> USD_API UsdPrim

predicate : _PrimFlagsPredicate


Return this prim's next sibling that matches C{predicate} if it has
one, otherwise return the invalid UsdPrim.


See Prim predicate flags and UsdPrimDefaultPredicate for more
information.

"""
   result["Prim"].GetAuthoredProperties.im_func.func_doc = """GetAuthoredProperties(predicate) -> USD_API sequence< UsdProperty >

predicate : PropertyPredicateFunc


Return this prim's properties (attributes and relationships) that have
authored scene description, ordered by name according to the strongest
propertyOrder statement in scene description if one exists, otherwise
ordered according to TfDictionaryLessThan.


If a valid C{predicate} is passed in, then only authored properties
whose names pass the predicate are included in the result. This is
useful if the client is interested only in a subset of authored
properties on the prim. For example, only the ones in a given
namespace or only the ones needed to compute a value.

GetProperties()

UsdProperty::IsAuthored()

"""
   result["Prim"].CreateAttribute.im_func.func_doc = """CreateAttribute(name, typeName, custom, variability) -> USD_API UsdAttribute

name : TfToken
typeName : SdfValueTypeName
custom : bool
variability : SdfVariability


Author scene description for the attribute named *attrName* at the
current EditTarget if none already exists.


Return a valid attribute if scene description was successfully
authored or if it already existed, return invalid attribute otherwise.
Note that the supplied *typeName* and *custom* arguments are only used
in one specific case. See below for details.

Suggested use: ::

  if (UsdAttribute myAttr = prim.CreateAttribute(...)) {
     // success. 
  }

To call this, GetPrim() must return a valid prim.

   - If a spec for this attribute already exists at the current edit
     target, do nothing.

   - If a spec for *attrName* of a different spec type (e.g. a
     relationship) exists at the current EditTarget, issue an error.

   - If *name* refers to a builtin attribute according to the prim's
     definition, author an attribute spec with required metadata from the
     definition.

   - If *name* refers to a builtin relationship, issue an error.

   - If there exists an absolute strongest authored attribute spec for
     *attrName*, author an attribute spec at the current EditTarget by
     copying required metadata from that strongest spec.

   - If there exists an absolute strongest authored relationship spec
     for *attrName*, issue an error.

   - Otherwise author an attribute spec at the current EditTarget
     using the provided *typeName* and *custom* for the required metadata
     fields. Note that these supplied arguments are only ever used in this
     particular circumstance, in all other cases they are ignored.



----------------------------------------------------------------------
CreateAttribute(name, typeName, variability) -> USD_API UsdAttribute

name : TfToken
typeName : SdfValueTypeName
variability : SdfVariability


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Create a custom attribute with C{name}, C{typeName} and
C{variability}.


----------------------------------------------------------------------
CreateAttribute(nameElts, typeName, custom, variability) -> USD_API UsdAttribute

nameElts : sequence<string>
typeName : SdfValueTypeName
custom : bool
variability : SdfVariability


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This overload of CreateAttribute() accepts a vector of name components
used to construct a *namespaced* property name.


For details, see Names, Namespace Ordering, and Property Namespaces


----------------------------------------------------------------------
CreateAttribute(nameElts, typeName, variability) -> USD_API UsdAttribute

nameElts : sequence<string>
typeName : SdfValueTypeName
variability : SdfVariability


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Create a custom attribute with C{nameElts}, C{typeName}, and
C{variability}.

"""
   result["Prim"].GetAttribute.im_func.func_doc = """GetAttribute(attrName) -> USD_API UsdAttribute

attrName : TfToken


Return a UsdAttribute with the name *attrName*.


The attribute returned may or may not B{actually} exist so it must be
checked for validity. Suggested use: ::

  if (UsdAttribute myAttr = prim.GetAttribute("myAttr")) {
     // myAttr is safe to use. 
     // Edits to the owning stage requires subsequent validation.
  } else {
     // myAttr was not defined/authored
  }


"""
   result["Prim"].GetAuthoredPropertiesInNamespace.im_func.func_doc = """GetAuthoredPropertiesInNamespace(namespaces) -> USD_API sequence< UsdProperty >

namespaces : sequence<string>


Like GetPropertiesInNamespace() , but exclude properties that do not
have authored scene description from the result.


See UsdProperty::IsAuthored() .

For details of namespaced properties, see Names, Namespace Ordering,
and Property Namespaces


----------------------------------------------------------------------
GetAuthoredPropertiesInNamespace(namespaces) -> USD_API sequence< UsdProperty >

namespaces : string


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
C{namespaces} must be an already-concatenated ordered set of
namespaces, and may or may not terminate with the namespace-separator
character.


If C{namespaces} is empty, this method is equivalent to
GetAuthoredProperties() .

"""
   result["Prim"].SetPropertyOrder.im_func.func_doc = """SetPropertyOrder(order) -> USD_API void

order : TfTokenVector


Author an opinion for propertyOrder metadata on this prim at the
current EditTarget.

"""
   result["Prim"].GetChild.im_func.func_doc = """GetChild(name) -> USD_API UsdPrim

name : TfToken


Return this prim's direct child named C{name} if it has one, otherwise
return an invalid UsdPrim.


Equivalent to: ::

  prim.GetStage()->GetPrimAtPath(prim.GetPath().AppendChild(name))


"""
   result["Prim"].ClearPayload.im_func.func_doc = """ClearPayload() -> USD_API bool



Clears the payload at the current EditTarget for this prim.


Return false if the payload could not be cleared.

"""
   result["Prim"].HasAttribute.im_func.func_doc = """HasAttribute(attrName) -> USD_API bool

attrName : TfToken


Return true if this prim has an attribute named C{attrName}, false
otherwise.

"""
   result["Prim"].RemoveProperty.im_func.func_doc = """RemoveProperty(propName) -> USD_API bool

propName : TfToken


Remove all scene description for the property with the given
C{propName} *in the current UsdEditTarget*.


Return true if the property is removed, false otherwise.

"""
   result["Prim"].IsA.im_func.func_doc = """IsA() -> bool



Return true if the UsdPrim is/inherits a Schema of type T.


This will also return true if the UsdPrim is a schema that inherits
from schema C{T}.

"""
   result["Prim"].GetFilteredChildren.im_func.func_doc = """GetFilteredChildren(predicate) -> SiblingRange

predicate : _PrimFlagsPredicate


Return a subset of all of this prim's children filtered by
C{predicate} as an iterable range.


The C{predicate} is generated by combining a series of prim flag terms
with either&&or || and !.

Example usage: ::

  // Get all active model children.
  GetFilteredChildren(UsdPrimIsActive && UsdPrimIsModel);
  
  // Get all model children that pass the default predicate.
  GetFilteredChildren(UsdPrimDefaultPredicate && UsdPrimIsModel);

If this prim is an instance, no children will be returned unless
UsdTraverseInstanceProxies is used to allow instance proxies to be
returned, or if this prim is itself an instance proxy.

See Prim predicate flags and UsdPrimDefaultPredicate for more
information.

"""
   result["Prim"].HasAuthoredSpecializes.im_func.func_doc = """HasAuthoredSpecializes() -> USD_API bool



Returns true if this prim has any authored specializes.

"""
   result["Prim"].GetInherits.im_func.func_doc = """GetInherits() -> USD_API UsdInherits



Return a UsdInherits object that allows one to add, remove, or mutate
inherits *at the currently set UsdEditTarget*.


There is currently no facility for *listing* the currently authored
inherits on a prim... the problem is somewhat ill-defined, and
requires some thought.

"""
   result["ListPosition"].__doc__ = """
Specifies a position to add items to lists.


Used by some Add() methods in the USD API that manipulate lists, such
as AddReference().

"""
   result["ResolveInfoSource"].__doc__ = """
Describes the various sources of attribute values.


For more details, see TimeSamples, Defaults, and Value Resolution.

"""
   result["Typed"].__doc__ = """
The base class for all *typed* schemas (those that can impart a
typeName to a UsdPrim), and therefore the base class for all
instantiable and "IsA" schemas.


UsdTyped implements a typeName-based query for its override of
UsdSchemaBase::_IsCompatible() . It provides no other behavior.

"""
   result["Typed"].__init__.im_func.func_doc = """__init__(prim)

prim : Prim


Construct a UsdTyped on UsdPrim C{prim}.


Equivalent to UsdTyped::Get (prim.GetStage(), prim.GetPath()) for a
*valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : SchemaBase


Construct a UsdTyped on the prim wrapped by C{schemaObj}.


Should be preferred over UsdTyped (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["Typed"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["StageCache"].__doc__ = """
A strongly concurrency safe collection of UsdStageRefPtr s, enabling
sharing across multiple clients and threads.


See UsdStageCacheContext for typical use cases finding UsdStage s in a
cache and publishing UsdStage s to a cache.

UsdStageCache is strongly thread safe: all operations other than
construction and destruction may be performed concurrently.

Clients typically populate and fetch UsdStage s in caches by binding a
UsdStageCacheContext object to a cache, then using the
UsdStage::Open() API. See UsdStageCacheContext for more details.
Clients may also populate and fetch directly via
UsdStageCache::Insert() , UsdStageCache::Find() ,
UsdStageCache::FindOneMatching() , and
UsdStageCache::FindAllMatching() API.

Caches provide a mechanism that associates a lightweight key,
UsdStageCache::Id, with a cached stage. A UsdStageCache::Id can be
converted to and from long int and string. This can be useful for
communicating within a third party application that cannot transmit
arbitrary C++ objects. See UsdStageCache::GetId() .

Clients may iterate all cache elements using
UsdStageCache::GetAllStages() and remove elements with
UsdStageCache::Erase() , UsdStageCache::EraseAll() , and
UsdStageCache::Clear() .

Note that this class is a regular type: it can be copied and assigned
at will. It is not a singleton. Also, since it holds a collection of
UsdStageRefPtr objects, copying it does not create new UsdStage
instances, it merely copies the RefPtrs.

Enabling the USD_STAGE_CACHE TF_DEBUG code will issue debug output for
UsdStageCache Find/Insert/Erase/Clear operations. Also see
UsdStageCache::SetDebugName() and UsdStageCache::GetDebugName() .

"""
   result["StageCache"].Insert.im_func.func_doc = """Insert(stage) -> USD_API Id

stage : StageRefPtr


Insert C{stage} into this cache and return its associated Id.


If the given C{stage} is already present in this cache, simply return
its associated Id.

"""
   result["StageCache"].Contains.im_func.func_doc = """Contains(stage) -> bool

stage : StageRefPtr


Return true if C{stage} is present in this cache, false otherwise.


----------------------------------------------------------------------
Contains(id) -> bool

id : Id


Return true if C{id} is present in this cache, false otherwise.

"""
   result["StageCache"].SetDebugName.im_func.func_doc = """SetDebugName(debugName) -> USD_API void

debugName : string


Assign a debug name to this cache.


This will be emitted in debug output messages when the
USD_STAGE_CACHES debug flag is enabled. If set to the empty string,
the cache's address will be used instead.

"""
   result["StageCache"].EraseAll.im_func.func_doc = """EraseAll(rootLayer) -> USD_API size_t

rootLayer : SdfLayerHandle


Erase all stages present in the cache with C{rootLayer} and return the
number erased.


Since the cache contains UsdStageRefPtr, erasing a stage from the
cache will only destroy the stage if no other UsdStageRefPtrs exist
referring to it.


----------------------------------------------------------------------
EraseAll(rootLayer, sessionLayer) -> USD_API size_t

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle


Erase all stages present in the cache with C{rootLayer} and
C{sessionLayer} and return the number erased.


Since the cache contains UsdStageRefPtr, erasing a stage from the
cache will only destroy the stage if no other UsdStageRefPtrs exist
referring to it.


----------------------------------------------------------------------
EraseAll(rootLayer, sessionLayer, pathResolverContext) -> USD_API size_t

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle
pathResolverContext : ArResolverContext


Erase all stages present in the cache with C{rootLayer},
C{sessionLayer}, and C{pathResolverContext} and return the number
erased.


Since the cache contains UsdStageRefPtr, erasing a stage from the
cache will only destroy the stage if no other UsdStageRefPtrs exist
referring to it.

"""
   result["StageCache"].GetDebugName.im_func.func_doc = """GetDebugName() -> USD_API string



Retrieve this cache's debug name, set with SetDebugName() .


If no debug name has been assigned, return the empty string.

"""
   result["StageCache"].Clear.im_func.func_doc = """Clear() -> USD_API void



Remove all entries from this cache, leaving it empty and equivalent to
a default-constructed cache.


Since the cache contains UsdStageRefPtr, erasing a stage from the
cache will only destroy the stage if no other UsdStageRefPtrs exist
referring to it.

"""
   result["StageCache"].FindAllMatching.im_func.func_doc = """FindAllMatching(rootLayer) -> USD_API sequence<UsdStageRefPtr>

rootLayer : SdfLayerHandle


Find all stages in this cache with C{rootLayer}.


If there is no matching stage in this cache, return an empty vector.


----------------------------------------------------------------------
FindAllMatching(rootLayer, sessionLayer) -> USD_API sequence<UsdStageRefPtr>

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle


Find all stages in this cache with C{rootLayer} and C{sessionLayer}.


If there is no matching stage in this cache, return an empty vector.


----------------------------------------------------------------------
FindAllMatching(rootLayer, pathResolverContext) -> USD_API sequence<UsdStageRefPtr>

rootLayer : SdfLayerHandle
pathResolverContext : ArResolverContext


Find all stages in this cache with C{rootLayer} and
C{pathResolverContext}.


If there is no matching stage in this cache, return an empty vector.


----------------------------------------------------------------------
FindAllMatching(rootLayer, sessionLayer, pathResolverContext) -> USD_API sequence<UsdStageRefPtr>

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle
pathResolverContext : ArResolverContext


Find all stages in this cache with C{rootLayer}, C{sessionLayer}, and
C{pathResolverContext}.


If there is no matching stage in this cache, return an empty vector.
If there is more than one matching stage in this cache, return an
arbitrary matching one.

"""
   result["StageCache"].GetId.im_func.func_doc = """GetId(stage) -> USD_API Id

stage : StageRefPtr


Return the Id associated with C{stage} in this cache.


If C{stage} is not present in this cache, return an invalid Id.

"""
   result["StageCache"].Id.__doc__ = """
A lightweight identifier that may be used to identify a particular
cached stage within a UsdStageCache.


An identifier may be converted to and from long int and string, to
facilitate use within restricted contexts.

Id objects are only valid with the stage from which they were
obtained. It never makes sense to use an Id with a stage other than
the one it was obtained from.

"""
   result["StageCache"].Id.ToLongInt.im_func.func_doc = """ToLongInt() -> long int



Convert this Id to an integral representation.

"""
   result["StageCache"].Id.IsValid.im_func.func_doc = """IsValid() -> bool



Return true if this Id is valid.

"""
   result["StageCache"].Id.ToString.im_func.func_doc = """ToString() -> string



Convert this Id to a string representation.

"""
   result["StageCache"].Id.FromString.func_doc = """**static** FromString(s) -> Id

s : string


Create an Id from a string value.


The supplied C{val} must have been obtained by calling ToString()
previously.

"""
   result["StageCache"].Id.__init__.im_func.func_doc = """__init__()



Default construct an invalid id.


----------------------------------------------------------------------
__init__(val)

val : long int

"""
   result["StageCache"].Id.FromLongInt.func_doc = """**static** FromLongInt(val) -> Id

val : long int


Create an Id from an integral value.


The supplied C{val} must have been obtained by calling ToLongInt()
previously.

"""
   result["StageCache"].FindOneMatching.im_func.func_doc = """FindOneMatching(rootLayer) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle


Find a stage in this cache with C{rootLayer}.


If there is no matching stage in this cache, return null. If there is
more than one matching stage in this cache, return an arbitrary
matching one. See also FindAllMatching() .


----------------------------------------------------------------------
FindOneMatching(rootLayer, sessionLayer) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle


Find a stage in this cache with C{rootLayer} and C{sessionLayer}.


If there is no matching stage in this cache, return null. If there is
more than one matching stage in this cache, return an arbitrary
matching one. See also FindAllMatching() .


----------------------------------------------------------------------
FindOneMatching(rootLayer, pathResolverContext) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
pathResolverContext : ArResolverContext


Find a stage in this cache with C{rootLayer} and
C{pathResolverContext}.


If there is no matching stage in this cache, return null. If there is
more than one matching stage in this cache, return an arbitrary
matching one.

FindAllMatching()


----------------------------------------------------------------------
FindOneMatching(rootLayer, sessionLayer, pathResolverContext) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle
pathResolverContext : ArResolverContext


Find a stage in this cache with C{rootLayer}, C{sessionLayer}, and
C{pathResolverContext}.


If there is no matching stage in this cache, return null. If there is
more than one matching stage in this cache, return an arbitrary
matching one.

FindAllMatching()

"""
   result["StageCache"].IsEmpty.im_func.func_doc = """IsEmpty() -> bool



Return true if this cache holds no stages, false otherwise.

"""
   result["StageCache"].Erase.im_func.func_doc = """Erase(id) -> USD_API bool

id : Id


Erase the stage identified by C{id} from this cache and return true.


If C{id} is invalid or there is no associated stage in this cache, do
nothing and return false. Since the cache contains UsdStageRefPtr,
erasing a stage from the cache will only destroy the stage if no other
UsdStageRefPtrs exist referring to it.


----------------------------------------------------------------------
Erase(stage) -> USD_API bool

stage : StageRefPtr


Erase C{stage} from this cache and return true.


If C{stage} is not present in this cache, do nothing and return false.
Since the cache contains UsdStageRefPtr, erasing a stage from the
cache will only destroy the stage if no other UsdStageRefPtrs exist
referring to it.

"""
   result["StageCache"].swap.im_func.func_doc = """swap(other) -> USD_API void

other : StageCache


Swap the contents of this cache with C{other}.

"""
   result["StageCache"].__init__.im_func.func_doc = """__init__() -> USD_API



Default construct an empty cache.


----------------------------------------------------------------------
__init__(other) -> USD_API

other : StageCache


Construct a new cache as a copy of C{other}.

"""
   result["StageCache"].GetAllStages.im_func.func_doc = """GetAllStages() -> USD_API sequence<UsdStageRefPtr>



Return a vector containing the stages present in this cache.

"""
   result["StageCache"].Find.im_func.func_doc = """Find(id) -> USD_API UsdStageRefPtr

id : Id


Find the stage in this cache corresponding to C{id} in this cache.


If C{id} is not valid (see Id::IsValid() ) or if this cache does not
have a stage corresponding to C{id}, return null.

"""
   result["StageCache"].Size.im_func.func_doc = """Size() -> USD_API size_t



Return the number of stages present in this cache.

"""
   result["ClipsAPI"].__doc__ = """
UsdClipsAPI is an API schema that provides an interface to a prim's
clip metadata.


Clips are a "value resolution" feature that allows one to specify a
sequence of usd files (clips) to be consulted, over time, as a source
of varying overrides for the prims at and beneath this prim in
namespace.

SetClipAssetPaths() establishes the set of clips that can be
consulted. SetClipActive() specifies the ordering of clip application
over time (clips can be repeated), while SetClipTimes() specifies
time-mapping from stage-time to clip-time for the clip active at a
given stage-time, which allows for time-dilation and repetition of
clips. Finally, SetClipPrimPath() determines the path within each clip
that will map to this prim, i.e. the location within the clip at which
we will look for opinions for this prim.

The clip asset paths, times and active metadata can also be specified
through template clip metadata. This can be desirable when your set of
assets is very large, as the template metadata is much more concise.
SetClipTemplateAssetPath() establishes the asset identifier pattern of
the set of clips to be consulted. SetClipTemplateStride() ,
SetClipTemplateEndTime() , and SetClipTemplateStartTime() specify the
range in which USD will search, based on the template. From the set of
resolved asset paths, times and active will be derived internally.

A prim may have multiple "clip sets"  named sets of clips that each
have their own values for the metadata described above. For example, a
prim might have a clip set named "Clips_1" that specifies some group
of clip asset paths, and another clip set named "Clips_2" that uses an
entirely different set of clip asset paths. These clip sets are
composed across composition arcs, so clip sets for a prim may be
defined in multiple sublayers or references, for example. Individual
metadata for a given clip set may be sparsely overridden.

Important facts about clips:
   - Within the layerstack in which clips are established, the
     opinions within the clips will be em weaker than any direct opinions
     in the layerstack, but em stronger than varying opinions coming across
     references and variants.

   - We will never look for metadata or default opinions in clips
     when performing value resolution on the owning stage, since these
     quantities must be time-invariant.  This leads to the common structure
     in which we reference a model asset on a prim, and then author clips
     at the same site: the asset reference will provide the topology and
     unvarying data for the model, while the clips will provide the time-
     sampled animation.
     For further information, see Sequencable, Re-timable Animated "Value
     Clips"

"""
   result["ClipsAPI"].GetClipSets.im_func.func_doc = """GetClipSets(clipSets) -> USD_API bool

clipSets : SdfStringListOp


ListOp that may be used to affect how opinions from clip sets are
applied during value resolution.


By default, clip sets in a layer stack are examined in lexicographical
order by name for attribute values during value resolution. The clip
sets listOp can be used to reorder the clip sets in a layer stack or
remove them entirely from consideration during value resolution
without modifying the clips dictionary.

This is *not* the list of clip sets that are authored on this prim. To
retrieve that information, use GetClips to examine the clips
dictionary directly.

This function returns the clip sets listOp from the current edit
target.

"""
   result["ClipsAPI"].SetClipTemplateStride.im_func.func_doc = """SetClipTemplateStride(clipTemplateStride, clipSet) -> USD_API bool

clipTemplateStride : double
clipSet : string


Set the template stride for the clip set named C{clipSet}.



GetClipTemplateStride()


----------------------------------------------------------------------
SetClipTemplateStride(clipTemplateStride) -> USD_API bool

clipTemplateStride : double


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].SetClipActive.im_func.func_doc = """SetClipActive(activeClips, clipSet) -> USD_API bool

activeClips : VtVec2dArray
clipSet : string


Set the active clip metadata for the clip set named C{clipSet}.



GetClipActive()


----------------------------------------------------------------------
SetClipActive(activeClips) -> USD_API bool

activeClips : VtVec2dArray


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].GetClipTimes.im_func.func_doc = """GetClipTimes(clipTimes, clipSet) -> USD_API bool

clipTimes : VtVec2dArray
clipSet : string


List of pairs (stage time, clip time) indicating the time in the
active clip in the clip set named C{clipSet} that should be consulted
for values at the corresponding stage time.


During value resolution, this list will be sorted by stage time; times
will then be linearly interpolated between consecutive entries. For
instance, for clip times [(0.0, 0.0), (10.0, 20.0)], at stage time 0,
values from the active clip at time 0 will be used, at stage time 5,
values from the active clip at time 10, and at stage time 10, clip
values at time 20.


----------------------------------------------------------------------
GetClipTimes(clipTimes) -> USD_API bool

clipTimes : VtVec2dArray


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].SetClipSets.im_func.func_doc = """SetClipSets(clipSets) -> USD_API bool

clipSets : SdfStringListOp


Set the clip sets list op for this prim.



GetClipSets

"""
   result["ClipsAPI"].GetClipTemplateStartTime.im_func.func_doc = """GetClipTemplateStartTime(clipTemplateStartTime, clipSet) -> USD_API bool

clipTemplateStartTime : double
clipSet : string


A double which indicates the start of the range USD will use to search
for asset paths for the clip set named C{clipSet}.


This value is inclusive in that range.

GetClipTemplateAssetPath.


----------------------------------------------------------------------
GetClipTemplateStartTime(clipTemplateStartTime) -> USD_API bool

clipTemplateStartTime : double


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].SetClipTemplateAssetPath.im_func.func_doc = """SetClipTemplateAssetPath(clipTemplateAssetPath, clipSet) -> USD_API bool

clipTemplateAssetPath : string
clipSet : string


Set the clip template asset path for the clip set named C{clipSet}.



GetClipTemplateAssetPath


----------------------------------------------------------------------
SetClipTemplateAssetPath(clipTemplateAssetPath) -> USD_API bool

clipTemplateAssetPath : string


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].GetClipTemplateEndTime.im_func.func_doc = """GetClipTemplateEndTime(clipTemplateEndTime, clipSet) -> USD_API bool

clipTemplateEndTime : double
clipSet : string


A double which indicates the end of the range USD will use to to
search for asset paths for the clip set named C{clipSet}.


This value is inclusive in that range.

GetClipTemplateAssetPath.


----------------------------------------------------------------------
GetClipTemplateEndTime(clipTemplateEndTime) -> USD_API bool

clipTemplateEndTime : double


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].SetClipTimes.im_func.func_doc = """SetClipTimes(clipTimes, clipSet) -> USD_API bool

clipTimes : VtVec2dArray
clipSet : string


Set the clip times metadata for this prim.



GetClipTimes()


----------------------------------------------------------------------
SetClipTimes(clipTimes) -> USD_API bool

clipTimes : VtVec2dArray


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].GetClipManifestAssetPath.im_func.func_doc = """GetClipManifestAssetPath(manifestAssetPath, clipSet) -> USD_API bool

manifestAssetPath : SdfAssetPath
clipSet : string


Asset path for the clip manifest for the clip set named C{clipSet}.


The clip manifest indicates which attributes have time samples
authored in the clips specified on this prim. During value resolution,
clips will only be examined if the attribute exists and is declared as
varying in the manifest. Note that the clip manifest is only consulted
to check if an attribute exists and what its variability is. Other
values and metadata authored in the manifest will be ignored.

For instance, if this prim's path is</Prim_1>, the clip prim path
is</Prim>, and we want values for the attribute</Prim_1.size>, we will
only look within this prim's clips if the attribute</Prim.size>exists
and is varying in the manifest.


----------------------------------------------------------------------
GetClipManifestAssetPath(manifestAssetPath) -> USD_API bool

manifestAssetPath : SdfAssetPath


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].SetClipAssetPaths.im_func.func_doc = """SetClipAssetPaths(assetPaths, clipSet) -> USD_API bool

assetPaths : VtArray < SdfAssetPath >
clipSet : string


Set the clip asset paths for the clip set named C{clipSet}.



GetClipAssetPaths()


----------------------------------------------------------------------
SetClipAssetPaths(assetPaths) -> USD_API bool

assetPaths : VtArray < SdfAssetPath >


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].Get.func_doc = """**static** Get(stage, path) -> USD_API UsdClipsAPI

stage : StagePtr
path : SdfPath


Return a UsdClipsAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdClipsAPI(stage->GetPrimAtPath(path));


"""
   result["ClipsAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : Prim


Construct a UsdClipsAPI on UsdPrim C{prim}.


Equivalent to UsdClipsAPI::Get (prim.GetStage(), prim.GetPath()) for a
*valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : SchemaBase


Construct a UsdClipsAPI on the prim held by C{schemaObj}.


Should be preferred over UsdClipsAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["ClipsAPI"].GetClipPrimPath.im_func.func_doc = """GetClipPrimPath(primPath, clipSet) -> USD_API bool

primPath : string
clipSet : string


Path to the prim in the clips in the clip set named C{clipSet} from
which time samples will be read.


This prim's path will be substituted with this value to determine the
final path in the clip from which to read data. For instance, if this
prims' path is '/Prim_1', the clip prim path is '/Prim', and we want
to get values for the attribute '/Prim_1.size'. The clip prim path
will be substituted in, yielding '/Prim.size', and each clip will be
examined for values at that path.


----------------------------------------------------------------------
GetClipPrimPath(primPath) -> USD_API bool

primPath : string


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].GetClipActive.im_func.func_doc = """GetClipActive(activeClips, clipSet) -> USD_API bool

activeClips : VtVec2dArray
clipSet : string


List of pairs (time, clip index) indicating the time on the stage at
which the clip in the clip set named C{clipSet} specified by the clip
index is active.


For instance, a value of [(0.0, 0), (20.0, 1)] indicates that clip 0
is active at time 0 and clip 1 is active at time 20.


----------------------------------------------------------------------
GetClipActive(activeClips) -> USD_API bool

activeClips : VtVec2dArray


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].SetClipTemplateActiveOffset.im_func.func_doc = """SetClipTemplateActiveOffset(clipTemplateActiveOffset, clipSet) -> USD_API bool

clipTemplateActiveOffset : double
clipSet : string


Set the clip template offset for the clip set named C{clipSet}.



GetClipTemplateActiveOffset


----------------------------------------------------------------------
SetClipTemplateActiveOffset(clipTemplateActiveOffset) -> USD_API bool

clipTemplateActiveOffset : double


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].GetClipTemplateStride.im_func.func_doc = """GetClipTemplateStride(clipTemplateStride, clipSet) -> USD_API bool

clipTemplateStride : double
clipSet : string


A double representing the increment value USD will use when searching
for asset paths for the clip set named C{clipSet}.



GetClipTemplateAssetPath.


----------------------------------------------------------------------
GetClipTemplateStride(clipTemplateStride) -> USD_API bool

clipTemplateStride : double


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USD_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["ClipsAPI"].SetClipPrimPath.im_func.func_doc = """SetClipPrimPath(primPath, clipSet) -> USD_API bool

primPath : string
clipSet : string


Set the clip prim path for the clip set named C{clipSet}.



GetClipPrimPath()


----------------------------------------------------------------------
SetClipPrimPath(primPath) -> USD_API bool

primPath : string


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].GetClipAssetPaths.im_func.func_doc = """GetClipAssetPaths(assetPaths, clipSet) -> USD_API bool

assetPaths : VtArray < SdfAssetPath >
clipSet : string


List of asset paths to the clips in the clip set named C{clipSet}.


This list is unordered, but elements in this list are referred to by
index in other clip-related fields.


----------------------------------------------------------------------
GetClipAssetPaths(assetPaths) -> USD_API bool

assetPaths : VtArray < SdfAssetPath >


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].GetClipTemplateActiveOffset.im_func.func_doc = """GetClipTemplateActiveOffset(clipTemplateActiveOffset, clipSet) -> USD_API bool

clipTemplateActiveOffset : double
clipSet : string


A double representing the offset value used by USD when determining
the active period for each clip.


----------------------------------------------------------------------
GetClipTemplateActiveOffset(clipTemplateActiveOffset) -> USD_API bool

clipTemplateActiveOffset : double


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].GetClipTemplateAssetPath.im_func.func_doc = """GetClipTemplateAssetPath(clipTemplateAssetPath, clipSet) -> USD_API bool

clipTemplateAssetPath : string
clipSet : string


A template string representing a set of assets to be used as clips for
the clip set named C{clipSet}.


This string can be of two forms:

integer frames: path/basename.###.usd

subinteger frames: path/basename.##.##.usd.

For the integer portion of the specification, USD will take a
particular time, determined by the template start time, stride, and
end time, and pad it with zeros up to the number of hashes provided so
long as the number of hashes is greater than the digits required to
specify the integer value.

For instance:

time = 12, template asset path = foo.##.usd =>foo.12.usd time = 12,
template asset path = foo.###.usd =>foo.012.usd time = 333, template
asset path = foo.#.usd =>foo.333.usd

In the case of subinteger portion of a specifications, USD requires
the specification to be exact.

For instance:

time = 1.15, template asset path = foo.#.###.usd =>foo.1.150.usd time
= 1.145, template asset path = foo.#.##.usd =>foo.1.15.usd time = 1.1,
template asset path = foo.#.##.usd =>foo.1.10.usd

Note that USD requires that hash groups be adjacent in the string, and
that there only be one or two such groups.


----------------------------------------------------------------------
GetClipTemplateAssetPath(clipTemplateAssetPath) -> USD_API bool

clipTemplateAssetPath : string


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].SetClipManifestAssetPath.im_func.func_doc = """SetClipManifestAssetPath(manifestAssetPath, clipSet) -> USD_API bool

manifestAssetPath : SdfAssetPath
clipSet : string


Set the clip manifest asset path for this prim.



GetClipManifestAssetPath()


----------------------------------------------------------------------
SetClipManifestAssetPath(manifestAssetPath) -> USD_API bool

manifestAssetPath : SdfAssetPath


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USD_API  TfType


"""
   result["ClipsAPI"].GetClips.im_func.func_doc = """GetClips(clips) -> USD_API bool

clips : VtDictionary


Dictionary that contains the definition of the clip sets on this prim.


Each entry in this dictionary defines a clip set: the entry's key is
the name of the clip set and the entry's value is a dictionary
containing the metadata that specifies the clips in the set.

See UsdClipsAPIInfoKeys for the keys used for each clip set's
dictionary, or use the other API to set or get values for a given clip
set.

"""
   result["ClipsAPI"].SetClipTemplateEndTime.im_func.func_doc = """SetClipTemplateEndTime(clipTemplateEndTime, clipSet) -> USD_API bool

clipTemplateEndTime : double
clipSet : string


Set the template end time for the clipset named C{clipSet}.



GetClipTemplateEndTime()


----------------------------------------------------------------------
SetClipTemplateEndTime(clipTemplateEndTime) -> USD_API bool

clipTemplateEndTime : double


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["ClipsAPI"].SetClips.im_func.func_doc = """SetClips(clips) -> USD_API bool

clips : VtDictionary


Set the clips dictionary for this prim.



GetClips

"""
   result["ClipsAPI"].SetClipTemplateStartTime.im_func.func_doc = """SetClipTemplateStartTime(clipTemplateStartTime, clipSet) -> USD_API bool

clipTemplateStartTime : double
clipSet : string


Set the template start time for the clip set named C{clipSet}.



GetClipTemplateStartTime


----------------------------------------------------------------------
SetClipTemplateStartTime(clipTemplateStartTime) -> USD_API bool

clipTemplateStartTime : double


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
This function operates on the default clip set.



UsdClipsAPISetNames

"""
   result["VariantSet"].__doc__ = """
A UsdVariantSet represents a single VariantSet in USD (e.g.


modelingVariant or shadingVariant), which can have multiple variations
that express different sets of opinions about the scene description
rooted at the prim that defines the VariantSet.

(More detailed description of variants to follow)

"""
   result["VariantSet"].SetVariantSelection.im_func.func_doc = """SetVariantSelection(variantName) -> USD_API bool

variantName : string


Author a variant selection for this VariantSet, setting it to
*variantName* in the stage's current EditTarget.


Return true if the selection was successfully authored, false
otherwise.

"""
   result["VariantSet"].GetVariantNames.im_func.func_doc = """GetVariantNames() -> USD_API sequence<string>



Return the composed variant names for this VariantSet, ordered
lexicographically.

"""
   result["VariantSet"].GetVariantEditContext.im_func.func_doc = """GetVariantEditContext(layer) -> USD_API pair<UsdStagePtr, UsdEditTarget >

layer : SdfLayerHandle


Helper function for configuring a UsdStage 's EditTarget to author
into the currently selected variant.


Returns configuration for a UsdEditContext

To begin editing into VariantSet *varSet's* currently selected
variant:

In C++, we would use the following pattern: ::

  {
      UsdEditContext ctxt(varSet.GetVariantEditContext());
  
      // All Usd mutation of the UsdStage on which varSet sits will
      // now go "inside" the currently selected variant of varSet
  }

In python, the pattern is: ::

  with varSet.GetVariantEditContext():
      # Now sending mutations to current variant

See GetVariantEditTarget() for discussion of C{layer} parameter

"""
   result["VariantSet"].AddVariant.im_func.func_doc = """AddVariant(variantName, position) -> USD_API bool

variantName : string
position : ListPosition


Author a variant spec for *variantName* in this VariantSet at the
stage's current EditTarget, in the position specified by C{position}.


Return true if the spec was successfully authored, false otherwise.

This will create the VariantSet itself, if necessary, so as long as
UsdPrim "prim" is valid, the following should always work: ::

  UsdVariantSet vs = prim.GetVariantSet("myVariantSet");
  vs.AddVariant("myFirstVariation");
  vs.SetVariantSelection("myFirstVariation");
  {
      UsdEditContext ctx(vs.GetVariantEditContext());
      // Now all of our subsequent edits will go "inside" the 
      // 'myFirstVariation' variant of 'myVariantSet'
  }


"""
   result["VariantSet"].IsValid.im_func.func_doc = """IsValid() -> bool



Is this UsdVariantSet object usable? If not, calling any of its other
methods is likely to crash.

"""
   result["VariantSet"].GetName.im_func.func_doc = """GetName() -> string



Return this VariantSet's name.

"""
   result["VariantSet"].HasAuthoredVariant.im_func.func_doc = """HasAuthoredVariant(variantName) -> USD_API bool

variantName : string


Returns true if this VariantSet already possesses a variant.

"""
   result["VariantSet"].GetVariantSelection.im_func.func_doc = """GetVariantSelection() -> USD_API string



Return the variant selection for this VariantSet.


If there is no selection, return the empty string.

"""
   result["VariantSet"].HasAuthoredVariantSelection.im_func.func_doc = """HasAuthoredVariantSelection(value) -> USD_API bool

value : string


Returns true if there is a selection authored for this VariantSet in
any layer.


If requested, the variant selection (if any) will be returned in
C{value}.

"""
   result["VariantSet"].GetVariantEditTarget.im_func.func_doc = """GetVariantEditTarget(layer) -> USD_API UsdEditTarget

layer : SdfLayerHandle


Return a *UsdEditTarget* that edits the currently selected variant in
this VariantSet in *layer*.


If there is no currently selected variant in this VariantSet, return
an invalid EditTarget.

If *layer* is unspecified, then we will use the layer of our prim's
stage's current UsdEditTarget.

Currently, we require *layer* to be in the stage's local LayerStack
(see UsdStage::HasLocalLayer() ), and will issue an error and return
an invalid EditTarget if *layer* is not. We may relax this restriction
in the future, if need arises, but it introduces several complications
in specification and behavior.

"""
   result["VariantSet"].GetPrim.im_func.func_doc = """GetPrim() -> Prim



Return this VariantSet's held prim.

"""
   result["VariantSet"].ClearVariantSelection.im_func.func_doc = """ClearVariantSelection() -> USD_API bool



Clear any selection for this VariantSet from the current EditTarget.


Return true on success, false otherwise.

"""
   result["StageCacheContextBlockType"].__doc__ = """"""
   result["CrateInfo"].__doc__ = """
A class for introspecting the underlying qualities of .usdc 'crate'
files, for diagnostic purposes.

"""
   result["CrateInfo"].GetSections.im_func.func_doc = """GetSections() -> USD_API sequence< Section >



Return the named file sections, their location and sizes in the file.

"""
   result["CrateInfo"].Open.func_doc = """**static** Open(fileName) -> USD_API UsdCrateInfo

fileName : string


Attempt to open and read C{fileName}.

"""
   result["CrateInfo"].GetSummaryStats.im_func.func_doc = """GetSummaryStats() -> USD_API SummaryStats



Return summary statistics structure for this file.

"""
   result["CrateInfo"].GetSoftwareVersion.im_func.func_doc = """GetSoftwareVersion() -> USD_API TfToken



Return the software version.

"""
   result["CrateInfo"].SummaryStats.__doc__ = """"""
   result["CrateInfo"].GetFileVersion.im_func.func_doc = """GetFileVersion() -> USD_API TfToken



Return the file version.

"""
   result["CrateInfo"].Section.__doc__ = """"""
   result["CrateInfo"].Section.__init__.im_func.func_doc = """__init__()



----------------------------------------------------------------------
__init__(name, start, size)

name : string
start : int64_t
size : int64_t

"""
   result["Specializes"].__doc__ = """
A proxy class for applying listOp edits to the specializes list for a
prim.


All paths passed to the UsdSpecializes API are expected to be in the
namespace of the owning prim's stage. Local specializes paths (i.e.,
non-root prim paths) will be translated from this namespace to the
namespace of the current edit target, if necessary. If a path cannot
be translated, a coding error will be issued and no changes will be
made. Global specializes paths (i.e., root prim paths) will not be
translated.

"""
   result["Specializes"].ClearSpecializes.im_func.func_doc = """ClearSpecializes() -> USD_API bool



Removes the authored specializes listOp edits at the current edit
target.

"""
   result["Specializes"].SetSpecializes.im_func.func_doc = """SetSpecializes(items) -> USD_API bool

items : SdfPathVector


Explicitly set specializes paths, potentially blocking weaker opinions
that add or remove items, returning true on success, false if the edit
could not be performed.

"""
   result["Specializes"].AddSpecialize.im_func.func_doc = """AddSpecialize(primPath, position) -> USD_API bool

primPath : SdfPath
position : ListPosition


Adds a path to the specializes listOp at the current EditTarget, in
the position specified by C{position}.

"""
   result["Specializes"].RemoveSpecialize.im_func.func_doc = """RemoveSpecialize(primPath) -> USD_API bool

primPath : SdfPath


Removes the specified path from the specializes listOp at the current
EditTarget.

"""
   result["Specializes"].GetPrim.im_func.func_doc = """GetPrim() -> Prim



Return the prim this object is bound to.


----------------------------------------------------------------------
GetPrim() -> Prim


"""
   result["UsesInverseLayerOffset"].func_doc = """UsesInverseLayerOffset() -> USD_API bool



Returns true if USD uses the historical behavior of applying the
inverse of composed layer offsets to map layer time to stage time.


Respects the env setting USD_USE_INVERSE_LAYER_OFFSET.

"""
   result["_PrimFlagsPredicate"].__doc__ = """"""
   result["_PrimFlagsPredicate"].Tautology.func_doc = """**static** Tautology() -> _PrimFlagsPredicate


"""
   result["_PrimFlagsPredicate"].Contradiction.func_doc = """**static** Contradiction() -> _PrimFlagsPredicate


"""
   result["LoadPolicy"].__doc__ = """
Controls UsdStage::Load() and UsdPrim::Load() behavior regarding
whether or not descendant prims are loaded.

"""
   result["Describe"].func_doc = """Describe(arg1) -> USD_API string

arg1 : Object


Return a human-readable description.


----------------------------------------------------------------------
Describe(arg1) -> USD_API string

arg1 : StageRefPtr


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
Describe(arg1) -> USD_API string

arg1 : StageWeakPtr


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
Describe(arg1) -> USD_API string

arg1 : Stage


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
Describe(arg1) -> USD_API string

arg1 : Stage


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
Describe(arg1) -> USD_API string

arg1 : StageCache


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Attribute"].__doc__ = """
Scenegraph object for authoring and retrieving numeric, string, and
array valued data, sampled over time.


The allowed value types for UsdAttribute are dictated by the Sdf
("Scene Description Foundations") core's data model, which we
summarize in Basic Datatypes for Scene Description Provided by Sdf.

Attribute Defining Qualities
============================

In addition to its value type, an Attribute has two other defining
qualities:
   - B{Variability} Expresses whether an attribute is intended to have
     time samples ( GetVariability() == SdfVariabilityVarying), or only a
     default ( GetVariability() == SdfVariabilityUniform). For more on
     reasoning about time samples, see Value & Time-Sample Accessors.

   - B{Custom} Determines whether an attribute belongs to a schema (
     IsCustom() == C{false}), or is a user-defined, custom attribute.
     schema attributes will always be defined on a prim of the schema type,
     ans may possess fallback values from the schema, whereas custom
     attributes must always first be authored in order to be defined. Note
     that *custom* is actually an aspect of UsdProperty, as UsdRelationship
     can also be custom or provided by a schema.

Attribute Creation and Existence
================================

One can always create an attribute generically via
UsdPrim::CreateAttribute() , which ensures that an attribute "is
defined" in the current UsdEditTarget. In order to author any metadata
or a default or timesample for an attribute, *it must first be
defined*. It is sufficient that the attribute be defined in any one of
the layers participating in the stage's current composition; for
*builtin* attributes (those belonging to the owning prim's defining
schema, i.e. the most specific subclass of UsdTypedSchema for which
prim.IsA<schema>() will evaluate to true) there need be no authored
scene description, because a definition is provided by the prim's
schema definition.

B{Creating} an attribute does not imply that the attribute has a
value. More broadly, in the following code: ::

  if (UsdAttribute attr = prim.GetAttribute(TfToken("myAttr"))){
     ...
  }

The UsdAttribute passes the bool test, because it is defined; however,
inside the clause, we have no guarantee that attr has a value.

Attribute Value Interpolation
=============================

UsdAttribute supports two interpolation behaviors when retrieving
attribute values at times where no value is explicitly authored. The
desired behavior may be specified via UsdStage::SetInterpolationType.
That behavior will be used for all calls to UsdAttribute::Get.

The supported interpolation types are:

   - B{Held} Attribute values are held constant between authored
     values. An attribute's value will be equal to the nearest preceding
     authored value. If there is no preceding authored value, the value
     will be equal to the nearest subsequent value.

   - B{Linear} Attribute values are linearly interpolated between
     authored values.
     Linear interpolation is only supported for certain data types. See
     USD_LINEAR_INTERPOLATION_TYPES for the list of these types. Types that
     do not support linear interpolation will use held interpolation
     instead.

Linear interpolation is done element-by-element for array, vector, and
matrix data types. If linear interpolation is requested for two array
values with different sizes, held interpolation will be used instead.

Attributes of type SdfAssetPath and UsdAttribute::Get()
=======================================================

If an attribute's value type is SdfAssetPath or SdfAssetPathArray,
Get() performs extra work to compute the resolved asset paths, using
the layer that has the strongest value opinion as the anchor for
"relative" asset paths. Both the unresolved and resolved results are
available through SdfAssetPath::GetAssetPath() and
SdfAssetPath::GetResolvedPath() , respectively.

Clients that call Get() on many asset-path-valued attributes may wish
to employ an ArResolverScopedCache to improve asset path resolution
performance.

"""
   result["Attribute"].SetColorSpace.im_func.func_doc = """SetColorSpace(colorSpace) -> USD_API void

colorSpace : TfToken


Sets the color space of the attribute to C{colorSpace}.



GetColorSpace() UsdStage Color Configuration API

"""
   result["Attribute"].GetBracketingTimeSamples.im_func.func_doc = """GetBracketingTimeSamples(desiredTime, lower, upper, hasTimeSamples) -> USD_API bool

desiredTime : double
lower : double
upper : double
hasTimeSamples : bool


Populate *lower* and *upper* with the next greater and lesser value
relative to the *desiredTime*.


Return false if no value exists or an error occurs, true if either a
default value or timeSamples exist.

Use standard resolution semantics: if a stronger default value is
authored over weaker time samples, the default value hides the
underlying timeSamples.

1) If a sample exists at the *desiredTime*, set both upper and lower
to *desiredTime*.

2) If samples exist surrounding, but not equal to the *desiredTime*,
set lower and upper to the bracketing samples nearest to the
*desiredTime*.

3) If the *desiredTime* is outside of the range of authored samples,
clamp upper and lower to the nearest time sample.

4) If no samples exist, do not modify upper and lower and set
*hasTimeSamples* to false.

In cases (1), (2) and (3), set *hasTimeSamples* to true.

All four cases above are considered to be successful, thus the return
value will be true and no error message will be emitted.

"""
   result["Attribute"].GetConnections.im_func.func_doc = """GetConnections(sources) -> USD_API bool

sources : SdfPathVector


Compose this attribute's connections and fill C{sources} with the
result.


All preexisting elements in C{sources} are lost.

See Relationship Targets and Attribute Connections for details on
behavior when targets point to objects beneath instance prims.

The result is not cached, and thus recomputed on each query.

"""
   result["Attribute"].GetTimeSamples.im_func.func_doc = """GetTimeSamples(times) -> USD_API bool

times : sequence<double>


Populates a vector with authored sample times.


Returns false only on error.

This method uses the standard resolution semantics, so if a stronger
default value is authored over weaker time samples, the default value
will hide the underlying timesamples.

This function will query all value clips that may contribute time
samples for this attribute, opening them if needed. This may be
expensive, especially if many clips are involved. times

- on return, will contain the *sorted*, ascending timeSample
ordinates. Any data in C{times} will be lost, as this method clears
C{times}.

UsdAttribute::GetTimeSamplesInInterval

"""
   result["Attribute"].GetUnionedTimeSamplesInInterval.func_doc = """**static** GetUnionedTimeSamplesInInterval(attrs, interval, times) -> USD_API bool

attrs : sequence< UsdAttribute >
interval : GfInterval
times : sequence<double>


Populates the given vector, C{times} with the union of all the
authored sample times in the GfInterval, C{interval} on all of the
given attributes, C{attrs}.



This function will only query the value clips that may contribute time
samples for the attributes in C{attrs}, in the given C{interval},
opening them if necessary. The accumulated sample times will be in
sorted (increasing) order and will not contain any duplicates.

This clears any existing values in the C{times} vector before
accumulating sample times of the given attributes.

false if any of the attributes in C{attr} are invalid or if there's an
error fetching time-samples for any of the attributes.

UsdAttribute::GetTimeSamplesInInterval

UsdAttribute::GetUnionedTimeSamples

"""
   result["Attribute"].SetConnections.im_func.func_doc = """SetConnections(sources) -> USD_API bool

sources : SdfPathVector


Make the authoring layer's opinion of the connection list explicit,
and set exactly to C{sources}.


Issue an error if C{source} identifies a master prim or an object
descendant to a master prim. It is not valid to author connections to
these objects.

If any path in C{sources} is invalid, issue an error and return false.

"""
   result["Attribute"].GetTypeName.im_func.func_doc = """GetTypeName() -> USD_API SdfValueTypeName



Return the "scene description" value type name for this attribute.

"""
   result["Attribute"].GetVariability.im_func.func_doc = """GetVariability() -> USD_API SdfVariability



An attribute's variability expresses whether it is intended to have
time-samples ( C{SdfVariabilityVarying}), or only a single default
value ( C{SdfVariabilityUniform}).


Variability is required meta-data of all attributes, and its fallback
value is SdfVariabilityVarying.

"""
   result["Attribute"].Get.im_func.func_doc = """Get(value, time) -> bool

value : T
time : TimeCode


Perform value resolution to fetch the value of this attribute at the
requested UsdTimeCode C{time}, which defaults to *default*.


If no value is authored at C{time} but values are authored at other
times, this function will return an interpolated value based on the
stage's interpolation type. See Attribute Value Interpolation.

This templated accessor is designed for high performance data-
streaming applications, allowing one to fetch data into the same
container repeatedly, avoiding memory allocations when possible
(VtArray containers will be resized as necessary to conform to the
size of data being read).

This template is only instantiated for the valid scene description
value types and their corresponding VtArray containers. See Basic
Datatypes for Scene Description Provided by Sdf for the complete list
of types.

Values are retrieved without regard to this attribute's variability.
For example, a uniform attribute may retrieve time sample values if
any are authored. However, the USD_VALIDATE_VARIABILITY TF_DEBUG code
will cause debug information to be output if values that are
inconsistent with this attribute's variability are retrieved. See
UsdAttribute::GetVariability for more details.

true if there was a value to be read, it was of the type T requested,
and we read it successfully - false otherwise. For more details, see
TimeSamples, Defaults, and Value Resolution, and also Attributes of
type SdfAssetPath and UsdAttribute::Get() for information on how to
retrieve resolved asset paths from SdfAssetPath-valued attributes.


----------------------------------------------------------------------
Get(value, time) -> USD_API bool

value : VtValue
time : TimeCode


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Type-erased access, often not as efficient as typed access.

"""
   result["Attribute"].ClearAtTime.im_func.func_doc = """ClearAtTime(time) -> USD_API bool

time : TimeCode


Clears the authored value for this attribute at the given *time*, at
the current EditTarget and returns true on success.


UsdTimeCode::Default() can be used to clear the default value.

Calling clear when either no value is authored or no spec is present,
is a silent no-op returning true.

"""
   result["Attribute"].BlockConnections.im_func.func_doc = """BlockConnections() -> USD_API bool



Clears all connection edits from the current EditTarget, and makes the
opinion explicit, which means we are effectively resetting the
composed value of the targets list to empty.

"""
   result["Attribute"].ValueMightBeTimeVarying.im_func.func_doc = """ValueMightBeTimeVarying() -> USD_API bool



Return true if it is possible, but not certain, that this attribute's
value changes over time, false otherwise.


If this function returns false, it is certain that this attribute's
value remains constant over time.

This function is equivalent to checking if GetNumTimeSamples() >1, but
may be more efficient since it does not actually need to get a full
count of all time samples.

"""
   result["Attribute"].AddConnection.im_func.func_doc = """AddConnection(source, position) -> USD_API bool

source : SdfPath
position : ListPosition


Adds C{source} to the list of connections, in the position specified
by C{position}.


Issue an error if C{source} identifies a master prim or an object
descendant to a master prim. It is not valid to author connections to
these objects.

What data this actually authors depends on what data is currently
authored in the authoring layer, with respect to list-editing
semantics, which we will document soon

"""
   result["Attribute"].GetResolveInfo.im_func.func_doc = """GetResolveInfo(time) -> USD_API UsdResolveInfo

time : TimeCode


Perform value resolution to determine the source of the resolved value
of this attribute at the requested UsdTimeCode C{time}, which defaults
to *default*.

"""
   result["Attribute"].SetVariability.im_func.func_doc = """SetVariability(variability) -> USD_API bool

variability : SdfVariability


Set the value for variability at the current EditTarget, return true
on success, false if the value can not be written.


B{Note} that this value should not be changed as it is typically
either automatically authored or provided by a property definition.
This method is provided primarily for fixing invalid scene
description.

"""
   result["Attribute"].HasFallbackValue.im_func.func_doc = """HasFallbackValue() -> USD_API bool



Return true if this attribute has a fallback value provided by a
registered schema.

"""
   result["Attribute"].GetUnionedTimeSamples.func_doc = """**static** GetUnionedTimeSamples(attrs, times) -> USD_API bool

attrs : sequence< UsdAttribute >
times : sequence<double>


Populates the given vector, C{times} with the union of all the
authored sample times on all of the given attributes, C{attrs}.



This function will query all value clips that may contribute time
samples for the attributes in C{attrs}, opening them if needed. This
may be expensive, especially if many clips are involved. The
accumulated sample times will be in sorted (increasing) order and will
not contain any duplicates.

This clears any existing values in the C{times} vector before
accumulating sample times of the given attributes.

false if any of the attributes in C{attr} are invalid or if there's an
error when fetching time-samples for any of the attributes.

UsdAttribute::GetTimeSamples

UsdAttribute::GetUnionedTimeSamplesInInterval

"""
   result["Attribute"].GetColorSpace.im_func.func_doc = """GetColorSpace() -> USD_API TfToken



Gets the color space in which the attribute is authored.



SetColorSpace() UsdStage Color Configuration API

"""
   result["Attribute"].Clear.im_func.func_doc = """Clear() -> USD_API bool



Clears the authored default value and all time samples for this
attribute at the current EditTarget and returns true on success.


Calling clear when either no value is authored or no spec is present,
is a silent no-op returning true.  This method does not affect any
other data authored on this attribute.

"""
   result["Attribute"].HasValue.im_func.func_doc = """HasValue() -> USD_API bool



Return true if this attribute has an authored default value, authored
time samples or a fallback value provided by a registered schema.

"""
   result["Attribute"].ClearColorSpace.im_func.func_doc = """ClearColorSpace() -> USD_API bool



Clears authored color-space value on the attribute.



SetColorSpace()

"""
   result["Attribute"].GetRoleName.im_func.func_doc = """GetRoleName() -> USD_API TfToken



Return the roleName for this attribute's typeName.

"""
   result["Attribute"].HasAuthoredValueOpinion.im_func.func_doc = """HasAuthoredValueOpinion() -> USD_API bool



Return true if this attribute has either an authored default value or
authored time samples.

"""
   result["Attribute"].Block.im_func.func_doc = """Block() -> USD_API void



Removes all time samples on an attribute and sets a block value as the
default.


See C{SdfValueBlock} for more information on the type being authored.
This value covers all lower opinions in the LayerStack. During value
resolution, if a block is authored, if there is a fallback, the client
will receive that, otherwise they will receive false when calling
Get() .

"""
   result["Attribute"].RemoveConnection.im_func.func_doc = """RemoveConnection(source) -> USD_API bool

source : SdfPath


Removes C{target} from the list of targets.


Issue an error if C{source} identifies a master prim or an object
descendant to a master prim. It is not valid to author connections to
these objects.

"""
   result["Attribute"].Set.im_func.func_doc = """Set(value, time) -> bool

value : T
time : TimeCode


Set the value of this attribute in the current UsdEditTarget to
C{value} at UsdTimeCode C{time}, which defaults to *default*.


Values are authored without regard to this attribute's variability.
For example, time sample values may be authored on a uniform
attribute. However, the USD_VALIDATE_VARIABILITY TF_DEBUG code will
cause debug information to be output if values that are inconsistent
with this attribute's variability are authored. See
UsdAttribute::GetVariability for more details.

false and generate an error if type C{T} does not match this
attribute's defined scene description type B{exactly}, or if there is
no existing definition for the attribute.


----------------------------------------------------------------------
Set(value, time) -> USD_API bool

value : VtValue
time : TimeCode


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Attribute"].HasColorSpace.im_func.func_doc = """HasColorSpace() -> USD_API bool



Returns whether color-space is authored on the attribute.



GetColorSpace()

"""
   result["Attribute"].HasAuthoredConnections.im_func.func_doc = """HasAuthoredConnections() -> USD_API bool



Return true if this attribute has any authored opinions regarding
connections.


Note that this includes opinions that remove connections, so a true
return does not necessarily indicate that this attribute has
connections.

"""
   result["Attribute"].__init__.im_func.func_doc = """__init__()



Construct an invalid attribute.


----------------------------------------------------------------------
__init__(prim, proxyPrimPath, attrName)

prim : _PrimDataHandle
proxyPrimPath : SdfPath
attrName : TfToken


----------------------------------------------------------------------
__init__(objType, prim, proxyPrimPath, propName)

objType : ObjType
prim : _PrimDataHandle
proxyPrimPath : SdfPath
propName : TfToken

"""
   result["Attribute"].SetTypeName.im_func.func_doc = """SetTypeName(typeName) -> USD_API bool

typeName : SdfValueTypeName


Set the value for typeName at the current EditTarget, return true on
success, false if the value can not be written.


B{Note} that this value should not be changed as it is typically
either automatically authored or provided by a property definition.
This method is provided primarily for fixing invalid scene
description.

"""
   result["Attribute"].ClearDefault.im_func.func_doc = """ClearDefault() -> USD_API bool



Shorthand for ClearAtTime(UsdTimeCode::Default()).

"""
   result["Attribute"].ClearConnections.im_func.func_doc = """ClearConnections() -> USD_API bool



Remove all opinions about the connections list from the current edit
target.

"""
   result["Attribute"].GetNumTimeSamples.im_func.func_doc = """GetNumTimeSamples() -> USD_API size_t



Returns the number of time samples that have been authored.


This method uses the standard resolution semantics, so if a stronger
default value is authored over weaker time samples, the default value
will hide the underlying timesamples.

This function will query all value clips that may contribute time
samples for this attribute, opening them if needed. This may be
expensive, especially if many clips are involved.

"""
   result["Attribute"].GetTimeSamplesInInterval.im_func.func_doc = """GetTimeSamplesInInterval(interval, times) -> USD_API bool

interval : GfInterval
times : sequence<double>


Populates a vector with authored sample times in C{interval}.


Returns false only on an error.

This function will only query the value clips that may contribute time
samples for this attribute in the given interval, opening them if
necessary. interval

- the GfInterval on which to gather time samples. times

- on return, will contain the *sorted*, ascending timeSample
ordinates. Any data in C{times} will be lost, as this method clears
C{times}.

UsdAttribute::GetTimeSamples

"""
   result["APISchemaBase"].__doc__ = """
The base class for all *API* schemas.


An API schema provides an interface to a prim's qualities, but does
not specify a typeName for the underlying prim. The prim's qualities
include its inheritance structure, attributes, relationships etc.
Since it cannot provide a typeName, an API schema is considered to be
non-concrete.

To auto-generate an API schema using usdGenSchema, simply leave the
typeName empty and make it inherit from "/APISchemaBase" or from
another API schema. See UsdModelAPI, UsdClipsAPI and UsdCollectionAPI
for examples.

API schemas are classified into applied and non-applied API schemas.
The author of an API schema has to decide on the type of API schema at
the time of its creation by setting customData['apiSchemaType'] in the
schema definition (i.e. in the associated primSpec inside the
schema.usda file). UsdAPISchemaBase implements methods that are used
to record the application of an API schema on a USD prim.

If an API schema only provides an interface to set certain core bits
of metadata (like UsdModelAPI, which sets model kind and UsdClipsAPI,
which sets clips-related metadata) OR if the API schema can apply to
any type of prim or only to a known fixed set of prim types OR if
there is no use of recording the application of the API schema, in
such cases, it would be better to make it a non-applied API schema.
Examples of non-applied API schemas include UsdModelAPI, UsdClipsAPI,
UsdShadeConnectableAPI and UsdGeomPrimvarsAPI.

If there is a need to discover (or record) whether a prim contains or
subscribes to a given API schema, it would be advantageous to make the
API schema be "applied". In general, API schemas that add one or more
properties to a prim should be tagged as applied API schemas. A public
Apply() (or private _Apply()) method is generated for applied API
schemas by usdGenSchema. An applied API schema must be applied to a
prim via a call to the generated Apply() method, for the schema object
to evaluate to true when converted to a bool using the explicit bool
conversion operator. Examples of applied API schemas include
UsdCollectionAPI, UsdGeomModelAPI and UsdGeomMotionAPI


"""
   result["APISchemaBase"].Get.func_doc = """**static** Get(stage, path) -> USD_API UsdAPISchemaBase

stage : StagePtr
path : SdfPath


Return a UsdAPISchemaBase holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdAPISchemaBase(stage->GetPrimAtPath(path));


"""
   result["APISchemaBase"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USD_API  TfType


"""
   result["APISchemaBase"].__init__.im_func.func_doc = """__init__(prim)

prim : Prim


Construct a UsdAPISchemaBase on UsdPrim C{prim}.


Equivalent to UsdAPISchemaBase::Get (prim.GetStage(), prim.GetPath())
for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : SchemaBase


Construct a UsdAPISchemaBase on the prim held by C{schemaObj}.


Should be preferred over UsdAPISchemaBase (schemaObj.GetPrim()), as it
preserves SchemaBase state.


----------------------------------------------------------------------
__init__(prim, instanceName)

prim : Prim
instanceName : TfToken


Construct a multiple-apply UsdAPISchemaBase on UsdPrim C{prim} with
the specified C{instanceName}.


----------------------------------------------------------------------
__init__(schemaObj, instanceName)

schemaObj : SchemaBase
instanceName : TfToken


Construct a multiple-apply UsdAPISchemaBase on the prim held by
C{schemaObj} with the given C{instanceName}.

"""
   result["APISchemaBase"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USD_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["TraverseInstanceProxies"].func_doc = """TraverseInstanceProxies(predicate) -> _PrimFlagsPredicate

predicate : _PrimFlagsPredicate


This function is used to allow the prim traversal functions listed
under Prim predicate flags to traverse beneath instance prims and
return descendants that pass the specified C{predicate} as instance
proxy prims.


For example: ::

  // Return all children of the specified prim.  
  // If prim is an instance, return all children as instance proxy prims.
  prim.GetFilteredChildren(
      UsdTraverseInstanceProxies(UsdPrimAllPrimsPredicate))
  
  // Return children of the specified prim that pass the default predicate.
  // If prim is an instance, return the children that pass this predicate
  // as instance proxy prims.
  prim.GetFilteredChildren(UsdTraverseInstanceProxies());
  
  // Return all model or group children of the specified prim.
  // If prim is an instance, return the children that pass this predicate 
  // as instance proxy prims.
  prim.GetFilteredChildren(UsdTraverseInstanceProxies(UsdPrimIsModel || UsdPrimIsGroup));

Users may also call Usd_PrimFlagsPredicate::TraverseInstanceProxies to
enable traversal beneath instance prims. This function is equivalent
to: ::

  predicate.TraverseInstanceProxies(true);

However, this function may be more convenient, especially when calling
a prim traversal function with a default-constructed tautology
predicate.


----------------------------------------------------------------------
TraverseInstanceProxies() -> _PrimFlagsPredicate



This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Convenience method equivalent to calling UsdTraverseInstanceProxies
with the UsdPrimDefaultPredicate that is used by default for prim
traversals.

"""
   result["PrimRange"].__doc__ = """
An forward-iterable range that traverses a subtree of prims rooted at
a given prim in depth-first order.


In addition to depth-first order, UsdPrimRange provides the optional
ability to traverse in depth-first pre- and post-order wher prims
appear twice in the range; first before all descendants and then again
immediately after all descendants. This is useful for maintaining
state associated with subtrees, in a stack-like fashion. See
UsdPrimRange::iterator::IsPostVisit() to detect when an iterator is
visiting a prim for the second time.

There are several constructors providing different levels of
configurability; ultimately, one can provide a prim predicate for a
custom iteration, just as one would use UsdPrim::GetFilteredChildren()
in a custom recursion.

Why would one want to use a UsdPrimRange rather than just iterating
over the results of UsdPrim::GetFilteredDescendants() ? Primarily, if
one of the following applies:
   - You need to perform pre-and-post-order processing

   - You may want to prune sub-trees from processing (see
     UsdPrimRange::iterator::PruneChildren() )

   - You want to treat the root prim itself uniformly with its
     descendents (GetFilteredDescendants() will not return the root prim
     itself, while UsdPrimRange will - see UsdPrimRange::Stage for an
     exception).
     B{Using UsdPrimRange in C++}

UsdPrimRange provides standard container-like semantics. For example:
::

  // simple range- for iteration
  for (UsdPrim prim: UsdPrimRange(rootPrim)) {
      ProcessPrim(prim);
  }
  
  // using stl algorithms
  std::vector<UsdPrim> meshes;
  auto range = stage->Traverse();
  std::copy_if(range.begin(), range.end(), std::back_inserter(meshes),
               [](UsdPrim const &) { return prim.IsA<UsdGeomMesh>(); });
  
  
// iterator-
based iterating, with subtree pruning
  UsdPrimRange range(rootPrim);
  for (auto iter = range.begin(); iter != range.end(); ++iter) {
      if (UsdModelAPI(*iter).GetKind() == KindTokens->component) {
          iter.PruneChildren();
      }
      else {
          nonComponents.push_back(*iter);
      }
  }

B{Using Usd.PrimRange in python}

The python wrapping for PrimRange is python-iterable, so it can used
directly as the object of a "for x in..." clause; however in that
usage one loses access to PrimRange methods such as PruneChildren()
and IsPostVisit(). Simply create the iterator outside the loop to
overcome this limitation. Finally, in python, prim predicates must be
combined with bit-wise operators rather than logical operators because
the latter are not overridable. ::

  # simple iteration
  for prim in Usd.PrimRange(rootPrim):
      ProcessPrim(prim)
  
  # filtered range using iterator to invoke iterator methods
  it = iter(Usd.PrimRange.Stage(stage, Usd.PrimIsLoaded 
&
 ~Usd.PrimIsAbstract))
  for prim in it:
      if Usd.ModelAPI(prim).GetKind() == Kind.Tokens.component:
          it.PruneChildren()
      else:
          nonComponents.append(prim)

Finally, since iterators in python are not directly dereferencable, we
provide the *python* *only* methods GetCurrentPrim() and IsValid(),
documented in the python help system.

"""
   result["PrimRange"].AllPrimsPreAndPostVisit.func_doc = """**static** AllPrimsPreAndPostVisit(start) -> PrimRange

start : Prim


Construct a PrimRange that traverses the subtree rooted at C{start} in
depth-first order, visiting all prims (including deactivated,
undefined, and abstract prims) with pre- and post-order visitation.


Pre- and post-order visitation means that each prim appears twice in
the range; not only prior to all its descendants as with an ordinary
traversal but also immediately following its descendants. This lets
client code maintain state for subtrees. See
UsdPrimRange::iterator::IsPostVisit() .

"""
   result["PrimRange"].PreAndPostVisit.func_doc = """**static** PreAndPostVisit(start) -> PrimRange

start : Prim


Create a PrimRange that traverses the subtree rooted at C{start} in
depth-first order, visiting prims that pass the default predicate (as
defined by UsdPrimDefaultPredicate) with pre- and post-order
visitation.


Pre- and post-order visitation means that each prim appears twice in
the range; not only prior to all its descendants as with an ordinary
traversal but also immediately following its descendants. This lets
client code maintain state for subtrees. See
UsdPrimRange::iterator::IsPostVisit() .


----------------------------------------------------------------------
PreAndPostVisit(start, predicate) -> PrimRange

start : Prim
predicate : _PrimFlagsPredicate


Create a PrimRange that traverses the subtree rooted at C{start} in
depth-first order, visiting prims that pass C{predicate} with pre- and
post-order visitation.


Pre- and post-order visitation means that each prim appears twice in
the range; not only prior to all its descendants as with an ordinary
traversal but also immediately following its descendants. This lets
client code maintain state for subtrees. See
UsdPrimRange::iterator::IsPostVisit() .

"""
   result["PrimRange"].__init__.im_func.func_doc = """__init__()



----------------------------------------------------------------------
__init__(start)

start : Prim


Construct a PrimRange that traverses the subtree rooted at C{start} in
depth-first order, visiting prims that pass the default predicate (as
defined by UsdPrimDefaultPredicate).


----------------------------------------------------------------------
__init__(start, predicate)

start : Prim
predicate : _PrimFlagsPredicate


Construct a PrimRange that traverses the subtree rooted at C{start} in
depth-first order, visiting prims that pass C{predicate}.


----------------------------------------------------------------------
__init__(begin, end, proxyPrimPath, predicate)

begin : _PrimDataConstPtr
end : _PrimDataConstPtr
proxyPrimPath : SdfPath
predicate : _PrimFlagsPredicate

"""
   result["PrimRange"].Stage.func_doc = """**static** Stage(stage, predicate) -> USD_API UsdPrimRange

stage : StagePtr
predicate : _PrimFlagsPredicate


Create a PrimRange that traverses all the prims on C{stage}, and
visits those that pass the default predicate (as defined by
UsdPrimDefaultPredicate).

"""
   result["PrimRange"].AllPrims.func_doc = """**static** AllPrims(start) -> PrimRange

start : Prim


Construct a PrimRange that traverses the subtree rooted at C{start} in
depth-first order, visiting all prims (including deactivated,
undefined, and abstract prims).

"""
   result["_NonPopulatingStageCacheWrapper"].__doc__ = """"""
   result["StagePopulationMask"].__doc__ = """
This class represents a mask that may be applied to a UsdStage to
limit the set of UsdPrim s it populates.


This is useful in cases where clients have a large scene but only wish
to view or query a single or a handful of objects. For example,
suppose we have a city block with buildings, cars, crowds of people,
and a couple of main characters. Some tasks might only require looking
at a single main character and perhaps a few props. We can create a
population mask with the paths to the character and props of interest
and open a UsdStage with that mask. Usd will avoid populating the
other objects in the scene, saving time and memory. See
UsdStage::OpenMasked() for more.

A mask is defined by a set of SdfPath s with the following qualities:
they are absolute prim paths (or the absolute root path), and no path
in the set is an ancestor path of any other path in the set other than
itself. For example, the set of paths ['/a/b', '/a/c', '/x/y'] is a
valid mask, but the set of paths ['/a/b', '/a/b/c', '/x/y'] is
redundant, since '/a/b' is an ancestor of '/a/b/c'. The path '/a/b/c'
may be removed. The GetUnion() and Add() methods ensure that no
redundant paths are added.

Default-constructed UsdStagePopulationMask s are considered empty (
IsEmpty() ) and include no paths. A population mask containing
SdfPath::AbsoluteRootPath() includes all paths.

"""
   result["StagePopulationMask"].GetPaths.im_func.func_doc = """GetPaths() -> USD_API sequence< SdfPath >



Return the set of paths that define this mask.

"""
   result["StagePopulationMask"].All.func_doc = """**static** All() -> StagePopulationMask



Return a mask that includes all paths.


This is the mask that contains the absolute root path.

"""
   result["StagePopulationMask"].GetUnion.im_func.func_doc = """GetUnion(other) -> USD_API UsdStagePopulationMask

other : StagePopulationMask


Return a mask that is the union of this and C{other}.


----------------------------------------------------------------------
GetUnion(path) -> USD_API UsdStagePopulationMask

path : SdfPath


Return a mask that is the union of this and a mask containing the
single C{path}.

"""
   result["StagePopulationMask"].Union.func_doc = """**static** Union(l, r) -> USD_API UsdStagePopulationMask

l : StagePopulationMask
r : StagePopulationMask


Return a mask that is the union of C{l} and C{r}.

"""
   result["StagePopulationMask"].GetIncludedChildNames.im_func.func_doc = """GetIncludedChildNames(path, childNames) -> USD_API bool

path : SdfPath
childNames : sequence< TfToken >


Return true if this mask includes any child prims beneath C{path},
false otherwise.


If only specific child prims beneath C{path} are included, the names
of those children will be returned in C{childNames}. If all child
prims beneath C{path} are included, C{childNames} will be empty.

"""
   result["StagePopulationMask"].GetIntersection.im_func.func_doc = """GetIntersection(other) -> USD_API UsdStagePopulationMask

other : StagePopulationMask


Return a mask that is the intersection of this and C{other}.

"""
   result["StagePopulationMask"].Includes.im_func.func_doc = """Includes(other) -> USD_API bool

other : StagePopulationMask


Return true if this mask is a superset of C{other}.


That is, if this mask includes at least every path that C{other}
includes.


----------------------------------------------------------------------
Includes(path) -> USD_API bool

path : SdfPath


Return true if this mask includes C{path}.


This is true if C{path} is one of the paths in this mask, or if it is
either a descendant or an ancestor of one of the paths in this mask.

"""
   result["StagePopulationMask"].__init__.im_func.func_doc = """__init__()



Construct an empty mask that includes no paths.


----------------------------------------------------------------------
__init__(arg1)

arg1 : StagePopulationMask


----------------------------------------------------------------------
__init__(arg1)

arg1 : StagePopulationMask


----------------------------------------------------------------------
__init__(f, l)

f : Iter
l : Iter


Construct a mask from the range of paths [f, l).


All paths in the range must be absolute prim paths or the absolute
root path. (See SdfPath::IsAbsolutePath,
SdfPath::IsAbsoluteRootOrPrimPath).


----------------------------------------------------------------------
__init__(paths)

paths : sequence< SdfPath >


Construct a mask from C{paths}.


All paths must be absolute prim paths or the absolute root path. (See
SdfPath::IsAbsolutePath, SdfPath::IsAbsoluteRootOrPrimPath).


----------------------------------------------------------------------
__init__(paths) -> USD_API

paths : sequence< SdfPath >


Construct a mask from C{paths}.


All paths must be absolute prim paths or the absolute root path. (See
SdfPath::IsAbsolutePath, SdfPath::IsAbsoluteRootOrPrimPath).

"""
   result["StagePopulationMask"].Add.im_func.func_doc = """Add(other) -> StagePopulationMask

other : StagePopulationMask


Assign this mask to be its union with C{other} and return a reference
to this mask.


----------------------------------------------------------------------
Add(path) -> StagePopulationMask

path : SdfPath


Assign this mask to be its union with C{path} and return a reference
to this mask.

"""
   result["StagePopulationMask"].IsEmpty.im_func.func_doc = """IsEmpty() -> bool



Return true if this mask contains no paths.


Empty masks include no paths.

"""
   result["StagePopulationMask"].IncludesSubtree.im_func.func_doc = """IncludesSubtree(path) -> USD_API bool

path : SdfPath


Return true if this mask includes C{path} and all paths descendant to
C{path}.


For example, consider a mask containing the path '/a/b'. Then the
following holds: ::

  mask.Includes('/a') -> true
  mask.Includes('/a/b') -> true
  mask.IncludesSubtree('/a') -> false
  mask.IncludesSubtree('/a/b') -> true


"""
   result["StagePopulationMask"].Intersection.func_doc = """**static** Intersection(l, r) -> USD_API UsdStagePopulationMask

l : StagePopulationMask
r : StagePopulationMask


Return a mask that is the intersection of C{l} and C{r}.

"""
   result["Stage"].__doc__ = """
The outermost container for scene description, which owns and presents
composed prims as a scenegraph, following the composition recipe
recursively described in its associated "root layer".


USD derives its persistent-storage scalability by combining and
reusing simple compositions into richer aggregates using referencing
and layering with sparse overrides. Ultimately, every composition
(i.e. "scene") is identifiable by its root layer, i.e. the C{.usd}
file, and a scene is instantiated in an application on a UsdStage that
presents a composed view of the scene's root layer. Each simple
composition referenced into a larger composition could be presented on
its own UsdStage, at the same (or not) time that it is participating
in the larger composition on its own UsdStage; all of the underlying
layers will be shared by the two stages, while each maintains its own
scenegraph of composed prims.

A UsdStage has sole ownership over the UsdPrim 's with which it is
populated, and retains *shared* ownership (with other stages and
direct clients of SdfLayer 's, via the Sdf_LayerRegistry that
underlies all SdfLayer creation methods) of layers. It provides
roughly five categories of API that address different aspects of scene
management:

   - Stage lifetime management methods for constructing and initially
     populating a UsdStage from an existing layer file, or one that will be
     created as a result, in memory or on the filesystem.

   - Load/unload working set management methods that allow you to
     specify which payloads should be included and excluded from the
     stage's composition.

   - Variant management methods to manage policy for which variant to
     use when composing prims that provide a named variant set, but do not
     specify a selection.

   - Prim access, creation, and mutation methods that allow you to
     find, create, or remove a prim identified by a path on the stage. This
     group also provides methods for efficiently traversing the prims on
     the stage.

   - Layers and EditTargets methods provide access to the layers in
     the stage's *root LayerStack* (i.e. the root layer and all of its
     recursive sublayers), and the ability to set a UsdEditTarget into
     which all subsequent mutations to objects associated with the stage
     (e.g. prims, properties, etc) will go.

   - Serialization methods for "flattening" a composition (to varying
     degrees), and exporting a completely flattened view of the stage to a
     string or file. These methods can be very useful for targetted asset
     optimization and debugging, though care should be exercized with large
     scenes, as flattening defeats some of the benefits of referenced scene
     description, and may produce very large results, especially in file
     formats that do not support data de-duplication, like the usda ASCII
     format!

Stage Session Layers
====================

Each UsdStage can possess an optional "session layer". The purpose of
a session layer is to hold ephemeral edits that modify a UsdStage 's
contents or behavior in a way that is useful to the client, but should
not be considered as permanent mutations to be recorded upon export. A
very common use of session layers is to make variant selections, to
pick a specific LOD or shading variation, for example. The session
layer is also frequently used to perform interactive vising/invsning
of geometry and assets in the scene. A session layer, if present,
contributes to a UsdStage 's identity, for purposes of stage-caching,
etc.

"""
   result["Stage"].IsLayerMuted.im_func.func_doc = """IsLayerMuted(layerIdentifier) -> USD_API bool

layerIdentifier : string


Returns true if the layer specified by C{layerIdentifier} is muted in
this cache, false otherwise.


See documentation on MuteLayer for details on how C{layerIdentifier}
is compared to the layers that have been muted.

"""
   result["Stage"].GetEditTargetForLocalLayer.im_func.func_doc = """GetEditTargetForLocalLayer(i) -> USD_API UsdEditTarget

i : size_t


Return a UsdEditTarget for editing the layer at index *i* in the layer
stack.


This edit target will incorporate any layer time offset that applies
to the sublayer.


----------------------------------------------------------------------
GetEditTargetForLocalLayer(layer) -> USD_API UsdEditTarget

layer : SdfLayerHandle


Return a UsdEditTarget for editing the given local *layer*.


If the given layer appears more than once in the layer stack, the time
offset to the first occurrence will be used.

"""
   result["Stage"].GetColorConfigFallbacks.func_doc = """**static** GetColorConfigFallbacks(colorConfiguration, colorManagementSystem) -> USD_API void

colorConfiguration : SdfAssetPath
colorManagementSystem : TfToken


Returns the global fallback values of 'colorConfiguration' and
'colorManagementSystem'.


These are set in the plugInfo.json file of a plugin, but can be
overridden by calling the static method SetColorConfigFallbacks() .

The python wrapping of this method returns a tuple containing
(colorConfiguration, colorManagementSystem).

SetColorConfigFallbacks, Color Configuration API

"""
   result["Stage"].HasAuthoredTimeCodeRange.im_func.func_doc = """HasAuthoredTimeCodeRange() -> USD_API bool



Returns true if the stage has both start and end timeCodes authored in
the session layer or the root layer of the stage.

"""
   result["Stage"].GetEndTimeCode.im_func.func_doc = """GetEndTimeCode() -> USD_API double



Returns the stage's end timeCode.


If the stage has an associated session layer with an end timeCode
opinion, this value is returned. Otherwise, the end timeCode opinion
from the root layer is returned.

"""
   result["Stage"].RemovePrim.im_func.func_doc = """RemovePrim(path) -> USD_API bool

path : SdfPath


Remove all scene description for the given C{path} and its subtree *in
the current UsdEditTarget*.


This method does not do what you might initially think! Calling this
function will not necessarily cause the UsdPrim at C{path} on this
stage to disappear. Completely eradicating a prim from a composition
can be an involved process, involving edits to many contributing
layers, some of which (in many circumstances) will not be editable by
a client. This method is a surgical instrument that *can* be used
iteratively to effect complete removal of a prim and its subtree from
namespace, assuming the proper permissions are acquired, but more
commonly it is used to perform layer-level operations; e.g.: ensuring
that a given layer (as expressed by a UsdEditTarget) provides no
opinions for a prim and its subtree.

Generally, if your eye is attracted to this method, you probably want
to instead use UsdPrim::SetActive(false), which will provide the
composed effect of removing the prim and its subtree from the
composition, without actually removing any scene description, which as
a bonus, means that the effect is reversible at a later time!

"""
   result["Stage"].ExpandPopulationMask.im_func.func_doc = """ExpandPopulationMask(relPred, attrPred) -> USD_API void

relPred : function<bool( UsdRelationship )>
attrPred : function<bool( UsdAttribute )>


Expand this stage's population mask to include the targets of all
relationships that pass C{relPred} and connections to all attributes
that pass C{attrPred} recursively.


If C{relPred} is null, include all relationship targets; if
C{attrPred} is null, include all connections.

This function can be used, for example, to expand a population mask
for a given prim to include bound materials, if those bound materials
are expressed as relationships or attribute connections.

See also UsdPrim::FindAllRelationshipTargetPaths() and
UsdPrim::FindAllAttributeConnectionPaths() .

"""
   result["Stage"].GetMetadata.im_func.func_doc = """GetMetadata(key, value) -> bool

key : TfToken
value : T


Return in C{value} an authored or fallback value (if one was defined
for the given metadatum) for Stage metadatum C{key}.


Order of resolution is session layer, followed by root layer, else
fallback to the SdfSchema.

true if we successfully retrieved a value of the requested type; false
if C{key} is not allowed as layer metadata or no value was found.
Generates a coding error if we retrieved a stored value of a type
other than the requested type

General Metadata in USD


----------------------------------------------------------------------
GetMetadata(key, value) -> USD_API bool

key : TfToken
value : VtValue


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Stage"].HasMetadataDictKey.im_func.func_doc = """HasMetadataDictKey(key, keyPath) -> USD_API bool

key : TfToken
keyPath : TfToken


Return true if there exists any authored or fallback opinion for
C{key} and C{keyPath}.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries stored in the metadata field at C{key}. If C{keyPath}
is empty, returns C{false}.

Returns false if C{key} is not allowed as layer metadata.

Dictionary-valued Metadata

"""
   result["Stage"].GetDefaultPrim.im_func.func_doc = """GetDefaultPrim() -> USD_API UsdPrim



Return the root UsdPrim on this stage whose name is the root layer's
defaultPrim metadata's value.


Return an invalid prim if there is no such prim or if the root layer's
defaultPrim metadata is unset or is not a valid prim name. Note that
this function only examines this stage's rootLayer. It does not
consider sublayers of the rootLayer. See also
SdfLayer::GetDefaultPrim() .

"""
   result["Stage"].ClearDefaultPrim.im_func.func_doc = """ClearDefaultPrim() -> USD_API void



Clear the default prim layer metadata in this stage's root layer.


This is shorthand for: ::

  stage->GetRootLayer()->ClearDefaultPrim();

 Note that this function always authors to the stage's root layer. To
author to a different layer, use the SdfLayer::SetDefaultPrim() API.

"""
   result["Stage"].SetPopulationMask.im_func.func_doc = """SetPopulationMask(mask) -> USD_API void

mask : StagePopulationMask


Set this stage's population mask and recompose the stage.

"""
   result["Stage"].SetMetadata.im_func.func_doc = """SetMetadata(key, value) -> bool

key : TfToken
value : T


Set the value of Stage metadatum C{key} to C{value}, if the stage's
current UsdEditTarget is the root or session layer.


If the current EditTarget is any other layer, raise a coding error.

true if authoring was successful, false otherwise. Generates a coding
error if C{key} is not allowed as layer metadata.

General Metadata in USD


----------------------------------------------------------------------
SetMetadata(key, value) -> USD_API bool

key : TfToken
value : VtValue


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Stage"].CreateInMemory.func_doc = """**static** CreateInMemory(load) -> USD_API UsdStageRefPtr

load : InitialLoadSet


Creates a new stage only in memory, analogous to creating an anonymous
SdfLayer.


Note that the C{pathResolverContext} passed here will apply to all
path resolutions for this stage, regardless of what other context may
be bound at resolve time. If no context is passed in here, Usd will
create one by calling

ArResolver::CreateDefaultContext. The initial set of prims to load on
the stage can be specified using the C{load} parameter.

UsdStage::InitialLoadSet. Invoking an overload that does not take a
C{sessionLayer} argument will create a stage with an anonymous in-
memory session layer. To create a stage without a session layer, pass
TfNullPtr (or None in python) as the C{sessionLayer} argument.


----------------------------------------------------------------------
CreateInMemory(identifier, load) -> USD_API UsdStageRefPtr

identifier : string
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CreateInMemory(identifier, pathResolverContext, load) -> USD_API UsdStageRefPtr

identifier : string
pathResolverContext : ArResolverContext
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CreateInMemory(identifier, sessionLayer, load) -> USD_API UsdStageRefPtr

identifier : string
sessionLayer : SdfLayerHandle
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CreateInMemory(identifier, sessionLayer, pathResolverContext, load) -> USD_API UsdStageRefPtr

identifier : string
sessionLayer : SdfLayerHandle
pathResolverContext : ArResolverContext
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Stage"].Unload.im_func.func_doc = """Unload(path) -> USD_API void

path : SdfPath


Unload the prim and its descendants specified by C{path}.


If an instance prim is encountered during this operation, this
function will also unload prims in the instance's master. In other
words, unloading a single instance may affect other instances because
it changes the load state of prims in the shared master. However,
unloading a single instance will never cause other instances to be
unloaded as well.

See the rules under Working Set Management for a discussion of what
paths are considered valid.

"""
   result["Stage"].GetGlobalVariantFallbacks.func_doc = """**static** GetGlobalVariantFallbacks() -> USD_API PcpVariantFallbackMap



Get the global variant fallback preferences used in new UsdStages.

"""
   result["Stage"].CreateNew.func_doc = """**static** CreateNew(identifier, load) -> USD_API UsdStageRefPtr

identifier : string
load : InitialLoadSet


Create a new stage with root layer C{identifier}, destroying
potentially existing files with that identifier; it is considered an
error if an existing, open layer is present with this identifier.



SdfLayer::CreateNew() Invoking an overload that does not take a
C{sessionLayer} argument will create a stage with an anonymous in-
memory session layer. To create a stage without a session layer, pass
TfNullPtr (or None in python) as the C{sessionLayer} argument. The
initial set of prims to load on the stage can be specified using the
C{load} parameter.

UsdStage::InitialLoadSet. Note that the C{pathResolverContext} passed
here will apply to all path resolutions for this stage, regardless of
what other context may be bound at resolve time. If no context is
passed in here, Usd will create one by calling

ArResolver::CreateDefaultContextForAsset with the root layer's
repository path if the layer has one, otherwise its real path.


----------------------------------------------------------------------
CreateNew(identifier, sessionLayer, load) -> USD_API UsdStageRefPtr

identifier : string
sessionLayer : SdfLayerHandle
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CreateNew(identifier, sessionLayer, pathResolverContext, load) -> USD_API UsdStageRefPtr

identifier : string
sessionLayer : SdfLayerHandle
pathResolverContext : ArResolverContext
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
CreateNew(identifier, pathResolverContext, load) -> USD_API UsdStageRefPtr

identifier : string
pathResolverContext : ArResolverContext
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Stage"].HasLocalLayer.im_func.func_doc = """HasLocalLayer(layer) -> USD_API bool

layer : SdfLayerHandle


Return true if *layer* is one of the layers in this stage's local,
root layerStack.

"""
   result["Stage"].ExportToString.im_func.func_doc = """ExportToString(result, addSourceFileComment) -> USD_API bool

result : string
addSourceFileComment : bool


Writes the composite scene as a flattened Usd text representation into
the given *string*.


If addSourceFileComment is true, a comment in the output layer will
mention the input layer it was generated from.

See UsdStage::Flatten for details of the flattening transformation.

"""
   result["Stage"].SetFramesPerSecond.im_func.func_doc = """SetFramesPerSecond(framesPerSecond) -> USD_API void

framesPerSecond : double


Sets the stage's framesPerSecond value.


The framesPerSecond value is set in the current EditTarget, if it is
the root layer of the stage or the session layer associated with the
stage. If the current EditTarget is neither, a warning is issued and
no value is set.

GetFramesPerSecond()

"""
   result["Stage"].HasAuthoredMetadataDictKey.im_func.func_doc = """HasAuthoredMetadataDictKey(key, keyPath) -> USD_API bool

key : TfToken
keyPath : TfToken


Return true if there exists any authored opinion (excluding fallbacks)
for C{key} and C{keyPath}.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries stored in the metadata field at C{key}. If C{keyPath}
is empty, returns C{false}.

Dictionary-valued Metadata

"""
   result["Stage"].SaveSessionLayers.im_func.func_doc = """SaveSessionLayers() -> USD_API void



Calls SdfLayer::Save on all dirty session layers and sublayers of
session layers contributing to this stage.


This function will emit a warning and skip each dirty anonymous layer
it encounters, since anonymous layers cannot be saved with
SdfLayer::Save. These layers must be manually exported by calling
SdfLayer::Export.

"""
   result["Stage"].UnmuteLayer.im_func.func_doc = """UnmuteLayer(layerIdentifier) -> USD_API void

layerIdentifier : string


Unmute the layer identified by C{layerIdentifier} if it had previously
been muted.

"""
   result["Stage"].HasDefaultPrim.im_func.func_doc = """HasDefaultPrim() -> USD_API bool



Return true if this stage's root layer has an authored opinion for the
default prim layer metadata.


This is shorthand for: ::

  stage->GetRootLayer()->HasDefaultPrim();

 Note that this function only consults the stage's root layer. To
consult a different layer, use the SdfLayer::HasDefaultPrim() API.

"""
   result["Stage"].Save.im_func.func_doc = """Save() -> USD_API void



Calls SdfLayer::Save on all dirty layers contributing to this stage
except session layers and sublayers of session layers.


This function will emit a warning and skip each dirty anonymous layer
it encounters, since anonymous layers cannot be saved with
SdfLayer::Save. These layers must be manually exported by calling
SdfLayer::Export.

"""
   result["Stage"].ResolveIdentifierToEditTarget.im_func.func_doc = """ResolveIdentifierToEditTarget(identifier) -> USD_API string

identifier : string


Resolve the given identifier using this stage's ArResolverContext and
the layer of its GetEditTarget() as an anchor for relative references
(e.g.


@./siblingFile.usd@).

a non-empty string containing either the same identifier that was
passed in (if the identifier refers to an already-opened layer or an
"anonymous", in-memory layer), or a resolved layer filepath. If the
identifier was not resolvable, return the empty string.

"""
   result["Stage"].GetMasters.im_func.func_doc = """GetMasters() -> USD_API sequence< UsdPrim >



Returns all master prims.

"""
   result["Stage"].GetFramesPerSecond.im_func.func_doc = """GetFramesPerSecond() -> USD_API double



Returns the stage's framesPerSecond value.


This makes an advisory statement about how the contained data can be
most usefully consumed and presented. It's primarily an indication of
the expected playback rate for the data, but a timeline editing tool
might also want to use this to decide how to scale and label its
timeline.  The default value of framesPerSecond is 24.

"""
   result["Stage"].GetMetadataByDictKey.im_func.func_doc = """GetMetadataByDictKey(key, keyPath, value) -> bool

key : TfToken
keyPath : TfToken
value : T


Resolve the requested dictionary sub-element C{keyPath} of dictionary-
valued metadatum named C{key}, returning the resolved value.


If you know you need just a small number of elements from a
dictionary, accessing them element-wise using this method can be much
less expensive than fetching the entire dictionary with
GetMetadata(key).

true if we successfully retrieved a value of the requested type; false
if C{key} is not allowed as layer metadata or no value was found.
Generates a coding error if we retrieved a stored value of a type
other than the requested type The C{keyPath} is a ':'-separated path
addressing an element in subdictionaries. If C{keyPath} is empty,
returns an empty VtValue.


----------------------------------------------------------------------
GetMetadataByDictKey(key, keyPath, value) -> USD_API bool

key : TfToken
keyPath : TfToken
value : VtValue


overload

"""
   result["Stage"].GetTimeCodesPerSecond.im_func.func_doc = """GetTimeCodesPerSecond() -> USD_API double



Returns the stage's timeCodesPerSecond value.


The timeCodesPerSecond value scales the time ordinate for the samples
contained in the stage to seconds. If timeCodesPerSecond is 24, then a
sample at time ordinate 24 should be viewed exactly one second after
the sample at time ordinate 0.

The default value of timeCodesPerSecond is 24.

"""
   result["Stage"].SetColorConfigFallbacks.func_doc = """**static** SetColorConfigFallbacks(colorConfiguration, colorManagementSystem) -> USD_API void

colorConfiguration : SdfAssetPath
colorManagementSystem : TfToken


Sets the global fallback values of color configuration metadata which
includes the 'colorConfiguration' asset path and the name of the color
management system.


This overrides any fallback values authored in plugInfo files.

If the specified value of C{colorConfiguration} or
C{colorManagementSystem} is empty, then the corresponding fallback
value isn't set. In other words, for this call to have an effect, at
least one value must be non-empty. Additionally, these can't be reset
to empty values.

GetColorConfigFallbacks() Color Configuration API

"""
   result["Stage"].SetDefaultPrim.im_func.func_doc = """SetDefaultPrim(prim) -> USD_API void

prim : Prim


Set the default prim layer metadata in this stage's root layer.


This is shorthand for: ::

  stage->GetRootLayer()->SetDefaultPrim(prim.GetName());

 Note that this function always authors to the stage's root layer. To
author to a different layer, use the SdfLayer::SetDefaultPrim() API.

"""
   result["Stage"].InitialLoadSet.__doc__ = """
Specifies the initial set of prims to load when opening a UsdStage.

"""
   result["Stage"].SetTimeCodesPerSecond.im_func.func_doc = """SetTimeCodesPerSecond(timeCodesPerSecond) -> USD_API void

timeCodesPerSecond : double


Sets the stage's timeCodesPerSecond value.


The timeCodesPerSecond value is set in the current EditTarget, if it
is the root layer of the stage or the session layer associated with
the stage. If the current EditTarget is neither, a warning is issued
and no value is set.

GetTimeCodesPerSecond()

"""
   result["Stage"].IsSupportedFile.func_doc = """**static** IsSupportedFile(filePath) -> USD_API bool

filePath : string


Indicates whether the specified file is supported by UsdStage.


This function is a cheap way to determine whether a file might be
open-able with UsdStage::Open. It is purely based on the given
C{filePath} and does not open the file or perform analysis on the
contents. As such, UsdStage::Open may still fail even if this function
returns true.

"""
   result["Stage"].GetColorManagementSystem.im_func.func_doc = """GetColorManagementSystem() -> USD_API TfToken



Sets the name of the color management system to be used for loading
and interpreting the color configuration file.


Color Configuration API

"""
   result["Stage"].GetPathResolverContext.im_func.func_doc = """GetPathResolverContext() -> USD_API ArResolverContext



Return the path resolver context for all path resolution during
composition of this stage.


Useful for external clients that want to resolve paths with the same
context as this stage, or create new stages with the same context.

"""
   result["Stage"].SetEditTarget.im_func.func_doc = """SetEditTarget(editTarget) -> USD_API void

editTarget : EditTarget


Set the stage's EditTarget.


If *editTarget.IsLocalLayer()*, check to see if it's a layer in this
stage's local LayerStack. If not, issue an error and do nothing. If
*editTarget* is invalid, issue an error and do nothing. If
*editTarget* differs from the stage's current EditTarget, set the
EditTarget and send UsdNotice::StageChangedEditTarget. Otherwise do
nothing.

"""
   result["Stage"].GetSessionLayer.im_func.func_doc = """GetSessionLayer() -> USD_API SdfLayerHandle



Return this stage's root session layer.

"""
   result["Stage"].CreateClassPrim.im_func.func_doc = """CreateClassPrim(rootPrimPath) -> USD_API UsdPrim

rootPrimPath : SdfPath


Author an *SdfPrimSpec* with *specifier* == *SdfSpecifierClass* for
the class at root prim path C{path} at the current EditTarget.


The current EditTarget must have UsdEditTarget::IsLocalLayer() ==
true.

The given *path* must be an absolute, root prim path that does not
contain any variant selections.

If a defined ( UsdPrim::IsDefined() ) non-class prim already exists at
C{path}, issue an error and return an invalid UsdPrim.

If it is impossible to author the necessary PrimSpec, issue an error
and return an invalid *UsdPrim*.

"""
   result["Stage"].ClearMetadataByDictKey.im_func.func_doc = """ClearMetadataByDictKey(key, keyPath) -> USD_API bool

key : TfToken
keyPath : TfToken


Clear any authored value identified by C{key} and C{keyPath} at the
current EditTarget.


The C{keyPath} is a ':'-separated path identifying a path in
subdictionaries stored in the metadata field at C{key}. If C{keyPath}
is empty, no action is taken.

true if the value is cleared successfully, false otherwise. Generates
a coding error if C{key} is not allowed as layer metadata.

Dictionary-valued Metadata

"""
   result["Stage"].SetInterpolationType.im_func.func_doc = """SetInterpolationType(interpolationType) -> USD_API void

interpolationType : InterpolationType


Sets the interpolation type used during value resolution for all
attributes on this stage.


Changing this will cause a UsdNotice::StageContentsChanged notice to
be sent, as values at times where no samples are authored may have
changed.

"""
   result["Stage"]._GetPcpCache.im_func.func_doc = """_GetPcpCache() -> PcpCache



----------------------------------------------------------------------
_GetPcpCache() -> PcpCache


"""
   result["Stage"].GetMutedLayers.im_func.func_doc = """GetMutedLayers() -> USD_API  sequence<string>



Returns a vector of all layers that have been muted on this stage.

"""
   result["Stage"].DefinePrim.im_func.func_doc = """DefinePrim(path, typeName) -> USD_API UsdPrim

path : SdfPath
typeName : TfToken


Attempt to ensure a *UsdPrim* at C{path} is defined (according to
UsdPrim::IsDefined() ) on this stage.


If a prim at C{path} is already defined on this stage and C{typeName}
is empty or equal to the existing prim's typeName, return that prim.
Otherwise author an *SdfPrimSpec* with *specifier* ==
*SdfSpecifierDef* and C{typeName} for the prim at C{path} at the
current EditTarget. Author *SdfPrimSpec* s with C{specifier} ==
*SdfSpecifierDef* and empty typeName at the current EditTarget for any
nonexistent, or existing but not *Defined* ancestors.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace or one of the ancestors of C{path} is inactive on the
UsdStage), issue an error and return an invalid *UsdPrim*.

Note that this method may return a defined prim whose typeName does
not match the supplied C{typeName}, in case a stronger typeName
opinion overrides the opinion at the current EditTarget.

"""
   result["Stage"].SetColorConfiguration.im_func.func_doc = """SetColorConfiguration(colorConfig) -> USD_API void

colorConfig : SdfAssetPath


Sets the default color configuration to be used to interpret the per-
attribute color-spaces in the composed USD stage.


This is specified as asset path which can be resolved to the color
spec file.

Color Configuration API

"""
   result["Stage"].GetPrimAtPath.im_func.func_doc = """GetPrimAtPath(path) -> USD_API UsdPrim

path : SdfPath


Return the UsdPrim at C{path}, or an invalid UsdPrim if none exists.


If C{path} indicates a prim beneath an instance, returns an instance
proxy prim if a prim exists at the corresponding path in that
instance's master.

Unlike OverridePrim() and DefinePrim() , this method will never author
scene description, and therefore is safe to use as a "reader" in the
Usd multi-threading model.

"""
   result["Stage"].SetGlobalVariantFallbacks.func_doc = """**static** SetGlobalVariantFallbacks(fallbacks) -> USD_API void

fallbacks : PcpVariantFallbackMap


Set the global variant fallback preferences used in new UsdStages.


This overrides any fallbacks configured in plugin metadata, and only
affects stages created after this call.

This does not affect existing UsdStages.

"""
   result["Stage"].SetMetadataByDictKey.im_func.func_doc = """SetMetadataByDictKey(key, keyPath, value) -> bool

key : TfToken
keyPath : TfToken
value : T


Author C{value} to the field identified by C{key} and C{keyPath} at
the current EditTarget.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries stored in the metadata field at C{key}. If C{keyPath}
is empty, no action is taken.

true if the value is authored successfully, false otherwise. Generates
a coding error if C{key} is not allowed as layer metadata.

Dictionary-valued Metadata


----------------------------------------------------------------------
SetMetadataByDictKey(key, keyPath, value) -> USD_API bool

key : TfToken
keyPath : TfToken
value : VtValue


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Stage"].Traverse.im_func.func_doc = """Traverse() -> USD_API UsdPrimRange



Traverse the active, loaded, defined, non-abstract prims on this stage
depth-first.


Traverse() returns a UsdPrimRange, which allows low-latency traversal,
with the ability to prune subtrees from traversal. It is python
iterable, so in its simplest form, one can do: ::

  for prim in stage.Traverse():
      print prim.GetPath()

If either a pre-and-post-order traversal or a traversal rooted at a
particular prim is desired, construct a UsdPrimRange directly.

This is equivalent to UsdPrimRange::Stage() .


----------------------------------------------------------------------
Traverse(predicate) -> USD_API UsdPrimRange

predicate : _PrimFlagsPredicate


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Traverse the prims on this stage subject to C{predicate}.


This is equivalent to UsdPrimRange::Stage() .

"""
   result["Stage"].TraverseAll.im_func.func_doc = """TraverseAll() -> USD_API UsdPrimRange



Traverse all the prims on this stage depth-first.



Traverse()

UsdPrimRange::Stage()

"""
   result["Stage"].MuteAndUnmuteLayers.im_func.func_doc = """MuteAndUnmuteLayers(muteLayers, unmuteLayers) -> USD_API void

muteLayers : sequence<string>
unmuteLayers : sequence<string>


Mute and unmute the layers identified in C{muteLayers} and
C{unmuteLayers}.


This is equivalent to calling UsdStage::UnmuteLayer for each layer in
C{unmuteLayers} followed by UsdStage::MuteLayer for each layer in
C{muteLayers}, however this method is more efficient as all operations
are committed in a single batch.

"""
   result["Stage"].Load.im_func.func_doc = """Load(path, policy) -> USD_API UsdPrim

path : SdfPath
policy : LoadPolicy


Load the prim at C{path}, its ancestors, and all of its descendants if
C{policy} is UsdLoadWithDescendants.


If C{policy} is UsdLoadWithoutDescendants, then descendants are not
loaded.

If an instance prim is encountered during this operation, this
function will also load prims in the instance's master. In other
words, loading a single instance may affect other instances because it
changes the load state of prims in the shared master. However, loading
a single instance will never cause other instances to be loaded as
well.

See the rules under Working Set Management for a discussion of what
paths are considered valid.

"""
   result["Stage"].OpenMasked.func_doc = """**static** OpenMasked(filePath, mask, load) -> USD_API UsdStageRefPtr

filePath : string
mask : StagePopulationMask
load : InitialLoadSet


Create a new stage and recursively compose prims defined within and
referenced by the layer at C{filePath} which must already exist,
subject to C{mask}.


These OpenMasked() methods do not automatically consult or populate
UsdStageCache s.

The initial set of prims to load on the stage can be specified using
the C{load} parameter.

UsdStage::InitialLoadSet. Note that the C{pathResolverContext} passed
here will apply to all path resolutions for this stage, regardless of
what other context may be bound at resolve time. If no context is
passed in here, Usd will create one by calling

ArResolver::CreateDefaultContextForAsset with the root layer's
repository path if the layer has one, otherwise its real path.


----------------------------------------------------------------------
OpenMasked(filePath, pathResolverContext, mask, load) -> USD_API UsdStageRefPtr

filePath : string
pathResolverContext : ArResolverContext
mask : StagePopulationMask
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
OpenMasked(rootLayer, mask, load) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
mask : StagePopulationMask
load : InitialLoadSet


Open a stage rooted at C{rootLayer} and with limited population
subject to C{mask}.


These OpenMasked() methods do not automatically consult or populate
UsdStageCache s.

Invoking an overload that does not take a C{sessionLayer} argument
will create a stage with an anonymous in-memory session layer. To
create a stage without a session layer, pass TfNullPtr (or None in
python) as the C{sessionLayer} argument.

The initial set of prims to load on the stage can be specified using
the C{load} parameter.

UsdStage::InitialLoadSet. Note that the C{pathResolverContext} passed
here will apply to all path resolutions for this stage, regardless of
what other context may be bound at resolve time. If no context is
passed in here, Usd will create one by calling

ArResolver::CreateDefaultContextForAsset with the root layer's
repository path if the layer has one, otherwise its real path.


----------------------------------------------------------------------
OpenMasked(rootLayer, sessionLayer, mask, load) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle
mask : StagePopulationMask
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
OpenMasked(rootLayer, pathResolverContext, mask, load) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
pathResolverContext : ArResolverContext
mask : StagePopulationMask
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
OpenMasked(rootLayer, sessionLayer, pathResolverContext, mask, load) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle
pathResolverContext : ArResolverContext
mask : StagePopulationMask
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Stage"].LoadAndUnload.im_func.func_doc = """LoadAndUnload(loadSet, unloadSet, policy) -> USD_API void

loadSet : SdfPathSet
unloadSet : SdfPathSet
policy : LoadPolicy


Unloads and loads the given path sets; the effect is as if the unload
set were processed first followed by the load set.


This is equivalent to calling UsdStage::Unload for each item in the
unloadSet followed by UsdStage::Load for each item in the loadSet,
however this method is more efficient as all operations are committed
in a single batch. The C{policy} argument is described in the
documentation for Load() .

See the rules under Working Set Management for a discussion of what
paths are considered valid.

"""
   result["Stage"].GetEditTarget.im_func.func_doc = """GetEditTarget() -> USD_API  UsdEditTarget



Return the stage's EditTarget.

"""
   result["Stage"].GetLayerStack.im_func.func_doc = """GetLayerStack(includeSessionLayers) -> USD_API SdfLayerHandleVector

includeSessionLayers : bool


Return this stage's local layers in strong-to-weak order.


If *includeSessionLayers* is true, return the linearized strong-to-
weak sublayers rooted at the stage's session layer followed by the
linearized strong-to-weak sublayers rooted at this stage's root layer.
If *includeSessionLayers* is false, omit the sublayers rooted at this
stage's session layer.

"""
   result["Stage"].HasMetadata.im_func.func_doc = """HasMetadata(key) -> USD_API bool

key : TfToken


Returns true if the *key* has a meaningful value, that is, if
GetMetadata() will provide a value, either because it was authored or
because the Stage metadata was defined with a meaningful fallback
value.


Returns false if C{key} is not allowed as layer metadata.

"""
   result["Stage"].Flatten.im_func.func_doc = """Flatten(addSourceFileComment) -> USD_API SdfLayerRefPtr

addSourceFileComment : bool


Returns a single, anonymous, merged layer for this composite scene.


Specifically, this function removes B{most} composition metadata and
authors the resolved values for each object directly into the
flattened layer.

All VariantSets are removed and only the currently selected variants
will be present in the resulting layer.

Class prims will still exist, however all inherits arcs will have been
removed and the inherited data will be copied onto each child object.
Composition arcs authored on the class itself will be flattened into
the class.

Flatten preserves scenegraph instancing by creating independent roots
for each master currently composed on this stage, and adding a single
internal reference arc on each instance prim to its corresponding
master.

Time samples across sublayer offsets will will have the time offset
and scale applied to each time index.

Finally, any deactivated prims will be pruned from the result.

"""
   result["Stage"].Open.func_doc = """**static** Open(filePath, load) -> USD_API UsdStageRefPtr

filePath : string
load : InitialLoadSet


Attempt to find a matching existing stage in a cache if
UsdStageCacheContext objects exist on the stack.


Failing that, create a new stage and recursively compose prims defined
within and referenced by the layer at C{filePath}, which must already
exist.

The initial set of prims to load on the stage can be specified using
the C{load} parameter.

UsdStage::InitialLoadSet. Note that the C{pathResolverContext} passed
here will apply to all path resolutions for this stage, regardless of
what other context may be bound at resolve time. If no context is
passed in here, Usd will create one by calling

ArResolver::CreateDefaultContextForAsset with the root layer's
repository path if the layer has one, otherwise its real path.


----------------------------------------------------------------------
Open(filePath, pathResolverContext, load) -> USD_API UsdStageRefPtr

filePath : string
pathResolverContext : ArResolverContext
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
Open(rootLayer, load) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
load : InitialLoadSet


Open a stage rooted at C{rootLayer}.


Attempt to find a stage that matches the passed arguments in a
UsdStageCache if UsdStageCacheContext objects exist on the calling
stack. If a matching stage is found, return that stage. Otherwise,
create a new stage rooted at C{rootLayer}.

Invoking an overload that does not take a C{sessionLayer} argument
will create a stage with an anonymous in-memory session layer. To
create a stage without a session layer, pass TfNullPtr (or None in
python) as the C{sessionLayer} argument.

The initial set of prims to load on the stage can be specified using
the C{load} parameter.

UsdStage::InitialLoadSet. Note that the C{pathResolverContext} passed
here will apply to all path resolutions for this stage, regardless of
what other context may be bound at resolve time. If no context is
passed in here, Usd will create one by calling

ArResolver::CreateDefaultContextForAsset with the root layer's
repository path if the layer has one, otherwise its real path. When
searching for a matching stage in bound UsdStageCache s, only the
provided arguments matter for cache lookup. For example, if only a
root layer (or a root layer file path) is provided, the first stage
found in any cache that has that root layer is returned. So, for
example if you require that the stage have no session layer, you must
explicitly specify TfNullPtr (or None in python) for the sessionLayer
argument.


----------------------------------------------------------------------
Open(rootLayer, sessionLayer, load) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
Open(rootLayer, pathResolverContext, load) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
pathResolverContext : ArResolverContext
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
Open(rootLayer, sessionLayer, pathResolverContext, load) -> USD_API UsdStageRefPtr

rootLayer : SdfLayerHandle
sessionLayer : SdfLayerHandle
pathResolverContext : ArResolverContext
load : InitialLoadSet


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Stage"].GetRootLayer.im_func.func_doc = """GetRootLayer() -> USD_API SdfLayerHandle



Return this stage's root layer.

"""
   result["Stage"].SetStartTimeCode.im_func.func_doc = """SetStartTimeCode(arg1) -> USD_API void

arg1 : double


Sets the stage's start timeCode.


The start timeCode is set in the current EditTarget, if it is the root
layer of the stage or the session layer associated with the stage. If
the current EditTarget is neither, a warning is issued and the start
timeCode is not set.

"""
   result["Stage"].SetEndTimeCode.im_func.func_doc = """SetEndTimeCode(arg1) -> USD_API void

arg1 : double


Sets the stage's end timeCode.


The end timeCode is set in the current EditTarget, if it is the root
layer of the stage or the session layer associated with the stage. If
the current EditTarget is neither, a warning is issued and the end
timeCode is not set.

"""
   result["Stage"].FindLoadable.im_func.func_doc = """FindLoadable(rootPath) -> USD_API SdfPathSet

rootPath : SdfPath


Returns an SdfPathSet of all paths that can be loaded.


Note that this method does not return paths to inactive prims as they
cannot be loaded.

The set returned includes loaded and unloaded paths. To determine the
set of unloaded paths, one can diff this set with the current load
set, for example: ::

  SdfPathSet loaded = stage->GetLoadSet(),
             all = stage->FindLoadable(),
             result;
  std::set_difference(loaded.begin(), loaded.end(),
                      all.begin(), all.end(),
                      std::inserter(result, result.end()));


"""
   result["Stage"].GetPseudoRoot.im_func.func_doc = """GetPseudoRoot() -> USD_API UsdPrim



Return the stage's "pseudo-root" prim, whose name is defined by Usd.


The stage's named root prims are namespace children of this prim,
which exists to make the namespace hierarchy a tree instead of a
forest. This simplifies algorithms that want to traverse all prims.

A UsdStage always has a pseudo-root prim, unless there was an error
opening or creating the stage, in which case this method returns an
invalid UsdPrim.

"""
   result["Stage"].GetObjectAtPath.im_func.func_doc = """GetObjectAtPath(path) -> USD_API UsdObject

path : SdfPath


Return the UsdObject at C{path}, or an invalid UsdObject if none
exists.


If C{path} indicates a prim beneath an instance, returns an instance
proxy prim if a prim exists at the corresponding path in that
instance's master. If C{path} indicates a property beneath a child of
an instance, returns a property whose parent prim is an instance proxy
prim.

Example: ::

  if (UsdObject obj = stage->GetObjectAtPath(path)) {
      if (UsdPrim prim = obj.As<UsdPrim>()) {
          // Do things with prim
      }
      else if (UsdProperty prop = obj.As<UsdProperty>()) {
          // Do things with property. We can also cast to
          // UsdRelationship or UsdAttribute using this same pattern.
      }
  }
  else {
      // No object at specified path
  }


"""
   result["Stage"].GetStartTimeCode.im_func.func_doc = """GetStartTimeCode() -> USD_API double



Returns the stage's start timeCode.


If the stage has an associated session layer with a start timeCode
opinion, this value is returned. Otherwise, the start timeCode opinion
from the root layer is returned.

"""
   result["Stage"].GetLoadSet.im_func.func_doc = """GetLoadSet() -> USD_API SdfPathSet



Returns a set of all loaded paths.


The paths returned are both those that have been explicitly loaded and
those that were loaded as a result of dependencies, ancestors or
descendants of explicitly loaded paths.

This method does not return paths to inactive prims.

"""
   result["Stage"].GetPopulationMask.im_func.func_doc = """GetPopulationMask() -> StagePopulationMask



Return this stage's population mask.

"""
   result["Stage"].HasAuthoredMetadata.im_func.func_doc = """HasAuthoredMetadata(key) -> USD_API bool

key : TfToken


Returns C{true} if the *key* has an authored value, C{false} if no
value was authored or the only value available is the SdfSchema 's
metadata fallback.



If a value for a metadatum *not* legal to author on layers is present
in the root or session layer (which could happen through hand-editing
or use of certain low-level API's), this method will still return
C{false}.

"""
   result["Stage"].GetColorConfiguration.im_func.func_doc = """GetColorConfiguration() -> USD_API SdfAssetPath



Returns the default color configuration used to interpret the per-
attribute color-spaces in the composed USD stage.


Color Configuration API

"""
   result["Stage"].ClearMetadata.im_func.func_doc = """ClearMetadata(key) -> USD_API bool

key : TfToken


Clear the value of stage metadatum C{key}, if the stage's current
UsdEditTarget is the root or session layer.


If the current EditTarget is any other layer, raise a coding error.

true if authoring was successful, false otherwise. Generates a coding
error if C{key} is not allowed as layer metadata.

General Metadata in USD

"""
   result["Stage"].GetUsedLayers.im_func.func_doc = """GetUsedLayers(includeClipLayers) -> USD_API SdfLayerHandleVector

includeClipLayers : bool


Return a vector of all of the layers *currently* consumed by this
stage, as determined by the composition arcs that were traversed to
compose and populate the stage.


The list of consumed layers will change with the stage's load-set and
variant selections, so the return value should be considered only a
snapshot. The return value will include the stage's session layer, if
it has one. If *includeClipLayers* is true, we will also include all
of the layers that this stage has had to open so far to perform value
resolution of attributes affected by Value Clips

"""
   result["Stage"].MuteLayer.im_func.func_doc = """MuteLayer(layerIdentifier) -> USD_API void

layerIdentifier : string


Mute the layer identified by C{layerIdentifier}.


Muted layers are ignored by the stage; they do not participate in
value resolution or composition and do not appear in any LayerStack.
If the root layer of a reference or payload LayerStack is muted, the
behavior is as if the muted layer did not exist, which means a
composition error will be generated.

A canonical identifier for C{layerIdentifier} will be computed using
ArResolver::ComputeRepositoryPath. Any layer encountered during
composition with the same repository path will be considered muted and
ignored. Relative paths will be assumed to be relative to the cache's
root layer. Search paths are immediately resolved and the result is
used for computing the canonical path.

Note that muting a layer will cause this stage to release all
references to that layer. If no other client is holding on to
references to that layer, it will be unloaded. In this case, if there
are unsaved edits to the muted layer, those edits are lost.  Since
anonymous layers are not serialized, muting an anonymous layer will
cause that layer and its contents to be lost in this case.

Muting a layer that has not been used by this stage is not an error.
If that layer is encountered later, muting will take effect and that
layer will be ignored.  The root layer of this stage may not be muted;
attempting to do so will generate a coding error.

"""
   result["Stage"].Reload.im_func.func_doc = """Reload() -> USD_API void



Calls SdfLayer::Reload on all layers contributing to this stage,
except session layers and sublayers of session layers.


This includes non-session sublayers, references and payloads. Note
that reloading anonymous layers clears their content, so invoking
Reload() on a stage constructed via CreateInMemory() will clear its
root layer.

This method is considered a mutation, which has potentially global
effect! Unlike the various Load() methods whose actions affect only
B{this stage}, Reload() may cause layers to change their contents, and
because layers are global resources shared by potentially many Stages,
calling Reload() on one stage may result in a mutation to any number
of stages. In general, unless you are highly confident your stage is
the only consumer of its layers, you should only call Reload() when
you are assured no other threads may be reading from any Stages.

"""
   result["Stage"].Export.im_func.func_doc = """Export(filename, addSourceFileComment, args) -> USD_API bool

filename : string
addSourceFileComment : bool
args : SdfLayer.FileFormatArguments


Writes out the composite scene as a single flattened layer into
*filename*.


If addSourceFileComment is true, a comment in the output layer will
mention the input layer it was generated from.

See UsdStage::Flatten for details of the flattening transformation.

"""
   result["Stage"].GetInterpolationType.im_func.func_doc = """GetInterpolationType() -> USD_API UsdInterpolationType



Returns the interpolation type used during value resolution for all
attributes on this stage.

"""
   result["Stage"].OverridePrim.im_func.func_doc = """OverridePrim(path) -> USD_API UsdPrim

path : SdfPath


Attempt to ensure a *UsdPrim* at C{path} exists on this stage.


If a prim already exists at C{path}, return it. Otherwise author
*SdfPrimSpecs* with *specifier* == *SdfSpecifierOver* and empty
*typeName* at the current EditTarget to create this prim and any
nonexistent ancestors, then return it.

The given *path* must be an absolute prim path that does not contain
any variant selections.

If it is impossible to author any of the necessary PrimSpecs, (for
example, in case *path* cannot map to the current UsdEditTarget 's
namespace) issue an error and return an invalid *UsdPrim*.

If an ancestor of C{path} identifies an *inactive* prim, author scene
description as described above but return an invalid prim, since the
resulting prim is descendant to an inactive prim.

"""
   result["Stage"].SetColorManagementSystem.im_func.func_doc = """SetColorManagementSystem(cms) -> USD_API void

cms : TfToken


Sets the name of the color management system used to interpret the
color configuration file pointed at by the colorConfiguration
metadata.


Color Configuration API

"""
   result["SchemaType"].__doc__ = """
An enum representing which type of schema a given schema class belongs
to.

"""
   result["_Term"].__doc__ = """"""
   result["InterpolationType"].__doc__ = """
Attribute value interpolation options.


See Attribute Value Interpolation for more details.

"""
   result["CollectionAPI"].__doc__ = """
This is a general purpose API schema, used to describe a collection of
heterogeneous objects within the scene.


"Objects" here may be prims or properties belonging to prims or other
collections. It's an add-on schema that can be applied many times to a
prim with different collection names.

A collection allows an enumeration of a set of paths to include and a
set of paths to exclude. Whether the descendants of an included path
are members of a collection are decided by its expansion rule (see
below). If the collection excludes paths that are not descendents of
included paths, the collection implicitly includes the root path</>.
If such a collection also includes paths that are not descendants of
the excluded paths, it is considered invalid, since the intention is
ambiguous.

All the properties authored by the schema are namespaced under
"collection:". The given name of the collection provides additional
namespacing for the various per-collection properties, which include
the following:

   - B{uniform token collection: *collectionName* :expansionRule} -
     specified how the paths that are included in the collection must be
     expanded to determine its members. Possible values include:
   - B{explicitOnly} - only paths in the includes rel targets and not
     in the excludes rel targets belong to the collection.

   - B{expandPrims} - all the prims at or below the includes rel-
     targets (and not under the excludes rel-targets) belong to the
     collection. Any property paths included in the collection would, of
     course, also be honored. This is the default behavior as it satisfies
     most use cases.

   - B{expandPrimsAndProperties} - like expandPrims, but also includes
     all properties on all matched prims. We're still not quite sure what
     the use cases are for this, but you can use it to capture a whole lot
     of UsdObjects very concisely.

   - B{rel collection: *collectionName* :includeRoot} - boolean
     attribute indicating whether the pseudo-root path</>should be counted
     as one of the included target paths. The fallback is false. This
     separate attribute is required because relationships cannot directly
     target the root.

   - B{rel collection: *collectionName* :includes} - specifies a list
     of targets that are included in the collection. This can target prims
     or properties directly. A collection can insert the rules of another
     collection by making its *includes* relationship target the
     B{collection:{collectionName}} property on the owning prim of the
     collection to be included. Such a property may not (and typically does
     not) exist on the UsdStage, but it is the path that is used to refer
     to the collection. It is important to note that including another
     collection does not guarantee the contents of that collection will be
     in the final collection; instead, the rules are merged. This means,
     for example, an exclude entry may exclude a portion of the included
     collection. When a collection includes one or more collections, the
     order in which targets are added to the includes relationship may
     become significant, if there are conflicting opinions about the same
     path. Targets that are added later are considered to be stronger than
     earlier targets for the same path.

   - B{rel collection: *collectionName* :excludes} - specifies a list
     of targets that are excluded below the B{included} paths in this
     collection. This can target prims or properties directly, but B{cannot
     target another collection}. This is to keep the membership determining
     logic simple, efficient and easier to reason about. Finally, it is
     invalid for a collection to exclude paths that are not included in it.
     The presence of such "orphaned" excluded paths will not affect the set
     of paths included in the collection, but may affect the performance of
     querying membership of a path in the collection (see
     UsdCollectionAPI::MembershipQuery::IsPathIncluded) or of enumerating
     the objects belonging to the collection (see
     UsdCollectionAPI::GetIncludedObjects).

B{Implicit inclusion}

In some scenarios it is useful to express a collection that includes
everything except certain paths. To support this, a collection that
has an exclude that is not a descendent of any include will include
the root path</>.

B{Creating collections in C++} ::

  bool ApplyCollections(UsdPrim const  & prim)
  {       
      /* Assuming the folling prim hierarchy:
      |- Vehicles 
      |    |- FourWheelers
      |    |    |- CarA
      |    |    |- CarB
      |    |    |- CarC
      |    |    |- CarD
      |    |    |- TruckA
      |    |    |- TruckB
      |    |- TwoWheelers
      |    |    |- BikeA
      |    |    |- BikeB
      |    |    |- BicycleA
      |    |        |- FrontWheel
      |    |        |- BackWheel
      |    |- Other
      |    |    |- TricycleA
      |    |        |- FrontWheel
      |    |        |- BackWheels
      */
  
      // Create a collection that includes only the cars, by adding all 
      // of "FourWheelers" and excluding the trucks.
      UsdCollectionAPI cars = UsdCollectionAPI::ApplyCollection(
          prim, "cars", /* expansionRule */ UsdTokens->expandPrims);
      cars.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers"));
      cars.CreateExcludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers/TruckA"));
      cars.CreateExcludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers/TruckB"));
  
      // Create a collection that includes only the bikes by explicitly inluding 
      // just the two bikes in the collection.
      UsdCollectionAPI bikes = UsdCollectionAPI::ApplyCollection(
          prim, "bikes", /* expansionRule */ UsdTokens->explicitOnly);
      bikes.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/TwoWheelers/BikeA"));
      bikes.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/TwoWheelers/BikeB"));
  
      
// Create an explicit collection of slow-
moving vehicles. 
      // An explicit collection implies that descendants (i.e. the front and back 
      // wheels) are not considered to be included in the collection.
      UsdCollectionAPI slowVehicles = UsdCollectionAPI::ApplyCollection(prim, 
          "slowVehicles", /* expansionRule */ UsdTokens->explicitOnly);
      slowVehicles.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/TwoWheelers/BicycleA"));
      slowVehicles.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/Other/TricycleA"));
  
      UsdCollectionAPI vehicles = UsdCollectionAPI::ApplyCollection(prim, 
          "vehicles", /* expansionRule */ UsdTokens->expandPrims);
      vehicles.CreateIncludesRel().AddTarget(cars.GetCollectionPath());
      vehicles.CreateIncludesRel().AddTarget(bikes.GetCollectionPath());
      vehicles.CreateIncludesRel().AddTarget(slowVehicles.GetCollectionPath());
      vehicles.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers/TruckA"));
      vehicles.CreateIncludesRel().AddTarget(SdfPath("/Vehicles/FourWheelers/TruckB"));
  
  
      UsdCollectionAPI::MembershipQuery query = vehicles.ComputeMembershipQuery();
  
      // CarA is included in the 'vehicles' collection through the 'cars' collection.
      assert(query.IsPathIncluded("/Vehicles/FourWheelers/CarA"))
  
      // BikeB is included in the 'vehicles' collection through the 'cars' collection.
      assert(query.IsPathIncluded("/Vehicles/TwoWheelers/BikeB"))
  
      // BikeB is included directly in the 'vehicles' collection 
      assert(query.IsPathIncluded("/Vehicles/FourWheelers/TruckA"))
  
      // BicycleA is included, but it's descendants are not, since it is part of 
      // an "explicitOnly" collection.
      assert(query.IsPathIncluded("/Vehicles/TwoWheelers/BicycleA"))
      assert(!query.IsPathIncluded("/Vehicles/TwoWheelers/BicycleA/FrontWheel"))
  
      // TricycleA is included, but it's descendants are not, since it is part of 
      // an "explicitOnly" collection.
      assert(query.IsPathIncluded("/Vehicles/Other/TricycleA"))
      assert(!query.IsPathIncluded("/Vehicles/Other/TricycleA/BackWheels"))
  
      SdfPathSet includedPaths;
      UsdCollectionAPI::ComputeIncludedPaths(query, prim.GetStage(), 
                                             
&
includedPaths);
      std::set<UsdObject> includedObjects;
      UsdCollectionAPI::ComputeIncludedObjects(query, prim.GetStage(), 
                                                & includedObjects);
  }
  

For any described attribute *Fallback* *Value* or *Allowed* *Values*
below that are text/tokens, the actual token is published and defined
in UsdTokens. So to set an attribute to the value "rightHanded", use
UsdTokens->rightHanded as the value.

"""
   result["CollectionAPI"].CreateExcludesRel.im_func.func_doc = """CreateExcludesRel() -> USD_API UsdRelationship



See GetExcludesRel() , and also Create vs Get Property Methods for
when to use Get vs Create.

"""
   result["CollectionAPI"].GetExcludesRel.im_func.func_doc = """GetExcludesRel() -> USD_API UsdRelationship



Specifies a list of targets that are excluded below the included paths
in this collection.


This can target prims or properties directly, but cannot target
another collection. This is to keep the membership determining logic
simple, efficient and easier to reason about. Finally, it is invalid
for a collection to exclude paths that are not included in it. The
presence of such "orphaned" excluded paths will not affect the set of
paths included in the collection, but may affect the performance of
querying membership of a path in the collection (see
UsdCollectionAPI::MembershipQuery::IsPathIncluded) or of enumerating
the objects belonging to the collection (see
UsdCollectionAPI::GetIncludedObjects).

"""
   result["CollectionAPI"].BlockCollection.im_func.func_doc = """BlockCollection() -> USD_API bool



Blocks the targets of the includes and excludes relationships of the
collection, making it<* *empty* if "includeRoot" is false (or unset)
or.



   - *include everything* if "includeRoot" is true. (assuming there
     are no opinions in stronger edit targets).


"""
   result["CollectionAPI"].CreateIncludesRel.im_func.func_doc = """CreateIncludesRel() -> USD_API UsdRelationship



See GetIncludesRel() , and also Create vs Get Property Methods for
when to use Get vs Create.

"""
   result["CollectionAPI"].GetCollectionPath.im_func.func_doc = """GetCollectionPath() -> USD_API SdfPath



Returns the canonical path that represents this collection.


This points to a property named "collection:{collectionName}" on the
prim defining the collection (which won't really exist as a property
on the UsdStage, but will be used to refer to the collection). This is
the path to be used to "include" this collection in another
collection.

"""
   result["CollectionAPI"].GetAllCollections.func_doc = """**static** GetAllCollections(prim) -> USD_API sequence< UsdCollectionAPI >

prim : Prim


Returns all the named collections on the given USD prim.

"""
   result["CollectionAPI"].ApplyCollection.func_doc = """**static** ApplyCollection(prim, name, expansionRule) -> USD_API UsdCollectionAPI

prim : Prim
name : TfToken
expansionRule : TfToken


Adds a new collection named C{name} on the given prim, C{prim} with
the specified expansion-rule, C{expansionRule}.


If a collection named C{name} already exists, its expansion-rule is
updated with the provided value and it is returned.

The name of a collection, C{name} may itself be namespaced, to
facilitate organization of collections into groups. However, the base-
name of a collection (i.e. the last component of the collection name)
should not be the same as one of the core collection schema
properties, i.e. should not be 'expansionRule' or 'includes' or
'excludes'.

"""
   result["CollectionAPI"].ExcludePath.im_func.func_doc = """ExcludePath(pathToExclude) -> USD_API bool

pathToExclude : SdfPath


Excludes or removes the given path, C{pathToExclude} from the
collection.


If the collection is empty, the collection becomes one that includes
all paths except the givne path. Otherwise, this does nothing if the
path is not included in the collection.

This does not modify the expansion-rule of the collection. Hence, if
the expansionRule is *expandPrims* or *expandPrimsAndProperties*, then
the descendants of C{pathToExclude} will also be excluded from the
collection, unless explicitly included.

UsdCollectionAPI::IncludePath()

"""
   result["CollectionAPI"].ResetCollection.im_func.func_doc = """ResetCollection() -> USD_API bool



Resets the collection by clearing both the includes and excludes
targets of the collection in the current UsdEditTarget.



This does not modify the "includeRoot" attribute which is used to
include or exclude everything (i.e. the pseudoRoot) in the USD stage.

"""
   result["CollectionAPI"].Get.func_doc = """**static** Get(stage, path) -> USD_API UsdCollectionAPI

stage : StagePtr
path : SdfPath


Return a UsdCollectionAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object.
C{path} must be of the format<path>.collection:name.

This is shorthand for the following: ::

  TfToken name = SdfPath::StripNamespace(path.GetToken());
  UsdCollectionAPI(
      stage->GetPrimAtPath(path.GetPrimPath()), name);



----------------------------------------------------------------------
Get(prim, name) -> USD_API UsdCollectionAPI

prim : Prim
name : TfToken


Return a UsdCollectionAPI with name C{name} holding the prim C{prim}.


Shorthand for UsdCollectionAPI(prim, name);

"""
   result["CollectionAPI"].GetIncludeRootAttr.im_func.func_doc = """GetIncludeRootAttr() -> USD_API UsdAttribute



Boolean attribute indicating whether the pseudo-root path</>should be
counted as one of the included target paths.


The fallback is false. This separate attribute is required because
relationships cannot directly target the root.

C++ Type: bool  Usd Type: SdfValueTypeNames->Bool  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["CollectionAPI"].GetCollection.func_doc = """**static** GetCollection(stage, collectionPath) -> USD_API UsdCollectionAPI

stage : StagePtr
collectionPath : SdfPath


Returns the collection represented by the given collection path,
C{collectionPath} on the given USD stage.


----------------------------------------------------------------------
GetCollection(prim, name) -> USD_API UsdCollectionAPI

prim : Prim
name : TfToken


Returns the schema object representing a collection named C{name} on
the given C{prim}.

"""
   result["CollectionAPI"].ComputeIncludedObjects.func_doc = """**static** ComputeIncludedObjects(query, stage, pred) -> USD_API set< UsdObject >

query : MembershipQuery
stage : StageWeakPtr
pred : _PrimFlagsPredicate


Returns all the usd objects that satisfy the predicate, C{pred} in the
collection represented by the MembershipQuery object, C{query}.


The results depends on the load state of the UsdStage, C{stage}.

"""
   result["CollectionAPI"].Validate.im_func.func_doc = """Validate(reason) -> USD_API bool

reason : string


Validates the collection by checking the following rules:



   - a collection's expansionRule should be one of "explicitOnly",
     "expandPrims" or "expandPrimsAndProperties".

   - a collection should not have have a circular dependency on
     another collection.

   - a collection should not have both includes and excludes among its
     top-level rules


"""
   result["CollectionAPI"].IsCollectionAPIPath.func_doc = """**static** IsCollectionAPIPath(path, name) -> USD_API bool

path : SdfPath
name : TfToken


Checks if the given path C{path} is an attribute of an API schema of
type CollectionAPI.


If so, it stores the instance name of the schema in C{name} and
returns true. Otherwise, it returns false.

"""
   result["CollectionAPI"].GetName.im_func.func_doc = """GetName() -> TfToken



Returns the name of this multiple-apply schema instance.

"""
   result["CollectionAPI"].GetIncludesRel.im_func.func_doc = """GetIncludesRel() -> USD_API UsdRelationship



Specifies a list of targets that are included in the collection.


This can target prims or properties directly. A collection can insert
the rules of another collection by making its *includes* relationship
target the B{collection:{collectionName}} property on the owning prim
of the collection to be included

"""
   result["CollectionAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited, instanceName) -> USD_API  TfTokenVector

includeInherited : bool
instanceName : TfToken


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes for a given instance name.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved. The names returned will have the
proper namespace prefix.

"""
   result["CollectionAPI"].MembershipQuery.__doc__ = """
Represents a flattened view of a collection.


An object of this class is computed by calling
UsdCollectionAPI::ComputeMembershipQuery() on a collection. It can be
used to answer queries about membership of paths in the collection
efficiently.

"""
   result["CollectionAPI"].MembershipQuery.HasExcludes.im_func.func_doc = """HasExcludes() -> bool



Returns true if the collection excludes one or more paths below an
included path.

"""
   result["CollectionAPI"].MembershipQuery.IsPathIncluded.im_func.func_doc = """IsPathIncluded(path, expansionRule) -> USD_API bool

path : SdfPath
expansionRule : TfToken


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Returns whether the given path is included in the collection from
which this MembershipQuery object was computed.


This is the API that clients should use for determining if a given
object is a member of the collection. To enumerate all the members of
a collection, use UsdCollectionAPI::ComputeIncludedObjects or
UsdCollectionAPI::ComputeIncludedPaths.

If C{expansionRule} is not None, it is set to the expansion- rule
value that caused the path to be included in or excluded from the
collection. If C{path} is not included in the collection,
C{expansionRule} is set to UsdTokens->exclude.

It is useful to specify this parameter and use this overload of
IsPathIncluded() , when you're interested in traversing a subtree and
want to know whether the root of the subtree is included in a
collection. For evaluating membership of descendants of the root,
please use the other overload of IsPathIncluded() , that takes both a
path and the parent expansionRule.

The python version of this method only returns the boolean result. It
does not return C{expansionRule}.


----------------------------------------------------------------------
IsPathIncluded(path, parentExpansionRule, expansionRule) -> USD_API bool

path : SdfPath
parentExpansionRule : TfToken
expansionRule : TfToken


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Returns whether the given path, C{path} is included in the collection
from which this MembershipQuery object was computed, given the parent-
path's inherited expansion rule, C{parentExpansionRule}.


If C{expansionRule} is not None, it is set to the expansion- rule
value that caused the path to be included in or excluded from the
collection. If C{path} is not included in the collection,
C{expansionRule} is set to UsdTokens->exclude.

The python version of this method only returns the boolean result. It
does not return C{expansionRule}.

"""
   result["CollectionAPI"].MembershipQuery.__init__.im_func.func_doc = """__init__()



Default Constructor, creates an empty MembershipQuery object for
passing into UsdCollectionAPI::ComputeMembershipQuery() via a pointer.

"""
   result["CollectionAPI"].MembershipQuery.GetAsPathExpansionRuleMap.im_func.func_doc = """GetAsPathExpansionRuleMap() -> USD_API PathExpansionRuleMap



Returns a raw map of the paths included or excluded in the collection
along with the expansion rules for the included paths.

"""
   result["CollectionAPI"].__init__.im_func.func_doc = """__init__(prim, name)

prim : Prim
name : TfToken


Construct a UsdCollectionAPI on UsdPrim C{prim} with name C{name}.


Equivalent to UsdCollectionAPI::Get ( prim.GetStage(),
prim.GetPath().AppendProperty( "collection:name"));

for a *valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj, name)

schemaObj : SchemaBase
name : TfToken


Construct a UsdCollectionAPI on the prim held by C{schemaObj} with
name C{name}.


Should be preferred over UsdCollectionAPI (schemaObj.GetPrim(), name),
as it preserves SchemaBase state.

"""
   result["CollectionAPI"].ComputeMembershipQuery.im_func.func_doc = """ComputeMembershipQuery() -> USD_API MembershipQuery



Computes and returns a MembershipQuery object which can be used to
query inclusion or exclusion of paths in the collection.


----------------------------------------------------------------------
ComputeMembershipQuery(query) -> USD_API void

query : MembershipQuery


Populates the MembershipQuery object with data from this collection,
so it can be used to query inclusion or exclusion of paths.

"""
   result["CollectionAPI"].IsSchemaPropertyBaseName.func_doc = """**static** IsSchemaPropertyBaseName(baseName) -> USD_API bool

baseName : TfToken


Checks if the given name C{baseName} is the base name of a property of
CollectionAPI.

"""
   result["CollectionAPI"].HasNoIncludedPaths.im_func.func_doc = """HasNoIncludedPaths() -> USD_API bool



Returns true if the collection has nothing included in it.


This requires both that the includes relationship have no target
paths, and that the includeRoot attribute be false. Note that there
may be cases where the collection has no objects included in it even
when HasNoIncludedPaths() returns false. For example, if the included
objects are unloaded or if the included objects are also excluded.

"""
   result["CollectionAPI"].CreateExpansionRuleAttr.im_func.func_doc = """CreateExpansionRuleAttr(defaultValue, writeSparsely) -> USD_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetExpansionRuleAttr() , and also Create vs Get Property Methods
for when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["CollectionAPI"].GetExpansionRuleAttr.im_func.func_doc = """GetExpansionRuleAttr() -> USD_API UsdAttribute



Specifies how the paths that are included in the collection must be
expanded to determine its members.


C++ Type: TfToken  Usd Type: SdfValueTypeNames->Token  Variability:
SdfVariabilityUniform  Fallback Value: No Fallback

"""
   result["CollectionAPI"].CreateIncludeRootAttr.im_func.func_doc = """CreateIncludeRootAttr(defaultValue, writeSparsely) -> USD_API UsdAttribute

defaultValue : VtValue
writeSparsely : bool


See GetIncludeRootAttr() , and also Create vs Get Property Methods for
when to use Get vs Create.


If specified, author C{defaultValue} as the attribute's default,
sparsely (when it makes sense to do so) if C{writeSparsely} is C{true}
- the default for C{writeSparsely} is C{false}.

"""
   result["CollectionAPI"].ComputeIncludedPaths.func_doc = """**static** ComputeIncludedPaths(query, stage, pred) -> USD_API SdfPathSet

query : MembershipQuery
stage : StageWeakPtr
pred : _PrimFlagsPredicate


Returns all the paths that satisfy the predicate, C{pred} in the
collection represented by the MembershipQuery object, C{query}.


The result depends on the load state of the UsdStage, C{stage}.

"""
   result["CollectionAPI"].IncludePath.im_func.func_doc = """IncludePath(pathToInclude) -> USD_API bool

pathToInclude : SdfPath


Includes or adds the given path, C{pathToInclude} in the collection.


This does nothing if the path is already included in the collection.

This does not modify the expansion-rule of the collection. Hence, if
the expansionRule is *expandPrims* or *expandPrimsAndProperties*, then
the descendants of C{pathToInclude} will be also included in the
collection unless explicitly excluded.

UsdCollectionAPI::ExcludePath()

"""
   result["CollectionAPI"].GetNamedCollectionPath.func_doc = """**static** GetNamedCollectionPath(prim, collectionName) -> USD_API SdfPath

prim : Prim
collectionName : TfToken


Returns the canonical path to the collection named, C{name} on the
given prim, C{prim}.



GetCollectionPath()

"""
   result["CollectionAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USD_API  TfType


"""
   result["Inherits"].__doc__ = """
A proxy class for applying listOp edits to the inherit paths list for
a prim.


All paths passed to the UsdInherits API are expected to be in the
namespace of the owning prim's stage. Local inherit paths (i.e., non-
root prim paths) will be translated from this namespace to the
namespace of the current edit target, if necessary. If a path cannot
be translated, a coding error will be issued and no changes will be
made. Global inherit paths (i.e., root prim paths) will not be
translated.

"""
   result["Inherits"].GetAllDirectInherits.im_func.func_doc = """GetAllDirectInherits() -> USD_API SdfPathVector



Return all the paths in this prim's stage's local layer stack that
would compose into this prim via direct inherits (excluding prim specs
that would be composed into this prim due to inherits authored on
ancestral prims) in strong-to-weak order.


Note that there currently may not be any scene description at these
paths on the stage. This returns all the potential places that such
opinions could appear.

"""
   result["Inherits"].ClearInherits.im_func.func_doc = """ClearInherits() -> USD_API bool



Removes the authored inheritPaths listOp edits at the current edit
target.

"""
   result["Inherits"].AddInherit.im_func.func_doc = """AddInherit(primPath, position) -> USD_API bool

primPath : SdfPath
position : ListPosition


Adds a path to the inheritPaths listOp at the current EditTarget, in
the position specified by C{position}.

"""
   result["Inherits"].RemoveInherit.im_func.func_doc = """RemoveInherit(primPath) -> USD_API bool

primPath : SdfPath


Removes the specified path from the inheritPaths listOp at the current
EditTarget.

"""
   result["Inherits"].SetInherits.im_func.func_doc = """SetInherits(items) -> USD_API bool

items : SdfPathVector


Explicitly set the inherited paths, potentially blocking weaker
opinions that add or remove items, returning true on success, false if
the edit could not be performed.

"""
   result["Inherits"].GetPrim.im_func.func_doc = """GetPrim() -> Prim



Return the prim this object is bound to.


----------------------------------------------------------------------
GetPrim() -> Prim


"""
   result["SchemaRegistry"].__doc__ = """
Singleton registry that provides access to prim and property
definition information for registered Usd "IsA" schema types.


The data contained herein comes from the processed (by *usdGenSchema*)
schema.usda files of each schema-defining module. The data is returned
in the form of SdfSpec 's of the appropriate subtype.

It is used by the Usd core to determine how to create scene
description for un-instantiated "builtin" properties of schema
classes, and also to enumerate all properties for a given schema
class, and finally to provide fallback values for unauthored builtin
properties.

"""
   result["SchemaRegistry"].GetPropertyDefinition.func_doc = """**static** GetPropertyDefinition(primType, propName) -> USD_API SdfPropertySpecHandle

primType : TfToken
propName : TfToken


Return the property spec that defines the fallback for the property
named *propName* on prims of type *primType*.


Return null if there is no such property definition.

"""
   result["SchemaRegistry"].GetPrimDefinition.func_doc = """**static** GetPrimDefinition(primType) -> USD_API SdfPrimSpecHandle

primType : TfToken


Return the PrimSpec that contains all the builtin metadata and
properties for the given *primType*.


Return null if there is no such prim definition.


----------------------------------------------------------------------
GetPrimDefinition(primType) -> USD_API SdfPrimSpecHandle

primType : TfType


Return the PrimSpec that contains all the bulitin metadata and
properties for the given *primType*.


Return null if there is no such prim definition.


----------------------------------------------------------------------
GetPrimDefinition() -> SdfPrimSpecHandle



Return the PrimSpec that contains all the builtin metadata and
properties for the given C{SchemaType}.


Return null if there is no such prim definition.

"""
   result["SchemaRegistry"].GetAttributeDefinition.func_doc = """**static** GetAttributeDefinition(primType, attrName) -> USD_API SdfAttributeSpecHandle

primType : TfToken
attrName : TfToken


This is a convenience method.


It is shorthand for TfDynamic_cast<SdfAttributeSpecHandle>(
GetPropertyDefinition(primType, attrName));

"""
   result["SchemaRegistry"].IsConcrete.func_doc = """**static** IsConcrete(primType) -> USD_API bool

primType : TfType


Returns true if the prim type C{primType} is instantiable in scene
description.

"""
   result["SchemaRegistry"].GetDisallowedFields.func_doc = """**static** GetDisallowedFields() -> USD_API sequence< TfToken >



Returns list of fields that cannot have fallback values specified in
schemas.


Fields are generally in this list because their fallback values aren't
used. For instance, fallback values for composition arcs aren't used
during composition, so allowing them to be set in schemas would be
misleading.

"""
   result["SchemaRegistry"].IsAppliedAPISchema.func_doc = """IsAppliedAPISchema(apiSchemaType) -> USD_API bool

apiSchemaType : TfType


Returns true if C{apiSchemaType} is an applied API schema type.

"""
   result["SchemaRegistry"].GetSchematics.func_doc = """**static** GetSchematics() -> SdfLayerRefPtr


"""
   result["SchemaRegistry"].IsMultipleApplyAPISchema.func_doc = """IsMultipleApplyAPISchema(apiSchemaType) -> USD_API bool

apiSchemaType : TfType


Returns true if C{apiSchemaType} is a multiple-apply API schema type.

"""
   result["SchemaRegistry"].IsTyped.func_doc = """**static** IsTyped(primType) -> USD_API bool

primType : TfType


Returns true if the prim type C{primType} inherits from UsdTyped.

"""
   result["SchemaRegistry"].GetRelationshipDefinition.func_doc = """**static** GetRelationshipDefinition(primType, relName) -> USD_API SdfRelationshipSpecHandle

primType : TfToken
relName : TfToken


This is a convenience method.


It is shorthand for TfDynamic_cast<SdfRelationshipSpecHandle>(
GetPropertyDefinition(primType, relName));

"""
   result["ZipFileWriter"].__doc__ = """
Class for writing a zip file.


This class is primarily intended to support the .usdz file format. It
is not a general-purpose zip writer, as it does not implement the full
zip file specification. However, all files written by this class
should be valid zip files and readable by external zip modules and
utilities.

"""
   result["ZipFileWriter"].AddFile.im_func.func_doc = """AddFile(filePath, filePathInArchive) -> USD_API string

filePath : string
filePathInArchive : string


Adds the file at C{filePath} to the zip archive with no compression
applied.


If C{filePathInArchive} is non-empty, the file will be added at that
path in the archive. Otherwise, it will be added at C{filePath}.

Returns the file path used to identify the file in the zip archive on
success. This path conforms to the zip file specification and may not
be the same as C{filePath} or C{filePathInArchive}. Returns an empty
string on failure.

"""
   result["ZipFileWriter"].CreateNew.func_doc = """**static** CreateNew(filePath) -> USD_API UsdZipFileWriter

filePath : string


Create a new file writer with C{filePath} as the destination file path
where the zip archive will be written.


The zip file will not be written to C{filePath} until the writer is
destroyed or Save() is called.

Returns an invalid object on error.

"""
   result["ZipFileWriter"].Discard.im_func.func_doc = """Discard() -> USD_API void



Discards the zip archive so that it is not saved to the destination
file path.


Once discarded, the file writer is invalid and may not be reused.

"""
   result["ZipFileWriter"].Save.im_func.func_doc = """Save() -> USD_API bool



Finalizes the zip archive and saves it to the destination file path.


Once saved, the file writer is invalid and may not be reused. Returns
true on success, false otherwise.

"""
   result["ResolveInfo"].__doc__ = """
Container for information about the source of an attribute's value,
i.e.


the 'resolved' location of the attribute.

For more details, see TimeSamples, Defaults, and Value Resolution.

"""
   result["ResolveInfo"].GetSource.im_func.func_doc = """GetSource() -> ResolveInfoSource



Return the source of the associated attribute's value.

"""
   result["ResolveInfo"].ValueIsBlocked.im_func.func_doc = """ValueIsBlocked() -> bool



Return true if this UsdResolveInfo represents an attribute whose value
is blocked.



UsdAttribute::Block()

"""
   result["ResolveInfo"].__init__.im_func.func_doc = """__init__()


"""
   result["ResolveInfo"].GetNode.im_func.func_doc = """GetNode() -> PcpNodeRef



Return the node within the containing PcpPrimIndex that provided the
resolved value opinion.

"""
   result["References"].__doc__ = """
UsdReferences provides an interface to authoring and introspecting
references in Usd.


References are the primary operator for "encapsulated aggregation" of
scene description. *aggregation* means that references let us build up
rich scenes by composing scene description recorded in a (most often)
different layer. A scene can reference the same layer many times at
different locations in a scene's namespace. Referenced scene
description can be overridden in the referencing (or stronger) layers,
allowing each instance of the reference to be directly
customized/overridden. *Encapsulated* means that regardless of how
much scene description is in the referenced layer, only the scene
description under and composed from (via other composition arcs in the
referenced layer) the targeted prim will be composed into the
aggregate scene. Multiple references to the same layer will result in
the layer being opened and retained in memory only once, although each
referencing prim will compose unique prim indices for the tree rooted
at the referenced prim.

Important Qualities and Effective Use of References
===================================================

   - Any prim can host zero, one or multiple references

   - References are list editable; that is, they compose differently
     than ordinary properties and metadata. In any given LayerStack, each
     authored reference operation at the same SdfPath location in each
     layer (i.e. on the same prim) will compose into an aggregate result by
     adding to, removing from, or replacing "weaker" references.

   - References can target the same LayerStack in which they are
     authored, as long as doing so does not introduce a cycle in the
     composition graph. See Expressing "internal" references to the
     containing LayerStack

   - The C{identifier} component of a reference in the provided API
     can be a resolvable asset-path to some external layer, empty, in which
     case the reference targets the root layer of the LayerStack containing
     the referencing layer, or the identifier of an existing anonymous, in-
     memory-only SdfLayer. Care should be exercised in the latter case:
     calling Export() on an anonymous layer to serialize it to a file will
     not attempt to replace any references to anonymous layers with
     references to file-backed layers.

   - Opinions brought in by reference on an ancestor prim are weaker
     than opinions brought in by references on a descendant prim.

References may omit the target prim path if the referenced layer has
the 'defaultPrim' metadata set. In this case, the reference targets
the 'defaultPrim' in the referenced layer. A layer's defaultPrim can
be authored and accessed on a UsdStage whose root layer is the layer
in question: see UsdStage::GetDefaultPrim() and
UsdStage::SetDefaultPrim() . One can also author defaultPrim directly
on an SdfLayer - see SdfLayer::GetDefaultPrim() ,
SdfLayer::SetDefaultPrim() .

References may omit the identifier specifying the referenced layer.
This creates an "internal" reference. During composition, the
referenced layer will be resolved to the root layer of the LayerStack
containing the layer where the reference was authored. See
AddInternalReference() .

References may target any prim in a layer. In the simplest and most
common case, a root prim in a layer will be referenced. However,
referencing sub-root prims can be useful in a variety of other cases;
for example, a user might organize prims into a meaningful hierarchy
in a layer for display purposes, then use sub-root references to
reference a selection from that hierarchy into a scene.

Sub-root references have subtle behaviors with respect to opinions and
composition arcs authored on ancestors of the referenced prim. Users
should carefully consider this when deciding whether to use sub-root
references. These issues can be avoided by not authoring any
properties or metadata on ancestors of prims that are meant to be
referenced.

Consider the following example: ::

  * shot.usda                                 | * asset.usda
                                              |
  #usda 1.0                                   | #usda 1.0
                                              |
  over "Class"                                | class "Class"
  {                                           | {
      over "B"                                | }
      {                                       |
          over "Model"                        | def "A" (
          {                                   |    inherits = </Class>
              int a = 3                       | )
          }                                   | {
      }                                       |     token purpose = "render"
  }                                           |
                                              |     def "B" (
  over "A"                                    |        variantSets = "type"
  {                                           |        variants = {
      over "B" (                              |             string type = "a"
          # variant selection won't be used   |        }
          variants = {                        |     )
              string type = "b"               |     {
          }                                   |         variantSet "type" = {
      )                                       |             "a" {
      {                                       |                 def "Model"
      }                                       |                 {
  }                                           |                     int a = 1
                                              |                 }
  def "ReferencedModel" (                     |             }
      references = @./asset.usda@</A/B/Model> |             "b" {
  )                                           |                 def "Model"
  {                                           |                 {
  }                                           |                     int a = 2
                                              |                 }
                                              |             }
                                              |         }
                                              |     }
                                              | }

   - Property and metadata opinions on the ancestors of the referenced
     prim *are not* present in the composed stage and will never contribute
     to any computations. In this example, the opinion for the attribute
     /A.purpose in asset.usda will never be visible in the UsdStage for
     shot.usda.

   - Property and metadata opinions due to ancestral composition arcs
     *are* present in the composed stage. In this example, the attribute
     /Class/B/Model.a in shot.usda will be present in the UsdStage for
     shot.usda, even though the inherit arc is authored on an ancestor of
     the referenced prim.

   - A consequence of these rules is that users might not be able to
     override ancestral variant selections that affect the referenced prim.
     In this example, the Model prim being referenced comes from the
     variant selection {type=a} on prim /A/B in asset.usda. The {type=b}
     variant cannot be selected in shot.usda, even if prims with the same
     hierarchy happen to exist there. There are various workarounds for
     this; in this example, the {type=b} variant selection could be
     authored on /Class/B/Model in shot.usda instead because of the inherit
     arc that was established on prim /A.

AddReference() and SetReferences() can each fail for a number of
reasons. If one of the specified prim targets for one of the
references is not a prim, we will generate an error, fail to author
any scene description, and return C{false}. If anything goes wrong in
attempting to write the reference, we also return false, and the
reference will also remain unauthored. Otherwise, if the reference was
successfully authored, we will return C{true}. B{A successful
reference authoring operation may still generate composition errors!}
Just because the reference you specified was syntactically correct and
therefore successfully authored, does not imply it was meaningful. If
you wish to ensure that the reference you are about to author will be
meaningfully consumable by your stage, you are strongly encouraged to
B{ensure it will resolve to an actual file by using
UsdStage::ResolveIdentifierToEditTarget() before authoring the
reference.}

When adding an internal reference, the given prim path is expected to
be in the namespace of the owning prim's stage. Sub-root prim paths
will be translated from this namespace to the namespace of the current
edit target, if necessary. If a path cannot be translated, a coding
error will be issued and no changes will be made. Non-sub-root paths
will not be translated.

Immediately upon successful authoring of the reference (before
returning from AddReference() , RemoveReference() , ClearReferences()
, or SetReferences() ), the UsdStage on which the reference was
authored will recompose the subtree rooted at the prim hosting the
reference. If the provided identifier does not resolve to a layer that
is already opened or that can be opened in the usd format, *or* if the
provided primPath is not an actual prim in that layer, the stage's
recomposition will fail, and pass on composition errors to the client.

"""
   result["References"].SetReferences.im_func.func_doc = """SetReferences(items) -> USD_API bool

items : SdfReferenceVector


Explicitly set the references, potentially blocking weaker opinions
that add or remove items.



Why adding references may fail for explanation of expectations on
C{ref} and what return values and errors to expect, and ListOps and
List Editing for details on list editing and composition of listOps.

"""
   result["References"].AddReference.im_func.func_doc = """AddReference(ref, position) -> USD_API bool

ref : SdfReference
position : ListPosition


Adds a reference to the reference listOp at the current EditTarget, in
the position specified by C{position}.



Why adding references may fail for explanation of expectations on
C{ref} and what return values and errors to expect, and ListOps and
List Editing for details on list editing and composition of listOps.


----------------------------------------------------------------------
AddReference(identifier, primPath, layerOffset, position) -> USD_API bool

identifier : string
primPath : SdfPath
layerOffset : SdfLayerOffset
position : ListPosition


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
AddReference(identifier, layerOffset, position) -> USD_API bool

identifier : string
layerOffset : SdfLayerOffset
position : ListPosition


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.



References Without Prim Paths

"""
   result["References"].AddInternalReference.im_func.func_doc = """AddInternalReference(primPath, layerOffset, position) -> USD_API bool

primPath : SdfPath
layerOffset : SdfLayerOffset
position : ListPosition


Add an internal reference to the specified prim.



Internal References

"""
   result["References"].RemoveReference.im_func.func_doc = """RemoveReference(ref) -> USD_API bool

ref : SdfReference


Removes the specified reference from the references listOp at the
current EditTarget.


This does not necessarily eliminate the reference completely, as it
may be added or set in another layer in the same LayerStack as the
current EditTarget.

ListOps and List Editing

"""
   result["References"].GetPrim.im_func.func_doc = """GetPrim() -> Prim



Return the prim this object is bound to.


----------------------------------------------------------------------
GetPrim() -> Prim



This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["References"].ClearReferences.im_func.func_doc = """ClearReferences() -> USD_API bool



Removes the authored reference listOp edits at the current EditTarget.


The same caveats for Remove() apply to Clear(). In fact, Clear() may
actually increase the number of composed references, if the listOp
being cleared contained the "remove" operator.

ListOps and List Editing

"""
   result["_PrimFlagsConjunction"].__doc__ = """
Conjunction of prim flag predicate terms.


Usually clients will implicitly create conjunctions by&&-ing together
flag predicate terms. For example: ::

  // Get all loaded model children.
  prim.GetFilteredChildren(UsdPrimIsModel && UsdPrimIsLoaded)

See primFlags.h for more details.

"""
   result["ZipFile"].__doc__ = """
Class for reading a zip file.


This class is primarily intended to support the .usdz file format. It
is not a general-purpose zip reader, as it does not implement the full
zip file specification. In particular:

   - This class does not natively support decompressing data from a
     zip archive. Clients may access the data exactly as stored in the file
     and perform their own decompression if desired.

   - This class does not rely on the central directory in order to
     read the contents of the file. This allows it to operate on partial
     zip archives. However, this also means it may handle certain zip files
     incorrectly. For example, if a file was deleted from a zip archive by
     just removing its central directory header, that file will still be
     found by this class.


"""
   result["ZipFile"].DumpContents.im_func.func_doc = """DumpContents() -> USD_API void



Print out listing of contents of this zip archive to stdout.


For diagnostic purposes only.

"""
   result["ZipFile"].FileInfo.__doc__ = """
Information for a file in the zip archive.

"""
   result["ZipFile"].Open.func_doc = """**static** Open(filePath) -> USD_API UsdZipFile

filePath : string


Opens the zip archive at C{filePath}.


Returns invalid object on error.


----------------------------------------------------------------------
Open(asset) -> USD_API UsdZipFile

asset : shared_ptr< ArAsset >


Opens the zip archive C{asset}.


Returns invalid object on error.

"""
   result["Object"].__doc__ = """
Base class for Usd scenegraph objects, providing common API.


The commonality between the three types of scenegraph objects in Usd (
UsdPrim, UsdAttribute, UsdRelationship) is that they can all have
metadata. Other objects in the API ( UsdReferences, UsdVariantSets,
etc.) simply *are* kinds of metadata.

UsdObject 's API primarily provides schema for interacting with the
metadata common to all the scenegraph objects, as well as generic
access to metadata.

section Usd_UsdObject_Lifetime Lifetime Management and Object Validity

Every derived class of UsdObject supports explicit detection of object
validity through an *unspecified-bool-type* operator (i.e. safe bool
conversion), so client code should always be able use objects safely,
even across edits to the owning UsdStage. UsdObject classes also
perform some level of validity checking upon every use, in order to
facilitate debugging of unsafe code, although we reserve the right to
activate that behavior only in debug builds, if it becomes compelling
to do so for performance reasons. This per-use checking will cause a
fatal error upon failing the inline validity check, with an error
message describing the namespace location of the dereferenced object
on its owning UsdStage.

"""
   result["Object"].ClearAssetInfo.im_func.func_doc = """ClearAssetInfo() -> USD_API void



Clear the authored opinion for this object's assetInfo dictionary at
the current EditTarget.


Do nothing if there is no such authored opinion.

"""
   result["Object"].ClearMetadataByDictKey.im_func.func_doc = """ClearMetadataByDictKey(key, keyPath) -> USD_API bool

key : TfToken
keyPath : TfToken


Clear any authored value identified by C{key} and C{keyPath} at the
current EditTarget.


The C{keyPath} is a ':'-separated path identifying a path in
subdictionaries stored in the metadata field at C{key}. Return true if
the value is cleared successfully, false otherwise.

Dictionary-valued Metadata

"""
   result["Object"].HasAuthoredDocumentation.im_func.func_doc = """HasAuthoredDocumentation() -> USD_API bool



Returns true if documentation was explicitly authored and
GetMetadata() will return a meaningful value for documentation.

"""
   result["Object"].ClearAssetInfoByKey.im_func.func_doc = """ClearAssetInfoByKey(keyPath) -> USD_API void

keyPath : TfToken


Clear the authored opinion identified by C{keyPath} in this object's
assetInfo dictionary at the current EditTarget.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries. Do nothing if there is no such authored opinion.

"""
   result["Object"].HasAuthoredAssetInfo.im_func.func_doc = """HasAuthoredAssetInfo() -> USD_API bool



Return true if there are any authored opinions (excluding fallback)
for this object's assetInfo dictionary, false otherwise.

"""
   result["Object"].ClearCustomDataByKey.im_func.func_doc = """ClearCustomDataByKey(keyPath) -> USD_API void

keyPath : TfToken


Clear the authored opinion identified by C{keyPath} in this object's
customData dictionary at the current EditTarget.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries. Do nothing if there is no such authored opinion.

"""
   result["Object"].GetPrim.im_func.func_doc = """GetPrim() -> Prim



Return this object if it is a prim, otherwise return this object's
nearest owning prim.

"""
   result["Object"].SetMetadataByDictKey.im_func.func_doc = """SetMetadataByDictKey(key, keyPath, value) -> bool

key : TfToken
keyPath : TfToken
value : T


Author C{value} to the field identified by C{key} and C{keyPath} at
the current EditTarget.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries stored in the metadata field at C{key}. Return true if
the value is authored successfully, false otherwise.

Dictionary-valued Metadata


----------------------------------------------------------------------
SetMetadataByDictKey(key, keyPath, value) -> USD_API bool

key : TfToken
keyPath : TfToken
value : VtValue


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Object"].__init__.im_func.func_doc = """__init__()



Default constructor produces an invalid object.


----------------------------------------------------------------------
__init__(prim, proxyPrimPath)

prim : _PrimDataHandle
proxyPrimPath : SdfPath


----------------------------------------------------------------------
__init__(objType, prim, proxyPrimPath, propName)

objType : ObjType
prim : _PrimDataHandle
proxyPrimPath : SdfPath
propName : TfToken

"""
   result["Object"].HasCustomDataKey.im_func.func_doc = """HasCustomDataKey(keyPath) -> USD_API bool

keyPath : TfToken


Return true if there are any authored or fallback opinions for the
element identified by C{keyPath} in this object's customData
dictionary, false otherwise.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries.

"""
   result["Object"].GetMetadata.im_func.func_doc = """GetMetadata(key, value) -> bool

key : TfToken
value : T


Resolve the requested metadatum named C{key} into C{value}, returning
true on success.



false if C{key} was not resolvable, or if C{value's} type C{T}
differed from that of the resolved metadatum.

For any composition-related metadata, as enumerated in
GetAllMetadata() , this method will return only the strongest opinion
found, not applying the composition rules used by Pcp to process the
data. For more processed/composed views of composition data, please
refer to the specific interface classes, such as UsdReferences,
UsdInherits, UsdVariantSets, etc.

General Metadata in USD


----------------------------------------------------------------------
GetMetadata(key, value) -> USD_API bool

key : TfToken
value : VtValue


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

Type-erased access.

"""
   result["Object"].GetMetadataByDictKey.im_func.func_doc = """GetMetadataByDictKey(key, keyPath, value) -> bool

key : TfToken
keyPath : TfToken
value : T


Resolve the requested dictionary sub-element C{keyPath} of dictionary-
valued metadatum named C{key} into C{value}, returning true on
success.


If you know you neeed just a small number of elements from a
dictionary, accessing them element-wise using this method can be much
less expensive than fetching the entire dictionary with
GetMetadata(key).

false if C{key} was not resolvable, or if C{value's} type C{T}
differed from that of the resolved metadatum. The C{keyPath} is a
':'-separated path addressing an element in subdictionaries.

Dictionary-valued Metadata


----------------------------------------------------------------------
GetMetadataByDictKey(key, keyPath, value) -> USD_API bool

key : TfToken
keyPath : TfToken
value : VtValue


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Object"].HasMetadataDictKey.im_func.func_doc = """HasMetadataDictKey(key, keyPath) -> USD_API bool

key : TfToken
keyPath : TfToken


Return true if there exists any authored or fallback opinion for
C{key} and C{keyPath}.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries stored in the metadata field at C{key}.

Dictionary-valued Metadata

"""
   result["Object"].GetDescription.im_func.func_doc = """GetDescription() -> USD_API string



Return a string that provides a brief summary description of the
object.


This method, along with IsValid() /bool_operator, is always safe to
call on a possibly-expired object, and the description will specify
whether the object is valid or expired, along with a few other bits of
data.

"""
   result["Object"].GetDocumentation.im_func.func_doc = """GetDocumentation() -> USD_API string



Return this object's documentation (metadata).


This returns the empty string if no documentation has been set.

SetDocumentation()

"""
   result["Object"].HasAuthoredAssetInfoKey.im_func.func_doc = """HasAuthoredAssetInfoKey(keyPath) -> USD_API bool

keyPath : TfToken


Return true if there are any authored opinions (excluding fallback)
for the element identified by C{keyPath} in this object's assetInfo
dictionary, false otherwise.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries.

"""
   result["Object"].ClearDocumentation.im_func.func_doc = """ClearDocumentation() -> USD_API bool



Clears this object's documentation (metadata) in the current
EditTarget (only).


Returns true on success.

"""
   result["Object"].GetAllAuthoredMetadata.im_func.func_doc = """GetAllAuthoredMetadata() -> USD_API UsdMetadataValueMap



Resolve and return all user-authored metadata on this object, sorted
lexicographically.



This method does not return field keys for composition arcs, such as
references, inherits, payloads, sublayers, variants, or primChildren,
nor does it return the default value or timeSamples.

"""
   result["Object"].GetAssetInfo.im_func.func_doc = """GetAssetInfo() -> USD_API VtDictionary



Return this object's composed assetInfo dictionary.


The asset info dictionary is used to annotate objects representing the
root-prims of assets (generally organized as models) with various data
related to asset management. For example, asset name, root layer
identifier, asset version etc.

The elements of this dictionary are composed element-wise, and are
nestable.

There is no means to query an assetInfo field's valuetype other than
fetching the value and interrogating it.

GetAssetInfoByKey()

"""
   result["Object"].SetHidden.im_func.func_doc = """SetHidden(hidden) -> USD_API bool

hidden : bool


Sets the value of the 'hidden' metadata field.


See IsHidden() for details.

"""
   result["Object"].HasAuthoredMetadata.im_func.func_doc = """HasAuthoredMetadata(key) -> USD_API bool

key : TfToken


Returns true if the *key* has an authored value, false if no value was
authored or the only value available is a prim's metadata fallback.

"""
   result["Object"].HasAuthoredHidden.im_func.func_doc = """HasAuthoredHidden() -> USD_API bool



Returns true if hidden was explicitly authored and GetMetadata() will
return a meaningful value for Hidden.


Note that IsHidden returns a fallback value (false) when hidden is not
authored.

"""
   result["Object"].SetMetadata.im_func.func_doc = """SetMetadata(key, value) -> bool

key : TfToken
value : T


Set metadatum C{key's} value to C{value}.



false if C{value's} type does not match the schema type for C{key}.

General Metadata in USD


----------------------------------------------------------------------
SetMetadata(key, value) -> USD_API bool

key : TfToken
value : VtValue


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Object"].ClearCustomData.im_func.func_doc = """ClearCustomData() -> USD_API void



Clear the authored opinion for this object's customData dictionary at
the current EditTarget.


Do nothing if there is no such authored opinion.

"""
   result["Object"].HasAuthoredCustomData.im_func.func_doc = """HasAuthoredCustomData() -> USD_API bool



Return true if there are any authored opinions (excluding fallback)
for this object's customData dictionary, false otherwise.

"""
   result["Object"].SetCustomDataByKey.im_func.func_doc = """SetCustomDataByKey(keyPath, value) -> USD_API void

keyPath : TfToken
value : VtValue


Author the element identified by C{keyPath} in this object's
customData dictionary at the current EditTarget.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries.

"""
   result["Object"].ClearHidden.im_func.func_doc = """ClearHidden() -> USD_API bool



Clears the opinion for "Hidden" at the current EditTarget.

"""
   result["Object"].ClearMetadata.im_func.func_doc = """ClearMetadata(key) -> USD_API bool

key : TfToken


Clears the authored *key's* value at the current EditTarget, returning
false on error.


If no value is present, this method is a no-op and returns true. It is
considered an error to call ClearMetadata when no spec is present for
this UsdObject, i.e. if the object has no presence in the current
UsdEditTarget.

General Metadata in USD

"""
   result["Object"].GetCustomData.im_func.func_doc = """GetCustomData() -> USD_API VtDictionary



Return this object's composed customData dictionary.


CustomData is "custom metadata", a place for applications and users to
put uniform data that is entirely dynamic and subject to no schema
known to Usd. Unlike metadata like 'hidden', 'displayName' etc, which
must be declared in code or a data file that is considered part of
one's Usd distribution (e.g. a plugInfo.json file) to be used,
customData keys and the datatypes of their corresponding values are ad
hoc. No validation will ever be performed that values for the same key
in different layers are of the same type - strongest simply wins.

Dictionaries like customData are composed element-wise, and are
nestable.

There is no means to query a customData field's valuetype other than
fetching the value and interrogating it.

GetCustomDataByKey()

"""
   result["Object"].SetDocumentation.im_func.func_doc = """SetDocumentation(doc) -> USD_API bool

doc : string


Sets this object's documentation (metadata). Returns true on success.

"""
   result["Object"].GetName.im_func.func_doc = """GetName() -> TfToken



Return the full name of this object, i.e.


the last component of its SdfPath in namespace.

This is equivalent to, but generally cheaper than, GetPath()
.GetNameToken()

"""
   result["Object"].SetCustomData.im_func.func_doc = """SetCustomData(customData) -> USD_API void

customData : VtDictionary


Author this object's customData dictionary to C{customData} at the
current EditTarget.

"""
   result["Object"].GetPath.im_func.func_doc = """GetPath() -> SdfPath



Return the complete scene path to this object on its UsdStage, which
may (UsdPrim) or may not (all other subclasses) return a cached
result.

"""
   result["Object"].HasAuthoredCustomDataKey.im_func.func_doc = """HasAuthoredCustomDataKey(keyPath) -> USD_API bool

keyPath : TfToken


Return true if there are any authored opinions (excluding fallback)
for the element identified by C{keyPath} in this object's customData
dictionary, false otherwise.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries.

"""
   result["Object"].SetAssetInfo.im_func.func_doc = """SetAssetInfo(customData) -> USD_API void

customData : VtDictionary


Author this object's assetInfo dictionary to C{assetInfo} at the
current EditTarget.

"""
   result["Object"].HasCustomData.im_func.func_doc = """HasCustomData() -> USD_API bool



Return true if there are any authored or fallback opinions for this
object's customData dictionary, false otherwise.

"""
   result["Object"].GetAssetInfoByKey.im_func.func_doc = """GetAssetInfoByKey(keyPath) -> USD_API VtValue

keyPath : TfToken


Return the element identified by C{keyPath} in this object's composed
assetInfo dictionary.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries. This is in general more efficient than composing the
entire assetInfo dictionary than pulling out one sub-element.

"""
   result["Object"].IsHidden.im_func.func_doc = """IsHidden() -> USD_API bool



Gets the value of the 'hidden' metadata field, false if not authored.


When an object is marked as hidden, it is an indicator to clients who
generically display objects (such as GUI widgets) that this object
should not be included, unless explicitly asked for. Although this is
just a hint and thus up to each application to interpret, we use it
primarily as a way of simplifying hierarchy displays, by hiding *only*
the representation of the object itself, *not* its subtree, instead
"pulling up" everything below it one level in the hierarchical
nesting.

Note again that this is a hint for UI only - it should not be
interpreted by any renderer as making a prim invisible to drawing.

"""
   result["Object"].HasAssetInfo.im_func.func_doc = """HasAssetInfo() -> USD_API bool



Return true if there are any authored or fallback opinions for this
object's assetInfo dictionary, false otherwise.

"""
   result["Object"].SetAssetInfoByKey.im_func.func_doc = """SetAssetInfoByKey(keyPath, value) -> USD_API void

keyPath : TfToken
value : VtValue


Author the element identified by C{keyPath} in this object's assetInfo
dictionary at the current EditTarget.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries.

"""
   result["Object"].IsValid.im_func.func_doc = """IsValid() -> bool



Return true if this is a valid object, false otherwise.

"""
   result["Object"].HasAssetInfoKey.im_func.func_doc = """HasAssetInfoKey(keyPath) -> USD_API bool

keyPath : TfToken


Return true if there are any authored or fallback opinions for the
element identified by C{keyPath} in this object's assetInfo
dictionary, false otherwise.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries.

"""
   result["Object"].GetAllMetadata.im_func.func_doc = """GetAllMetadata() -> USD_API UsdMetadataValueMap



Resolve and return all metadata (including both authored and fallback
values) on this object, sorted lexicographically.



This method does not return field keys for composition arcs, such as
references, inherits, payloads, sublayers, variants, or primChildren,
nor does it return the default value or timeSamples.

"""
   result["Object"].HasMetadata.im_func.func_doc = """HasMetadata(key) -> USD_API bool

key : TfToken


Returns true if the *key* has a meaningful value, that is, if
GetMetadata() will provide a value, either because it was authored or
because a prim's metadata fallback will be provided.

"""
   result["Object"].GetStage.im_func.func_doc = """GetStage() -> USD_API UsdStageWeakPtr



Return the stage that owns the object, and to whose state and lifetime
this object's validity is tied.

"""
   result["Object"].GetCustomDataByKey.im_func.func_doc = """GetCustomDataByKey(keyPath) -> USD_API VtValue

keyPath : TfToken


Return the element identified by C{keyPath} in this object's composed
customData dictionary.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries. This is in general more efficient than composing the
entire customData dictionary and then pulling out one sub-element.

"""
   result["Object"].HasAuthoredMetadataDictKey.im_func.func_doc = """HasAuthoredMetadataDictKey(key, keyPath) -> USD_API bool

key : TfToken
keyPath : TfToken


Return true if there exists any authored opinion (excluding fallbacks)
for C{key} and C{keyPath}.


The C{keyPath} is a ':'-separated path identifying a value in
subdictionaries stored in the metadata field at C{key}.

Dictionary-valued Metadata

"""
   result["Object"].GetPrimPath.im_func.func_doc = """GetPrimPath() -> SdfPath



Return this object's path if this object is a prim, otherwise this
object's nearest owning prim's path.


Equivalent to GetPrim() . GetPath() .

"""
   result["Object"].GetNamespaceDelimiter.func_doc = """**static** GetNamespaceDelimiter() -> char


"""
   result["__doc__"] = """

B{Usd} is the core client-facing module for authoring, composing, and
reading Universal Scene Description. USD is designed to encode
scalable, hierarchically organized, static and time-sampled data, for
the primary purpose of interchanging and augmenting the data between
cooperating Digital Content Creation applications.

Core API Manual
===============

This manual contains the API documentation for the core Usd module,
prefaced with an introduction to the key concepts behind the API, and
including a guide to making effective use of the API. In this manual
we do not deeply explore the composition semantics that underly Usd
scenegraphs - that is the domain of the (forthcoming) *Universal Scene
Description Composition Compendium*. We will discuss some aspects of
the composition operators, primarily as they affect authoring
workflows and/or scalability and/or import/export.

B{API Manual}

B{Key Classes}

   - Object Model and How the Classes Work Together
   - SdfLayer: Shared Data Files

   - UsdStage: Composed View of an SdfLayer

   - UsdPrim: Nestable Namespace Containers

   - UsdProperty: Common Interface for Attributes and Relationships

   - UsdAttribute: Typed, Sampled, Data

   - UsdRelationship: Targetting Namespace Objects

   - General Metadata in USD

   - Composition Operator Interfaces: UsdReferences, UsdInherits,
     UsdVariantSets

   - Basic Datatypes for Scene Description Provided by Sdf
   - Attribute value types

   - Basic data types

   - Roles

   - Array data types

   - Dictionary-valued Metadata

   - Important Properties of Scene Description
   - Names, Namespace Ordering, and Property Namespaces

   - TimeSamples, Defaults, and Value Resolution

   - Defs, Overs, Classes, and Prim Types

   - Model Hierarchy: Meaning and Purpose

   - How "active" Affects Prims on a UsdStage

   - Ascii, Binary, and Plugin Filetypes

   - Resolving Asset References

   - Advanced Scenegraph Scalability Features

   - Authoring and Editing Scene Description
   - Specifying Where Edits Should Go

   - Client Safety and Response to Edits

   - Common Idioms and Examples
   - Traversing a Stage

   - Working With Schema Classes

   - Bool Return Values and Safe Operator Bool

   - Error Reporting Policy and Control

   - Best Practices and Common Questions
   - Object Parameters as Const-Ref

   - Reading Data Efficiently

   - Payloads: Impact of Using and Not Using

   - Threading Model and Performance Considerations
   - Thread-safety Guarantee

   - Usd's Internal Use of Multi-threading

   - Creating New Schema Classes with usdGenSchema
   - IsA Vs. API Schemas

   - Impact on Interchange of Creating and Extending Schemas

UsdStage owns the scenegraph and provides access to a composition.
UsdPrim is the hierarchically nestable unit of scene description.
UsdAttribute records time-varying data on prims.  UsdRelationship
records links to other prims and properties.  UsdEditTarget allows
editing of any layer/variation contained in a stage.  UsdNotice
contains notifications that Usd issues when a stage's contents change.
UsdSchemaBase is the base class for generated schema classes.
UsdTimeCode is an ordinate that can be floating-point or an unvarying
'default'.


"""
   result["ModelAPI"].__doc__ = """
UsdModelAPI is an API schema that provides an interface to a prim's
model qualities, if it does, in fact, represent the root prim of a
model.


The first and foremost model quality is its *kind*, i.e. the metadata
that establishes it as a model (See KindRegistry). UsdModelAPI
provides various methods for setting and querying the prim's kind, as
well as queries (also available on UsdPrim) for asking what category
of model the prim is. See Kind and Model-ness.

UsdModelAPI also provides access to a prim's assetInfo data. While any
prim *can* host assetInfo, it is common that published (referenced)
assets are packaged as models, therefore it is convenient to provide
access to the one from the other.

"""
   result["ModelAPI"].GetPayloadAssetDependencies.im_func.func_doc = """GetPayloadAssetDependencies(assetDeps) -> USD_API bool

assetDeps : VtArray < SdfAssetPath >


Returns the list of asset dependencies referenced inside the payload
of the model.


This typically contains identifiers of external assets that are
referenced inside the model's payload. When the model is created, this
list is compiled and set at the root of the model. This enables
efficient dependency analysis without the need to include the model's
payload.

"""
   result["ModelAPI"].GetKind.im_func.func_doc = """GetKind(kind) -> USD_API bool

kind : TfToken


Retrieve the authored C{kind} for this prim.


To test whether the returned C{kind} matches a particular known
"clientKind": ::

  TfToken kind;
  
  bool isClientKind = UsdModelAPI(prim).GetKind(&kind) and
                      KindRegistry::IsA(kind, clientKind);

true if there was an authored kind that was successfully read,
otherwise false.

The Kind module for further details on how to use Kind for
classification, and how to extend the taxonomy.

"""
   result["ModelAPI"].SetAssetIdentifier.im_func.func_doc = """SetAssetIdentifier(identifier) -> USD_API void

identifier : SdfAssetPath


Sets the model's asset identifier to the given asset path,
C{identifier}.



GetAssetIdentifier()

"""
   result["ModelAPI"].Get.func_doc = """**static** Get(stage, path) -> USD_API UsdModelAPI

stage : StagePtr
path : SdfPath


Return a UsdModelAPI holding the prim adhering to this schema at
C{path} on C{stage}.


If no prim exists at C{path} on C{stage}, or if the prim at that path
does not adhere to this schema, return an invalid schema object. This
is shorthand for the following: ::

  UsdModelAPI(stage->GetPrimAtPath(path));


"""
   result["ModelAPI"].IsGroup.im_func.func_doc = """IsGroup() -> USD_API bool



Return true if this prim represents a model group, based on its kind
metadata.

"""
   result["ModelAPI"].GetAssetInfo.im_func.func_doc = """GetAssetInfo(info) -> USD_API bool

info : VtDictionary


Returns the model's composed assetInfo dictionary.


The asset info dictionary is used to annotate models with various data
related to asset management. For example, asset name, identifier,
version etc.

The elements of this dictionary are composed element-wise, and are
nestable.

"""
   result["ModelAPI"].GetAssetName.im_func.func_doc = """GetAssetName(assetName) -> USD_API bool

assetName : string


Returns the model's asset name from the composed assetInfo dictionary.


The asset name is the name of the asset, as would be used in a
database query.

"""
   result["ModelAPI"].IsModel.im_func.func_doc = """IsModel() -> USD_API bool



Return true if this prim represents a model, based on its kind
metadata.

"""
   result["ModelAPI"].SetAssetVersion.im_func.func_doc = """SetAssetVersion(version) -> USD_API void

version : string


Sets the model's asset version string.



GetAssetVersion()

"""
   result["ModelAPI"].__init__.im_func.func_doc = """__init__(prim)

prim : Prim


Construct a UsdModelAPI on UsdPrim C{prim}.


Equivalent to UsdModelAPI::Get (prim.GetStage(), prim.GetPath()) for a
*valid* C{prim}, but will not immediately throw an error for an
invalid C{prim}


----------------------------------------------------------------------
__init__(schemaObj)

schemaObj : SchemaBase


Construct a UsdModelAPI on the prim held by C{schemaObj}.


Should be preferred over UsdModelAPI (schemaObj.GetPrim()), as it
preserves SchemaBase state.

"""
   result["ModelAPI"].GetAssetIdentifier.im_func.func_doc = """GetAssetIdentifier(identifier) -> USD_API bool

identifier : SdfAssetPath


Returns the model's asset identifier as authored in the composed
assetInfo dictionary.


The asset identifier can be used to resolve the model's root layer via
the asset resolver plugin.

"""
   result["ModelAPI"].SetPayloadAssetDependencies.im_func.func_doc = """SetPayloadAssetDependencies(assetDeps) -> USD_API void

assetDeps : VtArray < SdfAssetPath >


Sets the list of external asset dependencies referenced inside the
payload of a model.



GetPayloadAssetDependencies()

"""
   result["ModelAPI"].GetAssetVersion.im_func.func_doc = """GetAssetVersion(version) -> USD_API bool

version : string


Returns the model's resolved asset version.


If you publish assets with an embedded version, then you may receive
that version string. You may, however, cause your authoring tools to
record the resolved version *at the time at which a reference to the
asset was added to an aggregate*, at the referencing site. In such a
pipeline, this API will always return that stronger opinion, even if
the asset is republished with a newer version, and even though that
newer version may be the one that is resolved when the UsdStage is
opened.

"""
   result["ModelAPI"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> USD_API  TfTokenVector

includeInherited : bool


Return a vector of names of all pre-declared attributes for this
schema class and all its ancestor classes.


Does not include attributes that may be authored by custom/extended
methods of the schemas involved.

"""
   result["ModelAPI"].SetKind.im_func.func_doc = """SetKind(kind) -> USD_API bool

kind : TfToken


Author a C{kind} for this prim, at the current UsdEditTarget.



true if C{kind} was successully authored, otherwise false.

"""
   result["ModelAPI"].SetAssetName.im_func.func_doc = """SetAssetName(assetName) -> USD_API void

assetName : string


Sets the model's asset name to C{assetName}.



GetAssetName()

"""
   result["ModelAPI"].SetAssetInfo.im_func.func_doc = """SetAssetInfo(info) -> USD_API void

info : VtDictionary


Sets the model's assetInfo dictionary to C{info} in the current edit
target.

"""
   result["ModelAPI"]._GetStaticTfType.func_doc = """**static** _GetStaticTfType() -> USD_API  TfType


"""
   result["Property"].__doc__ = """
Base class for UsdAttribute and UsdRelationship scenegraph objects.


UsdProperty has a bool conversion operator that validates that the
property IsDefined() and thus valid for querying and authoring values
and metadata. This is a fairly expensive query that we do B{not}
cache, so if client code retains UsdProperty objects it should manage
its object validity closely for performance. An ideal pattern is to
listen for UsdNotice::StageContentsChanged notifications, and
revalidate/refetch retained UsdObjects only then and otherwise use
them without validity checking.

"""
   result["Property"].SetCustom.im_func.func_doc = """SetCustom(isCustom) -> USD_API bool

isCustom : bool


Set the value for custom at the current EditTarget, return true on
success, false if the value can not be written.


B{Note} that this value should not be changed as it is typically
either automatically authored or provided by a property definition.
This method is provided primarily for fixing invalid scene
description.

"""
   result["Property"].SetDisplayName.im_func.func_doc = """SetDisplayName(name) -> USD_API bool

name : string


Sets this property's display name (metadata).


Returns true on success.

DisplayName is meant to be a descriptive label, not necessarily an
alternate identifier; therefore there is no restriction on which
characters can appear in it.

"""
   result["Property"].SetDisplayGroup.im_func.func_doc = """SetDisplayGroup(displayGroup) -> USD_API bool

displayGroup : string


Sets this property's display group (metadata).


Returns true on success.

DisplayGroup provides UI hinting for grouping related properties
together for display. We define a convention for specifying nesting of
groups by recognizing the property namespace separator in displayGroup
as denoting group-nesting.

SetNestedDisplayGroups()

"""
   result["Property"].HasAuthoredDisplayGroup.im_func.func_doc = """HasAuthoredDisplayGroup() -> USD_API bool



Returns true if displayGroup was explicitly authored and GetMetadata()
will return a meaningful value for displayGroup.

"""
   result["Property"].SetNestedDisplayGroups.im_func.func_doc = """SetNestedDisplayGroups(nestedGroups) -> USD_API bool

nestedGroups : sequence<string>


Sets this property's display group (metadata) to the nested sequence.


Returns true on success.

A displayGroup set with this method can still be retrieved with
GetDisplayGroup() , with the namespace separator embedded in the
result. If C{nestedGroups} is empty, we author an empty string for
displayGroup.

SetDisplayGroup()

"""
   result["Property"].IsAuthoredAt.im_func.func_doc = """IsAuthoredAt(editTarget) -> USD_API bool

editTarget : class UsdEditTarget


Return true if there is an SdfPropertySpec authored for this property
at the given *editTarget*, otherwise return false.


Note that this method does not do partial composition. It does not
consider whether authored scene description exists at *editTarget* or
weaker, only B{exactly at} the given *editTarget*.

"""
   result["Property"].ClearDisplayName.im_func.func_doc = """ClearDisplayName() -> USD_API bool



Clears this property's display name (metadata) in the current
EditTarget (only).


Returns true on success.

"""
   result["Property"].HasAuthoredDisplayName.im_func.func_doc = """HasAuthoredDisplayName() -> USD_API bool



Returns true if displayName was explicitly authored and GetMetadata()
will return a meaningful value for displayName.

"""
   result["Property"].GetNamespace.im_func.func_doc = """GetNamespace() -> USD_API TfToken



Return this property's complete namespace prefix.


Return the empty token if this property has no namespaces.

This is the complement of GetBaseName() , although it does *not*
contain a trailing namespace delimiter

"""
   result["Property"].IsDefined.im_func.func_doc = """IsDefined() -> USD_API bool



Return true if this is a builtin property or if the strongest authored
SdfPropertySpec for this property's path matches this property's
dynamic type.


That is, SdfRelationshipSpec in case this is a UsdRelationship, and
SdfAttributeSpec in case this is a UsdAttribute. Return C{false} if
this property's prim has expired.

For attributes, a C{true} return does not imply that this attribute
possesses a value, only that has been declared, is of a certain type
and variability, and that it is safe to use to query and author values
and metadata.

"""
   result["Property"].GetBaseName.im_func.func_doc = """GetBaseName() -> USD_API TfToken



Return this property's name with all namespace prefixes removed, i.e.


the last component of the return value of GetName()

This is generally the property's "client name"; property namespaces
are often used to group related properties together. The namespace
prefixes the property name but many consumers will care only about un-
namespaced name, i.e. its BaseName. For more information, see Names,
Namespace Ordering, and Property Namespaces

"""
   result["Property"].ClearDisplayGroup.im_func.func_doc = """ClearDisplayGroup() -> USD_API bool



Clears this property's display group (metadata) in the current
EditTarget (only).


Returns true on success.

"""
   result["Property"].GetDisplayGroup.im_func.func_doc = """GetDisplayGroup() -> USD_API string



Return this property's display group (metadata).


This returns the empty token if no display group has been set.

SetDisplayGroup()

"""
   result["Property"].GetDisplayName.im_func.func_doc = """GetDisplayName() -> USD_API string



Return this property's display name (metadata).


This returns the empty string if no display name has been set.

SetDisplayName()

"""
   result["Property"].IsAuthored.im_func.func_doc = """IsAuthored() -> USD_API bool



Return true if there are any authored opinions for this property in
any layer that contributes to this stage, false otherwise.

"""
   result["Property"].SplitName.im_func.func_doc = """SplitName() -> USD_API sequence<string>



Return this property's name elements including namespaces and its base
name as the final element.

"""
   result["Property"].IsCustom.im_func.func_doc = """IsCustom() -> USD_API bool



Return true if this is a custom property (i.e., not part of a prim
schema).


The 'custom' modifier in USD serves the same function as Alembic's
'userProperties', which is to say as a categorization for ad hoc
client data not formalized into any schema, and therefore not carrying
an expectation of specific processing by consuming applications.

"""
   result["Property"].FlattenTo.im_func.func_doc = """FlattenTo(parent) -> USD_API UsdProperty

parent : Prim


Flattens this property to a property spec with the same name beneath
the given C{parent} prim in the current edit target.


Flattening authors all authored resolved values and metadata for this
property into the destination property spec. If this property is a
builtin property, fallback values and metadata will also be authored
if the destination property has a different fallback value or no
fallback value, or if the destination property has an authored value
that overrides its fallback.

Attribute connections and relationship targets that target an object
beneath this property's owning prim will be remapped to target objects
beneath the destination C{parent} prim.

If the destination spec already exists, it will be overwritten.

UsdStage::Flatten


----------------------------------------------------------------------
FlattenTo(parent, propName) -> USD_API UsdProperty

parent : Prim
propName : TfToken


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Flattens this property to a property spec with the given C{propName}
beneath the given C{parent} prim in the current edit target.


----------------------------------------------------------------------
FlattenTo(property) -> USD_API UsdProperty

property : Property


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.
Flattens this property to a property spec for the given C{property} in
the current edit target.

"""
   result["Property"].GetNestedDisplayGroups.im_func.func_doc = """GetNestedDisplayGroups() -> USD_API sequence<string>



Return this property's displayGroup as a sequence of groups to be
nested, or an empty vector if displayGroup is empty or not authored.

"""
   result["Property"].__init__.im_func.func_doc = """__init__(objType, prim, proxyPrimPath, propName)

objType : ObjType
prim : _PrimDataHandle
proxyPrimPath : SdfPath
propName : TfToken


----------------------------------------------------------------------
__init__()



Construct an invalid property.

"""
   result["Property"].GetPropertyStack.im_func.func_doc = """GetPropertyStack(time) -> USD_API SdfPropertySpecHandleVector

time : TimeCode


Returns a strength-ordered list of property specs that provide
opinions for this property.


If C{time} is UsdTimeCode::Default() , *or* this property is a
UsdRelationship (which are never affected by clips), we will not
consider value clips for opinions. For any other C{time}, for a
UsdAttribute, clips whose samples may contribute an opinion will be
included. These specs are ordered from strongest to weakest opinion,
although if C{time} requires interpolation between two adjacent clips,
both clips will appear, sequentially.

The results returned by this method are meant for debugging and
diagnostic purposes. It is B{not} advisable to retain a PropertyStack
for the purposes of expedited value resolution for properties, since
the makeup of an attribute's PropertyStack may itself be time-varying.
To expedite repeated value resolution of attributes, you should
instead retain a C{UsdAttributeQuery}.

UsdClipsAPI

"""
   result["VariantSets"].__doc__ = """
UsdVariantSets represents the collection of VariantSets that are
present on a UsdPrim.


A UsdVariantSets object, retrieved from a prim via
UsdPrim::GetVariantSets() , provides the API for interrogating and
modifying the composed list of VariantSets active defined on the prim,
and also the facility for authoring a VariantSet *selection* for any
of those VariantSets.

"""
   result["VariantSets"].SetSelection.im_func.func_doc = """SetSelection(variantSetName, variantName) -> USD_API bool

variantSetName : string
variantName : string

"""
   result["VariantSets"].HasVariantSet.im_func.func_doc = """HasVariantSet(variantSetName) -> USD_API bool

variantSetName : string


Returns true if a VariantSet named C{variantSetName} exists on the
originating prim.

"""
   result["VariantSets"].GetVariantSelection.im_func.func_doc = """GetVariantSelection(variantSetName) -> USD_API string

variantSetName : string


Return the composed variant selection for the VariantSet named
*variantSetName*.


If there is no selection, (or C{variantSetName} does not exist) return
the empty string.

"""
   result["VariantSets"].GetVariantSet.im_func.func_doc = """GetVariantSet(variantSetName) -> USD_API UsdVariantSet

variantSetName : string


Return a UsdVariantSet object for C{variantSetName}.


This always succeeds, although the returned VariantSet will be invalid
if the originating prim is invalid

"""
   result["VariantSets"].AddVariantSet.im_func.func_doc = """AddVariantSet(variantSetName, position) -> USD_API UsdVariantSet

variantSetName : string
position : ListPosition


Find an existing, or create a new VariantSet on the originating
UsdPrim, named C{variantSetName}.


This step is not always necessary, because if this UsdVariantSets
object is valid, then ::

  varSetsObj.GetVariantSet(variantSetName).AddVariant(variantName);

 will always succeed, creating the VariantSet first, if necessary.
This method exists for situations in which you want to create a
VariantSet without necessarily populating it with variants.

"""
   result["VariantSets"].GetNames.im_func.func_doc = """GetNames(names) -> USD_API bool

names : sequence<string>


Compute a list of all VariantSets authored on the originiating
UsdPrim.


Always return true.


----------------------------------------------------------------------
GetNames() -> USD_API sequence<string>



Return a list of all VariantSets authored on the originiating UsdPrim.

"""
   result["Relationship"].__doc__ = """
A UsdRelationship creates dependencies between scenegraph objects by
allowing a prim to *target* other prims, attributes, or relationships.


Relationship Characteristics
============================

A UsdRelationship is a pointer to other objects, which are named by
their scenegraph paths. When authoring relationships, the *target*
parameters should be scenegraph paths in the composed namespace of the
UsdStage into which you are authoring. If your edits are targetted to
a different layer, across various composition arcs (because you
specified a non-default UsdEditTarget), the target's path will be
automatically translated into the proper namespace.

A single UsdRelationship can target multiple other objects, which can
be of UsdPrim, UsdAttribute, or UsdRelationship type. UsdRelationship
participates in "list editing", which means that stronger layers in a
composed scene can add, remove, or reorder targets authored on the
relationship in weaker layers *without* stomping the weaker opinions,
although stomping behavior is still possible, via SetTargets() .

An authored relationship creates a dependency of the targetting prim
on the targetted prim(s). We consider these dependencies to be
"loaddependencies", which means that when we load the targeting prim's
"load group", we will also load the targetted prims' load groups, to
ensure that all the data required to render the model containing the
targeting prim is composed and available.

Like UsdAttribute, UsdRelationship objects are meant to be ephemeral,
live on the stack, and be cheap to refetch from their owning UsdPrim.

Unlike UsdAttribute s, which can either be uniform over all time or
vary in value over time, UsdRelationship is B{always uniform}.

Relationship Restrictions
=========================

When authoring relationship targets in a stage's local LayerStack, all
target paths are legal (Note we may restrict this prior to launch to
only allowing targeting of already-extant scenegraph objects).
However, a relationship target that is legal in a local LayerStack may
become unreachable when the stage's root layer is *referenced* into an
aggregate, and will cause an error when attempting to load/compose the
aggregate.

This can happen because references encapsulate just the tree whose
root is targetted in the reference - no other scene description in the
referenced layer will be composed into the aggregate. So if some
descendant prim of the referenced root targets a relationship to
another tree in the same layer, that relationship would dangle, and
the client will error in GetTargets() or GetForwardedTargets() .

Authoring targets to objects within masters is not allowed, since
master prims do not have a stable identity across runs. Consumers must
author targets to the object within an instance instead.

Relationships authored in a descendent prim of a referenced prim may
not target the referenced prim itself or any of its immediate child
properties if the referencing prim is instanceable. Allowing this
would break the ability for this relationship to be instanced and
shared by multiple instances  it would force consumers of
relationships within masters to resolve targets in the context of each
of that master's instances.

Relationship Forwarding
=======================

Because a relationship can target another relationship, we can and do
provide the ability to resolve chained or *forwarded* relationships.
This can be useful in several situations, including:

   - Combining relationships with VariantSets to create
     demultiplexers. A prim can host a relationship that serves as a
     "binding post" for other prims to target. The prim also hosts a
     "bindingVariant" UsdVariantSet whose variants each modulate the target
     of the binding-post relationship. We can now change the *forwarded*
     target of all prims targetting the binding-post by simply switching
     the bindingVariant VariantSet. We will work through this example in
     the USD reference manual.

   - Defining a relationship as part of a model's interface (so that
     it can be targetted in model hierarchy with no models loaded), which,
     inside the model's payload, forwards to prims useful to a client, the
     set of which may vary depending on the model's configured VariantSets.


"""
   result["Relationship"].GetForwardedTargets.im_func.func_doc = """GetForwardedTargets(targets) -> USD_API bool

targets : SdfPathVector


Compose this relationship's *ultimate* targets, taking into account
"relationship forwarding", and fill C{targets} with the result.


All preexisting elements in C{targets} are lost. This method never
inserts relationship paths in C{targets}.

When composition errors occur, continue to collect successfully
composed targets, but return false to indicate to the caller that
errors occurred.

When a forwarded target cannot be determined, e.g. due to a
composition error, no value is returned for that target; the
alternative would be to return the relationship path at which the
forwarded targets could not be composed, however this would require
all callers of GetForwardedTargets() to account for unexpected
relationship paths being returned with the expected target results.
For example, a particular caller may expect only prim paths in the
target vector, but when composition errors occur, relationships would
be included, potentially triggering additional down stream errors.

See Relationship Forwarding for details on the semantics.

The result is not cached, so will be recomputed on every query.

"""
   result["Relationship"].BlockTargets.im_func.func_doc = """BlockTargets() -> USD_API bool



Clears all target edits from the current EditTarget, and makes the
opinion explicit, which means we are effectively resetting the
composed value of the targets list to empty.

"""
   result["Relationship"].__init__.im_func.func_doc = """__init__()



Construct an invalid relationship.


----------------------------------------------------------------------
__init__(prim, proxyPrimPath, relName)

prim : _PrimDataHandle
proxyPrimPath : SdfPath
relName : TfToken


----------------------------------------------------------------------
__init__(objType, prim, proxyPrimPath, propName)

objType : ObjType
prim : _PrimDataHandle
proxyPrimPath : SdfPath
propName : TfToken

"""
   result["Relationship"].RemoveTarget.im_func.func_doc = """RemoveTarget(target) -> USD_API bool

target : SdfPath


Removes C{target} from the list of targets.


Passing paths to master prims or any other objects in masters will
cause an error to be issued. It is not valid to author targets to
these objects.

"""
   result["Relationship"].HasAuthoredTargets.im_func.func_doc = """HasAuthoredTargets() -> USD_API bool



Returns true if any target path opinions have been authored.


Note that this may include opinions that clear targets and may not
indicate that target paths will exist for this relationship.

"""
   result["Relationship"].GetTargets.im_func.func_doc = """GetTargets(targets) -> USD_API bool

targets : SdfPathVector


Compose this relationship's targets and fill C{targets} with the
result.


All preexisting elements in C{targets} are lost.

See Relationship Targets and Attribute Connections for details on
behavior when targets point to objects beneath instance prims.

The result is not cached, so will be recomputed on every query.

"""
   result["Relationship"].ClearTargets.im_func.func_doc = """ClearTargets(removeSpec) -> USD_API bool

removeSpec : bool


Remove all opinions about the target list from the current edit
target.


Only remove the spec if C{removeSpec} is true (leave the spec to
preserve meta-data we may have intentionally authored on the
relationship)

"""
   result["Relationship"].SetTargets.im_func.func_doc = """SetTargets(targets) -> USD_API bool

targets : SdfPathVector


Make the authoring layer's opinion of the targets list explicit, and
set exactly to C{targets}.


Passing paths to master prims or any other objects in masters will
cause an error to be issued. It is not valid to author targets to
these objects.

If any target in C{targets} is invalid, no targets will be authored
and this function will return false.

"""
   result["Relationship"].AddTarget.im_func.func_doc = """AddTarget(target, position) -> USD_API bool

target : SdfPath
position : ListPosition


Adds C{target} to the list of targets, in the position specified by
C{position}.


Passing paths to master prims or any other objects in masters will
cause an error to be issued. It is not valid to author targets to
these objects.

What data this actually authors depends on what data is currently
authored in the authoring layer, with respect to list-editing
semantics, which we will document soon

"""
   result["SchemaBase"].__doc__ = """
The base class for all schema types in Usd.


Schema objects hold a UsdPrim internally and provide a layer of
specific named API atop the underlying scene graph.

Schema objects are polymorphic but they are intended to be created as
automatic local variables, so they may be passed and returned by-
value. This leaves them subject to slicing. This means that if one
passes a C{SpecificSchema} instance to a function that takes a
UsdSchemaBase *by-value*, all the polymorphic behavior specific to
C{SpecificSchema} is lost.

To avoid slicing, it is encouraged that functions taking schema object
arguments take them by C{const&} if const access is sufficient,
otherwise by non-const pointer.

"""
   result["SchemaBase"].GetSchemaClassPrimDefinition.im_func.func_doc = """GetSchemaClassPrimDefinition() -> USD_API SdfPrimSpecHandle



Return the prim definition associated with this schema instance if one
exists, otherwise return null.


This does not use the held prim's type. To get the held prim
instance's definition, use UsdPrim::GetPrimDefinition() .

UsdPrim::GetPrimDefinition()

"""
   result["SchemaBase"].IsMultipleApplyAPISchema.im_func.func_doc = """IsMultipleApplyAPISchema() -> bool



Returns whether this is an applied API schema or not.


If this returns true the constructor, Get and Apply methods of this
class will take in the name of the API schema instance.

"""
   result["SchemaBase"].GetSchemaType.im_func.func_doc = """GetSchemaType() -> SchemaType


"""
   result["SchemaBase"].IsConcrete.im_func.func_doc = """IsConcrete() -> bool



Returns whether or not this class corresponds to a concrete
instantiable prim type in scene description.


If this is true, GetStaticPrimDefinition() will return a valid prim
definition with a non-empty typeName.

"""
   result["SchemaBase"].GetPath.im_func.func_doc = """GetPath() -> SdfPath



Shorthand for GetPrim() -> GetPath() .

"""
   result["SchemaBase"].IsAppliedAPISchema.im_func.func_doc = """IsAppliedAPISchema() -> bool



Returns whether this is an applied API schema or not.


If this returns true this class will have an Apply() method

"""
   result["SchemaBase"].IsTyped.im_func.func_doc = """IsTyped() -> bool



Returns whether or not this class inherits from UsdTyped.


Types which inherit from UsdTyped can impart a typename on a UsdPrim.

"""
   result["SchemaBase"].IsAPISchema.im_func.func_doc = """IsAPISchema() -> bool



Returns whether this is an API schema or not.

"""
   result["SchemaBase"].GetPrim.im_func.func_doc = """GetPrim() -> Prim



Return this schema object's held prim.

"""
   result["SchemaBase"].GetSchemaAttributeNames.func_doc = """**static** GetSchemaAttributeNames(includeInherited) -> TfTokenVector

includeInherited : bool

"""
   result["SchemaBase"].__init__.im_func.func_doc = """__init__(prim) -> USD_API

prim : Prim


Construct and store C{prim} as the held prim.


----------------------------------------------------------------------
__init__(otherSchema) -> USD_API

otherSchema : SchemaBase


Construct and store for the same prim held by C{otherSchema}.

"""