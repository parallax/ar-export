def Execute(result):
   result["AllTrue"].func_doc = """AllTrue(a) -> bool

a : Array <T>


Returns true if every element of input array is not VtZero, else
false.


Intended to be used to evaluate results of boolean operations on
arrays, e.g. ::

  a = Vt.StringArray((3,),("foo","bar","baz"))
  t = Vt.AllTrue(Vt.Equal(a,"bar"))

(This example, if you look carefully, evaluates this function not on
the strings, but on the results of the comparison).

"""
   result["NotEqual"].func_doc = """NotEqual(a, b) -> Array <T>

a : Array <T>
b : Array <T>


Returns a bool array specifying, element-by-element, if the two inputs
contain inequal values.


The shape of the return array is the same as the shape of the largest
input array.

If one input is a single element (either a single-element array or a
scalar of the same type held in the array), it is compared to all the
elements in the other array. Otherwise both arrays must have the same
shape.


----------------------------------------------------------------------
NotEqual(a, b) -> Array <T>

a : T
b : Array <T>


----------------------------------------------------------------------
NotEqual(a, b) -> Array <T>

a : Array <T>
b : T

"""
   result["Less"].func_doc = """Less(a, b) -> Array <T>

a : Array <T>
b : Array <T>


Returns a bool array specifying, element-by-element, if the first
input contains values less than those in the second input.


The shape of the return array is the same as the shape of the largest
input array.

If one input is a single element (either a single-element array or a
scalar of the same type held in the array), it is compared to all the
elements in the other array. Otherwise both arrays must have the same
shape.


----------------------------------------------------------------------
Less(a, b) -> Array <T>

a : T
b : Array <T>


----------------------------------------------------------------------
Less(a, b) -> Array <T>

a : Array <T>
b : T

"""
   result["LessOrEqual"].func_doc = """LessOrEqual(a, b) -> Array <T>

a : Array <T>
b : Array <T>


Returns a bool array specifying, element-by-element, if the first
input contains values less than or equal to those in the second input.


The shape of the return array is the same as the shape of the largest
input array.

If one input is a single element (either a single-element array or a
scalar of the same type held in the array), it is compared to all the
elements in the other array. Otherwise both arrays must have the same
shape.


----------------------------------------------------------------------
LessOrEqual(a, b) -> Array <T>

a : T
b : Array <T>


----------------------------------------------------------------------
LessOrEqual(a, b) -> Array <T>

a : Array <T>
b : T

"""
   result["Equal"].func_doc = """Equal(a, b) -> Array <T>

a : Array <T>
b : Array <T>


Returns a bool array specifying, element-by-element, if the two inputs
contain equal values.


The shape of the return array is the same as the shape of the largest
input array.

If one input is a single element (either a single-element array or a
scalar of the same type held in the array), it is compared to all the
elements in the other array. Otherwise both arrays must have the same
shape.


----------------------------------------------------------------------
Equal(a, b) -> Array <T>

a : T
b : Array <T>


----------------------------------------------------------------------
Equal(a, b) -> Array <T>

a : Array <T>
b : T

"""
   result["Greater"].func_doc = """Greater(a, b) -> Array <T>

a : Array <T>
b : Array <T>


Returns a bool array specifying, element-by-element, if the first
input contains values greater than those in the second input.


The shape of the return array is the same as the shape of the largest
input array.

If one input is a single element (either a single-element array or a
scalar of the same type held in the array), it is compared to all the
elements in the other array. Otherwise both arrays must have the same
shape.


----------------------------------------------------------------------
Greater(a, b) -> Array <T>

a : T
b : Array <T>


----------------------------------------------------------------------
Greater(a, b) -> Array <T>

a : Array <T>
b : T

"""
   result["AnyTrue"].func_doc = """AnyTrue(a) -> bool

a : Array <T>


Returns true if any element of input array is not VtZero, else false.


Intended to be used to evaluate results of boolean operations on
arrays, e.g. ::

  a = Vt.StringArray((3,),("foo","bar","baz"))
  t = Vt.AnyTrue(Vt.Equal(a,"bar"))

(This example, if you look carefully, evaluates this function not on
the strings, but on the results of the comparison).

"""
   result["__doc__"] = """

Overview
========

Defines classes that provide for type abstraction (VtValue) and
enhanced array types (VtArray). The Vt module also provides functions
for manipulating value types. This module operates on the level of
language data types and there are differences in the C++ and Python
interfaces.

Type Erasure with VtValue
=========================

The VtValue class wraps type objects (float, int, bool, GfVec3d, and
so on) in a type-agnostic container that includes functions for
determining the content type within the container. The VtValue class
is found in the C++ API only, since Python does not have the strong
type restrictions of C++. Python to C++ type conversion is handled
automatically by the system.

Shared Arrays - VtArray
=======================

The VtArray class represents an arbitrary length homogeneous
container. In the C++ API, the constructor lets you create an array of
a specified size. The VtArray interface on the Python side is
implemented as a set of typed array classes (for example, BoolArray,
StringArray, Vec4dArray).

"""
   result["GreaterOrEqual"].func_doc = """GreaterOrEqual(a, b) -> Array <T>

a : Array <T>
b : Array <T>


Returns a bool array specifying, element-by-element, if the first
input contains values greater than or equal to those in the second
input.


The shape of the return array is the same as the shape of the largest
input array.

If one input is a single element (either a single-element array or a
scalar of the same type held in the array), it is compared to all the
elements in the other array. Otherwise both arrays must have the same
shape.


----------------------------------------------------------------------
GreaterOrEqual(a, b) -> Array <T>

a : T
b : Array <T>


----------------------------------------------------------------------
GreaterOrEqual(a, b) -> Array <T>

a : Array <T>
b : T

"""
   result["Cat"].func_doc = """Cat(a0, a1, aN) -> Array <T>

a0 : Array <T>
a1 : Array <T>
aN : ... VtArray <T>


Concatenates arrays.


The result is an array with length equal to the sum of the number of
elements in the source arrays.

"""