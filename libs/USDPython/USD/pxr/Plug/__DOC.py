def Execute(result):
   result["Plugin"].__doc__ = """
Defines an interface to registered plugins.


Plugins are registered using the interfaces in C{PlugRegistry}.

For each registered plugin, there is an instance of C{PlugPlugin}
which can be used to load and unload the plugin and to retrieve
information about the classes implemented by the plugin.

"""
   result["Plugin"].FindPluginResource.im_func.func_doc = """FindPluginResource(path, verify) -> PLUG_API string

path : string
verify : bool


Find a plugin resource by absolute or relative path optionally
verifying that file exists.


If verification fails an empty path is returned. Relative paths are
relative to the plugin's resource path.

"""
   result["Plugin"].DeclaresType.im_func.func_doc = """DeclaresType(type, includeSubclasses) -> PLUG_API bool

type : TfType
includeSubclasses : bool


Returns true if C{type} is declared by this plugin.


If C{includeSubclasses} is specified, also returns true if any
subclasses of C{type} have been declared.

"""
   result["Plugin"].GetMetadataForType.im_func.func_doc = """GetMetadataForType(type) -> PLUG_API JsObject

type : TfType


Returns the metadata sub-dictionary for a particular type.

"""
   result["Plugin"].MakeResourcePath.im_func.func_doc = """MakeResourcePath(path) -> PLUG_API string

path : string


Build a plugin resource path by returning a given absolute path or
combining the plugin's resource path with a given relative path.

"""
   result["Plugin"].Load.im_func.func_doc = """Load() -> PLUG_API bool



Loads the plugin.


This is a noop if the plugin is already loaded.

"""
   result["__doc__"] = """

Overview
========

Provides generic interface classes to implement a plug-in framework.
The PlugPlugin class defines the interface to plug-in modules. The
PlugRegistry class defines a mechanism for registering plug-in modules
and provides an interface for abstract plug-in base classes from which
you instantiate concrete plug-in subclasses.

The PlugPlugin class contains properties that indicate whether or not
a plug-in is currently loaded and whether a plug-in is a Python module
or not. It also includes functions that return a plug-in's name,
location in the file system, the names of its base classes, its
metadata, and any existing dependencies.

The PlugRegistry class includes methods that provides a way of
registering plug-ins with the system by providing one or more paths to
plugInfo.json files. Other methods provide different ways to get
references to registered plug-ins and get metadata for plug-ins.

For information on how to add concrete plug-in types to applications
like Presto, see the API documentation for the modules that
implement functionality for those types of components. For example,
the Mf module includes functions for registering prim plug-ins; the
Wd module includes functions for registering GUI components such as
editor plug-ins.

Metadata
========

Plugins are found and described using plugInfo.json files that may be
read without loading the plugin. The structure of a plugInfo.json file
is described in detail in the PlugRegistry class.

"""
   result["Registry"].__doc__ = """
Defines an interface for registering plugins.


PlugRegistry maintains a registry of plug-ins known to the system and
provides an interface for base classes to load any plug-ins required
to instantiate a subclass of a given type.

Defining a Base Class API
=========================

In order to use this facility you will generally provide a module
which defines the API for a plug-in base class. This API will be
sufficient for the application or framework to make use of custom
subclasses that will be written by plug-in developers.

For example, if you have an image processing application, you might
want to support plug-ins that implement image filters. You can define
an abstract base class for image filters that declares the API your
application will require image filters to implement; perhaps something
simple like C++ Code Example 1 (Doxygen only).

People writing custom filters would write a subclass of ImageFilter
that overrides the two methods, implementing their own special
filtering behavior.

Enabling Plug-in Loading for the Base Class
===========================================

In order for ImageFilter to be able to load plug-ins that implement
these custom subclasses, it must be registered with the TfType system.

The ImageFilter base class, as was mentioned earlier, should be made
available in a module that the application links with. This is done
so that plug-ins that want to provide ImageFilters can also link with
the module allowing them to subclass ImageFilter.

Registering Plug-ins
====================

A plug-in developer can now write plug-ins with ImageFilter
subclasses. Plug-ins can be implemented either as native dynamic
modules (either regular dynamic modules or framework bundles) or
as Python modules.

Plug-ins must be registered with the registry. All plugins are
registered via RegisterPlugins() . Plug-in Python modules must be
directly importable (in other words they must be able to be found in
Python's module path.) Plugins are registered by providing a path or
paths to JSON files that describe the location, structure and contents
of the plugin. The standard name for these files in plugInfo.json.

Typically, the application that hosts plug-ins will locate and
register plug-ins at startup.

The plug-in facility is lazy. It does not dynamically load code from
plug-in bundles until that code is required.

plugInfo.json
=============

A plugInfo.json file has the following structure: ::

  {
      # Comments are allowed and indicated by a hash at the start of a
      # line or after spaces and tabs.  They continue to the end of line.
      # Blank lines are okay, too.
  
      # This is optional.  It may contain any number of strings.
      #   Paths may be absolute or relative.
      #   Paths ending with slash have plugInfo.json appended automatically.
      #   '*' may be used anywhere to match any character except slash.
      #   '**' may be used anywhere to match any character including slash.
      "Includes": [
          "/absolute/path/to/plugInfo.json",
          "/absolute/path/to/custom.filename",
          "/absolute/path/to/directory/with/plugInfo/",
          "relative/path/to/plugInfo.json",
          "relative/path/to/directory/with/plugInfo/",
          "glob*/pa*th/*to*/*/plugInfo.json",
          "recursive/pa**th/**/"
      ],
  
      # This is optional.  It may contain any number of objects.
      "Plugins": [
          {
              # Type is required and may be "module", "python" or "resource".
              "Type": "module",
  
              # Name is required.  It should be the Python module name,
              # the shared module name, or a unique resource name.
              "Name": "myplugin",
  
              # Root is optional.  It defaults to ".".
              # This gives the path to the plugin as a whole if the plugin
              # has substructure.  For Python it should be the directory
              # with the __init__.py file.  The path is usually relative.
              "Root": ".",
  
              # LibraryPath is required by Type "module" and unused
              # otherwise.  It gives the path to the shared module
              # object, either absolute or relative to Root.
              "LibraryPath": "libmyplugin.so",
  
              # ResourcePath is option.  It defaults to ".".
              # This gives the path to the plugin's resources directory.
              # The path is either absolute or relative to Root.
              "ResourcePath": "resources",
  
              # Info is required.  It's described below.
              "Info": {
                  # Plugin contents.
              }
          }
      ]
  }

As a special case, if a plugInfo.json contains an object that doesn't
have either the "Includes" or "Plugins" keys then it's as if the
object was in a "Plugins" array.

Advertising a Plug-in's Contents
================================

Once the plug-ins are registered, the plug-in facility must also be
able to tell what they contain. Specifically, it must be able to find
out what subclasses of what plug-in base classes each plug-in
contains. Plug-ins must advertise this information through their
plugInfo.json file in the "Info" key. In the "Info" object there
should be a key "Types" holding an object.

This "Types" object's keys are names of subclasses and its values are
yet more objects (the subclass meta-data objects). The meta-data
objects can contain arbitrary key-value pairs. The plug-in mechanism
will look for a meta-data key called "displayName" whose value should
be the display name of the subclass. The plug-in mechanism will look
for a meta-data key called "bases" whose value should be an array of
base class type names.

For example, a bundle that contains a subclass of ImageFilter might
have a plugInfo.json that looks like the following example. ::

  {
      "Types": {
          "MyCustomCoolFilter" : {
              "bases": ["ImageFilter"],
              "displayName": "Add Coolness to Image"
              # other arbitrary metadata for MyCustomCoolFilter here
          }
      }
  }

What this says is that the plug-in contains a type called
MyCustomCoolFilter which has a base class ImageFilter and that this
subclass should be called "Add Coolness to Image" in user-visible
contexts.

In addition to the "displayName" meta-data key which is actually known
to the plug-in facility, you may put whatever other information you
want into a class' meta-data dictionary. If your plug-in base class
wants to define custom keys that it requires all subclasses to
provide, you can do that. Or, if a plug-in writer wants to define
their own keys that their code will look for at runtime, that is OK as
well.

Working with Subclasses of a Plug-in Base Class
===============================================

Most code with uses types defined in plug-ins doesn't deal with the
Plug API directly. Instead, the TfType interface is used to lookup
types and to manufacture instances. The TfType interface will take
care to load any required plugins.

To wrap up our example, the application that wants to actually use
ImageFilter plug-ins would probably do a couple of things. First, it
would get a list of available ImageFilters to present to the user.
This could be accomplished as shown in Python Code Example 2 (Doxygen
only).

Then, when the user picks a filter from the list, it would manufacture
and instance of the filter as shown in Python Code Example 3 (Doxygen
only).

As was mentioned earlier, this plug-in facility tries to be as lazy as
possible about loading the code associated with plug-ins. To that end,
loading of a plugin will be deferred until an instance of a type is
manufactured which requires the plugin.

Multiple Subclasses of Multiple Plug-in Base Classes
====================================================

It is possible for a bundle to implement multiple subclasses for a
plug-in base class if desired. If you want to package half a dozen
ImageFilter subclasses in one bundle, that will work fine. All must be
declared in the plugInfo.json.

It is possible for there to be multiple classes in your application or
framework that are plug-in base classes. Plug-ins that implement
subclasses of any of these base classes can all coexist. And, it is
possible to have subclasses of multiple plug-in base classes in the
same bundle.

When putting multiple subclasses (of the same or different base
classes) in a bundle, keep in mind that dynamic loading happens for
the whole bundle the first time any subclass is needed, the whole
bundle will be loaded. But this is generally not a big concern.

For example, say the example application also has a plug-in base class
"ImageCodec" that allows people to add support for reading and writing
other image formats. Imagine that you want to supply a plug-in that
has two codecs and a filter all in a single plug-in. Your
plugInfo.json "Info" object might look something like this example. ::

  {
      "Types": {
          "MyTIFFCodec": {
              "bases": ["ImageCodec"],
              "displayName": "TIFF Image"
          },
          "MyJPEGCodec": {
              "bases": ["ImageCodec"],
              "displayName": "JPEG Image"
          },
          "MyCustomCoolFilter" : {
              "bases": ["ImageFilter"],
              "displayName": "Add Coolness to Image"
          }
      }
  }

Dependencies on Other Plug-ins
==============================

If you write a plug-in that has dependencies on another plug-in that
you cannot (or do not want to) link against statically, you can
declare the dependencies in your plug-in's plugInfo.json. A plug-in
declares dependencies on other classes with a PluginDependencies key
whose value is a dictionary. The keys of the dictionary are plug-in
base class names and the values are arrays of subclass names.

The following example contains an example of a plug-in that depends on
two classes from the plug-in in the previous example. ::

  {
      "Types": {
          "UltraCoolFilter": {
              "bases": ["MyCustomCoolFilter"],
              "displayName": "Add Unbelievable Coolness to Image"
              # A subclass of MyCustomCoolFilter that also uses MyTIFFCodec
          }
      },
      "PluginDependencies": {
          "ImageFilter": ["MyCustomCoolFilter"],
          "ImageCodec": ["MyTIFFCodec"]
      }
  }

The ImageFilter provided by the plug-in in this example depends on the
other ImageFilter MyCoolImageFilter and the ImageCodec MyTIFFCodec.
Before loading this plug-in, the plug-in facility will ensure that
those two classes are present, loading the plug-in that contains them
if needed.

"""
   result["Registry"].GetDirectlyDerivedTypes.func_doc = """**static** GetDirectlyDerivedTypes(base) -> PLUG_API sequence< TfType >

base : TfType


Return a vector of types derived directly from *base*.


Use this function if you expect that plugins may provide types derived
from *base*. Otherwise, use *TfType::GetDirectlyDerivedTypes*.

"""
   result["Registry"].FindDerivedTypeByName.func_doc = """**static** FindDerivedTypeByName(base, typeName) -> PLUG_API TfType

base : TfType
typeName : string


Retrieve the C{TfType} that derives from C{base} and has the given
alias or type name C{typeName}.


See the documentation for C{TfType::FindDerivedByName} for more
information. Use this function if you expect that the derived type may
be provided by a plugin. Calling this function will incur plugin
discovery (but not loading) if plugin discovery has not yet occurred.


----------------------------------------------------------------------
FindDerivedTypeByName(typeName) -> TfType

typeName : string


Retrieve the C{TfType} that derives from C{Base} and has the given
alias or type name C{typeName}.


See the documentation for C{TfType::FindDerivedByName} for more
information. Use this function if you expect that the derived type may
be provided by a plugin. Calling this function will incur plugin
discovery (but not loading) if plugin discovery has not yet occurred.

"""
   result["Registry"].GetAllPlugins.im_func.func_doc = """GetAllPlugins() -> PLUG_API PlugPluginPtrVector



Returns all registered plug-ins.

"""
   result["Registry"].FindTypeByName.func_doc = """**static** FindTypeByName(typeName) -> PLUG_API TfType

typeName : string


Retrieve the C{TfType} corresponding to the given C{name}.


See the documentation for C{TfType::FindByName} for more information.
Use this function if you expect that C{name} may name a type provided
by a plugin. Calling this function will incur plugin discovery (but
not loading) if plugin discovery has not yet occurred.

"""
   result["Registry"].RegisterPlugins.im_func.func_doc = """RegisterPlugins(pathToPlugInfo) -> PLUG_API PlugPluginPtrVector

pathToPlugInfo : string


Registers all plug-ins discovered at *pathToPlugInfo*.


----------------------------------------------------------------------
RegisterPlugins(pathsToPlugInfo) -> PLUG_API PlugPluginPtrVector

pathsToPlugInfo : sequence<string>


Registers all plug-ins discovered in any of *pathsToPlugInfo*.

"""
   result["Registry"].__init__.im_func.func_doc = """__init__(arg1)

arg1 : Registry


----------------------------------------------------------------------
__init__() -> PLUG_LOCAL


"""
   result["Registry"].GetStringFromPluginMetaData.im_func.func_doc = """GetStringFromPluginMetaData(type, key) -> PLUG_API string

type : TfType
key : string


Looks for a string associated with *type* and *key* and returns it, or
an empty string if *type* or *key* are not found.

"""
   result["Registry"].GetPluginWithName.im_func.func_doc = """GetPluginWithName(name) -> PLUG_API PlugPluginPtr

name : string


Returns a plugin with the specified module name.

"""
   result["Registry"].GetPluginForType.im_func.func_doc = """GetPluginForType(t) -> PLUG_API PlugPluginPtr

t : TfType


Returns the plug-in for the given type, or a null pointer if the is no
registered plug-in.

"""
   result["Registry"].GetAllDerivedTypes.func_doc = """**static** GetAllDerivedTypes(base, result) -> PLUG_API void

base : TfType
result : set< TfType >


Return the set of all types derived (directly or indirectly) from
*base*.


Use this function if you expect that plugins may provide types derived
from *base*. Otherwise, use *TfType::GetAllDerivedTypes*.


----------------------------------------------------------------------
GetAllDerivedTypes(result)

result : set< TfType >


Return the set of all types derived (directly or indirectly) from
*Base*.


Use this function if you expect that plugins may provide types derived
from *base*. Otherwise, use *TfType::GetAllDerivedTypes*.

"""
   result["Notice"].__doc__ = """
Notifications sent by the Plug module.

"""
   result["Notice"].Base.__doc__ = """
Base class for all Plug notices.

"""
   result["Notice"].DidRegisterPlugins.__doc__ = """
Notice sent after new plugins have been registered with the Plug
registry.

"""
   result["Notice"].DidRegisterPlugins.GetNewPlugins.im_func.func_doc = """GetNewPlugins() -> PluginPtrVector


"""
   result["Plugin"].name = property(result["Plugin"].name.fget, result["Plugin"].name.fset, result["Plugin"].name.fdel, """type : string


Returns the plugin's name.

""")
   result["Plugin"].isLoaded = property(result["Plugin"].isLoaded.fget, result["Plugin"].isLoaded.fset, result["Plugin"].isLoaded.fdel, """type : PLUG_API bool


Returns C{true} if the plugin is currently loaded.


Resource plugins always report as loaded.

""")
   result["Plugin"].path = property(result["Plugin"].path.fget, result["Plugin"].path.fset, result["Plugin"].path.fdel, """type : string


Returns the plugin's filesystem path.

""")
   result["Plugin"].isResource = property(result["Plugin"].isResource.fget, result["Plugin"].isResource.fset, result["Plugin"].isResource.fdel, """type : PLUG_API bool


Returns C{true} if the plugin is resource-only.

""")
   result["Plugin"].resourcePath = property(result["Plugin"].resourcePath.fget, result["Plugin"].resourcePath.fset, result["Plugin"].resourcePath.fdel, """type : string


Returns the plugin's resources filesystem path.

""")
   result["Plugin"].metadata = property(result["Plugin"].metadata.fget, result["Plugin"].metadata.fset, result["Plugin"].metadata.fdel, """type : PLUG_API JsObject


Returns the dictionary containing meta-data for the plugin.

""")