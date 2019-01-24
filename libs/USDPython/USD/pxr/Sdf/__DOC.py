def Execute(result):
   result["_DumpPathStats"].func_doc = """_DumpPathStats() -> SDF_API void



Diagnostic output.

"""
   result["GetUnitFromName"].func_doc = """GetUnitFromName(name) -> SDF_API  TfEnum

name : string


Gets a unit for the given /a name.

"""
   result["FindOrOpenRelativeToLayer"].func_doc = """FindOrOpenRelativeToLayer(anchor, layerPath, args) -> SDF_API SdfLayerRefPtr

anchor : LayerHandle
layerPath : string
args : Layer.FileFormatArguments


Returns a layer with the given C{layerPath} relative to the C{anchor}
layer.


This function uses SdfComputeAssetPathRelativeToLayer with C{anchor}
and C{layerPath} to compute the layer path to find or open. See
documentation on that function for more details.

If the C{anchor} layer is invalid, the C{layerPath} pointer is
invalid, or C{layerPath} contains an empty string, a coding error is
raised and a null layer is returned.

"""
   result["LayerBase"].__doc__ = """
Base class for all layer implementations.


Holds a pointer to the file format for the layer.

"""
   result["LayerBase"].GetFileFormat.im_func.func_doc = """GetFileFormat() -> SDF_API SdfFileFormatConstPtr



Returns the file format used by this layer.

"""
   result["LayerBase"].GetFileFormatArguments.im_func.func_doc = """GetFileFormatArguments() -> SDF_API  FileFormatArguments



Returns the file format-specific arguments used during the
construction of this layer.

"""
   result["ValueHasValidType"].func_doc = """ValueHasValidType(value) -> SDF_API bool

value : VtValue


Given a value, returns if there is a valid corresponding valueType.

"""
   result["CreateVariantInLayer"].func_doc = """CreateVariantInLayer(layer, primPath, variantSetName, variantName) -> SDF_API SdfVariantSpecHandle

layer : LayerHandle
primPath : Path
variantSetName : string
variantName : string


Convenience function to create a variant spec for a given variant set
and a prim at the given path with.


The function creates the prim spec if it doesn't exist already and any
necessary parent prims, in the given layer.

It adds the variant set to the variant set list if it doesn't already
exist.

It creates a variant spec with the given name under the specified
variant set if it doesn't already exist.

"""
   result["GetNameForUnit"].func_doc = """GetNameForUnit(unit) -> SDF_API  string

unit : TfEnum


Gets the name for a given /a unit.

"""
   result["Path"].__doc__ = """
A path value used to locate objects in layers or scenegraphs.


Overview
========

SdfPath is used in several ways:
   - As a storage key for addressing and accessing values held in a
     SdfLayer

   - As a namespace identity for scenegraph objects

   - As a way to refer to other scenegraph objects through relative
     paths
     The paths represented by an SdfPath class may be either relative or
     absolute. Relative paths are relative to the prim object that contains
     them (that is, if an SdfRelationshipSpec target is relative, it is
     relative to the SdfPrimSpec object that owns the SdfRelationshipSpec
     object).

SdfPath objects can be readily created from and converted back to
strings, but as SdfPath objects, they have behaviors that make it easy
and efficient to work with them. The SdfPath class provides a full
range of methods for manipulating scene paths by appending a namespace
child, appending a relationship target, getting the parent path, and
so on. Since the SdfPath class uses a node-based representation
internally, you should use the editing functions rather than
converting to and from strings if possible.

Path Syntax
===========

Like a filesystem path, an SdfPath is conceptually just a sequence of
path components. Unlike a filesystem path, each component has a type,
and the type is indicated by the syntax.

Two separators are used between parts of a path. A slash ("/")
following an identifier is used to introduce a namespace child. A
period (".") following an identifier is used to introduce a property.
A property may also have several non-sequential colons (':') in its
name to provide a rudimentary namespace within properties but may not
end or begin with a colon.

A leading slash in the string representation of an SdfPath object
indicates an absolute path. Two adjacent periods indicate the parent
namespace.

Brackets ("[" and "]") are used to indicate relationship target paths
for relational attributes.

The first part in a path is assumed to be a namespace child unless it
is preceded by a period. That means:
   - C{/Foo} is an absolute path specifying the root prim Foo.

   - C{/Foo/Bar} is an absolute path specifying namespace child Bar of
     root prim Foo.

   - C{/Foo/Bar.baz} is an absolute path specifying property C{baz} of
     namespace child Bar of root prim Foo.

   - C{Foo} is a relative path specifying namespace child Foo of the
     current prim.

   - C{Foo/Bar} is a relative path specifying namespace child Bar of
     namespace child Foo of the current prim.

   - C{Foo/Bar.baz} is a relative path specifying property C{baz} of
     namespace child Bar of namespace child Foo of the current prim.

   - C{.foo} is a relative path specifying the property C{foo} of the
     current prim.

   - C{/Foo.bar[/Foo.baz].attrib} is a relational attribute path. The
     relationship C{/Foo.bar} has a target C{/Foo.baz}. There is a
     relational attribute C{attrib} on that relationship->target pair.

A Note on Thread-Safety
=======================

SdfPath is strongly thread-safe, in the sense that zero additional
synchronization is required between threads creating or using SdfPath
values. Just like TfToken, SdfPath values are immutable. Internally,
SdfPath uses a global prefix tree to efficiently share representations
of paths, and provide fast equality/hashing operations, but
modifications to this table are internally synchronized. Consequently,
as with TfToken, for best performance it is important to minimize the
number of values created (since it requires synchronized access to
this table) or copied (since it requires atomic ref-counting
operations).

"""
   result["Path"].TokenizeIdentifier.func_doc = """**static** TokenizeIdentifier(name) -> SDF_API sequence<string>

name : string


Tokenizes C{name} by the namespace delimiter.


Returns the empty vector if C{name} is not a valid namespaced
identifier.

"""
   result["Path"].ReplaceName.im_func.func_doc = """ReplaceName(newName) -> SDF_API SdfPath

newName : TfToken


Return a copy of this path with its final component changed to
*newName*.


This path must be a prim or property path.

This method is shorthand for path.GetParentPath().AppendChild(newName)
for prim paths, path.GetParentPath().AppendProperty(newName) for prim
property paths, and
path.GetParentPath().AppendRelationalAttribute(newName) for relational
attribute paths.

Note that only the final path component is ever changed. If the name
of the final path component appears elsewhere in the path, it will not
be modified.

Some examples:

ReplaceName('/chars/MeridaGroup', 'AngusGroup') ->'/chars/AngusGroup'
ReplaceName('/Merida.tx', 'ty') ->'/Merida.ty'
ReplaceName('/Merida.tx[targ].tx', 'ty') ->'/Merida.tx[targ].ty'

"""
   result["Path"].HasPrefix.im_func.func_doc = """HasPrefix(prefix) -> SDF_API bool

prefix : Path


Return true if both this path and *prefix* are not the empty path and
this path has *prefix* as a prefix.


Return false otherwise.

"""
   result["Path"].GetAbsoluteRootOrPrimPath.im_func.func_doc = """GetAbsoluteRootOrPrimPath() -> SDF_API SdfPath



Creates a path by stripping all properties and relational attributes
from this path, leaving the path to the containing prim.


If the path is already a prim or absolute root path, the same path is
returned.

"""
   result["Path"].RemoveAncestorPaths.func_doc = """**static** RemoveAncestorPaths(paths) -> SDF_API void

paths : PathVector


Remove all elements of *paths* that prefix other elements in *paths*.


As a side-effect, the result is left in sorted order.

"""
   result["Path"].IsValidNamespacedIdentifier.func_doc = """**static** IsValidNamespacedIdentifier(name) -> SDF_API bool

name : string


Returns whether C{name} is a legal namespaced identifier.


This returns C{true} if IsValidIdentifier() does.

"""
   result["Path"].GetVariantSelection.im_func.func_doc = """GetVariantSelection() -> SDF_API pair<string, string>



Returns the variant selection for this path, if this is a variant
selection path.


Returns a pair of empty strings if this path is not a variant
selection path.

"""
   result["Path"].AppendElementString.im_func.func_doc = """AppendElementString(element) -> SDF_API SdfPath

element : string


Creates a path by extracting and appending an element from the given
ascii element encoding.


Attempting to append a root or empty path (or malformed path) or
attempting to append *to* the EmptyPath will raise an error and return
the EmptyPath.

May also fail and return EmptyPath if this path's type cannot possess
a child of the type encoded in C{element}.

"""
   result["Path"].IsValidIdentifier.func_doc = """**static** IsValidIdentifier(name) -> SDF_API bool

name : string


Returns whether C{name} is a legal identifier for any path component.

"""
   result["Path"].IsMapperArgPath.im_func.func_doc = """IsMapperArgPath() -> SDF_API bool



Returns whether the path identifies a connection mapper arg.

"""
   result["Path"].IsNamespacedPropertyPath.im_func.func_doc = """IsNamespacedPropertyPath() -> SDF_API bool



Returns whether the path identifies a namespaced property.


A namespaced property has colon embedded in its name.

"""
   result["Path"].StripAllVariantSelections.im_func.func_doc = """StripAllVariantSelections() -> SDF_API SdfPath



Create a path by stripping all variant selections from all components
of this path, leaving a path with no embedded variant selections.

"""
   result["Path"].IsRelationalAttributePath.im_func.func_doc = """IsRelationalAttributePath() -> SDF_API bool



Returns whether the path identifies a relational attribute.


If this is true, IsPropertyPath() will also be true.

"""
   result["Path"].JoinIdentifier.func_doc = """**static** JoinIdentifier(names) -> SDF_API string

names : sequence<string>


Join C{names} into a single identifier using the namespace delimiter.


Any empty strings present in C{names} are ignored when joining.


----------------------------------------------------------------------
JoinIdentifier(names) -> SDF_API string

names : TfTokenVector


Join C{names} into a single identifier using the namespace delimiter.


Any empty strings present in C{names} are ignored when joining.


----------------------------------------------------------------------
JoinIdentifier(lhs, rhs) -> SDF_API string

lhs : string
rhs : string


Join C{lhs} and C{rhs} into a single identifier using the namespace
delimiter.


Returns C{lhs} if C{rhs} is empty and vice verse. Returns an empty
string if both C{lhs} and C{rhs} are empty.


----------------------------------------------------------------------
JoinIdentifier(lhs, rhs) -> SDF_API string

lhs : TfToken
rhs : TfToken


Join C{lhs} and C{rhs} into a single identifier using the namespace
delimiter.


Returns C{lhs} if C{rhs} is empty and vice verse. Returns an empty
string if both C{lhs} and C{rhs} are empty.

"""
   result["Path"].AppendChild.im_func.func_doc = """AppendChild(childName) -> SDF_API SdfPath

childName : TfToken


Creates a path by appending an element for C{childName} to this path.


This path must be a prim path, the AbsoluteRootPath or the
ReflexiveRelativePath.

"""
   result["Path"].AppendMapper.im_func.func_doc = """AppendMapper(targetPath) -> SDF_API SdfPath

targetPath : Path


Creates a path by appending a mapper element for C{targetPath}.


This path must be a prim property or relational attribute path.

"""
   result["Path"].AppendVariantSelection.im_func.func_doc = """AppendVariantSelection(variantSet, variant) -> SDF_API SdfPath

variantSet : string
variant : string


Creates a path by appending an element for C{variantSet} and
C{variant} to this path.


This path must be a prim path.

"""
   result["Path"].ContainsTargetPath.im_func.func_doc = """ContainsTargetPath() -> SDF_API bool



Return true if this path is or has a prefix that's a target path or a
mapper path.

"""
   result["Path"].GetParentPath.im_func.func_doc = """GetParentPath() -> SDF_API SdfPath



Creates a path by stripping a single element off of this path.


For a relational attribute path, returns the relationship target path.
For a path to a prim's property, returns the prim's path. For a prim
path, returns the prim's parent. For a root prim path, returns
EmptyPath. For a single element relative prim path, returns
ReflexiveRelativePath. For ReflexiveRelativePath, returns EmptyPath.

"""
   result["Path"].ReplacePrefix.im_func.func_doc = """ReplacePrefix(oldPrefix, newPrefix, fixTargetPaths) -> SDF_API SdfPath

oldPrefix : Path
newPrefix : Path
fixTargetPaths : bool


Returns a path with all occurrences of the prefix path C{oldPrefix}
replaced with the prefix path C{newPrefix}.


If fixTargetPaths is true, any embedded target paths will also have
their paths replaced. This is the default.

If this is not a target, relational attribute or mapper path this will
do zero or one path prefix replacements, if not the number of
replacements can be greater than one.

"""
   result["Path"].IsRootPrimPath.im_func.func_doc = """IsRootPrimPath() -> SDF_API bool



Returns whether the path identifies a root prim.


the path must be absolute and have a single element (for example
C{/foo}).

"""
   result["Path"].ReplaceTargetPath.im_func.func_doc = """ReplaceTargetPath(newTargetPath) -> SDF_API SdfPath

newTargetPath : Path


Replaces the relational attribute's target path.


The path must be a relational attribute path.

"""
   result["Path"].StripNamespace.func_doc = """**static** StripNamespace(name) -> SDF_API string

name : string


Returns C{name} stripped of any namespaces.


This does not check the validity of the name; it just attempts to
remove anything that looks like a namespace.


----------------------------------------------------------------------
StripNamespace(name) -> SDF_API TfToken

name : TfToken


Returns C{name} stripped of any namespaces.


This does not check the validity of the name; it just attempts to
remove anything that looks like a namespace.

"""
   result["Path"].GetConciseRelativePaths.func_doc = """**static** GetConciseRelativePaths(paths) -> SDF_API SdfPathVector

paths : PathVector


Given some vector of paths, get a vector of concise unambiguous
relative paths.


GetConciseRelativePaths requires a vector of absolute paths. It finds
a set of relative paths such that each relative path is unique.

"""
   result["Path"].IsValidPathString.func_doc = """**static** IsValidPathString(pathString, errMsg) -> SDF_API bool

pathString : string
errMsg : string


Return true if C{pathString} is a valid path string, meaning that
passing the string to the *SdfPath* constructor will result in a
valid, non-empty SdfPath.


Otherwise, return false and if C{errMsg} is not None, set the pointed-
to string to the parse error.

"""
   result["Path"].ContainsPrimVariantSelection.im_func.func_doc = """ContainsPrimVariantSelection() -> SDF_API bool



Returns whether the path or any of its parent paths identifies a
variant selection for a prim.

"""
   result["Path"].IsExpressionPath.im_func.func_doc = """IsExpressionPath() -> SDF_API bool



Returns whether the path identifies a connection expression.

"""
   result["Path"].__init__.im_func.func_doc = """__init__() -> SDF_API



Constructs the default, empty path.


----------------------------------------------------------------------
__init__(path) -> SDF_API

path : string


Creates a path from the given string.


If the given string is not a well-formed path, this will raise a Tf
error. Note that passing an empty std::string() will also raise an
error; the correct way to get the empty path is SdfPath() .

Internal dot-dots will be resolved by removing the first dot-dot, the
element preceding it, and repeating until no internal dot-dots remain.

Note that most often new paths are expected to be created by asking
existing paths to return modified versions of themselves.


----------------------------------------------------------------------
__init__(pathNode)

pathNode : _PathNodeConstRefPtr


----------------------------------------------------------------------
__init__(pathNode)

pathNode : _PathNodeConstRefPtr

"""
   result["Path"].IsPropertyPath.im_func.func_doc = """IsPropertyPath() -> SDF_API bool



Returns whether the path identifies a property.


A relational attribute is considered to be a property, so this method
will return true for relational attributes as well as properties of
prims.

"""
   result["Path"].RemoveCommonSuffix.im_func.func_doc = """RemoveCommonSuffix(otherPath, stopAtRootPrim) -> SDF_API pair< SdfPath , SdfPath >

otherPath : Path
stopAtRootPrim : bool


Find and remove the longest common suffix from two paths.


Returns this path and C{otherPath} with the longest common suffix
removed (first and second, respectively). If the two paths have no
common suffix then the paths are returned as-is. If the paths are
equal then this returns empty paths for relative paths and absolute
roots for absolute paths. The paths need not be the same length.

If C{stopAtRootPrim} is C{true} then neither returned path will be the
root path. That, in turn, means that some common suffixes will not be
removed. For example, if C{stopAtRootPrim} is C{true} then the paths
/A/B and /B will be returned as is. Were it C{false} then the result
would be /A and /. Similarly paths /A/B/C and /B/C would return /A/B
and /B if C{stopAtRootPrim} is C{true} but /A and / if it's C{false}.

"""
   result["Path"].MakeRelativePath.im_func.func_doc = """MakeRelativePath(anchor) -> SDF_API SdfPath

anchor : Path


Returns the relative form of this path using C{anchor} as the relative
basis.


C{anchor} must be an absolute prim path.

If this path is an absolute path, return the corresponding relative
path that is relative to the absolute path given by C{anchor}.

If this path is a relative path, return the optimal relative path to
the absolute path given by C{anchor}. (The optimal relative path from
a given prim path is the relative path with the least leading dot-
dots.

"""
   result["Path"].AppendTarget.im_func.func_doc = """AppendTarget(targetPath) -> SDF_API SdfPath

targetPath : Path


Creates a path by appending an element for C{targetPath}.


This path must be a prim property or relational attribute path.

"""
   result["Path"].IsAbsoluteRootOrPrimPath.im_func.func_doc = """IsAbsoluteRootOrPrimPath() -> SDF_API bool



Returns whether the path identifies a prim or the absolute root.

"""
   result["Path"].IsTargetPath.im_func.func_doc = """IsTargetPath() -> SDF_API bool



Returns whether the path identifies a relationship or connection
target.

"""
   result["Path"].IsPrimVariantSelectionPath.im_func.func_doc = """IsPrimVariantSelectionPath() -> SDF_API bool



Returns whether the path identifies a variant selection for a prim.

"""
   result["Path"].AppendProperty.im_func.func_doc = """AppendProperty(propName) -> SDF_API SdfPath

propName : TfToken


Creates a path by appending an element for C{propName} to this path.


This path must be a prim path or the ReflexiveRelativePath.

"""
   result["Path"].AppendMapperArg.im_func.func_doc = """AppendMapperArg(argName) -> SDF_API SdfPath

argName : TfToken


Creates a path by appending an element for C{argName}.


This path must be a mapper path.

"""
   result["Path"].IsPrimPropertyPath.im_func.func_doc = """IsPrimPropertyPath() -> SDF_API bool



Returns whether the path identifies a prim's property.


A relational attribute is not a prim property.

"""
   result["Path"].AppendPath.im_func.func_doc = """AppendPath(newSuffix) -> SDF_API SdfPath

newSuffix : Path


Creates a path by appending a given relative path to this path.


If the newSuffix is a prim path, then this path must be a prim path or
a root path.

If the newSuffix is a prim property path, then this path must be a
prim path or the ReflexiveRelativePath.

"""
   result["Path"].AppendRelationalAttribute.im_func.func_doc = """AppendRelationalAttribute(attrName) -> SDF_API SdfPath

attrName : TfToken


Creates a path by appending an element for C{attrName} to this path.


This path must be a target path.

"""
   result["Path"].RemoveDescendentPaths.func_doc = """**static** RemoveDescendentPaths(paths) -> SDF_API void

paths : PathVector


Remove all elements of *paths* that are prefixed by other elements in
*paths*.


As a side-effect, the result is left in sorted order.

"""
   result["Path"].IsAbsolutePath.im_func.func_doc = """IsAbsolutePath() -> SDF_API bool



Returns whether the path is absolute.

"""
   result["Path"].IsMapperPath.im_func.func_doc = """IsMapperPath() -> SDF_API bool



Returns whether the path identifies a connection mapper.

"""
   result["Path"].GetAllTargetPathsRecursively.im_func.func_doc = """GetAllTargetPathsRecursively(result) -> SDF_API void

result : PathVector


Returns all the relationship target or connection target paths
contained in this path, and recursively all the target paths contained
in those target paths in reverse depth-first order.


For example, given the path:
'/A/B.a[/C/D.a[/E/F.a]].a[/A/B.a[/C/D.a]]' this method produces:
'/A/B.a[/C/D.a]', '/C/D.a', '/C/D.a[/E/F.a]', '/E/F.a'

"""
   result["Path"].IsBuiltInMarker.func_doc = """**static** IsBuiltInMarker(marker) -> SDF_API bool

marker : string


Returns true, if C{marker} denotes a built in marker.

"""
   result["Path"].GetCommonPrefix.im_func.func_doc = """GetCommonPrefix(path) -> SDF_API SdfPath

path : Path


Returns a path with maximal length that is a prefix path of both this
path and C{path}.

"""
   result["Path"].GetPrimPath.im_func.func_doc = """GetPrimPath() -> SDF_API SdfPath



Creates a path by stripping all relational attributes, targets,
properties, and variant selections from the leafmost prim path,
leaving the nearest path for which *IsPrimPath()* returns true.


See *GetPrimOrPrimVariantSelectionPath* also.

If the path is already a prim path, the same path is returned.

"""
   result["Path"].MakeAbsolutePath.im_func.func_doc = """MakeAbsolutePath(anchor) -> SDF_API SdfPath

anchor : Path


Returns the absolute form of this path using C{anchor} as the relative
basis.


C{anchor} must be an absolute prim path.

If this path is a relative path, resolve it using C{anchor} as the
relative basis.

If this path is already an absolute path, just return a copy.

"""
   result["Path"].AppendExpression.im_func.func_doc = """AppendExpression() -> SDF_API SdfPath



Creates a path by appending an expression element.


This path must be a prim property or relational attribute path.

"""
   result["Path"].IsPrimPath.im_func.func_doc = """IsPrimPath() -> SDF_API bool



Returns whether the path identifies a prim.

"""
   result["CreatePrimInLayer"].func_doc = """CreatePrimInLayer(layer, primPath) -> SDF_API SdfPrimSpecHandle

layer : LayerHandle
primPath : Path


Convenience function to create a prim at the given path, and any
necessary parent prims, in the given layer.


If a prim already exists at the given path it will be returned
unmodified.

The new specs are created with SdfSpecifierOver and an empty type.
primPath must be a valid prim path.

"""
   result["MapperSpec"].__doc__ = """
Represents the mapper to be used for values coming from a particular
connection path of an attribute.


When instantiated on a stage, the appropriate subclass of MfMapper
will be chosen based on the mapper spec's type name.

"""
   result["PrimSpec"].__doc__ = """
Represents a prim description in an SdfLayer object.


Every SdfPrimSpec object is defined in a layer. It is identified by
its path (SdfPath class) in the namespace hierarchy of its layer.
SdfPrimSpecs can be created using the New() method as children of
either the containing SdfLayer itself (for "root level" prims), or as
children of other SdfPrimSpec objects to extend a hierarchy. The
helper function SdfCreatePrimInLayer() can be used to quickly create a
hierarchy of primSpecs.

SdfPrimSpec objects have properties of two general types: attributes
(containing values) and relationships (different types of connections
to other prims and attributes). Attributes are represented by the
SdfAttributeSpec class and relationships by the SdfRelationshipSpec
class. Each prim has its own namespace of properties. Properties are
stored and accessed by their name.

SdfPrimSpec objects have a typeName, permission restriction, and they
reference and inherit prim paths. Permission restrictions control
which other layers may refer to, or express opinions about a prim. See
the SdfPermission class for more information.

   - Insert doc about references and inherits here.

   - Should have validate... methods for name, children, properties


"""
   result["PrimSpec"].ClearKind.im_func.func_doc = """ClearKind() -> SDF_API void



Remove the kind opinion from this prim spec if there is one.

"""
   result["PrimSpec"].GetVariantNames.im_func.func_doc = """GetVariantNames(name) -> SDF_API sequence<string>

name : string


Returns list of variant names for the given variant set.

"""
   result["PrimSpec"].HasKind.im_func.func_doc = """HasKind() -> SDF_API bool



Returns true if this prim spec has an opinion about kind.

"""
   result["PrimSpec"].HasActive.im_func.func_doc = """HasActive() -> SDF_API bool



Returns true if this prim spec has an opinion about active.

"""
   result["PrimSpec"].HasInstanceable.im_func.func_doc = """HasInstanceable() -> SDF_API bool



Returns true if this prim spec has a value authored for its
instanceable flag, false otherwise.

"""
   result["PrimSpec"].GetRelationshipAtPath.im_func.func_doc = """GetRelationshipAtPath(path) -> SDF_API SdfRelationshipSpecHandle

path : Path


Returns a relationship given its C{path}.


Returns invalid handle if there is no relationship at C{path}. This is
simply a more specifically typed version of GetObjectAtPath.

"""
   result["PrimSpec"].ClearActive.im_func.func_doc = """ClearActive() -> SDF_API void



Removes the active opinion in this prim spec if there is one.

"""
   result["PrimSpec"].GetPrimAtPath.im_func.func_doc = """GetPrimAtPath(path) -> SDF_API SdfPrimSpecHandle

path : Path


Returns a prim given its C{path}.


Returns invalid handle if there is no prim at C{path}. This is simply
a more specifically typed version of GetObjectAtPath.

"""
   result["PrimSpec"].ApplyNameChildrenOrder.im_func.func_doc = """ApplyNameChildrenOrder(vec) -> SDF_API void

vec : sequence< TfToken >


Reorders the given list of child names according to the reorder
nameChildren statement for this prim.


This routine employs the standard list editing operation for ordered
items in a ListEditor.

"""
   result["PrimSpec"].ClearInstanceable.im_func.func_doc = """ClearInstanceable() -> SDF_API void



Clears the value for the prim's instanceable flag.

"""
   result["PrimSpec"].ApplyPropertyOrder.im_func.func_doc = """ApplyPropertyOrder(vec) -> SDF_API void

vec : sequence< TfToken >


Reorders the given list of property names according to the reorder
properties statement for this prim.


This routine employs the standard list editing operation for ordered
items in a ListEditor.

"""
   result["PrimSpec"].CanSetName.im_func.func_doc = """CanSetName(newName, whyNot) -> SDF_API bool

newName : string
whyNot : string


Returns true if setting the prim spec's name to C{newName} will
succeed.


Returns false if it won't, and sets C{whyNot} with a string describing
why not.

"""
   result["PrimSpec"].GetAttributeAtPath.im_func.func_doc = """GetAttributeAtPath(path) -> SDF_API SdfAttributeSpecHandle

path : Path


Returns an attribute given its C{path}.


Returns invalid handle if there is no attribute at C{path}. This is
simply a more specifically typed version of GetObjectAtPath.

"""
   result["PrimSpec"].RemoveProperty.im_func.func_doc = """RemoveProperty(property) -> SDF_API void

property : PropertySpecHandle


Removes the property.

"""
   result["PrimSpec"].GetPropertyAtPath.im_func.func_doc = """GetPropertyAtPath(path) -> SDF_API SdfPropertySpecHandle

path : Path


Returns a property given its C{path}.


Returns invalid handle if there is no property at C{path}. This is
simply a more specifically typed version of GetObjectAtPath.

"""
   result["ChangeBlock"].__doc__ = """
B{DANGER DANGER DANGER}


Please make sure you have read and fully understand the issues below
before using a changeblock! They are very easy to use in an unsafe way
that could make the system crash or corrupt data. If you have any
questions, please contact the USD team, who would be happy to help!

SdfChangeBlock provides a way to group a round of related changes to
scene description in order to process them more efficiently.

Normally, Sdf sends notification immediately as changes are made so
that downstream representations in Csd and Mf can update accordingly.

However, sometimes it can be advantageous to group a series of Sdf
changes into a batch so that they can be processed more efficiently,
with a single round of change processing. An example might be when
setting many avar values on a model at the same time.

Opening a changeblock tells Sdf to delay sending notification about
changes until the outermost changeblock is exited. Until then, Sdf
internally queues up the notification it needs to send.

It is *not* safe to use Csd, Mf, or other downstream API while a
changeblock is open!!111 This is because those derived representations
will not have had a chance to update while the changeblock is open.
Not only will their view of the world be stale, it could be unsafe to
even make queries from, since they may be holding onto expired handles
to Sdf objects that no longer exist. If you need to make a bunch of
changes to scene description, the best approach is to build a list of
necessary changes that can be performed directly via the Sdf API, then
submit those all inside a changeblock without talking to any
downstream modules. For example, this is how Csd performs namespace
edits.

"""
   result["ChangeBlock"].__init__.im_func.func_doc = """__init__() -> SDF_API


"""
   result["RelationshipSpec"].__doc__ = """
A property that contains a reference to one or more SdfPrimSpec
instances.


A relationship may refer to one or more target prims or attributes.
All targets of a single relationship are considered to be playing the
same role. Note that C{role} does not imply that the target prims or
attributes are of the same C{type}.

Relationships may be annotated with relational attributes. Relational
attributes are named SdfAttributeSpec objects containing values that
describe the relationship. For example, point weights are commonly
expressed as relational attributes.

"""
   result["RelationshipSpec"].GetTargetMarker.im_func.func_doc = """GetTargetMarker(path) -> SDF_API string

path : Path


Returns the marker for this relationship for the given target path.

"""
   result["RelationshipSpec"].InsertAttributeForTargetPath.im_func.func_doc = """InsertAttributeForTargetPath(path, attr, index) -> SDF_API bool

path : Path
attr : AttributeSpecHandle
index : int


Inserts the given attribute for the given target path.

"""
   result["RelationshipSpec"].GetOrCreateAttributeOrderForTargetPath.im_func.func_doc = """GetOrCreateAttributeOrderForTargetPath(path) -> SDF_API SdfNameOrderProxy

path : Path


Returns a list editor proxy for authoring relational attribute
orderings for the given target C{path}.


This may create a relationship target spec for C{path} if one does not
already exist.

"""
   result["RelationshipSpec"].SetTargetMarker.im_func.func_doc = """SetTargetMarker(path, marker) -> SDF_API void

path : Path
marker : string


Sets the marker for this relationship for the given target path.


If an empty string is specified, the target marker will be cleared.

"""
   result["RelationshipSpec"].ClearTargetMarker.im_func.func_doc = """ClearTargetMarker(path) -> SDF_API void

path : Path


Clears the marker for the given target path.

"""
   result["RelationshipSpec"].GetAttributeOrderTargetPaths.im_func.func_doc = """GetAttributeOrderTargetPaths() -> SDF_API SdfPathVector



Returns list of all target paths for which an ordering of relational
attributes exists.

"""
   result["RelationshipSpec"].HasAttributeOrderForTargetPath.im_func.func_doc = """HasAttributeOrderForTargetPath(path) -> SDF_API bool

path : Path


Returns true if a relational attribute ordering is authored for the
given target C{path}.

"""
   result["RelationshipSpec"].GetAttributeOrderForTargetPath.im_func.func_doc = """GetAttributeOrderForTargetPath(path) -> SDF_API SdfNameOrderProxy

path : Path


Returns a list editor proxy for authoring relational attribute
orderings for the given target C{path}.


If no ordering exists for C{path}, an invalid proxy object is
returned.

"""
   result["RelationshipSpec"].RemoveTargetPath.im_func.func_doc = """RemoveTargetPath(path, preserveTargetOrder) -> SDF_API void

path : Path
preserveTargetOrder : bool


Removes the specified target path.


Removes the given target path and any relational attributes for the
given target path. If C{preserveTargetOrder} is C{true}, Erase() is
called on the list editor instead of RemoveItemEdits(). This preserves
the ordered items list.

"""
   result["RelationshipSpec"].GetTargetMarkerPaths.im_func.func_doc = """GetTargetMarkerPaths() -> SDF_API SdfPathVector



Returns all target paths on which markers are specified.

"""
   result["RelationshipSpec"].GetTargetPathForAttribute.im_func.func_doc = """GetTargetPathForAttribute(attr) -> SDF_API SdfPath

attr : AttributeSpecConstHandle


Returns the target path for the given relational attribute.

"""
   result["RelationshipSpec"].ReplaceTargetPath.im_func.func_doc = """ReplaceTargetPath(oldPath, newPath) -> SDF_API void

oldPath : Path
newPath : Path


Updates the specified target path.


Replaces the path given by C{oldPath} with the one specified by
C{newPath}. Relational attributes are updated if necessary.

"""
   result["ValueBlock"].__doc__ = """
A special value type that can be used to explicitly author an opinion
for an attribute's default value or time sample value that represents
having no value.


Note that this is different from not having a value authored.

One could author such a value in two ways. ::

  attribute->SetDefaultValue(VtValue(SdfValueBlock());
  ...
  layer->SetTimeSample(attribute->GetPath(), 101, VtValue(SdfValueBlock()));


"""
   result["FileFormat"].__doc__ = """
Base class for file format implementations.

"""
   result["FileFormat"].IsPackage.im_func.func_doc = """IsPackage() -> SDF_API bool



Returns true if this file format is a package containing other assets.

"""
   result["FileFormat"].GetFileExtensions.im_func.func_doc = """GetFileExtensions() -> SDF_API  sequence<string>



Returns a list of extensions that this format supports.

"""
   result["FileFormat"].FindByExtension.func_doc = """**static** FindByExtension(extension, target) -> SDF_API SdfFileFormatConstPtr

extension : string
target : string


Returns the file format instance that supports the specified file
C{extension}.


If a format with a matching extension is not found, this returns a
null file format pointer.

An extension may be handled by multiple file formats, but each with a
different target. In such cases, if no C{target} is specified, the
file format that is registered as the primary plugin will be returned.
Otherwise, the file format whose target matches C{target} will be
returned.

"""
   result["FileFormat"].GetFileExtension.func_doc = """**static** GetFileExtension(s) -> SDF_API string

s : string


Returns the file extension for path or file name C{s}, without the
leading dot character.

"""
   result["FileFormat"].CanRead.im_func.func_doc = """CanRead(file) -> SDF_API bool

file : string


Returns true if C{file} can be read by this format.

"""
   result["FileFormat"].FindById.func_doc = """**static** FindById(formatId) -> SDF_API SdfFileFormatConstPtr

formatId : TfToken


Returns the file format instance with the specified C{formatId}
identifier.


If a format with a matching identifier is not found, this returns a
null file format pointer.

"""
   result["FileFormat"].IsSupportedExtension.im_func.func_doc = """IsSupportedExtension(extension) -> SDF_API bool

extension : string


Returns true if C{extension} matches one of the extensions returned by
GetFileExtensions.

"""
   result["ValueTypeName"].__doc__ = """
Represents a value type name, i.e.


an attribute's type name. Usually, a value type name associates a
string with a C{TfType} and an optional role, along with additional
metadata. A schema registers all known value type names and may
register multiple names for the same TfType and role pair. All name
strings for a given pair are collectively called its aliases.

A value type name may also represent just a name string, without a
C{TfType}, role or other metadata. This is currently used exclusively
to unserialize and re-serialize an attribute's type name where that
name is not known to the schema.

Because value type names can have aliases and those aliases may change
in the future, clients should avoid using the value type name's string
representation except to report human readable messages and when
serializing. Clients can look up a value type name by string using
C{SdfSchemaBase::FindType()} and shouldn't otherwise need the string.
Aliases compare equal, even if registered by different schemas.

"""
   result["ValueTypeName"].__init__.im_func.func_doc = """__init__() -> SDF_API



Constructs an invalid type name.


----------------------------------------------------------------------
__init__(arg1) -> SDF_API

arg1 : _ValueTypeImpl

"""
   result["Spec"].__doc__ = """
Base class for all Sdf spec classes.

"""
   result["Spec"].GetInfo.im_func.func_doc = """GetInfo(key) -> SDF_API VtValue

key : TfToken


Gets the value for the given metadata key.


This is interim API which is likely to change. Only editors with an
immediate specific need (like the Inspector) should use this API.

"""
   result["Spec"].ListInfoKeys.im_func.func_doc = """ListInfoKeys() -> SDF_API sequence< TfToken >



Returns the full list of info keys currently set on this object.



This does not include fields that represent names of children.

"""
   result["Spec"].GetMetaDataInfoKeys.im_func.func_doc = """GetMetaDataInfoKeys() -> SDF_API sequence< TfToken >



Returns the list of metadata info keys for this object.


This is not the complete list of keys, it is only those that should be
considered to be metadata by inspectors or other presentation UI.

This is interim API which is likely to change. Only editors with an
immediate specific need (like the Inspector) should use this API.

"""
   result["Spec"].GetMetaDataDisplayGroup.im_func.func_doc = """GetMetaDataDisplayGroup(key) -> SDF_API TfToken

key : TfToken


Returns this metadata key's displayGroup.

"""
   result["Spec"].SetInfo.im_func.func_doc = """SetInfo(key, value) -> SDF_API void

key : TfToken
value : VtValue


Sets the value for the given metadata key.


It is an error to pass a value that is not the correct type for that
given key.

This is interim API which is likely to change. Only editors with an
immediate specific need (like the Inspector) should use this API.

"""
   result["Spec"].SetInfoDictionaryValue.im_func.func_doc = """SetInfoDictionaryValue(dictionaryKey, entryKey, value) -> SDF_API void

dictionaryKey : TfToken
entryKey : TfToken
value : VtValue


Sets the value for C{entryKey} to C{value} within the dictionary with
the given metadata key C{dictionaryKey}.

"""
   result["LayerTree"].__doc__ = """
A SdfLayerTree is an immutable tree structure representing a sublayer
stack and its recursive structure.


Layers can have sublayers, which can in turn have sublayers of their
own. Clients that want to represent that hierarchical structure in
memory can build a SdfLayerTree for that purpose.

We use TfRefPtr<SdfLayerTree>as handles to LayerTrees, as a simple way
to pass them around as immutable trees without worrying about
lifetime.

"""
   result["LayerTree"].__init__.im_func.func_doc = """__init__(layer, childTrees, cumulativeOffset)

layer : LayerHandle
childTrees : LayerTreeHandleVector
cumulativeOffset : LayerOffset

"""
   result["Layer"].__doc__ = """
A unit of scene description that you combine with other units of scene
description to form a shot, model, set, shader, and so on.


SdfLayer objects provide a persistent way to store layers on the
filesystem in .menva files. Currently the supported file format is
C{.menva}, the ASCII file format.

The FindOrOpen() method returns a new SdfLayer object with scene
description from a C{.menva} file. Once read, a layer remembers which
asset it was read from. The Save() method saves the layer back out to
the original file. You can use the Export() method to write the layer
to a different location. You can use the GetIdentifier() method to get
the layer's Id or GetRealPath() to get the resolved, full file path.

Layers can have a timeCode range (startTimeCode and endTimeCode). This
range represents the suggested playback range, but has no impact on
the extent of the animation data that may be stored in the layer. The
metadatum "timeCodesPerSecond" is used to annotate how the time
ordinate for samples contained in the file scales to seconds. For
example, if timeCodesPerSecond is 24, then a sample at time ordinate
24 should be viewed exactly one second after the sample at time
ordinate 0.

Compared to Menv2x, layers are most closely analogous to hooksets,
C{.hook} files, and C{.cue} files.

   - Insert a discussion of subLayers semantics here.

   - Should have validate... methods for rootPrims


"""
   result["Layer"].HasFramesPerSecond.im_func.func_doc = """HasFramesPerSecond() -> SDF_API bool



Returns true if the layer has a frames per second opinion.

"""
   result["Layer"].ClearCustomLayerData.im_func.func_doc = """ClearCustomLayerData() -> SDF_API void



Clears out the CustomLayerData dictionary associated with this layer.

"""
   result["Layer"].GetDisplayNameFromIdentifier.func_doc = """**static** GetDisplayNameFromIdentifier(identifier) -> SDF_API string

identifier : string


Returns the display name for the given C{identifier}, using the same
rules as GetDisplayName.

"""
   result["Layer"].HasFramePrecision.im_func.func_doc = """HasFramePrecision() -> SDF_API bool



Returns true if the layer has a frames precision opinion.

"""
   result["Layer"].GetAttributeAtPath.im_func.func_doc = """GetAttributeAtPath(path) -> SDF_API SdfAttributeSpecHandle

path : Path


Returns an attribute at the given C{path}.


Returns C{None} if there is no attribute at C{path}. This is simply a
more specifically typed version of C{GetObjectAtPath()} .

"""
   result["Layer"].ClearFramePrecision.im_func.func_doc = """ClearFramePrecision() -> SDF_API void



Clear the framePrecision opinion.

"""
   result["Layer"].ClearDefaultPrim.im_func.func_doc = """ClearDefaultPrim() -> SDF_API void



Clear the default prim metadata for this layer.


See GetDefaultPrim() and SetDefaultPrim() .

"""
   result["Layer"].GetAssetName.im_func.func_doc = """GetAssetName() -> SDF_API  string



Returns the asset name associated with this layer.

"""
   result["Layer"].FindOrOpen.func_doc = """**static** FindOrOpen(identifier, args) -> SDF_API SdfLayerRefPtr

identifier : string
args : FileFormatArguments


Return an existing layer with the given C{identifier} and C{args}, or
else load it from disk.


If the layer can't be found or loaded, an error is posted and a null
layer is returned.

Arguments in C{args} will override any arguments specified in
C{identifier}.

"""
   result["Layer"].GetBracketingTimeSamplesForPath.im_func.func_doc = """GetBracketingTimeSamplesForPath(id, time, tLower, tUpper) -> SDF_API bool

id : AbstractDataSpecId
time : double
tLower : double
tUpper : double


----------------------------------------------------------------------
GetBracketingTimeSamplesForPath(path, time, tLower, tUpper) -> SDF_API bool

path : Path
time : double
tLower : double
tUpper : double

"""
   result["Layer"].ImportFromString.im_func.func_doc = """ImportFromString(string) -> SDF_API bool

string : string


Reads this layer from the given string.


Returns C{true} if successful, otherwise returns C{false}.

"""
   result["Layer"].ScheduleRemoveIfInert.im_func.func_doc = """ScheduleRemoveIfInert(spec) -> SDF_API void

spec : Spec


Cause C{spec} to be removed if it no longer affects the scene when the
last change block is closed, or now if there are no change blocks.

"""
   result["Layer"].SetPermissionToSave.im_func.func_doc = """SetPermissionToSave(allow) -> SDF_API void

allow : bool


Sets permission to save.

"""
   result["Layer"].ClearColorConfiguration.im_func.func_doc = """ClearColorConfiguration() -> SDF_API void



Clears the color configuration metadata authored in this layer.



HasColorConfiguration() , SetColorConfiguration()

"""
   result["Layer"].GetAssetInfo.im_func.func_doc = """GetAssetInfo() -> SDF_API  VtValue



Returns resolve information from the last time the layer identifier
was resolved.

"""
   result["Layer"].GetDisplayName.im_func.func_doc = """GetDisplayName() -> SDF_API string



Returns the layer's display name.


The display name is the base filename of the identifier.

"""
   result["Layer"].ListTimeSamplesForPath.im_func.func_doc = """ListTimeSamplesForPath(id) -> SDF_API set<double>

id : AbstractDataSpecId


----------------------------------------------------------------------
ListTimeSamplesForPath(path) -> SDF_API set<double>

path : Path

"""
   result["Layer"].CanApply.im_func.func_doc = """CanApply(arg1, details) -> SDF_API SdfNamespaceEditDetail.Result

arg1 : BatchNamespaceEdit
details : NamespaceEditDetailVector


Check if a batch of namespace edits will succeed.


This returns C{SdfNamespaceEditDetail::Okay} if they will succeed as a
batch, C{SdfNamespaceEditDetail::Unbatched} if the edits will succeed
but will be applied unbatched, and C{SdfNamespaceEditDetail::Error} if
they will not succeed. No edits will be performed in any case.

If C{details} is not C{None} and the method does not return C{Okay}
then details about the problems will be appended to C{details}. A
problem may cause the method to return early, so C{details} may not
list every problem.

Note that Sdf does not track backpointers so it's unable to fix up
targets/connections to namespace edited objects. Clients must fix
those to prevent them from falling off. In addition, this method will
report failure if any relational attribute with a target to a
namespace edited object is subsequently edited (in the same batch).
Clients should perform edits on relational attributes first.

Clients may wish to report unbatch details to the user to confirm that
the edits should be applied unbatched. This will give the user a
chance to correct any problems that cause batching to fail and try
again.

"""
   result["Layer"].CreateIdentifier.func_doc = """**static** CreateIdentifier(layerPath, arguments) -> SDF_API string

layerPath : string
arguments : FileFormatArguments


Joins the given layer path and arguments into an identifier.

"""
   result["Layer"].HasCustomLayerData.im_func.func_doc = """HasCustomLayerData() -> SDF_API bool



Returns true if CustomLayerData is authored on the layer.

"""
   result["Layer"].IsMuted.im_func.func_doc = """**static** IsMuted() -> SDF_API bool



Returns C{true} if the current layer is muted.


----------------------------------------------------------------------
IsMuted(path) -> SDF_API bool

path : string


Returns C{true} if the specified layer path is muted.

"""
   result["Layer"].New.func_doc = """**static** New(fileFormat, identifier, realPath, args) -> SDF_API SdfLayerRefPtr

fileFormat : FileFormatConstPtr
identifier : string
realPath : string
args : FileFormatArguments


Creates a new empty layer with the given identifier for a given file
format class.


This is so that Python File Format classes can create layers (
CreateNew() doesn't work, because it already saves during construction
of the layer. That is something specific (python generated) layer
types may choose to not do.)

The new layer will not be dirty.

Additional arguments may be supplied via the C{args} parameter. These
arguments may control behavior specific to the layer's file format.

"""
   result["Layer"].Save.im_func.func_doc = """Save(force) -> SDF_API bool

force : bool


Returns C{true} if successful, C{false} if an error occurred.


Returns C{false} if the layer has no remembered file name or the layer
type cannot be saved. The layer will not be overwritten if the file
exists and the layer is not dirty unless C{force} is true.

"""
   result["Layer"].HasSessionOwner.im_func.func_doc = """HasSessionOwner() -> SDF_API bool



Returns true if the layer has a session owner opinion.

"""
   result["Layer"].GetNumTimeSamplesForPath.im_func.func_doc = """GetNumTimeSamplesForPath(id) -> SDF_API size_t

id : AbstractDataSpecId


----------------------------------------------------------------------
GetNumTimeSamplesForPath(path) -> SDF_API size_t

path : Path


Convenience API that takes an SdfPath instead of an
SdfAbstractDataSpecId.


See documentation above for details.

"""
   result["Layer"].SplitIdentifier.func_doc = """**static** SplitIdentifier(identifier, layerPath, arguments) -> SDF_API bool

identifier : string
layerPath : string
arguments : FileFormatArguments


Splits the given layer identifier into its constituent layer path and
arguments.

"""
   result["Layer"].CreateNew.func_doc = """**static** CreateNew(identifier, realPath, args) -> SDF_API SdfLayerRefPtr

identifier : string
realPath : string
args : FileFormatArguments


Creates a new empty layer with the given identifier.


The C{identifier} must be either a real filesystem path or an asset
path without version modifier. Attempting to create a layer using an
identifier with a version specifier (e.g. layer.menva@300100,
layer.menva#5) raises a coding error, and returns a null layer
pointer.

Additional arguments may be supplied via the C{args} parameter. These
arguments may control behavior specific to the layer's file format.


----------------------------------------------------------------------
CreateNew(fileFormat, identifier, realPath, args) -> SDF_API SdfLayerRefPtr

fileFormat : FileFormatConstPtr
identifier : string
realPath : string
args : FileFormatArguments


Creates a new empty layer with the given identifier for a given file
format class.


This function has the same behavior as the other CreateNew function,
but uses the explicitly-specified C{fileFormat} instead of attempting
to discern the format from C{identifier}.

"""
   result["Layer"].RemoveFromMutedLayers.func_doc = """**static** RemoveFromMutedLayers(mutedPath) -> SDF_API void

mutedPath : string


Remove the specified path from the muted layers set.

"""
   result["Layer"].OpenAsAnonymous.func_doc = """**static** OpenAsAnonymous(layerPath, metadataOnly, tag) -> SDF_API SdfLayerRefPtr

layerPath : string
metadataOnly : bool
tag : string


Load the given layer from disk as a new anonymous layer.


If the layer can't be found or loaded, an error is posted and a null
layer is returned.

The anonymous layer does not retain any knowledge of the backing file
on the filesystem.

C{metadataOnly} is a flag that asks for only the layer metadata to be
read in, which can be much faster if that is all that is required.
Note that this is just a hint: some FileFormat readers may disregard
this flag and still fully populate the layer contents.

An optional C{tag} may be specified. See CreateAnonymous for details.

"""
   result["Layer"].EraseTimeSample.im_func.func_doc = """EraseTimeSample(id, time) -> SDF_API void

id : AbstractDataSpecId
time : double


----------------------------------------------------------------------
EraseTimeSample(path, time) -> SDF_API void

path : Path
time : double

"""
   result["Layer"].TransferContent.im_func.func_doc = """TransferContent(layer) -> SDF_API void

layer : LayerHandle


Copies the content of the given layer into this layer.


Source layer is unmodified.

"""
   result["Layer"].SetMuted.im_func.func_doc = """SetMuted(muted) -> SDF_API void

muted : bool


Mutes the current layer if C{muted} is C{true}, and unmutes it
otherwise.

"""
   result["Layer"].HasColorConfiguration.im_func.func_doc = """HasColorConfiguration() -> SDF_API bool



Returns true if color configuration metadata is set in this layer.



GetColorConfiguration() , SetColorConfiguration()

"""
   result["Layer"].UpdateExternalReference.im_func.func_doc = """UpdateExternalReference(oldAssetPath, newAssetPath) -> SDF_API bool

oldAssetPath : string
newAssetPath : string


Updates the external references of the layer.


If only the old asset path is given, this update works as delete,
removing any sublayers or prims referencing the pathtype using the old
asset path as reference.

If new asset path is supplied, the update works as "rename", updating
any occurrence of the old reference to the new reference.

"""
   result["Layer"].GetBracketingTimeSamples.im_func.func_doc = """GetBracketingTimeSamples(time, tLower, tUpper) -> SDF_API bool

time : double
tLower : double
tUpper : double

"""
   result["Layer"].Import.im_func.func_doc = """Import(layerPath) -> SDF_API bool

layerPath : string


Imports the content of the given layer path, replacing the content of
the current layer.


Note: If the layer path is the same as the current layer's real path,
no action is taken (and a warning occurs). For this case use Reload()
.

"""
   result["Layer"].ApplyRootPrimOrder.im_func.func_doc = """ApplyRootPrimOrder(vec) -> SDF_API void

vec : sequence< TfToken >


Reorders the given list of prim names according to the reorder
rootPrims statement for this layer.


This routine employs the standard list editing operations for ordered
items in a ListEditor.

"""
   result["Layer"].GetRelationshipAtPath.im_func.func_doc = """GetRelationshipAtPath(path) -> SDF_API SdfRelationshipSpecHandle

path : Path


Returns a relationship at the given C{path}.


Returns C{None} if there is no relationship at C{path}. This is simply
a more specifically typed version of C{GetObjectAtPath()} .

"""
   result["Layer"].RemoveInertSceneDescription.im_func.func_doc = """RemoveInertSceneDescription() -> SDF_API void



Removes all scene description in this layer that does not affect the
scene.


This method walks the layer namespace hierarchy and removes any prims
and that are not contributing any opinions.

"""
   result["Layer"].ClearSessionOwner.im_func.func_doc = """ClearSessionOwner() -> SDF_API void


"""
   result["Layer"].GetPrimAtPath.im_func.func_doc = """GetPrimAtPath(path) -> SDF_API SdfPrimSpecHandle

path : Path


Returns the prim at the given C{path}.


Returns C{None} if there is no prim at C{path}. This is simply a more
specifically typed version of C{GetObjectAtPath()} .

"""
   result["Layer"].ClearFramesPerSecond.im_func.func_doc = """ClearFramesPerSecond() -> SDF_API void



Clear the framesPerSecond opinion.

"""
   result["Layer"].AddToMutedLayers.func_doc = """**static** AddToMutedLayers(mutedPath) -> SDF_API void

mutedPath : string


Add the specified path to the muted layers set.

"""
   result["Layer"].ListAllTimeSamples.im_func.func_doc = """ListAllTimeSamples() -> SDF_API set<double>


"""
   result["Layer"].ClearStartTimeCode.im_func.func_doc = """ClearStartTimeCode() -> SDF_API void



Clear the startTimeCode opinion.

"""
   result["Layer"].QueryTimeSample.im_func.func_doc = """QueryTimeSample(id, time, value) -> SDF_API bool

id : AbstractDataSpecId
time : double
value : VtValue


----------------------------------------------------------------------
QueryTimeSample(id, time, value) -> SDF_API bool

id : AbstractDataSpecId
time : double
value : AbstractDataValue


----------------------------------------------------------------------
QueryTimeSample(id, time, data) -> bool

id : AbstractDataSpecId
time : double
data : T


----------------------------------------------------------------------
QueryTimeSample(path, time, data) -> bool

path : Path
time : double
data : T


----------------------------------------------------------------------
QueryTimeSample(path, time) -> SDF_API bool

path : Path
time : double

"""
   result["Layer"].ComputeAbsolutePath.im_func.func_doc = """ComputeAbsolutePath(relativePath) -> SDF_API string

relativePath : string


Make the given C{relativePath} absolute using the identifier of this
layer.


If this layer does not have an identifier, or if the layer identifier
is itself relative, C{relativePath} is returned unmodified.

"""
   result["Layer"].HasEndTimeCode.im_func.func_doc = """HasEndTimeCode() -> SDF_API bool



Returns true if the layer has an endTimeCode opinion.

"""
   result["Layer"].ClearEndTimeCode.im_func.func_doc = """ClearEndTimeCode() -> SDF_API void



Clear the endTimeCode opinion.

"""
   result["Layer"].ClearTimeCodesPerSecond.im_func.func_doc = """ClearTimeCodesPerSecond() -> SDF_API void



Clear the timeCodesPerSecond opinion.

"""
   result["Layer"].ClearColorManagementSystem.im_func.func_doc = """ClearColorManagementSystem() -> SDF_API void



Clears the 'colorManagementSystem' metadata authored in this layer.



HascolorManagementSystem(), SetColorManagementSystem()

"""
   result["Layer"].SetPermissionToEdit.im_func.func_doc = """SetPermissionToEdit(allow) -> SDF_API void

allow : bool


Sets permission to edit.

"""
   result["Layer"].HasDefaultPrim.im_func.func_doc = """HasDefaultPrim() -> SDF_API bool



Return true if the default prim metadata is set in this layer.


See GetDefaultPrim() and SetDefaultPrim() .

"""
   result["Layer"].GetObjectAtPath.im_func.func_doc = """GetObjectAtPath(path) -> SDF_API SdfSpecHandle

path : Path


Returns the object at the given C{path}.


There is no distinction between an absolute and relative path at the
SdLayer level.

Returns C{None} if there is no object at C{path}.

"""
   result["Layer"].HasStartTimeCode.im_func.func_doc = """HasStartTimeCode() -> SDF_API bool



Returns true if the layer has a startTimeCode opinion.

"""
   result["Layer"].HasTimeCodesPerSecond.im_func.func_doc = """HasTimeCodesPerSecond() -> SDF_API bool



Returns true if the layer has a timeCodesPerSecond opinion.

"""
   result["Layer"].CreateAnonymous.func_doc = """**static** CreateAnonymous(tag) -> SDF_API SdfLayerRefPtr

tag : string


Creates a new *anonymous* layer with an optional C{tag}.


An anonymous layer is a layer with a system assigned identifier, that
cannot be saved to disk via Save() . Anonymous layers have an
identifier, but no repository, overlay, real path, or other asset
information fields. Anonymous layers may be tagged, which can be done
to aid debugging subsystems that make use of anonymous layers. The tag
becomes the display name of an anonymous layer, and is also included
in the generated identifier. Untagged anonymous layers have an empty
display name.


----------------------------------------------------------------------
CreateAnonymous(tag, format) -> SDF_API SdfLayerRefPtr

tag : string
format : FileFormatConstPtr


Create an anonymous layer with a specific C{format}.

"""
   result["Layer"].IsAnonymousLayerIdentifier.func_doc = """**static** IsAnonymousLayerIdentifier(identifier) -> SDF_API bool

identifier : string


Returns true if the C{identifier} is an anonymous layer unique
identifier.

"""
   result["Layer"].UpdateAssetInfo.im_func.func_doc = """UpdateAssetInfo(fileVersion) -> SDF_API void

fileVersion : string


Update layer asset information.


Calling this method re-resolves the layer identifier, which updates
asset information such as the layer file revision, real path, and
repository path. If C{fileVersion} is supplied, it is used as the
layer version if the identifier does not have a version or label
specifier. This is typically used to tell Sd what the version of a
layer is after submitting a new revision to the asset system.

"""
   result["Layer"].ReloadLayers.func_doc = """**static** ReloadLayers(layers, force) -> SDF_API bool

layers : set<SdfLayerHandle>
force : bool


Reloads the specified layers.


Returns C{false} if one or more layers failed to reload.

See C{Reload()} for a description of the C{force} flag.

"""
   result["Layer"].Clear.im_func.func_doc = """Clear() -> SDF_API void



Clears the layer of all content.


This restores the layer to a state as if it had just been created with
CreateNew() . This operation is Undo-able.

The fileName and whether journaling is enabled are not affected by
this method.

"""
   result["Layer"].HasOwner.im_func.func_doc = """HasOwner() -> SDF_API bool



Returns true if the layer has an owner opinion.

"""
   result["Layer"].Reload.im_func.func_doc = """Reload(force) -> SDF_API bool

force : bool


Reloads the layer from its persistent representation.


This restores the layer to a state as if it had just been created with
FindOrOpen() . This operation is Undo-able.

The fileName and whether journaling is enabled are not affected by
this method.

When called with force = false (the default), Reload attempts to avoid
reloading layers that have not changed on disk. It does so by
comparing the file's modification time (mtime) to when the file was
loaded. If the layer has unsaved modifications, this mechanism is not
used, and the layer is reloaded from disk.

Passing true to the C{force} parameter overrides this behavior,
forcing the layer to be reloaded from disk regardless of whether it
has changed.

"""
   result["Layer"].HasColorManagementSystem.im_func.func_doc = """HasColorManagementSystem() -> SDF_API bool



Returns true if colorManagementSystem metadata is set in this layer.



GetColorManagementSystem() , SetColorManagementSystem()

"""
   result["Layer"].GetPropertyAtPath.im_func.func_doc = """GetPropertyAtPath(path) -> SDF_API SdfPropertySpecHandle

path : Path


Returns a property at the given C{path}.


Returns C{None} if there is no property at C{path}. This is simply a
more specifically typed version of C{GetObjectAtPath()} .

"""
   result["Layer"].SetTimeSample.im_func.func_doc = """SetTimeSample(id, time, value) -> SDF_API void

id : AbstractDataSpecId
time : double
value : VtValue


----------------------------------------------------------------------
SetTimeSample(id, time, value) -> SDF_API void

id : AbstractDataSpecId
time : double
value : AbstractDataConstValue


----------------------------------------------------------------------
SetTimeSample(id, time, value)

id : AbstractDataSpecId
time : double
value : T


----------------------------------------------------------------------
SetTimeSample(path, time, value)

path : Path
time : double
value : T

"""
   result["Layer"].ClearOwner.im_func.func_doc = """ClearOwner() -> SDF_API void



Clear the owner opinion.

"""
   result["Layer"].Export.im_func.func_doc = """Export(filename, comment, args) -> SDF_API bool

filename : string
comment : string
args : FileFormatArguments


Exports this layer to a file.


Returns C{true} if successful, C{false} if an error occurred.

If C{comment} is not empty, the layer gets exported with the given
comment. Additional arguments may be supplied via the C{args}
parameter. These arguments may control behavior specific to the
exported layer's file format.

Note that the file name or comment of the original layer is not
updated. This only saves a copy of the layer to the given filename.
Subsequent calls to Save() will still save the layer to it's
previously remembered file name.

"""
   result["Layer"].Apply.im_func.func_doc = """Apply(arg1) -> SDF_API bool

arg1 : BatchNamespaceEdit


Performs a batch of namespace edits.


Returns C{true} on success and C{false} on failure. On failure, no
namespace edits will have occurred.

"""
   result["Specifier"].__doc__ = """
An enum that identifies the possible specifiers for an SdfPrimSpec.


The SdfSpecifier enum is registered as a TfEnum for converting to and
from C{std::string}.

B{SdfSpecifier:}
   - B{SdfSpecifierDef.} Defines a concrete prim.

   - B{SdfSpecifierOver.} Overrides an existing prim.

   - B{SdfSpecifierClass.} Defines an abstract prim.

   - B{SdfNumSpecifiers.} The number of specifiers.


"""
   result["__doc__"] = """

Sdf provides the foundations for serializing scene description to a
reference ascii format, or a (multitude of) plugin-defined format. It
also provides the primitive abstractions for interacting with scene
description, such as SdfPath, SdfLayer, SdfPrimSpec.

Overview
========

Implements scene description *layers* in USD. In USD, a complete scene
description is composed from partial scene description stored in
SdfLayer objects. The primary unit of scene description within a layer
is a *prim* *spec*, represented by the SdfPrimSpec class. A complete
UsdPrim on a stage is a composition of the prim's built-in fallback
values and all of the prim spec objects specified in Sdf layers. (For
an overview of prims and stages, see the Usd module overview.)

Use methods on an SdfLayer object to export and save a layer to a
file, or to load a file from disk. Scene description files are stored
in C{.usd} format (one layer per file, ascii or binary). Other
features abstracted at the layer level include journaling (undo and
redo functionality) and logging, which can be customized by
subclassing SdfLayerStateDelegateBase.

You should primarily work with scene description using the classes in
the Usd module. The UsdStage object not only represents a complete
scene; it also knows how each of the partial scene descriptions were
combined to form the complete scene. For example, the UsdStage object
has the context to know how the path of a UsdPrim object on the stage
relates to the paths of each SdfPrimSpec object in each layer that
contributes a partial description to the complete prim. SdfLayer
objects do not have the context to know how they relate to other
layers.

Layering and Referencing
========================

An SdfPrimSpec object is named and forms a namespace hierarchy with
other prims. Each layer contains one or more root prims, each of which
may have a hierarchy of children. The SdfPath class provides methods
to manipulate paths for all of the objects that comprise a layer's
scene description. For example, SdfPath assigns unique paths for each
of the objects in a namespace hierarchy; this includes paths to scene
description that "lives inside of" particular variants of a
VariantSet.

Layers can be combined in several ways. An SdfLayer can have
*sublayers*. When layering, the SdfPrimSpec objects in an SdfLayer
object merge over the prims at the same namespace path in the layer.
An SdfPrimSpec object can also reference another prim within its own
layer or a prim from another layer. When referencing, a prim and its
name children merge over the other prim that it references.

Note that layering and referencing means that multiple SdfPrimSpec
objects may contribute partial descriptions for the same logical prim.
The full description of the prim in a given scene comes only from
combining or *composing* the contributions of each of the SdfPrimSpec
objects.

Layers and Opinions
===================

You can think of the partial scene spec in an SdfLayer object as one
*opinion* on an aspect of a complete scene. Several properties at the
layer level determine how or whether the opinion offered at a
particular layer is considered when the system composes a complete
prim on a stage. For example, the SdfPrimSpec and SdfPropertySpec
classes have an access permission property (SdfPermission) that you
can use to specify whether a layer is public or private.

Prim Spec
=========

There are many different kinds of prims, but at the level of scene
description they are all represented by an SdfPrimSpec object. An
SdfPrimSpec object represents a partial description of an individual
prim in a scene. It does not require values for every property it
contains. In addition, the list of properties that an SdfPrimSpec
object owns may be sparse. An SdfPrimSpec object that describes a
Cylinder may have a radius but no height, relying on either another
SdfPrimSpec object or the prim's fallback definition to provide the
height. Similarly, the list of name children on an SdfPrimSpec object
may be sparse.

SdfPrimSpec properties are represented by the SdfPropertySpec class.
Property specs also represent partial scene description. The
SdfPropertySpec subclasses represent the basic types of properties
that prims can have:

   - B{SdfAttributeSpec.} Represents values, which can be scalar or
     array-valued. For example, the C{radius} attribute of a Sphere gprim
     holds a scalar value; the C{points} attribute of a Mesh gprim holds an
     array value.

   - B{SdfRelationshipSpec.} Represents a relationship to other prims,
     attributes, or relationships, such as the C{material:binding}
     relationship that assigns Materials to Gprims.

Plugin Metadata
===============

Plugins can extend scene description to store additional plugin-
specific metadata by registering custom metadata fields. Consumers can
query and author data for these fields in the same way as the built-in
metadata fields in Sdf. This data will be serialized to and read from
layers just like all other scene description.

Plugin metadata fields must be defined in a dictionary called
"SdfMetadata" in the "Info" section of the plugin's C{plugInfo.json}
file. Each entry in the dictionary defines a single field and has the
following syntax: ::

  "<field_name>" : {
      "appliesTo": 
"<Optional comma-
separated list of spec types this field applies to>"
      "default": "<Optional default value for field>",
      "displayGroup": "<Optional name of associated display group>",
      "type": "<Required name indicating field type>",
  }

For example: ::

  # plugInfo.json
  {
      "Plugins": [
          {
              ...
              "Info": {
                  "SdfMetadata": {
                      "custom_double": {
                          "type": "double",
                          "appliesTo": "prims"
                      },
                      "custom_string": {
                          "type": "string",
                          "default": "default metadata value"
                      }
                  }
              }
              ...
          }
      ]
  }

Plugin metadata in a layer will remain intact and will round-trip
properly even if the definition for that metadata is unavailable when
the layer is opened. However, this metadata will not be inspectable
using the normal Sdf API.

The "type" entry for a metadata field must be one of the types listed
below.

Scalar Types

"type" value

C++ type

asset

SdfAssetPath

bool

bool

double

double

float

float

half

GfHalf

int

int

int64

int64_t

string

std::string

token

TfToken

uchar

unsigned char

uint

unsigned int

uint64

uint64_t

Dimensioned Types

"type" value

C++ type

double2

GfVec2d

double3

GfVec3d

double4

GfVec4d

float2

GfVec2f

float3

GfVec3f

float4

GfVec4f

half2

GfVec2h

half3

GfVec3h

half4

GfVec4h

int2

GfVec2i

int3

GfVec3i

int4

GfVec4i

matrix2d

GfMatrix2d

matrix3d

GfMatrix3d

matrix4d

GfMatrix4d

quatd

GfQuatd

quatf

GfQuatf

quath

GfQuath

Array Types

"type" value

C++ type

Element type name + "[]"

VtArray <Element C++ type>

Any scalar type + "[]"

VtArray <C++ type>

ex: string[]

ex: VtArray <std::string>

Any dimensioned type + "[]"

VtArray <C++ type>

ex: float2[]

ex: VtArray < GfVec2f>

Dictionary Types

"type" value

C++ type

dictionary

VtDictionary

List Operation Types

"type" value

C++ type

intlistop

SdfIntListOp

int64listop

SdfInt64ListOp

uintlistop

SdfUIntListOp

uint64listop

SdfUInt64ListOp

stringlistop

SdfStringListOp

tokenlistop

SdfTokenListOp

If not specified, the default value for plugin metadata fields is the
default value for the associated scene description type. However,
plugins may specify default values for each field. The current
implementation allows default values to be specified using a double,
an int, a string, or a flat list of one of these types. For example:
::

  "SdfMetadata": {
      # Defines a field named "double_single_default" with default value of 1.0
      "double_single_default": {
          "type": "double",
          "default": 1.0
      },
      # Defines a field named "double_shaped_default" with default value of VtArray<double>: {0.0, 1.0}
      "double_array_with_default": {
          "type": "double[]",
          "default": [0.0, 1.0]
      }
      # Defines a field named "double2_single_default" with default value of GfVec2d(0.0, 1.0)
      "double2_single_default": {
          "type": "double2",
          "default": [0.0, 1.0]
      }
      # Defines a field named "matrix4d_single_default" with default value of GfMatrix4d(0.5, 1.5, 2.5, 3.5, ...)
      "matrix4d_single_default": {
          "type": "matrix4d"
          "default": [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5]
      }
  }

Default values may not be specified for list operation types and
dictionary types.

Clients can query the default value for a plugin metadata field by
calling SdfSchema::GetFallback.

By default, a plugin metadata field can be used with any spec type.
However, this can be limited by setting the "appliesTo" field to a
comma-separated list of values from the table below:

"appliesTo" value

Spec type

layers

SdfLayer (SdfPseudoRootSpec)

prims

SdfPrimSpec, SdfVariantSpec

properties

SdfPropertySpec

attributes

SdfAttributeSpec

relationships

SdfRelationshipSpec

variants

SdfVariantSpec

Note that metadata that "appliesTo" prims also applies to variants, as
variants can hold the same scene description as prims.

A plugin metadata field may be associated with a display group by
specifying a value for the "displayGroup" field. This is purely an
affordance to allow external applications to group metadata fields
together for display purposes. Sdf does not consume this data itself.

Custom File Formats
===================

It is possible to create plugins that adapt other file formats to USD,
such that a USD file can reference a file of another format, and the
plugin will dynamically translate the file's contents into data
recognizable as SdfPrimSpec 's, SdfPropertySpec 's, etc. If it is
acceptable to have the file's entire contents translated and cached in
memory at the time the file is opened, then deriving a class from the
SdfFileFormat plugin base class is the primary task. If, however, one
wishes to access the data lazily (as most binary file formats are
designed to do), then one must also create an SdfAbstractData -derived
adapter as part of the plugin.

"""
   result["Variability"].__doc__ = """
An enum that identifies variability types for attributes.


Variability indicates whether the attribute may vary over time and
value coordinates, and if its value comes through authoring or or from
its owner.

B{SdfVariability:}
   - B{SdfVariabilityVarying.} Varying attributes may be directly
     authored, animated and affected on by Actions. They are the most
     flexible.

   - B{SdfVariabilityUniform.} Uniform attributes may be authored only
     with non-animated values (default values). They cannot be affected by
     Actions, but they can be connected to other Uniform attributes.

   - B{SdfVariabilityConfig.} Config attributes are the same as
     Uniform except that a Prim can choose to alter its collection of
     built-in properties based on the values of its Config attributes.

   - B{SdNumVariabilities.} Internal sentinel value.


"""
   result["UnregisteredValue"].__doc__ = """
Stores a representation of the value for an unregistered metadata
field encountered during text layer parsing.


This provides the ability to serialize this data to a layer, as well
as limited inspection and editing capabilities (e.g., moving this data
to a different spec or field) even when the data type of the value
isn't known.

"""
   result["UnregisteredValue"].__init__.im_func.func_doc = """__init__() -> SDF_API



Wraps an empty VtValue.


----------------------------------------------------------------------
__init__(value) -> SDF_API

value : string


Wraps a std::string.


----------------------------------------------------------------------
__init__(value) -> SDF_API

value : VtDictionary


Wraps a VtDictionary.


----------------------------------------------------------------------
__init__(value) -> SDF_API

value : UnregisteredValueListOp


Wraps a SdfUnregisteredValueListOp.

"""
   result["GetTypeForValueTypeName"].func_doc = """GetTypeForValueTypeName(name) -> SDF_API TfType

name : TfToken


Given an sdf valueType name, produce TfType if the type name specifies
a valid sdf value type.

"""
   result["ListOpType"].__doc__ = """
Enum for specifying one of the list editing operation types.

"""
   result["Payload"].__doc__ = """
Represents a payload and all its meta data.


A payload represents a prim reference to an external layer. A payload
is similar to a prim reference (see SdfReference) with the major
difference that payloads are explicitly loaded by the user.

Unloaded payloads represent a boundary that lazy composition and
system behaviors will not traverse across, providing a user-visible
way to manage the working set of the scene.

"""
   result["Payload"].__init__.im_func.func_doc = """__init__(assetPath, primPath) -> SDF_API

assetPath : string
primPath : Path


Creates a payload.

"""
   result["Reference"].__doc__ = """
Represents a reference and all its meta data.


A reference is expressed on a prim in a given layer and it identifies
a prim in a layer stack. All opinions in the namespace hierarchy under
the referenced prim will be composed with the opinions in the
namespace hierarchy under the referencing prim.

The asset path specifies the layer stack being referenced. If this
asset path is non-empty, this reference is considered an 'external'
reference to the layer stack rooted at the specified layer. If this is
empty, this reference is considered an 'internal' reference to the
layer stack containing (but not necessarily rooted at) the layer where
the reference is authored.

The prim path specifies the prim in the referenced layer stack from
which opinions will be composed. If this prim path is empty, it will
be considered a reference to the default prim specified in the root
layer of the referenced layer stack  see SdfLayer::GetDefaultPrim.

The meta data for a reference is its layer offset and custom data. The
layer offset is an affine transformation applied to all anim splines
in the referenced prim's namespace hierarchy, see SdfLayerOffset for
details. Custom data is for use by plugins or other non-tools supplied
extensions that need to be able to store data associated with
references.

"""
   result["Reference"].__init__.im_func.func_doc = """__init__(assetPath, primPath, layerOffset, customData) -> SDF_API

assetPath : string
primPath : Path
layerOffset : LayerOffset
customData : VtDictionary


Creates a reference with all its meta data.


The default reference is an internal reference to the default prim.

"""
   result["AttributeSpec"].__doc__ = """
A subclass of SdfPropertySpec that holds typed data.


Attributes are typed data containers that can optionally hold any and
all of the following:
   - A single default value.

   - An array of knot values describing how the value varies over
     time.

   - A dictionary of posed values, indexed by name.
     The values contained in an attribute must all be of the same type. In
     the Python API the C{typeName} property holds the attribute type. In
     the C++ API, you can get the attribute type using the GetTypeName()
     method. In addition, all values, including all knot values, must be
     the same shape. For information on shapes, see the VtShape class
     reference in the C++ documentation.

"""
   result["AttributeSpec"].SetConnectionMarker.im_func.func_doc = """SetConnectionMarker(path, marker) -> SDF_API void

path : Path
marker : string


Sets the marker for the given connection path.


Clears the marker if an empty string is given.

"""
   result["AttributeSpec"].ClearConnectionMarker.im_func.func_doc = """ClearConnectionMarker(path) -> SDF_API void

path : Path


Clears the marker for the given connection path.

"""
   result["AttributeSpec"].GetConnectionMarker.im_func.func_doc = """GetConnectionMarker(path) -> SDF_API string

path : Path


Returns the marker for the given connection path.


If no marker exists, returns the empty string.

"""
   result["AttributeSpec"].ClearColorSpace.im_func.func_doc = """ClearColorSpace() -> SDF_API void



Clears the colorSpace metadata value set on this attribute.

"""
   result["AttributeSpec"].GetConnectionMarkerPaths.im_func.func_doc = """GetConnectionMarkerPaths() -> SDF_API SdfPathVector



Returns all connection paths on which markers are specified.

"""
   result["AttributeSpec"].HasColorSpace.im_func.func_doc = """HasColorSpace() -> SDF_API bool



Returns true if this attribute has a colorSpace value authored.

"""
   result["AttributeSpec"].ChangeMapperPath.im_func.func_doc = """ChangeMapperPath(oldPath, newPath) -> SDF_API void

oldPath : Path
newPath : Path


Changes the path a mapper is associated with from C{oldPath} to
C{newPath}.

"""
   result["AttributeSpec"].GetConnectionPathForMapper.im_func.func_doc = """GetConnectionPathForMapper(mapper) -> SDF_API SdfPath

mapper : MapperSpecHandle


Returns the target path that mapper C{mapper} is associated with.

"""
   result["NamespaceEditDetail"].__doc__ = """
Detailed information about a namespace edit.

"""
   result["NamespaceEditDetail"].Result.__doc__ = """
Validity of an edit.

"""
   result["NamespaceEditDetail"].__init__.im_func.func_doc = """__init__() -> SDF_API



----------------------------------------------------------------------
__init__(arg1, edit, reason) -> SDF_API

arg1 : Result
edit : NamespaceEdit
reason : string

"""
   result["CleanupEnabler"].__doc__ = """
An RAII class which, when an instance is alive, enables scheduling of
automatic cleanup of SdfLayers.


Any affected specs which no longer contribute to the scene will be
removed when the last SdfCleanupEnabler instance goes out of scope.
Note that for this purpose, SdfPropertySpecs are removed if they have
only required fields (see SdfPropertySpecs::HasOnlyRequiredFields),
but only if the property spec itself was affected by an edit that left
it with only required fields. This will have the effect of
uninstantiating on-demand attributes. For example, if its parent prim
was affected by an edit that left it otherwise inert, it will not be
removed if it contains an SdfPropertySpec with only required fields,
but if the property spec itself is edited leaving it with only
required fields, it will be removed, potentially uninstantiating it if
it's an on-demand property.

SdfCleanupEnablers are accessible in both C++ and Python.

/// SdfCleanupEnabler can be used in the following manner: ::

  {
      SdfCleanupEnabler enabler;
      
      // Perform any action that might otherwise leave inert specs around, 
      // such as removing info from properties or prims, or removing name 
      // children. i.e:
      primSpec->ClearInfo(SdfFieldKeys->Default);
  
      // When enabler goes out of scope on the next line, primSpec will 
      // be removed if it has been left as an empty over.
  }


"""
   result["CopySpec"].func_doc = """CopySpec(srcLayer, srcPath, dstLayer, dstPath) -> SDF_API bool

srcLayer : LayerHandle
srcPath : Path
dstLayer : LayerHandle
dstPath : Path


Utility function for copying spec data at C{srcPath} in C{srcLayer} to
C{destPath} in C{destLayer}.


Copying is performed recursively: all child specs are copied as well.
Any destination specs that already exist will be overwritten.

Parent specs of the destination are not created, and must exist before
SdfCopySpec is called, or a coding error will result. For prim
parents, clients may find it convenient to call SdfCreatePrimInLayer
before SdfCopySpec.

As a special case, if the top-level object to be copied is a
relationship target or a connection, the destination spec must already
exist. That is because we don't want SdfCopySpec to impose any policy
on how list edits are made; client code should arrange for
relationship targets and connections to be specified as prepended,
appended, deleted, and/or ordered, as needed.

Attribute connections, relationship targets, inherit and specializes
paths, and internal sub-root references that target an object beneath
C{srcPath} will be remapped to target objects beneath C{dstPath}.


----------------------------------------------------------------------
CopySpec(srcLayer, srcPath, dstLayer, dstPath, shouldCopyValueFn, shouldCopyChildrenFn) -> SDF_API bool

srcLayer : LayerHandle
srcPath : Path
dstLayer : LayerHandle
dstPath : Path
shouldCopyValueFn : ShouldCopyValueFn
shouldCopyChildrenFn : ShouldCopyChildrenFn


Utility function for copying spec data at C{srcPath} in C{srcLayer} to
C{destPath} in C{destLayer}.


Various behaviors (such as which parts of the spec to copy) are
controlled by the supplied C{shouldCopyValueFn} and
C{shouldCopyChildrenFn}.

Copying is performed recursively: all child specs are copied as well,
except where prevented by C{shouldCopyChildrenFn}.

Parent specs of the destination are not created, and must exist before
SdfCopySpec is called, or a coding error will result. For prim
parents, clients may find it convenient to call SdfCreatePrimInLayer
before SdfCopySpec.

As a special case, if the top-level object to be copied is a
relationship target or a connection, the destination spec must already
exist. That is because we don't want SdfCopySpec to impose any policy
on how list edits are made; client code should arrange for
relationship targets and connections to be specified as prepended,
appended, deleted, and/or ordered, as needed.

"""
   result["Permission"].__doc__ = """
An enum that defines permission levels.


Permissions control which layers may refer to or express opinions
about a prim. Opinions expressed about a prim, or relationships to
that prim, by layers that are not allowed permission to access the
prim will be ignored.

B{SdfPermission:}
   - B{SdfPermissionPublic.} Public prims can be referred to by
     anything. (Available to any client.)

   - B{SdfPermissionPrivate.} Private prims can be referred to only
     within the local layer stack, and not across references or inherits.
     (Not available to clients.)

   - B{SdfNumPermission.} Internal sentinel value.


"""
   result["NamespaceEdit"].__doc__ = """
A single namespace edit.


It supports renaming, reparenting, reparenting with a rename,
reordering, and removal.

"""
   result["NamespaceEdit"].Rename.func_doc = """**static** Rename(currentPath, name) -> This

currentPath : Path
name : TfToken


Returns a namespace edit that renames the prim or property at
C{currentPath} to C{name}.

"""
   result["NamespaceEdit"].Reparent.func_doc = """**static** Reparent(currentPath, newParentPath, index) -> This

currentPath : Path
newParentPath : Path
index : Index


Returns a namespace edit to reparent the prim or property at
C{currentPath} to be under C{newParentPath} at index C{index}.

"""
   result["NamespaceEdit"].Remove.func_doc = """**static** Remove(currentPath) -> This

currentPath : Path


Returns a namespace edit that removes the object at C{currentPath}.

"""
   result["NamespaceEdit"].ReparentAndRename.func_doc = """**static** ReparentAndRename(currentPath, newParentPath, name, index) -> This

currentPath : Path
newParentPath : Path
name : TfToken
index : Index


Returns a namespace edit to reparent the prim or property at
C{currentPath} to be under C{newParentPath} at index C{index} with the
name C{name}.

"""
   result["NamespaceEdit"].__init__.im_func.func_doc = """__init__()



The default edit maps the empty path to the empty path.


----------------------------------------------------------------------
__init__(currentPath_, newPath_, index_)

currentPath_ : Path
newPath_ : Path
index_ : Index


The fully general edit.

"""
   result["NamespaceEdit"].Reorder.func_doc = """**static** Reorder(currentPath, index) -> This

currentPath : Path
index : Index


Returns a namespace edit to reorder the prim or property at
C{currentPath} to index C{index}.

"""
   result["ComputeAssetPathRelativeToLayer"].func_doc = """ComputeAssetPathRelativeToLayer(anchor, assetPath) -> SDF_API string

anchor : LayerHandle
assetPath : string


Returns the path to the asset specified by C{assetPath}, using the
C{anchor} layer to anchor the path if it is relative.


If that path cannot be resolved and C{layerPath} is a search path,
C{layerPath} will be returned. If C{layerPath} is not relative,
C{layerPath} will be returned. Otherwise, the anchored path will be
returned.

"""
   result["PseudoRootSpec"].__doc__ = """"""
   result["LayerOffset"].__doc__ = """
Represents a time offset and scale between layers.


The SdfLayerOffset class is an affine transform, providing both a
scale and a translate. It supports vector algebra semantics for
composing SdfLayerOffsets together via multiplication. The
SdfLayerOffset class is unitless: it does not refer to seconds or
frames.

For example, suppose layer A uses layer B, with an offset of X:  when
bringing animation from B into A, you first apply the scale of X, and
then the offset. Suppose you have a scale of 2 and an offset of 24:
first multiply B's frame numbers by 2, and then add 24. The animation
from B as seen in A will take twice as long and start 24 frames later.

Offsets are typically used in either sublayers or prim references. For
more information, see the SetSubLayerOffset() method of the SdfLayer
class (the subLayerOffsets property in Python), as well as the
SetReference() and GetReferenceLayerOffset() methods (the latter is
the referenceLayerOffset property in Python) of the SdfPrimSpec class.

"""
   result["LayerOffset"].__init__.im_func.func_doc = """__init__(offset, scale) -> SDF_API

offset : double
scale : double


Constructs a new SdfLayerOffset instance.

"""
   result["LayerOffset"].IsIdentity.im_func.func_doc = """IsIdentity() -> SDF_API bool



Returns C{true} if this is an identity transformation, with an offset
of 0.0 and a scale of 1.0.

"""
   result["LayerOffset"].GetInverse.im_func.func_doc = """GetInverse() -> SDF_API SdfLayerOffset



Gets the inverse offset, which performs the opposite transformation.

"""
   result["VariantSpec"].__doc__ = """
Represents a single variant in a variant set.


A variant contains a prim. This prim is the root prim of the variant.

SdfVariantSpecs are value objects. This means they are immutable once
created and they are passed by copy-in APIs. To change a variant spec,
you make a new one and replace the existing one.

"""
   result["VariantSpec"].GetVariantNames.im_func.func_doc = """GetVariantNames(name) -> SDF_API sequence<string>

name : string


Returns list of variant names for the given variant set.

"""
   result["MapperArgSpec"].__doc__ = """
Represents an argument to a specific mapper.

"""
   result["SpecType"].__doc__ = """
An enum that specifies the type of an object.


Objects are entities that have fields and are addressable by path.

"""
   result["BatchNamespaceEdit"].__doc__ = """
A description of an arbitrarily complex namespace edit.


A C{SdfBatchNamespaceEdit} object describes zero or more namespace
edits. Various types providing a namespace will allow the edits to be
applied in a single operation and also allow testing if this will
work.

Clients are encouraged to group several edits into one object because
that may allow more efficient processing of the edits. If, for
example, you need to reparent several prims it may be faster to add
all of the reparents to a single C{SdfBatchNamespaceEdit} and apply
them at once than to apply each separately.

Objects that allow applying edits are free to apply the edits in any
way and any order they see fit but they should guarantee that the
resulting namespace will be as if each edit was applied one at a time
in the order they were added.

Note that the above rule permits skipping edits that have no effect or
generate a non-final state. For example, if renaming A to B then to C
we could just rename A to C. This means notices may be elided.
However, implementations must not elide notices that contain
information about any edit that clients must be able to know but
otherwise cannot determine.

"""
   result["BatchNamespaceEdit"].Process.im_func.func_doc = """Process(processedEdits, hasObjectAtPath, canEdit, details, fixBackpointers) -> SDF_API bool

processedEdits : NamespaceEditVector
hasObjectAtPath : HasObjectAtPath
canEdit : CanEdit
details : NamespaceEditDetailVector
fixBackpointers : bool


Validate the edits and generate a possibly more efficient edit
sequence.


Edits are treated as if they were performed one at time in sequence,
therefore each edit occurs in the namespace resulting from all
previous edits.

Editing the descendants of the object in each edit is implied. If an
object is removed then the new path will be empty. If an object is
removed after being otherwise edited, the other edits will be
processed and included in C{processedEdits} followed by the removal.
This allows clients to fixup references to point to the object's final
location prior to removal.

This function needs help to determine if edits are allowed. The
callbacks provide that help. C{hasObjectAtPath} returns C{true} iff
there's an object at the given path. This path will be in the original
namespace not any intermediate or final namespace. C{canEdit} returns
C{true} iff the object at the current path can be namespace edited to
the new path, ignoring whether an object already exists at the new
path. Both paths are in the original namespace. If it returns C{false}
it should set the string to the reason why the edit isn't allowed. It
should not write either path to the string.

If C{hasObjectAtPath} is invalid then this assumes objects exist where
they should and don't exist where they shouldn't. Use this with care.
If C{canEdit} in invalid then it's assumed all edits are valid.

If C{fixBackpointers} is C{true} then target/connection paths are
expected to be in the intermediate namespace resulting from all
previous edits. If C{false} and any current or new path contains a
target or connection path that has been edited then this will generate
an error.

This method returns C{true} if the edits are allowed and sets
C{processedEdits} to a new edit sequence at least as efficient as the
input sequence. If not allowed it returns C{false} and appends reasons
why not to C{details}.

"""
   result["BatchNamespaceEdit"].Add.im_func.func_doc = """Add(edit)

edit : NamespaceEdit


Add a namespace edit.


----------------------------------------------------------------------
Add(currentPath, newPath, index)

currentPath : NamespaceEdit.Path
newPath : NamespaceEdit.Path
index : NamespaceEdit.Index


Add a namespace edit.

"""
   result["BatchNamespaceEdit"].__init__.im_func.func_doc = """__init__() -> SDF_API



Create an empty sequence of edits.


----------------------------------------------------------------------
__init__(arg1) -> SDF_API

arg1 : BatchNamespaceEdit


----------------------------------------------------------------------
__init__(arg1) -> SDF_API

arg1 : NamespaceEditVector

"""
   result["AssetPath"].__doc__ = """
Contains an asset path and an optional resolved path.

"""
   result["AssetPath"].__init__.im_func.func_doc = """__init__() -> SDF_API



Construct an empty asset path.


----------------------------------------------------------------------
__init__(path) -> SDF_API

path : string


Construct asset path with no associated resolved path.


----------------------------------------------------------------------
__init__(path, resolvedPath) -> SDF_API

path : string
resolvedPath : string


Construct an asset path with an associated resolved path.

"""
   result["GetValueTypeNameForValue"].func_doc = """GetValueTypeNameForValue(value) -> SDF_API SdfValueTypeName

value : VtValue


Given a value, produce the sdf valueType name.


If you provide a value that does not return true for
SdfValueHasValidType, the return value is unspecified.

"""
   result["PropertySpec"].__doc__ = """
Base class for SdfAttributeSpec and SdfRelationshipSpec.


Scene Spec Attributes (SdfAttributeSpec) and Relationships
(SdfRelationshipSpec) are the basic properties that make up Scene Spec
Prims (SdfPrimSpec). They share many qualities and can sometimes be
treated uniformly. The common qualities are provided by this base
class.

NOTE: Do not use Python reserved words and keywords as attribute
names. This will cause attribute resolution to fail.

"""
   result["PropertySpec"].HasDefaultValue.im_func.func_doc = """HasDefaultValue() -> SDF_API bool



Returns true if a default value is set for this attribute.

"""
   result["PropertySpec"].ClearDefaultValue.im_func.func_doc = """ClearDefaultValue() -> SDF_API void



Clear the attribute's default value.

"""
   result["VariantSetSpec"].__doc__ = """
Represents a coherent set of alternate representations for part of a
scene.


An SdfPrimSpec object may contain one or more named SdfVariantSetSpec
objects that define variations on the prim.

An SdfVariantSetSpec object contains one or more named SdfVariantSpec
objects. It may also define the name of one of its variants to be used
by default.

When a prim references another prim, the referencing prim may specify
one of the variants from each of the variant sets of the target prim.
The chosen variant from each set (or the default variant from those
sets that the referencing prim does not explicitly specify) is
composited over the target prim, and then the referencing prim is
composited over the result.

"""
   result["VariantSetSpec"].RemoveVariant.im_func.func_doc = """RemoveVariant(variant) -> SDF_API void

variant : VariantSpecHandle


Removes C{variant} from the list of variants.


If the variant set does not currently own C{variant}, no action is
taken.

"""
   result["Notice"].__doc__ = """
Wrapper class for Sdf notices.

"""
   result["Notice"].LayerMutenessChanged.__doc__ = """
Sent after a layer has been added or removed from the set of muted
layers.


Note this does not necessarily mean the specified layer is currently
loaded.

"""
   result["Notice"].LayersDidChange.__doc__ = """
Global notice sent to indicate that layer contents have changed.

"""
   result["Notice"].LayerDirtinessChanged.__doc__ = """
Similar behavior to LayersDidChange, but only gets sent if a change in
the dirty status of a layer occurs.

"""
   result["Notice"].Base.__doc__ = """
Base notification class for scene.


Only useful for type hierarchy purposes.

"""
   result["Notice"].LayerDidReplaceContent.__doc__ = """
Sent after a menv layer has been loaded from a file.

"""
   result["Notice"].LayersDidChangeSentPerLayer.__doc__ = """
Notice sent per-layer indicating all layers whose contents have
changed within a single round of change processing.


If more than one layer changes in a single round of change processing,
we send this notice once per layer with the same changeMap and
serialNumber. This is so clients can listen to notices from only the
set of layers they care about rather than listening to the global
LayersDidChange notice.

"""
   result["Notice"].LayerDidReloadContent.__doc__ = """
Sent after a layer is reloaded.

"""
   result["Notice"].LayerInfoDidChange.__doc__ = """
Sent when the (scene spec) info of a layer have changed.

"""
   result["Notice"].LayerInfoDidChange.key.im_func.func_doc = """key() -> TfToken



Return the key affected.

"""
   result["Notice"].LayerIdentifierDidChange.__doc__ = """
Sent when the identifier of a layer has changed.

"""
   result["AssetPath"].resolvedPath = property(result["AssetPath"].resolvedPath.fget, result["AssetPath"].resolvedPath.fset, result["AssetPath"].resolvedPath.fdel, """type : string


Return the resolved asset path, if any.


Note that SdfAssetPath only carries a resolved path if the creator of
an instance supplied one to the constructor. SdfAssetPath will never
call Rp itself.

""")
   result["ValueTypeName"].isArray = property(result["ValueTypeName"].isArray.fget, result["ValueTypeName"].isArray.fset, result["ValueTypeName"].isArray.fdel, """type : SDF_API bool


Returns C{true} iff this type is an array.


The invalid type is considered neither scalar nor array.

""")
   result["Reference"].customData = property(result["Reference"].customData.fget, result["Reference"].customData.fset, result["Reference"].customData.fdel, """
Sets the custom data associated with the reference.


----------------------------------------------------------------------
type : SDF_API void


Sets a custom data entry for the reference.


If *value* is empty, then this removes the given custom data entry.

----------------------------------------------------------------------type : VtDictionary


Returns the custom data associated with the reference.

""")
   result["ValueTypeName"].role = property(result["ValueTypeName"].role.fget, result["ValueTypeName"].role.fset, result["ValueTypeName"].role.fdel, """type : SDF_API  TfToken


Returns the type's role.

""")
   result["ValueTypeName"].defaultUnit = property(result["ValueTypeName"].defaultUnit.fget, result["ValueTypeName"].defaultUnit.fset, result["ValueTypeName"].defaultUnit.fdel, """type : SDF_API  TfEnum


Returns the default unit enum for the type.

""")
   result["UnregisteredValue"].value = property(result["UnregisteredValue"].value.fget, result["UnregisteredValue"].value.fset, result["UnregisteredValue"].value.fdel, """type : VtValue


Returns the wrapped VtValue specified in the constructor.

""")
   result["LayerTree"].childTrees = property(result["LayerTree"].childTrees.fget, result["LayerTree"].childTrees.fset, result["LayerTree"].childTrees.fdel, """type : SDF_API  SdfLayerTreeHandleVector


Returns the children of this tree node.

""")
   result["FileFormat"].primaryFileExtension = property(result["FileFormat"].primaryFileExtension.fget, result["FileFormat"].primaryFileExtension.fset, result["FileFormat"].primaryFileExtension.fdel, """type : SDF_API  string


Returns the primary file extension for this format.


This is the extension that is reported for layers using this file
format.

""")
   result["Path"].isEmpty = property(result["Path"].isEmpty.fget, result["Path"].isEmpty.fset, result["Path"].isEmpty.fdel, """type : SDF_API bool


Returns true if this is the empty path ( SdfPath::EmptyPath() ).

""")
   result["Reference"].assetPath = property(result["Reference"].assetPath.fget, result["Reference"].assetPath.fset, result["Reference"].assetPath.fdel, """type : string


Returns the asset path to the root layer of the referenced layer
stack.


This will be empty in the case of an internal reference.

----------------------------------------------------------------------
Sets the asset path for the root layer of the referenced layer stack.


This may be set to an empty string to specify an internal reference.

""")
   result["ValueTypeName"].isScalar = property(result["ValueTypeName"].isScalar.fget, result["ValueTypeName"].isScalar.fset, result["ValueTypeName"].isScalar.fdel, """type : SDF_API bool


Returns C{true} iff this type is a scalar.


The invalid type is considered neither scalar nor array.

""")
   result["BatchNamespaceEdit"].edits = property(result["BatchNamespaceEdit"].edits.fget, result["BatchNamespaceEdit"].edits.fset, result["BatchNamespaceEdit"].edits.fdel, """type : NamespaceEditVector


Returns the edits.

""")
   result["LayerTree"].offset = property(result["LayerTree"].offset.fget, result["LayerTree"].offset.fset, result["LayerTree"].offset.fdel, """type : SDF_API  SdfLayerOffset


Returns the cumulative layer offset from the root of the tree.

""")
   result["Notice"].LayerIdentifierDidChange.newIdentifier = property(result["Notice"].LayerIdentifierDidChange.newIdentifier.fget, result["Notice"].LayerIdentifierDidChange.newIdentifier.fset, result["Notice"].LayerIdentifierDidChange.newIdentifier.fdel, """type : string


Returns the new identifier for the layer.

""")
   result["LayerTree"].layer = property(result["LayerTree"].layer.fget, result["LayerTree"].layer.fset, result["LayerTree"].layer.fdel, """type : SDF_API  SdfLayerHandle


Returns the layer handle this tree node represents.

""")
   result["Reference"].layerOffset = property(result["Reference"].layerOffset.fget, result["Reference"].layerOffset.fset, result["Reference"].layerOffset.fdel, """type : LayerOffset


Returns the layer offset associated with the reference.

----------------------------------------------------------------------
Sets a new layer offset.

""")
   result["FileFormat"].fileCookie = property(result["FileFormat"].fileCookie.fget, result["FileFormat"].fileCookie.fset, result["FileFormat"].fileCookie.fdel, """type : SDF_API  string


Returns the cookie to be used when writing files with this format.

""")
   result["ValueTypeName"].scalarType = property(result["ValueTypeName"].scalarType.fget, result["ValueTypeName"].scalarType.fset, result["ValueTypeName"].scalarType.fdel, """type : SDF_API SdfValueTypeName


Returns the scalar version of this type name if it's an array type
name, otherwise returns this type name.


If there is no scalar type name then this returns the invalid type
name.

""")
   result["FileFormat"].target = property(result["FileFormat"].target.fget, result["FileFormat"].target.fset, result["FileFormat"].target.fdel, """type : SDF_API  TfToken


Returns the target for this file format.

""")
   result["FileFormat"].formatId = property(result["FileFormat"].formatId.fget, result["FileFormat"].formatId.fset, result["FileFormat"].formatId.fdel, """type : SDF_API  TfToken


Returns the format identifier.

""")
   result["LayerOffset"].scale = property(result["LayerOffset"].scale.fget, result["LayerOffset"].scale.fset, result["LayerOffset"].scale.fdel, """type : double


Returns the time scale factor.

----------------------------------------------------------------------
Sets the time scale factor.

""")
   result["ValueTypeName"].type = property(result["ValueTypeName"].type.fget, result["ValueTypeName"].type.fset, result["ValueTypeName"].type.fdel, """type : SDF_API  TfType


Returns the C{TfType} of the type.

""")
   result["VariantSpec"].variantSets = property(result["VariantSpec"].variantSets.fget, result["VariantSpec"].variantSets.fset, result["VariantSpec"].variantSets.fdel, """type : SDF_API SdfVariantSetsProxy


Returns the nested variant sets.


The result maps variant set names to variant sets. Variant sets may be
removed through the proxy.

""")
   result["LayerOffset"].offset = property(result["LayerOffset"].offset.fget, result["LayerOffset"].offset.fset, result["LayerOffset"].offset.fdel, """type : double


Returns the time offset.

----------------------------------------------------------------------
Sets the time offset.

""")
   result["Notice"].LayerMutenessChanged.layerPath = property(result["Notice"].LayerMutenessChanged.layerPath.fget, result["Notice"].LayerMutenessChanged.layerPath.fset, result["Notice"].LayerMutenessChanged.layerPath.fdel, """type : string


Returns the path of the layer that was muted or unmuted.

""")
   result["Layer"].empty = property(result["Layer"].empty.fget, result["Layer"].empty.fset, result["Layer"].empty.fdel, """type : SDF_API bool


Returns whether this layer has no significant data.

""")
   result["Reference"].primPath = property(result["Reference"].primPath.fget, result["Reference"].primPath.fset, result["Reference"].primPath.fdel, """type : Path


Returns the path of the referenced prim.


This will be empty if the referenced prim is the default prim
specified in the referenced layer stack.

----------------------------------------------------------------------
Sets the path of the referenced prim.


This may be set to an empty path to specify a reference to the default
prim in the referenced layer stack.

""")
   result["ValueTypeName"].arrayType = property(result["ValueTypeName"].arrayType.fget, result["ValueTypeName"].arrayType.fset, result["ValueTypeName"].arrayType.fdel, """type : SDF_API SdfValueTypeName


Returns the array version of this type name if it's an scalar type
name, otherwise returns this type name.


If there is no array type name then this returns the invalid type
name.

""")
   result["Payload"].primPath = property(result["Payload"].primPath.fget, result["Payload"].primPath.fset, result["Payload"].primPath.fdel, """type : Path


Returns the scene path of the prim for the payload.

----------------------------------------------------------------------
Sets a new prim path for the prim that the payload uses.

""")
   result["ValueTypeName"].defaultValue = property(result["ValueTypeName"].defaultValue.fget, result["ValueTypeName"].defaultValue.fset, result["ValueTypeName"].defaultValue.fdel, """type : SDF_API  VtValue


Returns the default value for the type.

""")
   result["Notice"].LayerIdentifierDidChange.oldIdentifier = property(result["Notice"].LayerIdentifierDidChange.oldIdentifier.fget, result["Notice"].LayerIdentifierDidChange.oldIdentifier.fset, result["Notice"].LayerIdentifierDidChange.oldIdentifier.fdel, """type : string


Returns the old identifier for the layer.

""")
   result["Layer"].anonymous = property(result["Layer"].anonymous.fget, result["Layer"].anonymous.fset, result["Layer"].anonymous.fdel, """type : SDF_API bool


Returns true if this layer is an anonymous layer.

""")
   result["Payload"].assetPath = property(result["Payload"].assetPath.fget, result["Payload"].assetPath.fset, result["Payload"].assetPath.fdel, """type : string


Returns the asset path of the layer that the payload uses.

----------------------------------------------------------------------
Sets a new asset path for the layer the payload uses.

""")
   result["Layer"].dirty = property(result["Layer"].dirty.fget, result["Layer"].dirty.fset, result["Layer"].dirty.fdel, """type : SDF_API bool


Returns C{true} if the layer is dirty, i.e.


has changed from its persistent representation.

""")