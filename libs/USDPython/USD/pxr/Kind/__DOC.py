def Execute(result):
   result["__doc__"] = """
The Kind module provides a runtime-extensible taxonomy known as
"kinds".

Kinds are just TfToken symbols, but the KindRegistry allows for
organizing kinds into taxonomies of related/refined concepts, and the
KindRegistry::GetBaseKind() and KindRegistry::IsA() queries enable
reasoning about the hierarchy and classifying objects by kind.

Kinds are useful for classifying scenegraph objects, such as by
tagging objects representing the roots of models with the kind of
model it represents; it is scenegraph taxonomy that motivates the
"builtin" kind hierarchy.

The Core Kind Hierarchy
=======================

The KindRegistry begins its life pre-loaded with the following
hierarchy of kinds that define our concept of "model hierarchy", which
is so central to our organization and discovery of scene description.
Of course, as described in the next section, unlimited new, entirely
unrelated taxonomies can be created by extension.
   - B{model} - Everything in the model hierarchy is a kind of model.
   - B{component} - A component model is a terminal model in the model
     hierarchy - it can have no child models.

   - B{group} - a model that is simply a container for other models.
   - B{assembly} - An "important" group model - often because it is
     itself a published asset.

   - B{subcomponent} - Within a component model, subcomponents
     identify important (generally articulable) sub-trees. Subcomponents
     are "stopping points" when dynamically unrolling/expanding a
     component.

Extending the KindRegistry
==========================

The kind registry can be *extended* using the facilities provided by
PlugRegistry, by adding a 'Kinds' sub-dictionary to the
*plugInfo.json* file of any module within your "pixar-base aware"
build environment. The dictionary entries will look like the
following: ::

  "Kinds": {
      "chargroup": {
          "baseKind": "assembly",
          "description": "A chargroup is an assembly comprised of a single character plus some associated models 
--
 typically hair, garments, and charprops."
      },
      "charprop": {
          "baseKind": "component"
      },
      "newRootKind": {
      }
  },

One cannot alter core kinds or their place in the hierarchy or any
other data associated with them by attempting to override them in the
extension file. Attempting to do so will result in a registration
error.

"""
   result["Registry"].__doc__ = """
A singleton that holds known kinds and information about them.


See Kind Overview for a description of why kind exists, what the
builtin registered kinds are, and how to extend the core kinds.

KindRegistry Threadsafty
========================

KindRegistry serves performance-critical clients that operate under
the stl threading model, and therefore itself follows that model in
order to avoid locking during HasKind() and IsA() queries.

To make this robust, KindRegistry exposes no means to mutate the
registry. All extensions must be accomplished via plugInfo.json files,
which are consumed once during the registry initialization (See
Extending the KindRegistry)

"""
   result["Registry"].GetAllKinds.func_doc = """**static** GetAllKinds() -> KIND_API sequence< TfToken >



Return an unordered vector of all kinds known to the registry.

"""
   result["Registry"].HasKind.func_doc = """**static** HasKind(kind) -> KIND_API bool

kind : TfToken


Test whether *kind* is known to the registry.

"""
   result["Registry"].GetBaseKind.func_doc = """**static** GetBaseKind(kind) -> KIND_API TfToken

kind : TfToken


Return the base kind of the given kind.


If there is no base, the result will be an empty token. Issues a
coding error if *kind* is unknown to the registry.

"""
   result["Registry"].IsA.func_doc = """**static** IsA(derivedKind, baseKind) -> KIND_API bool

derivedKind : TfToken
baseKind : TfToken


Test whether *derivedKind* is the same as *baseKind* or has it as a
base kind (either directly or indirectly).


It is *not* required that *derivedKind* or *baseKind* be known to the
registry: if they are unknown but equal, IsA will return C{true};
otherwise if either is unknown, we will simply return false.

Therefore this method will not raise any errors.

"""
   result["Registry"].__init__.im_func.func_doc = """__init__()


"""