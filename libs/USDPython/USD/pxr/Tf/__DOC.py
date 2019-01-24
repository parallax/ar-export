def Execute(result):
   result["PyModuleWasLoaded"].__doc__ = """
A *TfNotice* that is sent when a script module is loaded.


Since many modules may be loaded at once, listeners are encouraged to
defer work triggered by this notice to the end of an application
iteration. This, of course, is good practice in general.

"""
   result["GetCurrentScopeDescriptionStack"].func_doc = """GetCurrentScopeDescriptionStack() -> sequence<string>



Return a copy of the current description stack for the "main" thread
as identified by ArchGetMainThreadId() as a vector of strings.


The most recently pushed description is at back(), and the least
recently pushed description is at front().

"""
   result["__doc__"] = """

Contains foundation classes and functions for all C/C++ software
development.  The high-level grouping of C++ classes and functions is
as follows:

   - B{Memory} B{Management} - TfRefPtr, TfWeakPtr, TfRefBase,
     TfWeakBase, TfMallocTag

   - B{Runtime} B{Typing} - TfType, TfEnum, TfTypeInfoMap

   - B{Path} B{Utilities} - TfRealPath, TfNormPath, TfAbsPath,
     TfReadLink, TfGlob

   - B{Diagnostic} B{Utilities} - TF_AXIOM() , TF_FATAL_ERROR() ,
     TF_CODING_ERROR() , TF_RUNTIME_ERROR() , TF_WARN() , TF_STATUS()

   - B{Output} B{For} B{Debugging} - TfDebug, TF_DEBUG() ,
     TF_FUNC_NAME()

   - B{String} B{Utilities} - TfStringPrintf() , TfHash, (and a large
     number of miscellaneous free functions)

   - B{Containers} - TfByteData, TfArray2, TfArray3, TfTypeInfoMap

   - B{STL} B{Utilities} - TfIterator, TfDeleter, TfMapLookup() ,
     TfOrderedPair()

   - B{Object} B{Creation} - TfSingleton, TfType

   - B{Mathematical} B{Operations} - TfAbs() , TfMin() , TfMax()

   - B{Performance} B{Measurements} - TfStopwatch

   - B{File} B{Utilities} - TfSearchPath

   - B{Systems} B{Extensions} B{and} B{Enhancements} - TfDlopen() ,
     TfDlclose() , TfGetenv()

For a detailed explanation of topics specific to C++, see these
additional Related Pages in the C++ API documentation:
   - The TfNotice Notification System

   - The TfError Error Posting System

   - Guide To Diagnostic Facilities

   - The TfRegistryManager Registry Initialization System

   - The TfMallocTag Memory Tagging System


"""
   result["FindLongestAccessiblePrefix"].func_doc = """FindLongestAccessiblePrefix(path, error) -> string.size_type

path : string
error : string


Return the index delimiting the longest accessible prefix of *path*.


The returned value is safe to use to split the string via it's
generalized copy constructor. If the entire path is accessible, return
the length of the input string. If none of the path is accessible,
return 0. Otherwise the index points to the path separator that
delimits the existing prefix from the non-existing suffix.

Examples: suppose the paths /, /usr, and /usr/anim exist, but no other
paths exist.

TfFindLongestAccessiblePrefix('/usr/anim') ->9
TfFindLongestAccessiblePrefix('/usr/anim/foo') ->9
TfFindLongestAccessiblePrefix('/foo/bar') ->0

If an error occurs, and the *error* string is not null, it is set to
the reason for the error. If the error string is set, the returned
index is the path separator before the element at which the error
occurred.

"""
   result["TouchFile"].func_doc = """TouchFile(fileName, create) -> bool

fileName : string
create : bool


Touch C{fileName}, updating access and modification time to 'now'.


A simple touch-like functionality. Simple in a sense that it does not
offer as many options as the same-name unix touch command, but
otherwise is identical to the default touch behavior. If C{create} is
true, an empty file gets created, otherwise the touch call fails if
the file does not already exist.

"""
   result["Enum"].__doc__ = """
An enum class that records both enum type and enum value.

"""
   result["Enum"].GetValueFromFullName.func_doc = """**static** GetValueFromFullName(fullname, foundIt) -> Enum

fullname : string
foundIt : bool


Returns the enumerated value for a fully-qualified name.


This takes a fully-qualified enumerated value name (e.g.,
C{"Season::WINTER"} ) and returns the associated value. If there is no
such name, this returns -1. Since -1 can sometimes be a valid value,
the C{foundIt} flag pointer, if not C{None}, is set to C{true} if the
name was found and C{false} otherwise. Also, since this is not a
templated function, it has to return a generic value type, so we use
C{TfEnum}.

"""
   result["ScopeDescription"].__doc__ = """
This class is used to provide high-level descriptions about scopes of
execution that could possibly block, or to provide relevant
information about high-level action that would be useful in a crash
report.


This class is reasonably fast to use, especially if the message
strings are not dynamically created, however it should not be used in
very highly performance sensitive contexts. The cost to push & pop is
essentially a TLS lookup plus a couple of atomic operations.

"""
   result["ScopeDescription"].SetDescription.im_func.func_doc = """SetDescription(description)

description : string


Replace the description stack entry for this scope description.


Caller guarantees that the string C{description} lives at least as
long as this TfScopeDescription object.


----------------------------------------------------------------------
SetDescription(description)

description : string


Replace the description stack entry for this scope description.


This object adopts ownership of the rvalue C{description}.


----------------------------------------------------------------------
SetDescription(description)

description : char


Replace the description stack entry for this scope description.


Caller guarantees that the string C{description} lives at least as
long as this TfScopeDescription object.

"""
   result["ScopeDescription"].__init__.im_func.func_doc = """__init__()



----------------------------------------------------------------------
__init__(arg1)

arg1 : ScopeDescription


----------------------------------------------------------------------
__init__(description, context)

description : string
context : CallContext


Construct with a description.


Push *description* on the stack of descriptions for this thread.
Caller guarantees that the string C{description} lives at least as
long as this TfScopeDescription object.


----------------------------------------------------------------------
__init__(description, context)

description : string
context : CallContext


Construct with a description.


Push *description* on the stack of descriptions for this thread. This
object adopts ownership of the rvalue C{description}.


----------------------------------------------------------------------
__init__(description, context)

description : char
context : CallContext


Construct with a description.


Push *description* on the stack of descriptions for this thread.
Caller guarantees that the string C{description} lives at least as
long as this TfScopeDescription object.

"""
   result["Stopwatch"].__doc__ = """
Low-cost, high-resolution timer datatype.


A C{TfStopwatch} can be used to perform very precise timings at
runtime, even in very tight loops. The cost of "starting" or
"stopping" a C{TfStopwatch} is very small: approximately 40
nanoseconds on a 900 Mhz Pentium III Linux box, 300 nanoseconds on a
400 Mhz Sun, and 200 nanoseconds on a 250 Mhz SGI.

Note that this class is not thread-safe: if you need to take timings
in a multi-threaded region of a process, let each thread have its own
C{TfStopwatch} and then combine results using the C{AddFrom()} member
function.

"""
   result["Stopwatch"].Reset.im_func.func_doc = """Reset()



Resets the accumulated time and the sample count to zero.

"""
   result["Stopwatch"].__init__.im_func.func_doc = """__init__(name, share)

name : string
share : bool


Constructor with optionally supplied name, which is used only by
GetName() .


If C{share} is true, then this stopwatch is saved in an internal set
and can be retrieved via C{GetNamedStopwatch}. No provision is made
for multiple stopwatches with the same name. So if you want to
retrieve it, make sure you name it uniquely.


----------------------------------------------------------------------
__init__(other)

other : Stopwatch


Copy constructor.


We have a copy constructor because copies are never shared.

"""
   result["Stopwatch"].GetStopwatchNames.func_doc = """**static** GetStopwatchNames() -> sequence<string>



Return the names of the currently shared stopwatches.


Return a vector of strings that are the names of the currently
available shared stopwatches. Note that in a multithreaded
environment, the available stopwatches can change between the time you
retrieve the list of their names and when you retrieve the stopwatch
objects themselves. Fortunately, TfStopwatch objects are typically
static and even if they are not, it does no harm to request a named
stopwatch that does not exist.

"""
   result["Stopwatch"].Stop.im_func.func_doc = """Stop()



Increases the accumulated time stored in the C{TfStopwatch}.


The C{Stop()} function increases the accumulated time by the duration
between the current time and the last time recorded by a C{Start()}
call. A subsequent call to C{Stop()} before another call to C{Start()}
will therefore double-count time and throw off the results.

A C{TfStopwatch} also counts the number of samples it has taken. The
"sample count" is simply the number of times that C{Stop()} has been
called.

"""
   result["Stopwatch"].GetNamedStopwatch.func_doc = """**static** GetNamedStopwatch(name) -> Stopwatch

name : string


Return a copy of a particular named stopwatch.


C{GetNamedStopwatch} returns an unshared copy of the named stopwatch.

"""
   result["Stopwatch"].Start.im_func.func_doc = """Start()



Record the current time for use by the next C{Stop()} call.


The C{Start()} function records the current time. A subsequent call to
C{Start()} before a call to C{Stop()} simply records a later current
time, but does not change the accumulated time of the C{TfStopwatch}.

"""
   result["Stopwatch"].AddFrom.im_func.func_doc = """AddFrom(t)

t : Stopwatch


Adds the accumulated time and sample count from C{t} into the
C{TfStopwatch}.


If you have several timers taking measurements, and you wish to
combine them together, you can add one timer's results into another;
for example, C{t2.AddFrom(t1)} will add C{t1} 's time and sample count
into C{t2}.

"""
   result["CallContext"].__doc__ = """"""
   result["IsValidIdentifier"].func_doc = """IsValidIdentifier(identifier) -> bool

identifier : string


Test whether *identifier* is valid.


An identifier is valid if it follows the C/Python identifier
convention; that is, it must be at least one character long, must
start with a letter or underscore, and must contain only letters,
underscores, and numerals.


----------------------------------------------------------------------
IsValidIdentifier(identifier) -> bool

identifier : string


Test whether *identifier* is valid.


An identifier is valid if it follows the C/Python identifier
convention; that is, it must be at least one character long, must
start with a letter or underscore, and must contain only letters,
underscores, and numerals.

"""
   result["StringToDouble"].func_doc = """StringToDouble(txt) -> double

txt : string


Converts text string to double.


This method converts strings to floating point numbers. It is similar
to libc's atof(), but performs the conversion much more quickly.

It expects somewhat valid input: it will continue parsing the input
until it hits an unrecognized character, as described by the regexp
below, and at that point will return the results up to that point.

(-?[0-9]+(.[0-9]*)?|-?.[0-9]+)([eE][-+]?[0-9]+)?

It will not check to see if there is any input at all, or whitespace
after the digits. Ie: TfStringToDouble("") == 0.0
TfStringToDouble("blah") == 0.0 TfStringToDouble("-") == -0.0
TfStringToDouble("1.2foo") == 1.2

C{TfStringToDouble} is a wrapper around the extern-c TfStringToDouble


----------------------------------------------------------------------
StringToDouble(text) -> double

text : char


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
StringToDouble(txt) -> double

txt : string


Converts text string to double.


This method converts strings to floating point numbers. It is similar
to libc's atof(), but performs the conversion much more quickly.

It expects somewhat valid input: it will continue parsing the input
until it hits an unrecognized character, as described by the regexp
below, and at that point will return the results up to that point.

(-?[0-9]+(.[0-9]*)?|-?.[0-9]+)([eE][-+]?[0-9]+)?

It will not check to see if there is any input at all, or whitespace
after the digits. Ie: TfStringToDouble("") == 0.0
TfStringToDouble("blah") == 0.0 TfStringToDouble("-") == -0.0
TfStringToDouble("1.2foo") == 1.2

C{TfStringToDouble} is a wrapper around the extern-c TfStringToDouble


----------------------------------------------------------------------
StringToDouble(text) -> double

text : char


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["DiagnosticType"].__doc__ = """
Enum describing various diagnostic conditions.

"""
   result["MallocTag"].__doc__ = """
Top-down memory tagging system.


See The TfMallocTag Memory Tagging System for a detailed description.

"""
   result["MallocTag"].SetDebugMatchList.func_doc = """**static** SetDebugMatchList(matchList)

matchList : string


Sets the tags to trap in the debugger.


When memory is allocated or freed for any tag that matches
C{matchList} the debugger trap is invoked. If a debugger is attached
the program will stop in the debugger, otherwise the program will
continue to run. See C{ArchDebuggerTrap()} and C{ArchDebuggerWait()} .

C{matchList} is a comma, tab or newline separated list of malloc tag
names. The names can have internal spaces but leading and trailing
spaces are stripped. If a name ends in '*' then the suffix is
wildcarded. A name can have a leading '-' or '+' to prevent or allow a
match. Each name is considered in order and later matches override
earlier matches. For example, 'Csd*, -CsdScene::_Populate*,
+CsdScene::_PopulatePrimCacheLocal' matches any malloc tag starting
with 'Csd' but nothing starting with 'CsdScene::_Populate' except
'CsdScene::_PopulatePrimCacheLocal'. Use the empty string to disable
debugging traps.

"""
   result["MallocTag"].SetCapturedMallocStacksMatchList.func_doc = """**static** SetCapturedMallocStacksMatchList(matchList)

matchList : string


Sets the tags to trace.


When memory is allocated for any tag that matches C{matchList} a stack
trace is recorded. When that memory is released the stack trace is
discarded. Clients can call C{GetCapturedMallocStacks()} to get a list
of all recorded stack traces. This is useful for finding leaks.

Traces recorded for any tag that will no longer be matched are
discarded by this call. Traces recorded for tags that continue to be
matched are retained.

C{matchList} is a comma, tab or newline separated list of malloc tag
names. The names can have internal spaces but leading and trailing
spaces are stripped. If a name ends in '*' then the suffix is
wildcarded. A name can have a leading '-' or '+' to prevent or allow a
match. Each name is considered in order and later matches override
earlier matches. For example, 'Csd*, -CsdScene::_Populate*,
+CsdScene::_PopulatePrimCacheLocal' matches any malloc tag starting
with 'Csd' but nothing starting with 'CsdScene::_Populate' except
'CsdScene::_PopulatePrimCacheLocal'. Use the empty string to disable
stack capturing.

"""
   result["MallocTag"].GetTotalBytes.func_doc = """**static** GetTotalBytes() -> size_t



Return total number of allocated bytes.


The current total memory that has been allocated and not freed is
returned. Memory allocated before calling C{Initialize()} is not
accounted for.

"""
   result["MallocTag"].Initialize.func_doc = """**static** Initialize(errMsg) -> bool

errMsg : string


Initialize the memory tagging system.


This function returns C{true} if the memory tagging system can be
successfully initialized or it has already been initialized.
Otherwise, C{*errMsg} is set with an explanation for the failure.

Until the system is initialized, the various memory reporting calls
will indicate that no memory has been allocated. Note also that memory
allocated prior to calling C{Initialize()} is not tracked i.e. all
data refers to allocations that happen subsequent to calling
C{Initialize()} .

"""
   result["MallocTag"].GetMaxTotalBytes.func_doc = """**static** GetMaxTotalBytes() -> size_t



Return the maximum total number of bytes that have ever been allocated
at one time.


This is simply the maximum value of GetTotalBytes() since Initialize()
was called.

"""
   result["MallocTag"].CallTree.__doc__ = """
Summary data structure for C{malloc} statistics.


The C{CallTree} structure is used to deliver a snapshot of the current
malloc usage. It is accessible as publicly modifiable data because it
is simply a returned snapshot of the current memory state.

"""
   result["MallocTag"].CallTree.CallSite.__doc__ = """
Record of the bytes allocated under each different tag.


Each construction of a C{TfAutoMallocTag} object with a different
argument produces a distinct C{CallSite} record. The total bytes
outstanding for all memory allocations made under a given call-site
are recorded in C{nBytes}, while the name of the call site is
available as C{name}.

"""
   result["MallocTag"].CallTree.PathNode.__doc__ = """
Node in the call tree structure.


A C{PathNode} captures the hierarchy of active C{TfAutoMallocTag}
objects that are pushed and popped during program execution. Each
C{PathNode} thus describes a sequence of call-sites (i.e. a path down
the call tree). Repeated call sites (in the case of co-recursive
function calls) can be skipped, e.g. pushing tags "A", "B", "C", "B",
"C" leads to only three path-nodes, representing the paths "A", "AB",
and "ABC". Allocations done at the bottom (i.e. when tags "A", "B",
"C", "B", "C" are all active) are billed to the longest path node in
the sequence, which corresponds to the path "ABC").

Path nodes track both the memory they incur directly (
C{nBytesDirect}) but more importantly, the total memory allocated by
themselves and any of their children ( C{nBytes}). The name of a node
( C{siteName}) corresponds to the tag name of the final tag in the
path.

"""
   result["MallocTag"].CallTree.GetPrettyPrintString.im_func.func_doc = """GetPrettyPrintString(setting, maxPrintedNodes) -> string

setting : PrintSetting
maxPrintedNodes : size_t


Return the malloc report string.


Get a malloc report of the tree and/or callsites.

The columns in the report are abbreviated. Here are the definitions.

B{TAGNAME} : The name of the tag being tracked. This matches the
string argument to TfAutoMallocTag constructor.

B{BytesIncl} : Bytes Inclusive. This includes all bytes allocated by
this tag and any bytes of its children.

B{BytesExcl} : Bytes Exclusive. Only bytes allocated exclusively by
this tag, not including any bytes of its children.

B{%Prnt} : (%% Parent). me.BytesIncl / parent.BytesIncl * 100

B{%Exc} : BytesExcl / BytesIncl * 100

B{%Totl} : (%% Total). BytesExcl / TotalBytes * 100

"""
   result["MallocTag"].CallTree.Report.im_func.func_doc = """Report(out, rootName)

out : ostream
rootName : string


Generates a report to the ostream C{out}.


This report is printed in a way that is intended to be used by
xxtracediff. If C{rootName} is non-empty it will replace the name of
the tree root in the report.


----------------------------------------------------------------------
Report(out)

out : ostream


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["MallocTag"].GetCallTree.func_doc = """**static** GetCallTree(tree, skipRepeated) -> bool

tree : CallTree
skipRepeated : bool


Return a snapshot of memory usage.


Returns a snapshot by writing into C{*tree}. See the C{C} *tree
structure for documentation. If C{Initialize()} has not been called, \
*tree is set to a rather blank structure (empty vectors, empty
strings, zero in all integral fields) and C{false} is returned;
otherwise, C{*tree} is set with the contents of the current memory
snapshot and C{true} is returned. It is fine to call this function on
the same C{*tree} instance; each call simply overwrites the data from
the last call. If /p skipRepeated is C{true}, then any repeated
callsite is skipped. See the C{CallTree} documentation for more
details.

"""
   result["MallocTag"].IsInitialized.func_doc = """**static** IsInitialized() -> bool



Return true if the tagging system is active.


If C{Initialize()} has been successfully called, this function returns
C{true}.

"""
   result["Type"].__doc__ = """
TfType represents a dynamic runtime type.


TfTypes are created and discovered at runtime, rather than compile
time.

Features:

   - unique typename

   - safe across DSO boundaries

   - can represent C++ types, pure Python types, or Python subclasses
     of wrapped C++ types

   - lightweight value semantics  you can copy and default construct
     TfType, unlike C{std::type_info}.

   - totally ordered  can use as a C{std::map} key


"""
   result["Type"].GetRoot.func_doc = """**static** GetRoot() -> Type



Return the root type of the type hierarchy.


All known types derive (directly or indirectly) from the root. If a
type is specified with no bases, it is implicitly considered to derive
from the root type.

"""
   result["Type"].GetAllDerivedTypes.im_func.func_doc = """GetAllDerivedTypes(result)

result : set< TfType >


Return the set of all types derived (directly or indirectly) from this
type.

"""
   result["Type"].__init__.im_func.func_doc = """__init__()



Construct an TfType representing an unknown type.


To actually register a new type with the TfType system, see
TfType::Declare() .

Note that this always holds true: ::

  TfType().IsUnknown() == true



----------------------------------------------------------------------
__init__(info)

info : _TypeInfo

"""
   result["Type"].GetAliases.im_func.func_doc = """GetAliases(derivedType) -> sequence<string>

derivedType : Type


Returns a vector of the aliases registered for the derivedType under
this, the base type.



AddAlias()

"""
   result["Type"].Define.func_doc = """**static** Define() -> Type



Define a TfType with the given C++ type T and C++ base types B.


Each of the base types will be declared (but not defined) as TfTypes
if they have not already been.

The typeName of the created TfType will be the canonical demangled
RTTI type name, as defined by GetCanonicalTypeName() .

It is an error to attempt to define a type that has already been
defined.


----------------------------------------------------------------------
Define() -> Type



Define a TfType with the given C++ type T and no bases.


See the other Define() template for more details.

C++ does not allow default template arguments for function templates,
so we provide this separate definition for the case of no bases.

"""
   result["Type"].FindDerivedByName.im_func.func_doc = """**static** FindDerivedByName(name) -> Type

name : string


Retrieve the C{TfType} that derives from this type and has the given
alias or typename.



AddAlias


----------------------------------------------------------------------
FindDerivedByName(name) -> Type

name : string


Retrieve the C{TfType} that derives from BASE and has the given alias
or typename.


This is a convenience method, and is equivalent to: ::

  TfType::Find<BASE>().FindDerivedByName(name)


"""
   result["Type"].GetAllAncestorTypes.im_func.func_doc = """GetAllAncestorTypes(result)

result : sequence< TfType >


Build a vector of all ancestor types inherited by this type.


The starting type is itself included, as the first element of the
results vector.

Types are given in "C3" resolution order, as used for new-style
classes starting in Python 2.3. This algorithm is more complicated
than a simple depth-first traversal of base classes, in order to
prevent some subtle errors with multiple-inheritance. See the
references below for more background.

This can be expensive; consider caching the results. TfType does not
cache this itself since it is not needed internally.

Guido van Rossum. "Unifying types and classes in Python 2.2: Method
resolution order."
http://www.python.org/download/releases/2.2.2/descrintro/#mro

Barrett, Cassels, Haahr, Moon, Playford, Withington. "A Monotonic
Superclass Linearization for Dylan." OOPSLA 96.
http://www.webcom.com/haahr/dylan/linearization-oopsla96.html

"""
   result["Type"].AddAlias.im_func.func_doc = """**static** AddAlias(base, name)

base : Type
name : string


Add an alias name for this type under the given base type.


Aliases are similar to typedefs in C++: they provide an alternate name
for a type. The alias is defined with respect to the given C{base}
type; aliases must be unique beneath that base type.


----------------------------------------------------------------------
AddAlias(name)

name : string


Add an alias for DERIVED beneath BASE.


This is a convenience method, that declares both DERIVED and BASE as
TfTypes before adding the alias.

"""
   result["Type"].FindByName.func_doc = """**static** FindByName(name) -> Type

name : string


Retrieve the C{TfType} corresponding to the given C{name}.


Every type defined in the TfType system has a unique, implementation
independent name. In addition, aliases can be added to identify a type
underneath a specific base type; see TfType::AddAlias() . The given
name will first be tried as an alias under the root type, and
subsequently as a typename.

This method is equivalent to: ::

  TfType::GetRoot().FindDerivedByName(name)

For any object C{obj}, ::

  Find(obj) == FindByName( Find(obj).GetTypeName() )


"""
   result["Type"].IsA.im_func.func_doc = """IsA(queryType) -> bool

queryType : Type


Return true if this type is the same as or derived from C{queryType}.


If C{queryType} is unknown, this always returns C{false}.


----------------------------------------------------------------------
IsA() -> bool



Return true if this type is the same as or derived from T.


This is equivalent to: ::

  IsA(Find<T>())


"""
   result["Type"].Find.func_doc = """**static** Find() -> Type



Retrieve the C{TfType} corresponding to type C{T}.


The type C{T} must have been defined in the type system or the
C{TfType} corresponding to an unknown type is returned.

IsUnknown()


----------------------------------------------------------------------
Find(obj) -> Type

obj : T


Retrieve the C{TfType} corresponding to C{obj}.


The C{TfType} corresponding to the actual object represented by C{obj}
is returned; this may not be the object returned by
C{TfType::Find<T>()} if C{T} is a polymorphic type.

This works for Python subclasses of the C++ type C{T} as well, as long
as C{T} has been wrapped using TfPyPolymorphic.

Of course, the object's type must have been defined in the type system
or the C{TfType} corresponding to an unknown type is returned.

IsUnknown()


----------------------------------------------------------------------
Find(t) -> Type

t : type_info


Retrieve the C{TfType} corresponding to an obj with the given
C{type_info}.

"""
   result["Warning"].__doc__ = """
Represents an object that contains information about a warning.


See Guide To Diagnostic Facilities in the C++ API reference for a
detailed description of the warning issuing API. For a example of how
to post a warning, see C{TF_WARN()} , also in the C++ API reference.

In the Python API, you can issue a warning with Tf.Warn().

"""
   result["ReportActiveErrorMarks"].func_doc = """ReportActiveErrorMarks()



Report current TfErrorMark instances and the stack traces that created
them to stdout for debugging purposes.


To call this function, set _enableTfErrorMarkStackTraces in
errorMark.cpp and enable the TF_ERROR_MARK_TRACKING TfDebug code.


----------------------------------------------------------------------
ReportActiveErrorMarks()



Report current TfErrorMark instances and the stack traces that created
them to stdout for debugging purposes.


To call this function, set _enableTfErrorMarkStackTraces in
errorMark.cpp and enable the TF_ERROR_MARK_TRACKING TfDebug code.

"""
   result["Notice"].__doc__ = """
The base class for objects used to notify interested parties
(listeners) when events have occurred.


The TfNotice class also serves as a container for various dispatching
routines such as Register() and Send() .

See The TfNotice Notification System in the C++ API reference for a
detailed description of the notification system.

Python Example: Registering For and Sending
===========================================

Notices The following code provides examples of how to set up a Notice
listener connection (represented in Python by the Listener class),
including creating and sending notices, registering to receive
notices, and breaking a listener connection. ::

  # To create a new notice type:
  class APythonClass(Tf.Notice):
      '''TfNotice sent when APythonClass does something of interest.'''
      pass
  Tf.Type.Define(APythonClass)
  
  # An interested listener can register to receive notices from all
  # senders, or from a particular type of sender.
  
  # To send a notice to all registered listeners:;
  APythonClass().SendGlobally()
  
  # To send a notice to listeners who register with a specific sender:
  APythonClass().Send(self)
  
  # To register for the notice from any sender:
  my_listener = Tf.Notice.RegisterGlobally(APythonClass, self._HandleNotice)
  
  # To register for the notice from a specific sender
  my_listener = Tf.Notice.Register(APythonClass, self._HandleNotice, sender)
  
  def _HandleNotice(self, notice, sender):
     '''callback function for handling a notice'''
     # do something when the notice arrives
  
  # To revoke interest in a notice
  my_listener.Revoke()

For more on using notices in Python, see the Editor With Notices
tutorial.

"""
   result["InstallTerminateAndCrashHandlers"].func_doc = """InstallTerminateAndCrashHandlers()



(Re)install Tf's crash handler.


This should not generally need to be called since Tf does this itself
when loaded. However, when run in 3rd party environments that install
their own signal handlers, possibly overriding Tf's, this provides a
way to reinstall them, in hopes that they'll stick.

This calls std::set_terminate() and installs signal handlers for
SIGSEGV, SIGBUS, SIGFPE, and SIGABRT.


----------------------------------------------------------------------
InstallTerminateAndCrashHandlers()



(Re)install Tf's crash handler.


This should not generally need to be called since Tf does this itself
when loaded. However, when run in 3rd party environments that install
their own signal handlers, possibly overriding Tf's, this provides a
way to reinstall them, in hopes that they'll stick.

This calls std::set_terminate() and installs signal handlers for
SIGSEGV, SIGBUS, SIGFPE, and SIGABRT.

"""
   result["Debug"].__doc__ = """
Enum-based debugging messages.


The C{TfDebug} class encapsulates a simple enum-based conditional
debugging message system. It is meant as a tool for developers, and
*NOT* as a means of issuing diagnostic messages to end-users. (This is
not strictly true. The TfDebug class is extremely useful and has many
properties that make its use attractive for issuing messages to end-
users. However, for this purpose, please use the C{TF_INFO} macro
which more clearly indicates its intent.)

The features of C{TfDebug} are:
   - Debugging messages/calls for an entire enum group can be compiled
     out-of-existence.

   - The cost of checking if a specific message should be printed at
     runtime (assuming the enum group of the message has not been compile-
     time disabled) is a single inline array lookup, with a compile-time
     index into a global array.

   - Parent/child relationships can be defined so that groups of
     messages can be hierarchically enabled or disabled.
     The use of the facility is simple: ::

  // header file
  #include "pxr/base/tf/debug.h"
  TF_DEBUG_CODES(MY_E1, MY_E2, MY_E3);
  
  // source file
  TF_DEBUG(MY_E2).Msg("something about e2\n");
  
  TF_DEBUG(MY_E3).Msg("val = %d\n", value);

The code in the header file declares the debug symbols to use. Under
the hood, this creates an enum with the values given in the argument
to TF_DEBUG_CODES, along with a first and last sentinel values and
passes that to TF_DEBUG_RANGE. If you'd like to be more explicit
(e.g., because you need the enum type name, or need to be able to turn
off the facility at compile time), you could use the following,
equivalent, form: ::

  // header file
  #include "pxr/base/tf/debug.h"
  enum MyDebugCodes { MY_FIRST, MY_E1, MY_E2, MY_E3, MY_LAST };
  TF_DEBUG_RANGE(MyDebugCodes, MY_FIRST, MY_LAST, true);
  
  // source file
  TF_DEBUG(MY_E2).Msg("something about e2\n");
  
  TF_DEBUG(MY_E3).Msg("val = %d\n", value);

In the source file, the indicated debugging messages are printed only
if the debugging symbols are enabled. Effectively, the construct ::

  TF_DEBUG(MY_E1).Msg(msgExpr)

 is translated to ::

  if (symbol-MY_E1-is- enabled)
      output(msgExpr)

The implications are that C{msgExpr} is only evaluated if symbol
C{MY_E1} symbol is enabled. Further, if the last argument (which must
be a compile-time constant) to the C{TF_DEBUG_RANGE()} macro is
C{false}, then the test is known to fail at compile time; in this
case, the compiler will even eliminate outputting the code to execute
C{msgExpr}. This scheme allows the costs of debugging code to be
controlled at a fine level of detail.

Most commonly debug symbols are inactive by default, but can be turned
on either by an environment variable C{TF_DEBUG}, or interactively
once a program has started by a script interpreter. Both of these are
accomplished as follows: ::

  // source file xyz/debugCodes.cpp
  
  #include "proj/my/debugCodes.h"
  #include "pxr/base/tf/debug.h"
  #include "pxr/base/tf/registryManager.h"
  
  TF_REGISTRY_FUNCTION(TfDebug, MyDebugCodes) {
      TF_DEBUG_ENVIRONMENT_SYMBOL(MY_E1, 
"loading of blah-
blah files");
      TF_DEBUG_ENVIRONMENT_SYMBOL(MY_E2, "parsing of mdl code");
      // etc.
  }

Once this is done, symbols are enabled as follows: ::

  TfDebug::DisableAll<MyDebugCodes>();     // disable everything
  
  TfDebug::Enable(MY_E1);                  // enable just MY_E1


"""
   result["Debug"].IsDebugSymbolNameEnabled.func_doc = """**static** IsDebugSymbolNameEnabled(name) -> bool

name : string


True if the specified debug symbol is set.

"""
   result["Debug"].GetDebugSymbolNames.func_doc = """**static** GetDebugSymbolNames() -> sequence<string>



Get a listing of all debug symbols.

"""
   result["Debug"].GetDebugSymbolDescription.func_doc = """**static** GetDebugSymbolDescription(name) -> string

name : string


Get a description for the specified debug symbol.


A short description of the debug symbol is returned. This is the same
description string that is embedded in the return value of
GetDebugSymbolDescriptions.

"""
   result["Debug"].GetDebugSymbolDescriptions.func_doc = """**static** GetDebugSymbolDescriptions() -> string



Get a description of all debug symbols and their purpose.


A single string describing all registered debug symbols along with
short descriptions is returned.

"""
   result["Debug"].SetDebugSymbolsByName.func_doc = """**static** SetDebugSymbolsByName(pattern, value) -> sequence<string>

pattern : string
value : bool


Set registered debug symbols matching C{pattern} to C{value}.


All registered debug symbols matching C{pattern} are set to C{value}.
The only matching is an exact match with C{pattern}, or if C{pattern}
ends with an '*' as is otherwise a prefix of a debug symbols. The
names of all debug symbols set by this call are returned as a vector.

"""
   result["Debug"].SetOutputFile.func_doc = """**static** SetOutputFile(file)

file : FILE


Direct debug output to *either* stdout or stderr.


Note that *file* MUST be either stdout or stderr. If not, issue an
error and do nothing. Debug output is issued to stdout by default. If
the environment variable TF_DEBUG_OUTPUT_FILE is set to 'stderr', then
output is issued to stderr by default.

"""
   result["GetEnvSetting"].func_doc = """GetEnvSetting(setting) -> T

setting : EnvSetting <T>


Returns the value of the specified env setting, registered using
C{TF_DEFINE_ENV_SETTING}.

"""
   result["LogStackTrace"].func_doc = """LogStackTrace(reason, logtodb)

reason : string
logtodb : bool


Logs both the C++ and the python stack to a file in /var/tmp A message
is printed to stderr reporting that a stack trace has been taken and
what file it has been written to.


If C{logtodb} is true, then the stack trace will be added to the
stack_trace database table.

"""
   result["ScriptModuleLoader"].__doc__ = """
Provides low-level facilities for shared modules with script
bindings to register themselves with their dependences, and provides a
mechanism whereby those script modules will be loaded when necessary.


Currently, this is when one of our script modules is loaded, when
TfPyInitialize is called, and when Plug opens shared modules.

Generally, user code will not make use of this.

"""
   result["ScriptModuleLoader"].__init__.im_func.func_doc = """__init__()


"""
   result["ScriptModuleLoader"].WriteDotFile.im_func.func_doc = """WriteDotFile(file)

file : string


Write a graphviz dot-file for the dependency graph of all.


currently known modules/modules to *file*.

"""
   result["ScriptModuleLoader"].GetModuleNames.im_func.func_doc = """GetModuleNames() -> sequence<string>



Return a list of all currently known modules in a valid dependency
order.

"""
   result["ScriptModuleLoader"].GetModulesDict.im_func.func_doc = """GetModulesDict() -> python.dict



Return a python dict containing all currently known modules under
their canonical names.

"""
   result["StringSplit"].func_doc = """StringSplit(src, separator) -> sequence<string>

src : string
separator : string


Breaks the given string apart, returning a vector of strings.


The string C{source} is broken apart into individual words, where a
word is delimited by the string C{separator}. This function behaves
like pythons string split method.


----------------------------------------------------------------------
StringSplit(src, separator) -> sequence<string>

src : string
separator : string


Breaks the given string apart, returning a vector of strings.


The string C{source} is broken apart into individual words, where a
word is delimited by the string C{separator}. This function behaves
like pythons string split method.

"""
   result["TemplateString"].__doc__ = """
TfTemplateString provides simple string substitutions based on named
placeholders.


Instead of the ''-based substitutions used by printf, template strings
use '$'-based substitutions, using the following rules:

   - "$$" is replaced with a single "$"

   - "$identifier" names a substitution placeholder matching a mapping
     key of "identifier". The first non-identifier character after the "$"
     character terminates the placeholder specification.

   - "${identifier}" is equivalent to "$identifier". It is required
     when valid identifier characters follow the placeholder but are not
     part of the placeholder, such as "${noun}ification".

   - An identifier is a sequence of characters "[A-Z][a-z][0-9]_".
     *TfTemplateString* is immutable: once one is created it may not be
     modified. *TfTemplateString* is fast to copy, since it shares state
     internally between copies. *TfTemplateString* is thread-safe. It may
     be read freely by multiple threads concurrently.

"""
   result["TemplateString"].__init__.im_func.func_doc = """__init__()



Constructs a new template string.


----------------------------------------------------------------------
__init__(template_)

template_ : string


Constructs a new template string.

"""
   result["TemplateString"].GetParseErrors.im_func.func_doc = """GetParseErrors() -> sequence<string>



Returns any error messages generated during template parsing.

"""
   result["TemplateString"].GetEmptyMapping.im_func.func_doc = """GetEmptyMapping() -> Mapping



Returns an empty mapping for the current template.


This method first calls IsValid to ensure that the template is valid.

"""
   result["TemplateString"].SafeSubstitute.im_func.func_doc = """SafeSubstitute(arg1) -> string

arg1 : Mapping


Like Substitute() , except that if placeholders are missing from the
mapping, instead of raising a coding error, the original placeholder
will appear in the resulting string intact.

"""
   result["TemplateString"].Substitute.im_func.func_doc = """Substitute(arg1) -> string

arg1 : Mapping


Performs the template substitution, returning a new string.


The mapping contains keys which match the placeholders in the
template. If a placeholder is found for which no mapping is present, a
coding error is raised.

"""
   result["Error"].__doc__ = """
Represents an object that contains error information.


See Guide To Diagnostic Facilities in the C++ API reference for a
detailed description of the error issuing API. For a example of how to
post an error, see C{TF_ERROR()} , also in the C++ API reference.

In the Python API, you can raise several different types of errors,
including coding errors (Tf.RaiseCodingError), run time errors
(Tf.RaiseRuntimeError), fatal errors (Tf.Fatal).

"""
   result["StringToLong"].func_doc = """StringToLong(txt, outOfRange) -> long

txt : string
outOfRange : bool


Convert a sequence of digits in C{txt} to a long int value.


Caller is responsible for ensuring that C{txt} has content matching:
::

  -?[0-9]+

If the digit sequence's value is out of range, set C{*outOfRange} to
true (if C{outOfRange} is not None) and return either
std::numeric_limits<long>::min() or max(), whichever is closest to the
true value.


----------------------------------------------------------------------
StringToLong(txt, outOfRange) -> long

txt : char
outOfRange : bool


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
StringToLong(txt, outOfRange) -> long

txt : string
outOfRange : bool


Convert a sequence of digits in C{txt} to a long int value.


Caller is responsible for ensuring that C{txt} has content matching:
::

  -?[0-9]+

If the digit sequence's value is out of range, set C{*outOfRange} to
true (if C{outOfRange} is not None) and return either
std::numeric_limits<long>::min() or max(), whichever is closest to the
true value.


----------------------------------------------------------------------
StringToLong(txt, outOfRange) -> long

txt : char
outOfRange : bool


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["MakeValidIdentifier"].func_doc = """MakeValidIdentifier(in) -> string

in : string


Produce a valid identifier (see TfIsValidIdentifier) from C{in} by
replacing invalid characters with '_'.


If C{in} is empty, return "_".


----------------------------------------------------------------------
MakeValidIdentifier(in) -> string

in : string


Produce a valid identifier (see TfIsValidIdentifier) from C{in} by
replacing invalid characters with '_'.


If C{in} is empty, return "_".

"""
   result["Singleton"].__doc__ = """
Manage a single instance of an object (see.


Typical Use for a canonical example).

"""
   result["StringToULong"].func_doc = """StringToULong(txt, outOfRange) -> unsigned long

txt : string
outOfRange : bool


Convert a sequence of digits in C{txt} to an unsigned long value.


Caller is responsible for ensuring that C{txt} has content matching:
::

  [0-9]+

If the digit sequence's value is out of range, set C{*outOfRange} to
true (if C{outOfRange} is not None) and return
std::numeric_limits<unsigned long>="">::max().


----------------------------------------------------------------------
StringToULong(txt, outOfRange) -> unsigned long

txt : char
outOfRange : bool


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
StringToULong(txt, outOfRange) -> unsigned long

txt : string
outOfRange : bool


Convert a sequence of digits in C{txt} to an unsigned long value.


Caller is responsible for ensuring that C{txt} has content matching:
::

  [0-9]+

If the digit sequence's value is out of range, set C{*outOfRange} to
true (if C{outOfRange} is not None) and return
std::numeric_limits<unsigned long>="">::max().


----------------------------------------------------------------------
StringToULong(txt, outOfRange) -> unsigned long

txt : char
outOfRange : bool


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["RefPtrTracker"].__doc__ = """
Provides tracking of C{TfRefPtr} objects to particular objects.


Clients can enable, at compile time, tracking of C{TfRefPtr} objects
that point to particular instances of classes derived from
C{TfRefBase}. This is useful if you have a ref counted object with a
ref count that should've gone to zero but didn't. This tracker can
tell you every C{TfRefPtr} that's holding the C{TfRefBase} and a stack
trace where it was created or last assigned to.

Clients can get a report of all watched instances and how many
C{TfRefPtr} objects are holding them using C{ReportAllWatchedCounts()}
(in python use C{Tf.RefPtrTracker()} .GetAllWatchedCountsReport()).
You can see all of the stack traces using C{ReportAllTraces()} (in
python use C{Tf.RefPtrTracker()} .GetAllTracesReport()).

Clients will typically enable tracking using code like this: ::

  #include "pxr/base/tf/refPtrTracker.h"
  
  class MyRefBaseType;
  typedef TfRefPtr<MyRefBaseType> MyRefBaseTypeRefPtr;
  
  TF_DECLARE_REFPTR_TRACK(MyRefBaseType);
  
  class MyRefBaseType {
  ...
  public:
      static bool _ShouldWatch(const MyRefBaseType*);
  ...
  };
  
  TF_DEFINE_REFPTR_TRACK(MyRefBaseType, MyRefBaseType::_ShouldWatch);

Note that the C{TF_DECLARE_REFPTR_TRACK()} macro must be invoked
before any use of the C{MyRefBaseTypeRefPtr} type.

The C{MyRefBaseType::_ShouldWatch()} function returns C{true} if the
given instance of C{MyRefBaseType} should be tracked. You can also use
C{TfRefPtrTracker::WatchAll()} to watch every instance (but that might
use a lot of memory and time).

If you have a base type, C{B}, and a derived type, C{D}, and you hold
instances of C{D} in a C{TfRefPtr < C{B>}} (i.e. a pointer to the
base) then you must track both type C{B} and type C{D}. But you can
use C{TfRefPtrTracker::WatchNone()} when tracking C{B} if you're not
interested in instances of C{B}.

"""
   result["RefPtrTracker"].__init__.im_func.func_doc = """__init__()


"""
   result["RealPath"].func_doc = """RealPath(path, allowInaccessibleSuffix, error) -> string

path : string
allowInaccessibleSuffix : bool
error : string


Returns the canonical path of the specified filename, eliminating any
symbolic links encountered in the path.


This is a wrapper to realpath(3), which caters for situations where
the real realpath() would return a None string, such as the case where
the path is really just a program name. The memory allocated by
realpath is managed internally.

If *allowInaccessibleSuffix* is true, then this function will only
invoke realpath on the longest accessible prefix of *path*, and then
append the inaccessible suffix.

If *error* is provided, it is set to the error reason should an error
occur while computing the real path. If no error occurs, the string is
cleared.

"""
   result["TemplateString"].template = property(result["TemplateString"].template.fget, result["TemplateString"].template.fset, result["TemplateString"].template.fdel, """type : string


Returns the template source string supplied to the constructor.

""")
   result["Stopwatch"].microseconds = property(result["Stopwatch"].microseconds.fget, result["Stopwatch"].microseconds.fset, result["Stopwatch"].microseconds.fdel, """type : int64_t


Return the accumulated time in microseconds.


Note that 45 minutes will overflow a 32-bit counter, so take care to
save the result in an C{int64_t}, and not a regular C{int} or C{long}.

""")
   result["CallContext"].file = property(result["CallContext"].file.fget, result["CallContext"].file.fset, result["CallContext"].file.fdel, """type : char

""")
   result["Stopwatch"].isShared = property(result["Stopwatch"].isShared.fget, result["Stopwatch"].isShared.fset, result["Stopwatch"].isShared.fdel, """type : bool


Returns true if this stopwatch is shared.

""")
   result["Stopwatch"].milliseconds = property(result["Stopwatch"].milliseconds.fget, result["Stopwatch"].milliseconds.fset, result["Stopwatch"].milliseconds.fdel, """type : int64_t


Return the accumulated time in milliseconds.

""")
   result["Type"].isUnknown = property(result["Type"].isUnknown.fget, result["Type"].isUnknown.fset, result["Type"].isUnknown.fdel, """type : bool


Return true if this is the unknown type, representing a type unknown
to the TfType system.


The unknown type does not derive from the root type, or any other
type.

""")
   result["CallContext"].function = property(result["CallContext"].function.fget, result["CallContext"].function.fset, result["CallContext"].function.fdel, """type : char

""")
   result["Type"].baseTypes = property(result["Type"].baseTypes.fget, result["Type"].baseTypes.fset, result["Type"].baseTypes.fdel, """type : sequence< TfType >


Return a vector of types from which this type was derived.

""")
   result["CallContext"].prettyFunction = property(result["CallContext"].prettyFunction.fget, result["CallContext"].prettyFunction.fset, result["CallContext"].prettyFunction.fdel, """type : char

""")
   result["Type"].isPlainOldDataType = property(result["Type"].isPlainOldDataType.fget, result["Type"].isPlainOldDataType.fset, result["Type"].isPlainOldDataType.fdel, """type : bool


Return true if this is a plain old data type, as defined by C++.

""")
   result["Type"].typeName = property(result["Type"].typeName.fget, result["Type"].typeName.fset, result["Type"].typeName.fdel, """type : string


Return the machine-independent name for this type.


This name is specified when the TfType is declared.

Declare()

""")
   result["PyModuleWasLoaded"].name.im_func.func_doc = """name() -> string



Return the name of the module that was loaded.

"""
   result["Type"].sizeof = property(result["Type"].sizeof.fget, result["Type"].sizeof.fset, result["Type"].sizeof.fdel, """type : size_t


Return the size required to hold an instance of this type on the stack
(does not include any heap allocated memory the instance uses).


This is what the C++ sizeof operator returns for the type, so this
value is not very useful for Python types (it will always be
sizeof(boost::python::object)).

""")
   result["Stopwatch"].name = property(result["Stopwatch"].name.fget, result["Stopwatch"].name.fset, result["Stopwatch"].name.fdel, """type : string


Return the name of the C{TfStopwatch}.

""")
   result["Stopwatch"].nanoseconds = property(result["Stopwatch"].nanoseconds.fget, result["Stopwatch"].nanoseconds.fset, result["Stopwatch"].nanoseconds.fdel, """type : int64_t


Return the accumulated time in nanoseconds.


Note that this number can easily overflow a 32-bit counter, so take
care to save the result in an C{int64_t}, and not a regular C{int} or
C{long}.

""")
   result["TemplateString"].valid = property(result["TemplateString"].valid.fget, result["TemplateString"].valid.fset, result["TemplateString"].valid.fdel, """type : bool


Returns true if the current template is well formed.


Empty templates are valid.

""")
   result["CallContext"].line = property(result["CallContext"].line.fget, result["CallContext"].line.fset, result["CallContext"].line.fdel, """type : size_t

""")
   result["Stopwatch"].sampleCount = property(result["Stopwatch"].sampleCount.fget, result["Stopwatch"].sampleCount.fset, result["Stopwatch"].sampleCount.fdel, """type : size_t


Return the current sample count.


The sample count, which is simply the number of calls to C{Stop()}
since creation or a call to C{Reset()} , is useful for computing
average running times of a repeated task.

""")
   result["Type"].isEnumType = property(result["Type"].isEnumType.fget, result["Type"].isEnumType.fset, result["Type"].isEnumType.fdel, """type : bool


Return true if this is an enum type.

""")
   result["Stopwatch"].seconds = property(result["Stopwatch"].seconds.fget, result["Stopwatch"].seconds.fset, result["Stopwatch"].seconds.fdel, """type : double


Return the accumulated time in seconds as a C{double}.

""")