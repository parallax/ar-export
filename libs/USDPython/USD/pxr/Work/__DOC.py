def Execute(result):
   result["GetPhysicalConcurrencyLimit"].func_doc = """GetPhysicalConcurrencyLimit() -> WORK_API unsigned



Return the number of physical execution cores available to the
program.


This is either the number of physical cores on the machine or the
number of cores specified by the process's affinity mask, whichever is
smaller.

"""
   result["SetConcurrencyLimitArgument"].func_doc = """SetConcurrencyLimitArgument(n) -> WORK_API void

n : int


Sanitize C{n} as described below and set the concurrency limit
accordingly.


This function is useful for interpreting command line arguments.

If C{n} is zero, then do not change the current concurrency limit.

If C{n} is a positive, non-zero value then call
WorkSetConcurrencyLimit(n). Note that calling this method with C{n}
greater than the value returned by WorkGetPhysicalConcurrencyLimit()
may overtax the machine.

If C{n} is negative, then set the concurrency limit to all but abs(
C{n}) cores. The number of cores is determined by the value returned
by WorkGetPhysicalConcurrencyLimit() . For example, if C{n} is -2,
then use all but two cores. If abs( C{n}) is greater than the number
of physical cores, then call WorkSetConcurrencyLimit(1), effectively
disabling concurrency.

"""
   result["SetConcurrencyLimit"].func_doc = """SetConcurrencyLimit(n) -> WORK_API void

n : unsigned


Set the concurrency limit to C{n}, if C{n} is a non-zero value.


If C{n} is zero, then do not change the current concurrency limit.

Note, calling this function with n> WorkGetPhysicalConcurrencyLimit()
may overtax the machine.

In general, very few places should call this function. Call it in
places where the number of allowed threads is dictated, for example,
by a hosting environment. Lower-level module code should never call
this function.

"""
   result["SetMaximumConcurrencyLimit"].func_doc = """SetMaximumConcurrencyLimit() -> WORK_API void



Set the concurrency limit to be the maximum recommended for the
hardware on which it's running.


Equivalent to: ::

  WorkSetConcurrencyLimit(WorkGetPhysicalConcurrencyLimit()).


"""
   result["__doc__"] = """

Summary
=======

The B{work} module is intended to simplify the use of multithreading
in the context of our software ecosystem.

This module is intended as a thin abstraction layer on top of a
multithreading subsystem. The abstraction serves two purposes:
   - To simplify the use of common constructs like "Parallel For"

   - To centralize our dependency on a particular multithreading
     subsystem (e.g., TBB, etc.).

Because of the way multithreading subsystems work and because of the
way they need to interact with each other in managing system
resources, it is not generally practical for each client to use
whatever threading system they like (e.g., TBB for one client, OpenMP
for another).

Initializing and Limiting Multithreading
========================================

The module defaults to maximum concurrency, i.e. it will attempt to
use as many threads as available on the system. The default
concurrency limit is established at static initialization time. The
PXR_WORK_THREAD_LIMIT environment variable can be set to further limit
concurrency, such as for example in a farm environment.
PXR_WORK_THREAD_LIMIT must be set to an integer N, denoting one of the
following:
   - 0 - maximum concurrency (default if unset)

   - 1 - single-threaded mode

   - positive N - limit to N threads (clamped to number of hardware
     threads available)

   - negative N - limit to all but N hardware threads (clamped to 1)

The concurrency limit can be set programmatically, using for example:
::

  WorkSetConcurrencyLimitArgument(N);

or ::

  WorkSetMaximumConcurrencyLimit();

It is preferable to use WorkSetMaximumConcurrencyLimit() when the
desire to use the hardware to its fullest rather than specify the
maximum concurrency limit manually.

Simple "Parallel For" Example
=============================

Once you've initialized the module, you can now harness the awesome
power of your multi-core machine. Here's a simple example of a
Parallel For. ::

  static void _DoubleTheValues(size_t begin, size_t end, std::vector<int> *v)
  {
      for (size_t i = begin; i < end; ++i)
          (*v)[i] *= 2;
  }
  
  
  static void DoubleInParallel(std::vector<int> *v)
  {
      WorkParallelForN(v->size(), boost::bind(&_DoubleTheValues, _1, _2, v));
  }

You can avoid the boost::bind and provide your own functor object as
well.

"""
   result["GetConcurrencyLimit"].func_doc = """GetConcurrencyLimit() -> WORK_API unsigned



Return the current concurrency limit, always>= 1.


The initial value is determined by the PXR_WORK_THREAD_LIMIT env
setting, which defaults to WorkGetPhysicalConcurrencyLimit() . If the
env setting has been explicitly set to a non-zero value, it will
always override any concurrency limit set via the API calls below.

Note that this can return a value larger than
WorkGetPhysicalConcurrencyLimit() if WorkSetConcurrencyLimit() was
called with such a value, or if PXR_WORK_THREAD_LIMIT was set with
such a value.

"""