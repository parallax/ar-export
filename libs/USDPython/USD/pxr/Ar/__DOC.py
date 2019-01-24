def Execute(result):
   result["ResolverContextBinder"].__doc__ = """
Helper object for managing the binding and unbinding of
ArResolverContext objects with the asset resolver.



Asset Resolver Context Operations

"""
   result["ResolverContextBinder"].__init__.im_func.func_doc = """__init__(context) -> AR_API

context : ResolverContext


Bind the given C{context} with the asset resolver.


Calls ArResolver::BindContext on the configured asset resolver and
saves the bindingData populated by that function.


----------------------------------------------------------------------
__init__(assetResolver, context) -> AR_API

assetResolver : Resolver
context : ResolverContext


Bind the given C{context} to the given C{assetResolver}.


Calls ArResolver::BindContext on the given C{assetResolver} and saves
the bindingData populated by that function.

"""
   result["ResolverScopedCache"].__doc__ = """
Helper object for managing asset resolver cache scopes.


A scoped resolution cache indicates to the resolver that results of
calls to Resolve should be cached for a certain scope. This is
important for performance and also for consistency  it ensures that
repeated calls to Resolve with the same parameters will return the
same result.

Scoped Resolution Cache

"""
   result["ResolverScopedCache"].__init__.im_func.func_doc = """__init__() -> AR_API



Begin an asset resolver cache scope.


Calls ArResolver::BeginCacheScope on the configured asset resolver and
saves the cacheScopeData populated by that function.


----------------------------------------------------------------------
__init__(parent) -> AR_API

parent : ResolverScopedCache


Begin an asset resolver cache scope that shares data with the given
C{parent} scope.


Calls ArResolver::BeginCacheScope on the configured asset resolver,
saves the cacheScopeData stored in C{parent} and passes that to that
function.

"""
   result["GetResolver"].func_doc = """GetResolver() -> AR_API ArResolver



Returns the configured asset resolver.


When first called, this function will determine the ArResolver
subclass to use for asset resolution via the following process:

   - If a preferred resolver has been set via ArSetPreferredResolver,
     it will be selected.

   - Otherwise, a list of available ArResolver subclasses in plugins
     will be generated. If multiple ArResolver subclasses are found, the
     list will be sorted by typename. ArDefaultResolver will be added as
     the last element of this list, and the first resolver in the list will
     be selected.

   - The plugin for the selected subclass will be loaded and an
     instance of the subclass will be constructed.

   - If an error occurs, an ArDefaultResolver will be constructed.

The constructed ArResolver subclass will be cached and used to service
function calls made on the returned resolver.

Note that this function may not return the constructed subclass
itself, meaning that dynamic casts to the subclass type may fail. See
ArGetUnderlyingResolver if access to this object is needed.

"""
   result["SplitPackageRelativePathInner"].func_doc = """SplitPackageRelativePathInner(path) -> AR_API pair<string, string>

path : string


Split package-relative path C{path} into a (package path, packaged
path) pair.


If C{packageRelativePath} contains nested package-relative paths the
package path will be the outermost package-relative path, and the
packaged path will be the innermost packaged path. ::

  ArSplitPackageRelativePathInner("a.pack[b.pack]")
     => ("a.pack", "b.pack")
  
  ArSplitPackageRelativePathInner("a.pack[b.pack[c.pack]]")
     => ("a.pack[b.pack]", "c.pack")


"""
   result["__doc__"] = """

Overview
========

The Ar (asset resolution) module provides functions for interacting
with asset paths in USD. An asset path is a string that describes the
location of an asset in a user's system. These paths are used
extensively throughout USD; for example, asset paths are used to
specify sublayers, references, and other composition arcs in scene
description.

Ar's primary responsibility is to 'resolve' an asset path into a
corresponding filesystem path. By default, Ar assumes that all asset
paths are simple filesystem paths and treats them accordingly.
However, clients may implement their own resolver class by
implementing the ArResolver interface to provide custom resolution
logic for asset paths. This allows clients to use asset paths that are
appropriate for their situation.

For example, a client might have an asset management system that uses
URLs to identify assets. That client could implement a custom resolver
that would resolve those URLs and fetch data from a server to the
local filesystem and return that filesystem path as the 'resolved'
path. This would enable the client to use these URLs in scene
description (e.g., for referencing) for USD.

Accessing the Resolver
======================

Consumers may access the asset resolver by calling ArGetResolver.

Default Resolver
================

If no custom implementation of ArResolver is found, Ar will fall back
to using an ArDefaultResolver, which assumes all asset paths it
encounters are filesystem paths. ArDefaultResolver also performs
simple search path-based resolution that will search for an asset in a
specified list of directories. See documentation on ArDefaultResolver
for more information on configuring this behavior.

Implementing a Custom Resolver
==============================

To implement a custom asset resolver, users must create a plugin
containing a subclass of ArResolver. This subclass must be registered
with the plugin system so that it can be discovered and instantiated
at runtime. Keep in mind that the subclass may be constructed at any
time; at a minimum, the subclass will be constructed during the first
call to ArGetResolver.

   - Implement an ArResolver subclass ::

  class CustomResolver : public ArResolver {
      // ...
  }

   - In its implementation, register the ArResolver subclass with the
     TfType system using AR_DEFINE_RESOLVER ::

  # custom resolver's .cpp file
  AR_DEFINE_RESOLVER(CustomResolver, ArResolver);

   - Declare the ArResolver subclass in the plugin's plugInfo.json
     file. See PlugRegistry for more details. ::

  # plugInfo.json
  {
      "Plugins": [
          {
              "Info": {
                  "Types" : {
                      "CustomResolver" : {
                          "bases": [ "ArResolver" ]
                      }
                  }
              },
              ... 
          },
          ...
      ]
  
  }

   - Ensure that the resolver plugin is located where the plugin
     system can find it.

Ar does not support custom resolvers implemented in Python to avoid
performance issues, especially for multi-threaded consumers.

Resolver Context Objects
========================

Each custom resolver can reason about its own ArResolverContext type,
which allows a single process to access multiple different state-sets
(contexts) to guide asset resolution differently for different
datasets/contexts.

Users may declare that a particular object type may be used as a
context object by using AR_DECLARE_RESOLVER_CONTEXT. This allows
ArResolverContext objects to be constructed from objects of this type.

Resolver Scoped Caches
======================

Since resolving assets to filesystem paths can be expensive, and
typically clients (such as USD) will commonly attempt to resolve the
same assets over and over again, we also provide an RAII
ArResolverScopedCache that can greatly speed up asset resolution by
caching results. See ArDefaultResolver for an example implementation.

"""
   result["DefaultResolver"].__doc__ = """
Default asset resolution implementation used when no plugin
implementation is provided.


In order to resolve assets specified by relative paths, this resolver
implements a simple "search path" scheme. The resolver will anchor the
relative path to a series of directories and return the first absolute
path where the asset exists.

The first directory will always be the current working directory. The
resolver will then examine the directories specified via the following
mechanisms (in order):

   - The currently-bound ArDefaultResolverContext for the calling
     thread

   - ArDefaultResolver::SetDefaultSearchPath

   - The environment variable PXR_AR_DEFAULT_SEARCH_PATH. This is
     expected to be a list of directories delimited by the platform's
     standard path separator.


"""
   result["DefaultResolver"].GetCurrentContext.im_func.func_doc = """GetCurrentContext() -> AR_API ArResolverContext



Returns the currently-bound asset resolver context.



ArResolver::BindContext, ArResolver::UnbindContext

"""
   result["DefaultResolver"].ConfigureResolverForAsset.im_func.func_doc = """ConfigureResolverForAsset(path) -> AR_API void

path : string


Sets the resolver's default context (returned by
CreateDefaultContext() ) to the same context you would get by calling
CreateDefaultContextForAsset() .


Has no other effect on the resolver's configuration.

"""
   result["DefaultResolver"].CreateDefaultContextForAsset.im_func.func_doc = """CreateDefaultContextForAsset(filePath) -> AR_API ArResolverContext

filePath : string


Creates a context that adds the directory containing C{filePath} as a
first directory to be searched, when the resulting context is bound (.



ArResolverContextBinder).  If C{filePath} is empty, returns an empty
context; otherwise, if C{filePath} is not an absolute filesystem path,
it will first be anchored to the process's current working directory.

"""
   result["DefaultResolver"].SetDefaultSearchPath.func_doc = """**static** SetDefaultSearchPath(searchPath) -> AR_API void

searchPath : sequence<string>


Set the default search path that will be used during asset resolution.


This must be called before the first call to ArGetResolver. The
specified paths will be searched *in addition to, and before* paths
specified via the environment variable PXR_AR_DEFAULT_SEARCH_PATH

"""
   result["DefaultResolver"].Resolve.im_func.func_doc = """Resolve(path) -> AR_API string

path : string


Returns the resolved filesystem path for the file identified by the
given C{path} if it exists.


If the file does not exist, returns an empty string.

"""
   result["DefaultResolver"].GetExtension.im_func.func_doc = """GetExtension(path) -> AR_API string

path : string


Returns the normalized extension for the given C{path}.

"""
   result["DefaultResolver"].AnchorRelativePath.im_func.func_doc = """AnchorRelativePath(anchorPath, path) -> AR_API string

anchorPath : string
path : string


Returns the path formed by anchoring C{path} to C{anchorPath}.


If C{anchorPath} ends with a trailing '/', it is treated as a
directory to which C{path} will be anchored. Otherwise, it is treated
as a file and C{path} will be anchored to its containing directory.

If C{anchorPath} is empty, C{path} will be returned as-is.

If C{path} is empty or not a relative path, it will be returned as-is.

"""
   result["DefaultResolver"].CreateDefaultContext.im_func.func_doc = """CreateDefaultContext() -> AR_API ArResolverContext



Return a default ArResolverContext that may be bound to this resolver
to resolve assets when no other context is explicitly specified.


This function should not automatically bind this context, but should
create one that may be used later.

"""
   result["JoinPackageRelativePath"].func_doc = """JoinPackageRelativePath(paths) -> AR_API string

paths : sequence<string>


Combines the given C{paths} into a single package-relative path,
nesting paths as necessary.

::

  ArJoinPackageRelativePath(["a.pack", "b.pack"])
     => "a.pack[b.pack]"
  
  ArJoinPackageRelativePath(["a.pack", "b.pack", "c.pack"])
     => "a.pack[b.pack[c.pack]]"
  
  ArJoinPackageRelativePath(["a.pack[b.pack]", "c.pack"])
     => "a.pack[b.pack[c.pack]]"



----------------------------------------------------------------------
JoinPackageRelativePath(paths) -> AR_API string

paths : pair<string, string>


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
JoinPackageRelativePath(packagePath, packagedPath) -> AR_API string

packagePath : string
packagedPath : string


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Resolver"].__doc__ = """
Interface for the asset resolution system.


An asset resolver is responsible for resolving asset information
(including the asset's physical path) from a logical path.

See Implementing a Custom Resolver for information on how to customize
asset resolution behavior by implementing a subclass of ArResolver.
Clients may use ArGetResolver to access the configured asset resolver.

"""
   result["Resolver"].CreateDefaultContextForAsset.im_func.func_doc = """CreateDefaultContextForAsset(filePath) -> AR_API ArResolverContext

filePath : string


Return a default ArResolverContext that may be bound to this resolver
to resolve the asset located at C{filePath} when no other context is
explicitly specified.


This function should not automatically bind this context, but should
create one that may be used later.

"""
   result["Resolver"].ConfigureResolverForAsset.im_func.func_doc = """ConfigureResolverForAsset(path) -> AR_API void

path : string


Configures the resolver for a given asset path.

"""
   result["Resolver"].Resolve.im_func.func_doc = """Resolve(path) -> AR_API string

path : string


Returns the resolved filesystem path for the file identified by the
given C{path} if it exists.


If the file does not exist, returns an empty string.

"""
   result["Resolver"].GetExtension.im_func.func_doc = """GetExtension(path) -> AR_API string

path : string


Returns the normalized extension for the given C{path}.

"""
   result["Resolver"].AnchorRelativePath.im_func.func_doc = """AnchorRelativePath(anchorPath, path) -> AR_API string

anchorPath : string
path : string


Returns the path formed by anchoring C{path} to C{anchorPath}.


If C{anchorPath} ends with a trailing '/', it is treated as a
directory to which C{path} will be anchored. Otherwise, it is treated
as a file and C{path} will be anchored to its containing directory.

If C{anchorPath} is empty, C{path} will be returned as-is.

If C{path} is empty or not a relative path, it will be returned as-is.

"""
   result["Resolver"].GetCurrentContext.im_func.func_doc = """GetCurrentContext() -> AR_API ArResolverContext



Returns the currently-bound asset resolver context.



ArResolver::BindContext, ArResolver::UnbindContext

"""
   result["Resolver"].CreateDefaultContext.im_func.func_doc = """CreateDefaultContext() -> AR_API ArResolverContext



Return a default ArResolverContext that may be bound to this resolver
to resolve assets when no other context is explicitly specified.


This function should not automatically bind this context, but should
create one that may be used later.

"""
   result["SplitPackageRelativePathOuter"].func_doc = """SplitPackageRelativePathOuter(path) -> AR_API pair<string, string>

path : string


Split package-relative path C{path} into a (package path, packaged
path) pair.


If C{packageRelativePath} contains nested package-relative paths the
package path will be the outermost package path, and the packaged path
will be the inner package-relative path. ::

  ArSplitPackageRelativePathOuter("a.pack[b.pack]")
     => ("a.pack", "b.pack")
  
  ArSplitPackageRelativePathOuter("a.pack[b.pack[c.pack]]")
     => ("a.pack", "b.pack[c.pack]")


"""
   result["IsPackageRelativePath"].func_doc = """IsPackageRelativePath(path) -> AR_API bool

path : string


Return true if C{path} is a package-relative path, false otherwise.

"""
   result["GetUnderlyingResolver"].func_doc = """GetUnderlyingResolver() -> AR_API ArResolver



Returns the underlying ArResolver instance used by ArGetResolver.


This function returns the instance of the ArResolver subclass used by
ArGetResolver and can be dynamic_cast to that type.

This functions should typically not be used by consumers except in
very specific cases. Consumers who want to retrieve an ArResolver to
perform asset resolution should use ArGetResolver.

"""
   result["DefaultResolverContext"].__doc__ = """
Resolver context object that specifies a search path to use during
asset resolution.


This object is intended for use with the default ArDefaultResolver
asset resolution implementation; see documentation for that class for
more details on the search path resolution algorithm.

Example usage: ::

  ArDefaultResolverContext ctx({"/Local/Models", "/Installed/Models"});
  {
      // Bind the context object:
      ArResolverContextBinder binder(ctx);
  
     // While the context is bound, all calls to ArResolver::Resolve
     // (assuming ArDefaultResolver is the underlying implementation being
     // used) will include the specified paths during resolution.
     std::string resolvedPath = resolver.Resolve("ModelName/File.txt")
  }
  
  // Once the context is no longer bound (due to the ArResolverContextBinder
  // going out of scope), its search path no longer factors into asset
  // resolution.


"""
   result["DefaultResolverContext"].GetSearchPath.im_func.func_doc = """GetSearchPath() -> sequence<string>



Return this context's search path.

"""
   result["DefaultResolverContext"].__init__.im_func.func_doc = """__init__()



Default construct a context with no search path.


----------------------------------------------------------------------
__init__(searchPath) -> AR_API

searchPath : sequence<string>


Construct a context with the given C{searchPath}.


Elements in C{searchPath} should be absolute paths. If they are not,
they will be anchored to the current working directory.

"""
   result["SetPreferredResolver"].func_doc = """SetPreferredResolver(resolverTypeName) -> AR_API void

resolverTypeName : string


Set the preferred ArResolver subclass used by ArGetResolver.


Consumers may override ArGetResolver's plugin resolver discovery and
force the use of a specific resolver subclass by calling this function
with the typename of the implementation to use.

If the subclass specified by C{resolverTypeName} cannot be found,
ArGetResolver will issue a warning and fall back to using
ArDefaultResolver.

This must be called before the first call to ArGetResolver.

"""