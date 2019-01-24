def Execute(result):
   result["Collector"].__doc__ = """
This is a singleton class that records TraceEvent instances and
populates TraceCollection instances.


All public methods of TraceCollector are safe to call from any thread.

"""
   result["Collector"].EndEventAtTime.im_func.func_doc = """EndEventAtTime(key, ms)

key : Key
ms : double


Record an end event with *key* at a specified time if C{Category} is
enabled.


This version of the method allows the passing of a specific number of
elapsed milliseconds, *ms*, to use for this event. This method is used
for testing and debugging code.

"""
   result["Collector"].EndEvent.im_func.func_doc = """EndEvent(key) -> TimeStamp

key : Key


Record an end event with *key* if C{Category} is enabled.


A matching begin event must have preceded this end event.

If the key is known at compile time EndScope and Scope methods are
preferred because they have lower overhead.

The TimeStamp of the TraceEvent or 0 if the collector is disabled.

EndScope

Scope

"""
   result["Collector"].GetLabel.im_func.func_doc = """GetLabel() -> string



Return the label associated with this collector.

"""
   result["Collector"].Clear.im_func.func_doc = """Clear() -> TRACE_API void



Clear all pending events from the collector.


No TraceCollection will be made for these events.

"""
   result["Collector"].__init__.im_func.func_doc = """__init__()


"""
   result["Collector"].BeginEventAtTime.im_func.func_doc = """BeginEventAtTime(key, ms)

key : Key
ms : double


Record a begin event with *key* at a specified time if C{Category} is
enabled.


This version of the method allows the passing of a specific number of
elapsed milliseconds, *ms*, to use for this event. This method is used
for testing and debugging code.

"""
   result["Collector"].BeginEvent.im_func.func_doc = """BeginEvent(key) -> TimeStamp

key : Key


Record a begin event with *key* if C{Category} is enabled.


A matching end event is expected some time in the future.

If the key is known at compile time C{BeginScope} and C{Scope} methods
are preferred because they have lower overhead.

The TimeStamp of the TraceEvent or 0 if the collector is disabled.

BeginScope

Scope

"""
   result["AggregateNode"].__doc__ = """
A representation of a call tree.


Each node represents one or more calls that occurred in the trace.
Multiple calls to a child node are aggregated into one node.

"""
   result["__doc__"] = """

Contents
========

   - Overview

   - Instrumentation

   - Recording and Reporting

   - Performance Overhead

   - Details

Overview
========

Defines utility classes for counting, timing, measuring, and recording
events. The TraceCollector class records TraceEvent objects. The
TraceReporter class contains functions to generate reports on events
gathered by the TraceCollector object.

Instrumentation
===============

Instrumentation is done by adding TRACE macros to code.

For example: ::

  #include "pxr/base/trace/trace.h"
  
  // Typical usage.
  void Foo()
  {
      TRACE_FUNCTION();
      ...
      {
          // More work is done here that needs timing separated.
          TRACE_SCOPE("Inner Scope");
          ...
      }
  }

Python tracing is also supported: ::

  from pxr import Trace
  
  @Trace.TraceFunction
  def foo():
      ...
      with Trace.TraceScope("Inner Scope"):
          ...

Adding Trace macros does have a small overhead even when tracing is
disabled. Sometimes a performance sensitive function may have a slow
path that is taken infrequently, but timing information is needed. In
cases like this, it is possible to reduce the overhead of the
instrumentation to specific scopes. ::

  // This is an example of a performance sensitive function that has a slow path.
  void PerformanceSensitiveFunction(bool slowPath)
  {
      // No TRACE Macro is used in the fast path to avoid any overhead.
      if (slowPath) {
          // This will only pay the overhead cost of the trace instrumentation on
          // the slow path.
          TRACE_FUNCTION_SCOPE("Slow path");
          ...
      }
      ...
  }

Recording and Reporting
=======================

Recording is done through the TraceCollector class. Enabling the
collector will cause TRACE macros to record events. Reports are
generated with the TraceReporter class. ::

  int main(int argc, char* argv[])
  {
      // Start recording events.
      TraceCollector::GetInstance().SetEnabled(true);
      Foo();
      ...
      // Stop recording events.
      TraceCollector::GetInstance().SetEnabled(false);
      // Print the report.
      ofstream reportFile("trace.txt");
      TraceReporter::GetGlobalReporter().Report(reportFile);
  }

The default report is an aggregated call graph showing the include
time, exclusive time, and call count of each scope.

Example Report: ::

  Tree view  ==============
     inclusive    exclusive        
     13.000 ms                    1 samples    MainThread
     13.000 ms     4.000 ms       1 samples    | OuterScope
      9.000 ms     8.000 ms       1 samples    |   InnerScope
      1.000 ms     1.000 ms       2 samples    |   | Inner Scope 2
     13.000 ms                    1 samples    Thread 1
     13.000 ms     4.000 ms       1 samples    | OuterScope
      9.000 ms     8.000 ms       1 samples    |   InnerScope
      1.000 ms     1.000 ms       2 samples    |   | Inner Scope 2

The Chrome tracing format is also supported using the
TraceReporter::ReportChromeTracing method.

A report can also be generated from a program instrumented with
libtrace using the PXR_ENABLE_GLOBAL_TRACE environment variable. If
this variable is set, the TraceCollector singleton will start
recording on initialization, and a report will be written to stdout at
program exit. ::

  >env PXR_ENABLE_GLOBAL_TRACE=1 usdview HelloWorld.usda 
--
quitAfterStartup
  
  Tree view  ==============
     inclusive    exclusive        
    358.500 ms                    1 samples    Main Thread
      0.701 ms     0.701 ms       8 samples    | SdfPath::_InitWithString
      0.003 ms     0.003 ms       2 samples    | {anonymous}::VtDictionaryToPython::convert
    275.580 ms   275.580 ms       3 samples    | PlugPlugin::_Load
      0.014 ms     0.014 ms       3 samples    | UcGetCurrentUnit
      1.470 ms     0.002 ms       1 samples    | UcIsKnownUnit
      1.467 ms     0.026 ms       1 samples    |   Uc::_InitUnitData [initialization]
      1.442 ms     1.442 ms       1 samples    |   | Uc_Engine::GetValue
      0.750 ms     0.000 ms       1 samples    | UcGetValue
      0.750 ms     0.750 ms       1 samples    |   Uc_Engine::GetValue
      9.141 ms     0.053 ms       1 samples    | PrCreatePathResolverForUnit
      0.002 ms     0.002 ms       6 samples    |   UcIsKnownUnit
      ...

The aggregated call graph can be accessed through
TraceReporter::GetAggregateTreeRoot. The non-aggregated call graph can
be access through TraceReporter::GetEventTree.

Performance Overhead
====================

Adding trace instrumentation macros has the following overhead:
   - When tracing is disabled, TRACE_FUNCTION() ,
     TRACE_FUNCTION_SCOPE() , and TRACE_SCOPE() initialize 16 bytes of
     stack memory, read an atomic int, and have 2 branches.

   - When tracing is enabled, overhead of TRACE_FUNCTION() ,
     TRACE_FUNCTION_SCOPE() , and TRACE_SCOPE() is about 100 times larger
     than the disabled case. (.33ns vs 33ns in microbenchmarks on our
     workstations).

   - The dynamic versions of the macros TRACE_FUNCTION_DYNAMIC() ,
     TRACE_SCOPE_DYNAMIC() have a much higher overhead than the static
     versions. The reason for this is that for the static versions, the
     names of the scopes are compiled as constexpr data, but the dynamic
     versions construct strings at runtime. This overhead of dynamic macros
     is true whether tracing is enabled or not. Because of this, the static
     versions should be preferred whenever possible.
     It is possible to disable TRACE macros from generating code by
     defining TRACE_DISABLE in the preprocessor.

The TraceCollector class and TRACE macros are thread-safe.

Details
=======

For more detailed information see Trace Details

"""
   result["Reporter"].__doc__ = """
This class converters streams of TraceEvent objects into call trees
which can then be used as a data source to a GUI or written out to a
file.

"""
   result["Reporter"].ReportChromeTracing.im_func.func_doc = """ReportChromeTracing(s) -> TRACE_API void

s : ostream


Generates a timeline trace report suitable for viewing in Chrome's
trace viewer.

"""
   result["Reporter"].GetLabel.im_func.func_doc = """GetLabel() -> string



Return the label associated with this reporter.

"""
   result["Reporter"].UpdateAggregateTree.im_func.func_doc = """UpdateAggregateTree() -> TRACE_API void



If we want to have multiple reporters per collector, this will need to
be changed so that all reporters reporting on a collector update their
respective trees.

"""
   result["Reporter"].Report.im_func.func_doc = """Report(s, iterationCount) -> TRACE_API void

s : ostream
iterationCount : int


Generates a report to the ostream *s*, dividing all times by
*iterationCount*.

"""
   result["Reporter"].__init__.im_func.func_doc = """__init__(label, dataSource) -> TRACE_API

label : string
dataSource : DataSourcePtr

"""
   result["Reporter"].ReportTimes.im_func.func_doc = """ReportTimes(s) -> TRACE_API void

s : ostream


Generates a report of the times to the ostream *s*.

"""
   result["Reporter"].ClearTree.im_func.func_doc = """ClearTree() -> TRACE_API void



Clears event tree and counters.

"""
   result["Reporter"].aggregateTreeRoot = property(result["Reporter"].aggregateTreeRoot.fget, result["Reporter"].aggregateTreeRoot.fset, result["Reporter"].aggregateTreeRoot.fdel, """type : TRACE_API TraceAggregateNodePtr


Returns the root node of the aggregated call tree.

""")
   result["AggregateNode"].expanded = property(result["AggregateNode"].expanded.fget, result["AggregateNode"].expanded.fset, result["AggregateNode"].expanded.fdel, """type : bool


Returns whether this node is expanded in a gui.

----------------------------------------------------------------------
Sets whether or not this node is expanded in a gui.

""")
   result["Reporter"].foldRecursiveCalls = property(result["Reporter"].foldRecursiveCalls.fget, result["Reporter"].foldRecursiveCalls.fset, result["Reporter"].foldRecursiveCalls.fdel, """type : TRACE_API bool


Returns the current setting for recursion folding for stack trace
event reporting.

----------------------------------------------------------------------type : TRACE_API void


When stack trace event reporting, this sets whether or not recursive
calls are folded in the output.


Recursion folding is useful when the stacks contain deep recursive
structures.

""")
   result["AggregateNode"].inclusiveTime = property(result["AggregateNode"].inclusiveTime.fget, result["AggregateNode"].inclusiveTime.fset, result["AggregateNode"].inclusiveTime.fdel, """type : TimeStamp


Returns the total time of this node ands its children.

""")
   result["AggregateNode"].key = property(result["AggregateNode"].key.fget, result["AggregateNode"].key.fset, result["AggregateNode"].key.fdel, """type : TfToken


Returns the node's key.

""")
   result["AggregateNode"].exclusiveCount = property(result["AggregateNode"].exclusiveCount.fget, result["AggregateNode"].exclusiveCount.fset, result["AggregateNode"].exclusiveCount.fdel, """type : int


Returns the exclusive count.

""")
   result["Reporter"].globalReporter.__doc__ = """**static** globalReporter() -> TRACE_API TraceReporterPtr



Returns the global reporter.

"""
   result["AggregateNode"].count = property(result["AggregateNode"].count.fget, result["AggregateNode"].count.fset, result["AggregateNode"].count.fdel, """type : int


Returns the call count of this node.


C{recursive} determines if recursive calls are counted.

""")
   result["Reporter"].groupByFunction = property(result["Reporter"].groupByFunction.fget, result["Reporter"].groupByFunction.fset, result["Reporter"].groupByFunction.fdel, """type : TRACE_API bool


Returns the current group-by-function state.

----------------------------------------------------------------------type : TRACE_API void


This affects only stack trace event reporting.


If C{true} then all events in a function are grouped together
otherwise events are split out by address.

""")
   result["AggregateNode"].children = property(result["AggregateNode"].children.fget, result["AggregateNode"].children.fset, result["AggregateNode"].children.fdel, """type : AggregateNodePtrVector

""")
   result["AggregateNode"].exclusiveTime = property(result["AggregateNode"].exclusiveTime.fget, result["AggregateNode"].exclusiveTime.fset, result["AggregateNode"].exclusiveTime.fdel, """type : TRACE_API TimeStamp


Returns the time spent in this node but not its children.

""")
   result["Collector"].enabled = property(result["Collector"].enabled.fget, result["Collector"].enabled.fset, result["Collector"].enabled.fdel, """type : TRACE_API void


Enables or disables collection of events for DefaultCategory.

----------------------------------------------------------------------**static** type : bool


Returns whether collection of events is enabled for DefaultCategory.

""")
   result["AggregateNode"].id = property(result["AggregateNode"].id.fget, result["AggregateNode"].id.fset, result["AggregateNode"].id.fdel, """type : Id


Returns the node's id.

""")