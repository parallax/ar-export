def Execute(result):
   result["GetLength"].func_doc = """GetLength(v) -> double

v : Vec2d


Returns the geometric length of C{v}.


----------------------------------------------------------------------
GetLength(v) -> float

v : Vec2f


Returns the geometric length of C{v}.


----------------------------------------------------------------------
GetLength(v) -> Half

v : Vec2h


Returns the geometric length of C{v}.


----------------------------------------------------------------------
GetLength(v) -> double

v : Vec3d


Returns the geometric length of C{v}.


----------------------------------------------------------------------
GetLength(v) -> float

v : Vec3f


Returns the geometric length of C{v}.


----------------------------------------------------------------------
GetLength(v) -> Half

v : Vec3h


Returns the geometric length of C{v}.


----------------------------------------------------------------------
GetLength(v) -> double

v : Vec4d


Returns the geometric length of C{v}.


----------------------------------------------------------------------
GetLength(v) -> float

v : Vec4f


Returns the geometric length of C{v}.


----------------------------------------------------------------------
GetLength(v) -> Half

v : Vec4h


Returns the geometric length of C{v}.

"""
   result["Floor"].func_doc = """Floor(f) -> double

f : double


Return floor( C{f}).


----------------------------------------------------------------------
Floor(f) -> float

f : float


Return floor( C{f}).


----------------------------------------------------------------------
Floor(f) -> double

f : double


Return floor( C{f}).


----------------------------------------------------------------------
Floor(f) -> float

f : float


Return floor( C{f}).

"""
   result["Matrix3f"].__doc__ = """
Stores a 3x3 matrix of C{float} elements.


A basic type.

Matrices are defined to be in row-major order, so C{matrix[i][j]}
indexes the element in the *i* th row and the *j* th column.

3D Transformations
==================

Three methods, SetRotate() , SetScale() , and ExtractRotation() ,
interpret a GfMatrix3f as a 3D transformation. By convention, vectors
are treated primarily as row vectors, implying the following:

   - Transformation matrices are organized to deal with row vectors,
     not column vectors.

   - Each of the Set() methods in this class completely rewrites the
     matrix; for example, SetRotate() yields a matrix which does nothing
     but rotate.

   - When multiplying two transformation matrices, the matrix on the
     left applies a more local transformation to a row vector. For example,
     if R represents a rotation matrix and S represents a scale matrix, the
     product R*S will rotate a row vector, then scale it.


"""
   result["Matrix3f"].GetTranspose.im_func.func_doc = """GetTranspose() -> GF_API GfMatrix3f



Returns the transpose of the matrix.

"""
   result["Matrix3f"].SetZero.im_func.func_doc = """SetZero() -> Matrix3f



Sets the matrix to zero.

"""
   result["Matrix3f"].SetScale.im_func.func_doc = """SetScale(scaleFactors) -> GF_API GfMatrix3f

scaleFactors : Vec3f


Sets the matrix to specify a nonuniform scaling in x, y, and z by the
factors in vector *scaleFactors*.


----------------------------------------------------------------------
SetScale(scaleFactor) -> GF_API GfMatrix3f

scaleFactor : float


Sets matrix to specify a uniform scaling by *scaleFactor*.

"""
   result["Matrix3f"].GetHandedness.im_func.func_doc = """GetHandedness() -> GF_API double



Returns the sign of the determinant of the matrix, i.e.


1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
singular matrix.

"""
   result["Matrix3f"].SetRow.im_func.func_doc = """SetRow(i, v)

i : int
v : Vec3f


Sets a row of the matrix from a Vec3.

"""
   result["Matrix3f"].Orthonormalize.im_func.func_doc = """Orthonormalize(issueWarning) -> GF_API bool

issueWarning : bool


Makes the matrix orthonormal in place.


This is an iterative method that is much more stable than the previous
cross/cross method. If the iterative method does not converge, a
warning is issued.

Returns true if the iteration converged, false otherwise. Leaves any
translation part of the matrix unchanged. If *issueWarning* is true,
this method will issue a warning if the iteration does not converge,
otherwise it will be silent.

"""
   result["Matrix3f"].GetColumn.im_func.func_doc = """GetColumn(i) -> Vec3f

i : int


Gets a column of the matrix as a Vec3.

"""
   result["Matrix3f"].__init__.im_func.func_doc = """__init__()



Default constructor. Leaves the matrix component values undefined.


----------------------------------------------------------------------
__init__(m00, m01, m02, m10, m11, m12, m20, m21, m22)

m00 : float
m01 : float
m02 : float
m10 : float
m11 : float
m12 : float
m20 : float
m21 : float
m22 : float


Constructor.


Initializes the matrix from 9 independent C{float} values, specified
in row-major order. For example, parameter *m10* specifies the value
in row 1 and column 0.


----------------------------------------------------------------------
__init__(m)

m : float


Constructor.


Initializes the matrix from a 3x3 array of C{float} values, specified
in row-major order.


----------------------------------------------------------------------
__init__(s)

s : float


Constructor.


Explicitly initializes the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
__init__(s)

s : int


This explicit constructor initializes the matrix to C{s} times the
identity matrix.


----------------------------------------------------------------------
__init__(v)

v : Vec3f


Constructor.


Explicitly initializes the matrix to diagonal form, with the *i* th
element on the diagonal set to C{v[i]} .


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<double>>


Constructor.


Initialize the matrix from a vector of vectors of double. The vector
is expected to be 3x3. If it is too big, only the first 3 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<float>>


Constructor.


Initialize the matrix from a vector of vectors of float. The vector is
expected to be 3x3. If it is too big, only the first 3 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(rot) -> GF_API

rot : Rotation


Constructor. Initialize matrix from rotation.


----------------------------------------------------------------------
__init__(rot) -> GF_API

rot : Quatf


Constructor. Initialize matrix from a quaternion.


----------------------------------------------------------------------
__init__(m) -> GF_API

m : class GfMatrix3d


This explicit constructor converts a "double" matrix to a "float"
matrix.

"""
   result["Matrix3f"].GetDeterminant.im_func.func_doc = """GetDeterminant() -> GF_API double



Returns the determinant of the matrix.

"""
   result["Matrix3f"].ExtractRotation.im_func.func_doc = """ExtractRotation() -> GF_API GfRotation



Returns the rotation corresponding to this matrix.


This works well only if the matrix represents a rotation.

For good results, consider calling Orthonormalize() before calling
this method.

"""
   result["Matrix3f"].SetDiagonal.im_func.func_doc = """SetDiagonal(s) -> GF_API GfMatrix3f

s : float


Sets the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
SetDiagonal(arg1) -> GF_API GfMatrix3f

arg1 : Vec3f


Sets the matrix to have diagonal ( C{v[0], v[1], v[2]} ).

"""
   result["Matrix3f"].GetRow.im_func.func_doc = """GetRow(i) -> Vec3f

i : int


Gets a row of the matrix as a Vec3.

"""
   result["Matrix3f"].GetInverse.im_func.func_doc = """GetInverse(det, eps) -> GF_API GfMatrix3f

det : double
eps : double


Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
matrix is singular.


(FLT_MAX is the largest value a C{float} can have, as defined by the
system.) The matrix is considered singular if the determinant is less
than or equal to the optional parameter *eps*. If *det* is non-null,
C{*det} is set to the determinant.

"""
   result["Matrix3f"].SetIdentity.im_func.func_doc = """SetIdentity() -> Matrix3f



Sets the matrix to the identity matrix.

"""
   result["Matrix3f"].Set.im_func.func_doc = """Set(m00, m01, m02, m10, m11, m12, m20, m21, m22) -> Matrix3f

m00 : float
m01 : float
m02 : float
m10 : float
m11 : float
m12 : float
m20 : float
m21 : float
m22 : float


Sets the matrix from 9 independent C{float} values, specified in row-
major order.


For example, parameter *m10* specifies the value in row 1 and column
0.


----------------------------------------------------------------------
Set(m) -> Matrix3f

m : float


Sets the matrix from a 3x3 array of C{float} values, specified in row-
major order.

"""
   result["Matrix3f"].SetColumn.im_func.func_doc = """SetColumn(i, v)

i : int
v : Vec3f


Sets a column of the matrix from a Vec3.

"""
   result["Matrix3f"].IsLeftHanded.im_func.func_doc = """IsLeftHanded() -> bool



Returns true if the vectors in matrix form a left-handed coordinate
system.

"""
   result["Matrix3f"].SetRotate.im_func.func_doc = """SetRotate(rot) -> GF_API GfMatrix3f

rot : Quatf


Sets the matrix to specify a rotation equivalent to *rot*.


----------------------------------------------------------------------
SetRotate(rot) -> GF_API GfMatrix3f

rot : Rotation


Sets the matrix to specify a rotation equivalent to *rot*.

"""
   result["Matrix3f"].GetOrthonormalized.im_func.func_doc = """GetOrthonormalized(issueWarning) -> GF_API GfMatrix3f

issueWarning : bool


Returns an orthonormalized copy of the matrix.

"""
   result["Matrix3f"].IsRightHanded.im_func.func_doc = """IsRightHanded() -> bool



Returns true if the vectors in the matrix form a right-handed
coordinate system.

"""
   result["Interval"].IsMaxFinite.im_func.func_doc = """IsMaxFinite() -> bool



Returns true if the maximum value is finite.

"""
   result["Interval"].IsMinOpen.im_func.func_doc = """IsMinOpen() -> bool



Minimum boundary condition.

"""
   result["Interval"].GetFullInterval.func_doc = """**static** GetFullInterval() -> Interval



Returns the full interval (-inf, inf).

"""
   result["Interval"].IsMinClosed.im_func.func_doc = """IsMinClosed() -> bool



Minimum boundary condition.

"""
   result["Interval"].IsMaxOpen.im_func.func_doc = """IsMaxOpen() -> bool



Maximum boundary condition.

"""
   result["Interval"].Intersects.im_func.func_doc = """Intersects(i) -> bool

i : Interval


Return true iff the given interval i intersects this interval.

"""
   result["Interval"].IsMinFinite.im_func.func_doc = """IsMinFinite() -> bool



Returns true if the minimum value is finite.

"""
   result["Interval"].IsFinite.im_func.func_doc = """IsFinite() -> bool



Returns true if both the maximum and minimum value are finite.

"""
   result["Interval"].IsMaxClosed.im_func.func_doc = """IsMaxClosed() -> bool



Maximum boundary condition.

"""
   result["Vec3f"].__doc__ = """
Basic type for a vector of 3 float components.


Represents a vector of 3 components of type C{float}. It is intended
to be fast and simple.

"""
   result["Vec3f"].Normalize.im_func.func_doc = """Normalize(eps) -> float

eps : float


Normalizes the vector in place to unit length, returning the length
before normalization.


If the length of the vector is smaller than C{eps}, then the vector is
set to vector/ C{eps}. The original length of the vector is returned.
See also GfNormalize() .

"""
   result["Vec3f"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec3f


----------------------------------------------------------------------
__init__(value)

value : float


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1, s2)

s0 : float
s1 : float
s2 : float


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.


----------------------------------------------------------------------
__init__(other)

other : class GfVec3d


Construct from GfVec3d.


----------------------------------------------------------------------
__init__(other)

other : class GfVec3h


Implicitly convert from GfVec3h.


----------------------------------------------------------------------
__init__(other)

other : class GfVec3i


Implicitly convert from GfVec3i.

"""
   result["Vec3f"].OrthogonalizeBasis.func_doc = """**static** OrthogonalizeBasis(tx, ty, tz, normalize, eps) -> GF_API bool

tx : Vec3f
ty : Vec3f
tz : Vec3f
normalize : bool
eps : double


Orthogonalize and optionally normalize a set of basis vectors.


This uses an iterative method that is very stable even when the
vectors are far from orthogonal (close to colinear). The number of
iterations and thus the computation time does increase as the vectors
become close to colinear, however. Returns a bool specifying whether
the solution converged after a number of iterations. If it did not
converge, the returned vectors will be as close as possible to
orthogonal within the iteration limit. Colinear vectors will be
unaltered, and the method will return false.

"""
   result["Vec3f"].BuildOrthonormalFrame.im_func.func_doc = """BuildOrthonormalFrame(v1, v2, eps) -> GF_API void

v1 : Vec3f
v2 : Vec3f
eps : float


Sets C{v1} and C{v2} to unit vectors such that v1, v2 and *this are
mutually orthogonal.


If the length L of *this is smaller than C{eps}, then v1 and v2 will
have magnitude L/eps. As a result, the function delivers a continuous
result as *this shrinks in length.

"""
   result["Vec3f"].GetLength.im_func.func_doc = """GetLength() -> float



Length.

"""
   result["Vec3f"].ZAxis.func_doc = """**static** ZAxis() -> Vec3f



Create a unit vector along the Z-axis.

"""
   result["Vec3f"].GetComplement.im_func.func_doc = """GetComplement(b) -> Vec3f

b : Vec3f


Returns the orthogonal complement of C{this->GetProjection(b)} .


That is: ::

  *this - this->GetProjection(b)


"""
   result["Vec3f"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Vec3f

eps : float

"""
   result["Vec3f"].GetProjection.im_func.func_doc = """GetProjection(v) -> Vec3f

v : Vec3f


Returns the projection of C{this} onto C{v}.


That is: ::

  v * (*this * v)


"""
   result["Vec3f"].YAxis.func_doc = """**static** YAxis() -> Vec3f



Create a unit vector along the Y-axis.

"""
   result["Vec3f"].XAxis.func_doc = """**static** XAxis() -> Vec3f



Create a unit vector along the X-axis.

"""
   result["Vec3f"].Axis.func_doc = """**static** Axis(i) -> Vec3f

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 3.

"""
   result["Vec3h"].__doc__ = """
Basic type for a vector of 3 GfHalf components.


Represents a vector of 3 components of type C{GfHalf}. It is intended
to be fast and simple.

"""
   result["Vec3h"].Normalize.im_func.func_doc = """Normalize(eps) -> Half

eps : Half


Normalizes the vector in place to unit length, returning the length
before normalization.


If the length of the vector is smaller than C{eps}, then the vector is
set to vector/ C{eps}. The original length of the vector is returned.
See also GfNormalize() .

"""
   result["Vec3h"].YAxis.func_doc = """**static** YAxis() -> Vec3h



Create a unit vector along the Y-axis.

"""
   result["Vec3h"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec3h


----------------------------------------------------------------------
__init__(value)

value : Half


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1, s2)

s0 : Half
s1 : Half
s2 : Half


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.


----------------------------------------------------------------------
__init__(other)

other : class GfVec3d


Construct from GfVec3d.


----------------------------------------------------------------------
__init__(other)

other : class GfVec3f


Construct from GfVec3f.


----------------------------------------------------------------------
__init__(other)

other : class GfVec3i


Implicitly convert from GfVec3i.

"""
   result["Vec3h"].OrthogonalizeBasis.func_doc = """**static** OrthogonalizeBasis(tx, ty, tz, normalize, eps) -> GF_API bool

tx : Vec3h
ty : Vec3h
tz : Vec3h
normalize : bool
eps : double


Orthogonalize and optionally normalize a set of basis vectors.


This uses an iterative method that is very stable even when the
vectors are far from orthogonal (close to colinear). The number of
iterations and thus the computation time does increase as the vectors
become close to colinear, however. Returns a bool specifying whether
the solution converged after a number of iterations. If it did not
converge, the returned vectors will be as close as possible to
orthogonal within the iteration limit. Colinear vectors will be
unaltered, and the method will return false.

"""
   result["Vec3h"].BuildOrthonormalFrame.im_func.func_doc = """BuildOrthonormalFrame(v1, v2, eps) -> GF_API void

v1 : Vec3h
v2 : Vec3h
eps : Half


Sets C{v1} and C{v2} to unit vectors such that v1, v2 and *this are
mutually orthogonal.


If the length L of *this is smaller than C{eps}, then v1 and v2 will
have magnitude L/eps. As a result, the function delivers a continuous
result as *this shrinks in length.

"""
   result["Vec3h"].GetComplement.im_func.func_doc = """GetComplement(b) -> Vec3h

b : Vec3h


Returns the orthogonal complement of C{this->GetProjection(b)} .


That is: ::

  *this - this->GetProjection(b)


"""
   result["Vec3h"].ZAxis.func_doc = """**static** ZAxis() -> Vec3h



Create a unit vector along the Z-axis.

"""
   result["Vec3h"].GetLength.im_func.func_doc = """GetLength() -> Half



Length.

"""
   result["Vec3h"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Vec3h

eps : Half

"""
   result["Vec3h"].GetProjection.im_func.func_doc = """GetProjection(v) -> Vec3h

v : Vec3h


Returns the projection of C{this} onto C{v}.


That is: ::

  v * (*this * v)


"""
   result["Vec3h"].XAxis.func_doc = """**static** XAxis() -> Vec3h



Create a unit vector along the X-axis.

"""
   result["Vec3h"].Axis.func_doc = """**static** Axis(i) -> Vec3h

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 3.

"""
   result["CompMult"].func_doc = """CompMult(v1, v2) -> Vec2d

v1 : Vec2d
v2 : Vec2d


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec2f

v1 : Vec2f
v2 : Vec2f


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec2h

v1 : Vec2h
v2 : Vec2h


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec2i

v1 : Vec2i
v2 : Vec2i


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec3d

v1 : Vec3d
v2 : Vec3d


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec3f

v1 : Vec3f
v2 : Vec3f


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec3h

v1 : Vec3h
v2 : Vec3h


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec3i

v1 : Vec3i
v2 : Vec3i


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec4d

v1 : Vec4d
v2 : Vec4d


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec4f

v1 : Vec4f
v2 : Vec4f


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec4h

v1 : Vec4h
v2 : Vec4h


Returns component-wise multiplication of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompMult(v1, v2) -> Vec4i

v1 : Vec4i
v2 : Vec4i


Returns component-wise multiplication of vectors C{v1} and C{v2}.

"""
   result["GetNormalized"].func_doc = """GetNormalized(v, eps) -> Vec2d

v : Vec2d
eps : double


Returns a normalized (unit-length) vector with the same direction as
C{v}.


If the length of this vector is smaller than C{eps}, the vector
divided by C{eps} is returned.


----------------------------------------------------------------------
GetNormalized(v, eps) -> Vec2f

v : Vec2f
eps : float


Returns a normalized (unit-length) vector with the same direction as
C{v}.


If the length of this vector is smaller than C{eps}, the vector
divided by C{eps} is returned.


----------------------------------------------------------------------
GetNormalized(v, eps) -> Vec2h

v : Vec2h
eps : Half


Returns a normalized (unit-length) vector with the same direction as
C{v}.


If the length of this vector is smaller than C{eps}, the vector
divided by C{eps} is returned.


----------------------------------------------------------------------
GetNormalized(v, eps) -> Vec3d

v : Vec3d
eps : double


Returns a normalized (unit-length) vector with the same direction as
C{v}.


If the length of this vector is smaller than C{eps}, the vector
divided by C{eps} is returned.


----------------------------------------------------------------------
GetNormalized(v, eps) -> Vec3f

v : Vec3f
eps : float


Returns a normalized (unit-length) vector with the same direction as
C{v}.


If the length of this vector is smaller than C{eps}, the vector
divided by C{eps} is returned.


----------------------------------------------------------------------
GetNormalized(v, eps) -> Vec3h

v : Vec3h
eps : Half


Returns a normalized (unit-length) vector with the same direction as
C{v}.


If the length of this vector is smaller than C{eps}, the vector
divided by C{eps} is returned.


----------------------------------------------------------------------
GetNormalized(v, eps) -> Vec4d

v : Vec4d
eps : double


Returns a normalized (unit-length) vector with the same direction as
C{v}.


If the length of this vector is smaller than C{eps}, the vector
divided by C{eps} is returned.


----------------------------------------------------------------------
GetNormalized(v, eps) -> Vec4f

v : Vec4f
eps : float


Returns a normalized (unit-length) vector with the same direction as
C{v}.


If the length of this vector is smaller than C{eps}, the vector
divided by C{eps} is returned.


----------------------------------------------------------------------
GetNormalized(v, eps) -> Vec4h

v : Vec4h
eps : Half


Returns a normalized (unit-length) vector with the same direction as
C{v}.


If the length of this vector is smaller than C{eps}, the vector
divided by C{eps} is returned.

"""
   result["Size3"].Set.im_func.func_doc = """Set(v) -> Size3

v : size_t


Set to the values in C{v}.


----------------------------------------------------------------------
Set(v0, v1, v2) -> Size3

v0 : size_t
v1 : size_t
v2 : size_t


Set to values passed directly.

"""
   result["Size3"].__init__.im_func.func_doc = """__init__()



Default constructor initializes components to zero.


----------------------------------------------------------------------
__init__(o)

o : Size3


Copy constructor.


----------------------------------------------------------------------
__init__(o)

o : Vec3i


Conversion from GfVec3i.


----------------------------------------------------------------------
__init__(v)

v : size_t


Construct from an array.


----------------------------------------------------------------------
__init__(v0, v1, v2)

v0 : size_t
v1 : size_t
v2 : size_t


Construct from three values.

"""
   result["Size2"].Set.im_func.func_doc = """Set(v) -> Size2

v : size_t


Set to the values in a given array.


----------------------------------------------------------------------
Set(v0, v1) -> Size2

v0 : size_t
v1 : size_t


Set to values passed directly.

"""
   result["Size2"].__init__.im_func.func_doc = """__init__()



Default constructor initializes components to zero.


----------------------------------------------------------------------
__init__(o)

o : Size2


Copy constructor.


----------------------------------------------------------------------
__init__(o)

o : Vec2i


Conversion from GfVec2i.


----------------------------------------------------------------------
__init__(v)

v : size_t


Construct from an array.


----------------------------------------------------------------------
__init__(v0, v1)

v0 : size_t
v1 : size_t


Construct from two values.

"""
   result["Camera"].__doc__ = """
Object-based representation of a camera.


This class provides a thin wrapper on the camera data model, with a
small number of computations.

"""
   result["Camera"].SetOrthographicFromAspectRatioAndSize.im_func.func_doc = """SetOrthographicFromAspectRatioAndSize(aspectRatio, orthographicSize, direction) -> GF_API void

aspectRatio : float
orthographicSize : float
direction : FOVDirection


Sets the frustum to be orthographic such that it has the given
C{aspectRatio} and such that the orthographic width, respectively,
orthographic height (in cm) is equal to C{orthographicSize} (depending
on direction).

"""
   result["Camera"].FOVDirection.__doc__ = """
Direction used for Field of View or orthographic size.

"""
   result["Camera"].GetFieldOfView.im_func.func_doc = """GetFieldOfView(direction) -> GF_API float

direction : FOVDirection


Returns the horizontal or vertical field of view in degrees.

"""
   result["Camera"].SetPerspectiveFromAspectRatioAndFieldOfView.im_func.func_doc = """SetPerspectiveFromAspectRatioAndFieldOfView(aspectRatio, fieldOfView, direction, horizontalAperture) -> GF_API void

aspectRatio : float
fieldOfView : float
direction : FOVDirection
horizontalAperture : float


Sets the frustum to be projective with the given C{aspectRatio} and
horizontal, respectively, vertical field of view C{fieldOfView}
(similar to gluPerspective when direction = FOVVertical).


Do not pass values for C{horionztalAperture} unless you care about
DepthOfField.

"""
   result["Camera"].__init__.im_func.func_doc = """__init__(transform, projection, horizontalAperture, verticalAperture, horizontalApertureOffset, verticalApertureOffset, focalLength, clippingRange, clippingPlanes, fStop, focusDistance) -> GF_API

transform : Matrix4d
projection : Projection
horizontalAperture : float
verticalAperture : float
horizontalApertureOffset : float
verticalApertureOffset : float
focalLength : float
clippingRange : Range1f
clippingPlanes : sequence< GfVec4f >
fStop : float
focusDistance : float

"""
   result["Camera"].Projection.__doc__ = """
Projection type.

"""
   result["Range1d"].__doc__ = """
Basic type: 1-dimensional floating point range.


This class represents a 1-dimensional range (or interval) All
operations are component-wise and conform to interval mathematics. An
empty range is one where max<min. The default empty is
[FLT_MAX,-FLT_MAX]

"""
   result["Range1d"].Contains.im_func.func_doc = """Contains(point) -> bool

point : double


Returns true if the C{point} is located inside the range.


As with all operations of this type, the range is assumed to include
its extrema.


----------------------------------------------------------------------
Contains(range) -> bool

range : Range1d


Returns true if the C{range} is located entirely inside the range.


As with all operations of this type, the ranges are assumed to include
their extrema.

"""
   result["Range1d"].IntersectWith.im_func.func_doc = """IntersectWith(b) -> Range1d

b : Range1d


Modifies this range to hold its intersection with C{b} and returns the
result.

"""
   result["Range1d"].SetMin.im_func.func_doc = """SetMin(min)

min : double


Sets the minimum value of the range.

"""
   result["Range1d"].GetSize.im_func.func_doc = """GetSize() -> double



Returns the size of the range.

"""
   result["Range1d"].SetEmpty.im_func.func_doc = """SetEmpty()



Sets the range to an empty interval.

"""
   result["Range1d"].GetMin.im_func.func_doc = """GetMin() -> double



Returns the minimum value of the range.

"""
   result["Range1d"].GetMax.im_func.func_doc = """GetMax() -> double



Returns the maximum value of the range.

"""
   result["Range1d"].UnionWith.im_func.func_doc = """UnionWith(b) -> Range1d

b : Range1d


Extend C{this} to include C{b}.


----------------------------------------------------------------------
UnionWith(b) -> Range1d

b : double


Extend C{this} to include C{b}.

"""
   result["Range1d"].SetMax.im_func.func_doc = """SetMax(max)

max : double


Sets the maximum value of the range.

"""
   result["Range1d"].IsEmpty.im_func.func_doc = """IsEmpty() -> bool



Returns whether the range is empty (max<min).

"""
   result["Range1d"].GetIntersection.func_doc = """**static** GetIntersection(a, b) -> Range1d

a : Range1d
b : Range1d


Returns a C{GfRange1d} that describes the intersection of C{a} and
C{b}.

"""
   result["Range1d"].GetMidpoint.im_func.func_doc = """GetMidpoint() -> double



Returns the midpoint of the range, that is, 0.5*(min+max).


Note: this returns zero in the case of default-constructed ranges, or
ranges set via SetEmpty() .

"""
   result["Range1d"].GetDistanceSquared.im_func.func_doc = """GetDistanceSquared(p) -> GF_API double

p : double


Compute the squared distance from a point to the range.

"""
   result["Range1d"].__init__.im_func.func_doc = """__init__()



The default constructor creates an empty range.


----------------------------------------------------------------------
__init__(min, max)

min : double
max : double


This constructor initializes the minimum and maximum points.

"""
   result["Range1d"].GetUnion.func_doc = """**static** GetUnion(a, b) -> Range1d

a : Range1d
b : Range1d


Returns the smallest C{GfRange1d} which contains both C{a} and C{b}.

"""
   result["Matrix2f"].__doc__ = """
Stores a 2x2 matrix of C{float} elements.


A basic type.

Matrices are defined to be in row-major order, so C{matrix[i][j]}
indexes the element in the *i* th row and the *j* th column.

"""
   result["Matrix2f"].Set.im_func.func_doc = """Set(m00, m01, m10, m11) -> Matrix2f

m00 : float
m01 : float
m10 : float
m11 : float


Sets the matrix from 4 independent C{float} values, specified in row-
major order.


For example, parameter *m10* specifies the value in row 1 and column
0.


----------------------------------------------------------------------
Set(m) -> Matrix2f

m : float


Sets the matrix from a 2x2 array of C{float} values, specified in row-
major order.

"""
   result["Matrix2f"].GetInverse.im_func.func_doc = """GetInverse(det, eps) -> GF_API GfMatrix2f

det : double
eps : double


Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
matrix is singular.


(FLT_MAX is the largest value a C{float} can have, as defined by the
system.) The matrix is considered singular if the determinant is less
than or equal to the optional parameter *eps*. If *det* is non-null,
C{*det} is set to the determinant.

"""
   result["Matrix2f"].SetColumn.im_func.func_doc = """SetColumn(i, v)

i : int
v : Vec2f


Sets a column of the matrix from a Vec2.

"""
   result["Matrix2f"].__init__.im_func.func_doc = """__init__()



Default constructor. Leaves the matrix component values undefined.


----------------------------------------------------------------------
__init__(m00, m01, m10, m11)

m00 : float
m01 : float
m10 : float
m11 : float


Constructor.


Initializes the matrix from 4 independent C{float} values, specified
in row-major order. For example, parameter *m10* specifies the value
in row 1 and column 0.


----------------------------------------------------------------------
__init__(m)

m : float


Constructor.


Initializes the matrix from a 2x2 array of C{float} values, specified
in row-major order.


----------------------------------------------------------------------
__init__(s)

s : float


Constructor.


Explicitly initializes the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
__init__(s)

s : int


This explicit constructor initializes the matrix to C{s} times the
identity matrix.


----------------------------------------------------------------------
__init__(v)

v : Vec2f


Constructor.


Explicitly initializes the matrix to diagonal form, with the *i* th
element on the diagonal set to C{v[i]} .


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<double>>


Constructor.


Initialize the matrix from a vector of vectors of double. The vector
is expected to be 2x2. If it is too big, only the first 2 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<float>>


Constructor.


Initialize the matrix from a vector of vectors of float. The vector is
expected to be 2x2. If it is too big, only the first 2 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(m) -> GF_API

m : class GfMatrix2d


This explicit constructor converts a "double" matrix to a "float"
matrix.

"""
   result["Matrix2f"].GetDeterminant.im_func.func_doc = """GetDeterminant() -> GF_API double



Returns the determinant of the matrix.

"""
   result["Matrix2f"].GetTranspose.im_func.func_doc = """GetTranspose() -> GF_API GfMatrix2f



Returns the transpose of the matrix.

"""
   result["Matrix2f"].GetRow.im_func.func_doc = """GetRow(i) -> Vec2f

i : int


Gets a row of the matrix as a Vec2.

"""
   result["Matrix2f"].SetZero.im_func.func_doc = """SetZero() -> Matrix2f



Sets the matrix to zero.

"""
   result["Matrix2f"].GetColumn.im_func.func_doc = """GetColumn(i) -> Vec2f

i : int


Gets a column of the matrix as a Vec2.

"""
   result["Matrix2f"].SetDiagonal.im_func.func_doc = """SetDiagonal(s) -> GF_API GfMatrix2f

s : float


Sets the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
SetDiagonal(arg1) -> GF_API GfMatrix2f

arg1 : Vec2f


Sets the matrix to have diagonal ( C{v[0], v[1]} ).

"""
   result["Matrix2f"].SetRow.im_func.func_doc = """SetRow(i, v)

i : int
v : Vec2f


Sets a row of the matrix from a Vec2.

"""
   result["Matrix2f"].SetIdentity.im_func.func_doc = """SetIdentity() -> Matrix2f



Sets the matrix to the identity matrix.

"""
   result["Matrix2d"].__doc__ = """
Stores a 2x2 matrix of C{double} elements.


A basic type.

Matrices are defined to be in row-major order, so C{matrix[i][j]}
indexes the element in the *i* th row and the *j* th column.

"""
   result["Matrix2d"].GetColumn.im_func.func_doc = """GetColumn(i) -> Vec2d

i : int


Gets a column of the matrix as a Vec2.

"""
   result["Matrix2d"].GetInverse.im_func.func_doc = """GetInverse(det, eps) -> GF_API GfMatrix2d

det : double
eps : double


Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
matrix is singular.


(FLT_MAX is the largest value a C{float} can have, as defined by the
system.) The matrix is considered singular if the determinant is less
than or equal to the optional parameter *eps*. If *det* is non-null,
C{*det} is set to the determinant.

"""
   result["Matrix2d"].SetColumn.im_func.func_doc = """SetColumn(i, v)

i : int
v : Vec2d


Sets a column of the matrix from a Vec2.

"""
   result["Matrix2d"].__init__.im_func.func_doc = """__init__()



Default constructor. Leaves the matrix component values undefined.


----------------------------------------------------------------------
__init__(m00, m01, m10, m11)

m00 : double
m01 : double
m10 : double
m11 : double


Constructor.


Initializes the matrix from 4 independent C{double} values, specified
in row-major order. For example, parameter *m10* specifies the value
in row 1 and column 0.


----------------------------------------------------------------------
__init__(m)

m : double


Constructor.


Initializes the matrix from a 2x2 array of C{double} values, specified
in row-major order.


----------------------------------------------------------------------
__init__(s)

s : double


Constructor.


Explicitly initializes the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
__init__(s)

s : int


This explicit constructor initializes the matrix to C{s} times the
identity matrix.


----------------------------------------------------------------------
__init__(v)

v : Vec2d


Constructor.


Explicitly initializes the matrix to diagonal form, with the *i* th
element on the diagonal set to C{v[i]} .


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<double>>


Constructor.


Initialize the matrix from a vector of vectors of double. The vector
is expected to be 2x2. If it is too big, only the first 2 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<float>>


Constructor.


Initialize the matrix from a vector of vectors of float. The vector is
expected to be 2x2. If it is too big, only the first 2 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(m) -> GF_API

m : class GfMatrix2f


This explicit constructor converts a "float" matrix to a "double"
matrix.

"""
   result["Matrix2d"].GetDeterminant.im_func.func_doc = """GetDeterminant() -> GF_API double



Returns the determinant of the matrix.

"""
   result["Matrix2d"].GetTranspose.im_func.func_doc = """GetTranspose() -> GF_API GfMatrix2d



Returns the transpose of the matrix.

"""
   result["Matrix2d"].GetRow.im_func.func_doc = """GetRow(i) -> Vec2d

i : int


Gets a row of the matrix as a Vec2.

"""
   result["Matrix2d"].SetZero.im_func.func_doc = """SetZero() -> Matrix2d



Sets the matrix to zero.

"""
   result["Matrix2d"].Set.im_func.func_doc = """Set(m00, m01, m10, m11) -> Matrix2d

m00 : double
m01 : double
m10 : double
m11 : double


Sets the matrix from 4 independent C{double} values, specified in row-
major order.


For example, parameter *m10* specifies the value in row 1 and column
0.


----------------------------------------------------------------------
Set(m) -> Matrix2d

m : double


Sets the matrix from a 2x2 array of C{double} values, specified in
row-major order.

"""
   result["Matrix2d"].SetDiagonal.im_func.func_doc = """SetDiagonal(s) -> GF_API GfMatrix2d

s : double


Sets the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
SetDiagonal(arg1) -> GF_API GfMatrix2d

arg1 : Vec2d


Sets the matrix to have diagonal ( C{v[0], v[1]} ).

"""
   result["Matrix2d"].SetRow.im_func.func_doc = """SetRow(i, v)

i : int
v : Vec2d


Sets a row of the matrix from a Vec2.

"""
   result["Matrix2d"].SetIdentity.im_func.func_doc = """SetIdentity() -> Matrix2d



Sets the matrix to the identity matrix.

"""
   result["Slerp"].func_doc = """Slerp(alpha, q0, q1) -> GF_API GfQuatd

alpha : double
q0 : Quatd
q1 : Quatd


Spherically linearly interpolate between C{q0} and C{q1}.


If the interpolant C{alpha} is zero, then the result is C{q0}, while
C{alpha} of one yields C{q1}.


----------------------------------------------------------------------
Slerp(q0, q1, alpha) -> GF_API GfQuatd

q0 : Quatd
q1 : Quatd
alpha : double


----------------------------------------------------------------------
Slerp(alpha, q0, q1) -> GF_API GfQuaternion

alpha : double
q0 : Quaternion
q1 : Quaternion


If the interpolant C{alpha} is zero, then the result is C{q0}, while
C{alpha} of one yields C{q1}.


----------------------------------------------------------------------
Slerp(q0, q1, alpha) -> GF_API GfQuaternion

q0 : Quaternion
q1 : Quaternion
alpha : double


----------------------------------------------------------------------
Slerp(alpha, q0, q1) -> GF_API GfQuatf

alpha : double
q0 : Quatf
q1 : Quatf


Spherically linearly interpolate between C{q0} and C{q1}.


If the interpolant C{alpha} is zero, then the result is C{q0}, while
C{alpha} of one yields C{q1}.


----------------------------------------------------------------------
Slerp(q0, q1, alpha) -> GF_API GfQuatf

q0 : Quatf
q1 : Quatf
alpha : double


----------------------------------------------------------------------
Slerp(alpha, q0, q1) -> GF_API GfQuath

alpha : double
q0 : Quath
q1 : Quath


Spherically linearly interpolate between C{q0} and C{q1}.


If the interpolant C{alpha} is zero, then the result is C{q0}, while
C{alpha} of one yields C{q1}.


----------------------------------------------------------------------
Slerp(q0, q1, alpha) -> GF_API GfQuath

q0 : Quath
q1 : Quath
alpha : double


----------------------------------------------------------------------
Slerp(alpha, v0, v1) -> GF_API GfVec3d

alpha : double
v0 : Vec3d
v1 : Vec3d


Spherical linear interpolation in three dimensions.


----------------------------------------------------------------------
Slerp(alpha, v0, v1) -> GF_API GfVec3f

alpha : double
v0 : Vec3f
v1 : Vec3f


Spherical linear interpolation in three dimensions.


----------------------------------------------------------------------
Slerp(alpha, v0, v1) -> GF_API GfVec3h

alpha : double
v0 : Vec3h
v1 : Vec3h


Spherical linear interpolation in three dimensions.

"""
   result["Frustum"].GetNearFar.im_func.func_doc = """GetNearFar() -> Range1d



Returns the near/far interval.

"""
   result["Frustum"].Transform.im_func.func_doc = """Transform(matrix) -> GF_API GfFrustum

matrix : Matrix4d


Transforms the frustum by the given matrix.


The transformation matrix is applied as follows: the position and the
direction vector are transformed with the given matrix. Then the
length of the new direction vector is used to rescale the near and far
plane and the view distance. Finally, the points that define the
reference plane are transformed by the matrix. This method assures
that the frustum will not be sheared or perspective-projected.

Note that this definition means that the transformed frustum does not
preserve scales very well. Do *not* use this function to transform a
frustum that is to be used for precise operations such as intersection
testing.

"""
   result["Frustum"].SetPerspective.im_func.func_doc = """SetPerspective(fieldOfViewHeight, aspectRatio, nearDistance, farDistance) -> GF_API void

fieldOfViewHeight : double
aspectRatio : double
nearDistance : double
farDistance : double


Sets up the frustum in a manner similar to C{gluPerspective()} .


It sets the projection type to C{GfFrustum::PERSPECTIVE} and sets the
window specification so that the resulting symmetric frustum encloses
an angle of C{fieldOfViewHeight} degrees in the vertical direction,
with C{aspectRatio} used to figure the angle in the horizontal
direction. The near and far distances are specified as well. The
window coordinates are computed as: ::

  top    = tan(fieldOfViewHeight / 2)
  bottom 
= -
top
  right  = top * aspectRatio
  left   
= -
right
  near   = nearDistance
  far    = farDistance



----------------------------------------------------------------------
SetPerspective(fieldOfView, isFovVertical, aspectRatio, nearDistance, farDistance) -> GF_API void

fieldOfView : double
isFovVertical : bool
aspectRatio : double
nearDistance : double
farDistance : double


Sets up the frustum in a manner similar to gluPerspective().


It sets the projection type to C{GfFrustum::Perspective} and sets the
window specification so that:

If *isFovVertical* is true, the resulting symmetric frustum encloses
an angle of C{fieldOfView} degrees in the vertical direction, with
C{aspectRatio} used to figure the angle in the horizontal direction.

If *isFovVertical* is false, the resulting symmetric frustum encloses
an angle of C{fieldOfView} degrees in the horizontal direction, with
C{aspectRatio} used to figure the angle in the vertical direction.

The near and far distances are specified as well. The window
coordinates are computed as follows:

   - if isFovVertical:

   - top = tan(fieldOfView / 2)

   - right = top * aspectRatio

   - if NOT isFovVertical:

   - right = tan(fieldOfView / 2)

   - top = right / aspectRation

   - bottom = -top

   - left = -right

   - near = nearDistance

   - far = farDistance


"""
   result["Frustum"].GetProjectionType.im_func.func_doc = """GetProjectionType() -> Frustum.ProjectionType



Returns the projection type.

"""
   result["Frustum"].SetOrthographic.im_func.func_doc = """SetOrthographic(left, right, bottom, top, nearPlane, farPlane) -> GF_API void

left : double
right : double
bottom : double
top : double
nearPlane : double
farPlane : double


Sets up the frustum in a manner similar to C{glOrtho()} .


Sets the projection to C{GfFrustum::Orthographic} and sets the window
and near/far specifications based on the given values.

"""
   result["Frustum"].ComputeUpVector.im_func.func_doc = """ComputeUpVector() -> GF_API GfVec3d



Returns the normalized world-space up vector, which is computed by
rotating the y axis by the frustum's rotation.

"""
   result["Frustum"].ProjectionType.__doc__ = """
This enum is used to determine the type of projection represented by a
frustum.

"""
   result["Frustum"].IntersectsViewVolume.func_doc = """**static** IntersectsViewVolume(bbox, vpMat) -> GF_API bool

bbox : BBox3d
vpMat : Matrix4d


Returns C{true} if the bbox volume intersects the view volume given by
the view-projection matrix, erring on the side of false positives for
efficiency.


This method is intended for cases where a GfFrustum is not available
or when the view-projection matrix yields a view volume that is not
expressable as a GfFrustum.

Because it errs on the side of false positives, it is suitable for
early-out tests such as draw or intersection culling.

"""
   result["Frustum"].SetNearFar.im_func.func_doc = """SetNearFar(nearFar)

nearFar : Range1d


Sets the near/far interval.

"""
   result["Frustum"].SetProjectionType.im_func.func_doc = """SetProjectionType(projectionType)

projectionType : Frustum.ProjectionType


Sets the projection type.

"""
   result["Frustum"].SetPositionAndRotationFromMatrix.im_func.func_doc = """SetPositionAndRotationFromMatrix(camToWorldXf) -> GF_API void

camToWorldXf : Matrix4d


Sets the position and rotation of the frustum from a camera matrix
(always from a y-Up camera).


The resulting frustum's transform will always represent a right-handed
and orthonormal coordinate sytem (scale, shear, and projection are
removed from the given C{camToWorldXf}).

"""
   result["Frustum"].GetViewDistance.im_func.func_doc = """GetViewDistance() -> double



Returns the view distance.

"""
   result["Frustum"].ComputeViewMatrix.im_func.func_doc = """ComputeViewMatrix() -> GF_API GfMatrix4d



Returns a matrix that represents the viewing transformation for this
frustum.


That is, it returns the matrix that converts points from world space
to eye (frustum) space.

"""
   result["Frustum"].GetOrthographic.im_func.func_doc = """GetOrthographic(left, right, bottom, top, nearPlane, farPlane) -> GF_API bool

left : double
right : double
bottom : double
top : double
nearPlane : double
farPlane : double


Returns the current frustum in the format used by C{SetOrthographic()}
.


If the current frustum is not an orthographic projection, this returns
C{false} and leaves the parameters untouched.

"""
   result["Frustum"].ComputeViewDirection.im_func.func_doc = """ComputeViewDirection() -> GF_API GfVec3d



Returns the normalized world-space view direction vector, which is
computed by rotating the -z axis by the frustum's rotation.

"""
   result["Frustum"].SetViewDistance.im_func.func_doc = """SetViewDistance(viewDistance)

viewDistance : double


Sets the view distance.

"""
   result["Frustum"].GetWindow.im_func.func_doc = """GetWindow() -> Range2d



Returns the window rectangle in the reference plane.

"""
   result["Frustum"].SetWindow.im_func.func_doc = """SetWindow(window)

window : Range2d


Sets the window rectangle in the reference plane that defines the
left, right, top, and bottom planes of the frustum.

"""
   result["Frustum"].GetRotation.im_func.func_doc = """GetRotation() -> Rotation



Returns the orientation of the frustum in world space as a rotation to
apply to the -z axis.

"""
   result["Frustum"].ComputeCornersAtDistance.im_func.func_doc = """ComputeCornersAtDistance(d) -> GF_API sequence< GfVec3d >

d : double


Returns the world-space corners of the intersection of the frustum
with a plane parallel to the near/far plane at distance d from the
apex, ordered as:



   - Left bottom

   - Right bottom

   - Left top

   - Right top In particular, it gives the partial result of
     ComputeCorners when given near or far distance.


"""
   result["Frustum"].ComputeNarrowedFrustum.im_func.func_doc = """ComputeNarrowedFrustum(point, halfSize) -> GF_API GfFrustum

point : Vec2d
halfSize : Vec2d


Returns a frustum that is a narrowed-down version of this frustum,
such that the frustum rectangle on the near plane encloses C{point}
with at most C{halfSize} [0] distance on the left and right and at
most C{halfSize} [1] distance on the top and bottom.


(If C{point} is closer than the half size to a side of the frustum,
that side is left alone. The point and sizes are in normalized 2D
coordinates; they range from (-1, -1) at the lower left corner of the
near-plane window rectangle to (1,1) at the upper right corner.

C{point} is a 2d point expressed as a normalized window position.

This method is useful for computing a volume to use for interactive
picking.


----------------------------------------------------------------------
ComputeNarrowedFrustum(worldPoint, halfSize) -> GF_API GfFrustum

worldPoint : Vec3d
halfSize : Vec2d


Returns a frustum that is a narrowed-down version of this frustum,
such that the frustum rectangle on the near plane encloses C{point}
with at most C{halfSize} [0] distance on the left and right and at
most C{halfSize} [1] distance on the top and bottom.


(If C{point} is closer than the half size to a side of the frustum,
that side is left alone. The point and sizes are in normalized 2D
coordinates; they range from (-1, -1) at the lower left corner of the
near-plane window rectangle to (1,1) at the upper right corner.

C{point} is a 3d point expressed in world coordinates

This method is useful for computing a volume to use for interactive
picking.

"""
   result["Frustum"].ComputeLookAtPoint.im_func.func_doc = """ComputeLookAtPoint() -> GF_API GfVec3d



Computes and returns the world-space look-at point from the eye point
(position), view direction (rotation), and view distance.

"""
   result["Frustum"].ComputeViewFrame.im_func.func_doc = """ComputeViewFrame(side, up, view) -> GF_API void

side : Vec3d
up : Vec3d
view : Vec3d


Computes the view frame defined by this frustum.


The frame consists of the view direction, up vector and side vector,
as shown in this diagram. ::

  up
  ^   ^
  |  / 
  | / view
  |/
   +- - - - > side


"""
   result["Frustum"].GetReferencePlaneDepth.func_doc = """**static** GetReferencePlaneDepth() -> double



Returns the depth of the reference plane.

"""
   result["Frustum"].SetRotation.im_func.func_doc = """SetRotation(rotation)

rotation : Rotation


Sets the orientation of the frustum in world space as a rotation to
apply to the default frame: looking along the -z axis with the +y axis
as "up".

"""
   result["Frustum"].ComputeCorners.im_func.func_doc = """ComputeCorners() -> GF_API sequence< GfVec3d >



Returns the world-space corners of the frustum as a vector of 8
points, ordered as:



   - Left bottom near

   - Right bottom near

   - Left top near

   - Right top near

   - Left bottom far

   - Right bottom far

   - Left top far

   - Right top far


"""
   result["Frustum"].Intersects.im_func.func_doc = """Intersects(bbox) -> GF_API bool

bbox : BBox3d


Returns true if the given axis-aligned bbox is inside or intersecting
the frustum.


Otherwise, it returns false. Useful when doing picking or frustum
culling.


----------------------------------------------------------------------
Intersects(point) -> GF_API bool

point : Vec3d


Returns true if the given point is inside or intersecting the frustum.


Otherwise, it returns false.


----------------------------------------------------------------------
Intersects(p0, p1) -> GF_API bool

p0 : Vec3d
p1 : Vec3d


Returns C{true} if the line segment formed by the given points is
inside or intersecting the frustum.


Otherwise, it returns false.


----------------------------------------------------------------------
Intersects(p0, p1, p2) -> GF_API bool

p0 : Vec3d
p1 : Vec3d
p2 : Vec3d


Returns C{true} if the triangle formed by the given points is inside
or intersecting the frustum.


Otherwise, it returns false.

"""
   result["Frustum"].ComputePickRay.im_func.func_doc = """ComputePickRay(windowPos) -> GF_API GfRay

windowPos : Vec2d


Builds and returns a C{GfRay} that can be used for picking at the
given normalized (-1 to +1 in both dimensions) window position.


Contrasted with ComputeRay() , that method returns a ray whose origin
is the eyepoint, while this method returns a ray whose origin is on
the near plane.


----------------------------------------------------------------------
ComputePickRay(worldSpacePos) -> GF_API GfRay

worldSpacePos : Vec3d


Builds and returns a C{GfRay} that can be used for picking that
connects the viewpoint to the given 3d point in worldspace.

"""
   result["Frustum"].ComputeViewInverse.im_func.func_doc = """ComputeViewInverse() -> GF_API GfMatrix4d



Returns a matrix that represents the inverse viewing transformation
for this frustum.


That is, it returns the matrix that converts points from eye (frustum)
space to world space.

"""
   result["Frustum"].ComputeProjectionMatrix.im_func.func_doc = """ComputeProjectionMatrix() -> GF_API GfMatrix4d



Returns a GL-style projection matrix corresponding to the frustum's
projection.

"""
   result["Frustum"].ComputeAspectRatio.im_func.func_doc = """ComputeAspectRatio() -> GF_API double



Returns the aspect ratio of the frustum, defined as the width of the
window divided by the height.


If the height is zero or negative, this returns 0.

"""
   result["Frustum"].FitToSphere.im_func.func_doc = """FitToSphere(center, radius, slack) -> GF_API void

center : Vec3d
radius : double
slack : double


Modifies the frustum to tightly enclose a sphere with the given center
and radius, using the current view direction.


The planes of the frustum are adjusted as necessary. The given amount
of slack is added to the sphere's radius is used around the sphere to
avoid boundary problems.

"""
   result["Frustum"].SetPosition.im_func.func_doc = """SetPosition(position)

position : Vec3d


Sets the position of the frustum in world space.

"""
   result["Frustum"].__init__.im_func.func_doc = """__init__() -> GF_API



This constructor creates an instance with default viewing parameters:



   - The position is the origin.

   - The rotation is the identity rotation. (The view is along the -z
     axis, with the +y axis as "up").

   - The window is -1 to +1 in both dimensions.

   - The near/far interval is (1, 10).

   - The view distance is 5.0.

   - The projection type is C{GfFrustum::Perspective}.



----------------------------------------------------------------------
__init__(position, rotation, window, nearFar, projectionType, viewDistance) -> GF_API

position : Vec3d
rotation : Rotation
window : Range2d
nearFar : Range1d
projectionType : Frustum.ProjectionType
viewDistance : double


This constructor creates an instance with the given viewing
parameters.


----------------------------------------------------------------------
__init__(camToWorldXf, window, nearFar, projectionType, viewDistance) -> GF_API

camToWorldXf : Matrix4d
window : Range2d
nearFar : Range1d
projectionType : Frustum.ProjectionType
viewDistance : double


This constructor creates an instance from a camera matrix (always of a
y-Up camera, also see SetPositionAndRotationFromMatrix) and the given
viewing parameters.

"""
   result["Frustum"].GetPosition.im_func.func_doc = """GetPosition() -> Vec3d



Returns the position of the frustum in world space.

"""
   result["Range1f"].__doc__ = """
Basic type: 1-dimensional floating point range.


This class represents a 1-dimensional range (or interval) All
operations are component-wise and conform to interval mathematics. An
empty range is one where max<min. The default empty is
[FLT_MAX,-FLT_MAX]

"""
   result["Range1f"].Contains.im_func.func_doc = """Contains(point) -> bool

point : float


Returns true if the C{point} is located inside the range.


As with all operations of this type, the range is assumed to include
its extrema.


----------------------------------------------------------------------
Contains(range) -> bool

range : Range1f


Returns true if the C{range} is located entirely inside the range.


As with all operations of this type, the ranges are assumed to include
their extrema.

"""
   result["Range1f"].IntersectWith.im_func.func_doc = """IntersectWith(b) -> Range1f

b : Range1f


Modifies this range to hold its intersection with C{b} and returns the
result.

"""
   result["Range1f"].SetMin.im_func.func_doc = """SetMin(min)

min : float


Sets the minimum value of the range.

"""
   result["Range1f"].GetSize.im_func.func_doc = """GetSize() -> float



Returns the size of the range.

"""
   result["Range1f"].SetEmpty.im_func.func_doc = """SetEmpty()



Sets the range to an empty interval.

"""
   result["Range1f"].GetMin.im_func.func_doc = """GetMin() -> float



Returns the minimum value of the range.

"""
   result["Range1f"].GetMax.im_func.func_doc = """GetMax() -> float



Returns the maximum value of the range.

"""
   result["Range1f"].UnionWith.im_func.func_doc = """UnionWith(b) -> Range1f

b : Range1f


Extend C{this} to include C{b}.


----------------------------------------------------------------------
UnionWith(b) -> Range1f

b : float


Extend C{this} to include C{b}.

"""
   result["Range1f"].SetMax.im_func.func_doc = """SetMax(max)

max : float


Sets the maximum value of the range.

"""
   result["Range1f"].IsEmpty.im_func.func_doc = """IsEmpty() -> bool



Returns whether the range is empty (max<min).

"""
   result["Range1f"].GetIntersection.func_doc = """**static** GetIntersection(a, b) -> Range1f

a : Range1f
b : Range1f


Returns a C{GfRange1f} that describes the intersection of C{a} and
C{b}.

"""
   result["Range1f"].GetMidpoint.im_func.func_doc = """GetMidpoint() -> float



Returns the midpoint of the range, that is, 0.5*(min+max).


Note: this returns zero in the case of default-constructed ranges, or
ranges set via SetEmpty() .

"""
   result["Range1f"].GetDistanceSquared.im_func.func_doc = """GetDistanceSquared(p) -> GF_API double

p : float


Compute the squared distance from a point to the range.

"""
   result["Range1f"].__init__.im_func.func_doc = """__init__()



The default constructor creates an empty range.


----------------------------------------------------------------------
__init__(min, max)

min : float
max : float


This constructor initializes the minimum and maximum points.

"""
   result["Range1f"].GetUnion.func_doc = """**static** GetUnion(a, b) -> Range1f

a : Range1f
b : Range1f


Returns the smallest C{GfRange1f} which contains both C{a} and C{b}.

"""
   result["Lerp"].func_doc = """Lerp(alpha, a, b) -> T

alpha : double
a : T
b : T


Linear interpolation function.


For any type that supports multiplication by a scalar and binary
addition, returns ::

  (1-alpha) * a + alpha * b 



----------------------------------------------------------------------
Lerp(alpha, a, b) -> T

alpha : double
a : T
b : T


Linear interpolation function.


For any type that supports multiplication by a scalar and binary
addition, returns ::

  (1-alpha) * a + alpha * b 


"""
   result["HomogeneousCross"].func_doc = """HomogeneousCross(a, b) -> GF_API GfVec4f

a : Vec4f
b : Vec4f


Homogenizes C{a} and C{b} and then performs the cross product on the
first three elements of each.


Returns the cross product as a homogenized vector.


----------------------------------------------------------------------
HomogeneousCross(a, b) -> GF_API GfVec4d

a : Vec4d
b : Vec4d


Homogenizes C{a} and C{b} and then performs the cross product on the
first three elements of each.


Returns the cross product as a homogenized vector.


----------------------------------------------------------------------
HomogeneousCross(a, b) -> GF_API GfVec4f

a : Vec4f
b : Vec4f


Homogenizes C{a} and C{b} and then performs the cross product on the
first three elements of each.


Returns the cross product as a homogenized vector.


----------------------------------------------------------------------
HomogeneousCross(a, b) -> GF_API GfVec4d

a : Vec4d
b : Vec4d


Homogenizes C{a} and C{b} and then performs the cross product on the
first three elements of each.


Returns the cross product as a homogenized vector.

"""
   result["Log"].func_doc = """Log(f) -> double

f : double


Return log( C{f}).


----------------------------------------------------------------------
Log(f) -> float

f : float


Return log( C{f}).


----------------------------------------------------------------------
Log(f) -> double

f : double


Return log( C{f}).


----------------------------------------------------------------------
Log(f) -> float

f : float


Return log( C{f}).

"""
   result["DegreesToRadians"].func_doc = """DegreesToRadians(degrees) -> double

degrees : double


Converts an angle in degrees to radians.


----------------------------------------------------------------------
DegreesToRadians(degrees) -> double

degrees : double


Converts an angle in degrees to radians.

"""
   result["CompDiv"].func_doc = """CompDiv(v1, v2) -> Vec2d

v1 : Vec2d
v2 : Vec2d


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec2f

v1 : Vec2f
v2 : Vec2f


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec2h

v1 : Vec2h
v2 : Vec2h


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec2i

v1 : Vec2i
v2 : Vec2i


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec3d

v1 : Vec3d
v2 : Vec3d


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec3f

v1 : Vec3f
v2 : Vec3f


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec3h

v1 : Vec3h
v2 : Vec3h


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec3i

v1 : Vec3i
v2 : Vec3i


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec4d

v1 : Vec4d
v2 : Vec4d


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec4f

v1 : Vec4f
v2 : Vec4f


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec4h

v1 : Vec4h
v2 : Vec4h


Returns component-wise quotient of vectors C{v1} and C{v2}.


----------------------------------------------------------------------
CompDiv(v1, v2) -> Vec4i

v1 : Vec4i
v2 : Vec4i


Returns component-wise quotient of vectors C{v1} and C{v2}.

"""
   result["Clamp"].func_doc = """Clamp(value, min, max) -> double

value : double
min : double
max : double


Return the resulting of clamping C{value} to lie between C{min} and
C{max}.


This function is also defined for GfVecs.


----------------------------------------------------------------------
Clamp(value, min, max) -> float

value : float
min : float
max : float


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
Clamp(value, min, max) -> double

value : double
min : double
max : double


Return the resulting of clamping C{value} to lie between C{min} and
C{max}.


This function is also defined for GfVecs.


----------------------------------------------------------------------
Clamp(value, min, max) -> float

value : float
min : float
max : float


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["__doc__"] = """

Overview
========

Contains foundation classes and functions for working with the basic
mathematical aspects of graphics.  The high-level grouping of the
classes and functions is as follows:

   - B{Linear} B{Algebra} - Includes classes representing basic types,
     including vectors of varying numbers and types (such as vectors of
     two, three, and four float components), two and three-dimensional
     arrays of sizes, and compound linear transformations.

   - B{Basic} B{Mathematical} B{Operations} - Includes classes and
     functions for performing operations such as converting between radians
     and degrees, calculating square roots, minimum and maximum values,
     absolute values, and so on.

   - B{Basic} B{Geometry} -  Includes classes that represent basic
     types such as one to three-dimensional floating point ranges, three-
     dimensional bounding boxes, planes, rays, frusta, and a camera model.

   - B{Output} B{For} B{Debugging} - Includes functions for quickly
     outputting Gf types (these are particularly useful for diagnostic
     purposes).


"""
   result["Rect2i"].__doc__ = """
A 2D rectangle with integer coordinates for windowing operations.


A rectangle is internally represented as an upper left corner and a
bottom right corner, but it is normally expressed as an upper left
corner and a size.

Note that the size (width and height) of a rectangle might be
different from what you are used to. If the top left corner and the
bottom right corner are the same, then the height and the width of the
rectangle will both be one.

Specifically, *width = right - left + 1* and *height = bottom - top +
1.* The design corresponds to rectangular spaces used by drawing
functions, where the width and height denote a number of pixels. For
example, drawing a rectangle with width and height one draws a single
pixel.

The default coordinate system has origin (0,0) in the top left corner,
the positive direction of the y axis is downward and the positive x
axis is to the right.

"""
   result["Rect2i"].Contains.im_func.func_doc = """Contains(p) -> bool

p : Vec2i


Returns true if the specified point in the rectangle.

"""
   result["Rect2i"].SetRight.im_func.func_doc = """SetRight(x)

x : int


Set the X value of the right edge.

"""
   result["Rect2i"].IsNull.im_func.func_doc = """IsNull() -> bool



Returns true if the rectangle is a null rectangle.


A null rectangle has both the width and the height set to 0, that is
::

  GetRight() == GetLeft() - 1

 and ::

  GetBottom() == GetTop() - 1

 Remember that if C{GetRight()} and C{GetLeft()} return the same value
then the rectangle has width 1, and similarly for the height.

A null rectangle is both empty, and not valid.

"""
   result["Rect2i"].Translate.im_func.func_doc = """Translate(displacement)

displacement : Vec2i


Move the rectangle by C{displ}.

"""
   result["Rect2i"].GetWidth.im_func.func_doc = """GetWidth() -> int



Returns the width of the rectangle.



If the left and right sides are coincident, the width is one.

"""
   result["Rect2i"].SetBottom.im_func.func_doc = """SetBottom(y)

y : int


Set the Y value of the bottom edge.

"""
   result["Rect2i"].__init__.im_func.func_doc = """__init__()



Constructs an empty rectangle.


----------------------------------------------------------------------
__init__(topLeft, bottomRight)

topLeft : Vec2i
bottomRight : Vec2i


Constructs a rectangle with C{topLeft} as the top left corner and
C{bottomRight} as the bottom right corner.


----------------------------------------------------------------------
__init__(topLeft, width, height)

topLeft : Vec2i
width : int
height : int


Constructs a rectangle with C{topLeft} as the top left corner and with
the indicated width and height.

"""
   result["Rect2i"].SetTop.im_func.func_doc = """SetTop(y)

y : int


Set the Y value of the top edge.

"""
   result["Rect2i"].GetSize.im_func.func_doc = """GetSize() -> Vec2i



Returns the size of the rectangle as a vector (width,height).

"""
   result["Rect2i"].GetArea.im_func.func_doc = """GetArea() -> unsigned long



Return the area of the rectangle.

"""
   result["Rect2i"].GetLower.im_func.func_doc = """GetLower() -> Vec2i



Returns the lower corner of the rectangle.

"""
   result["Rect2i"].SetHigher.im_func.func_doc = """SetHigher(higher)

higher : Vec2i


Sets the upper corner of the rectangle.

"""
   result["Rect2i"].GetHigher.im_func.func_doc = """GetHigher() -> Vec2i



Returns the upper corner of the rectangle.

"""
   result["Rect2i"].GetLeft.im_func.func_doc = """GetLeft() -> int



Return the X value of the left edge.

"""
   result["Rect2i"].GetIntersection.im_func.func_doc = """GetIntersection(that) -> Rect2i

that : Rect2i


Computes the intersection of two rectangles.

"""
   result["Rect2i"].GetHeight.im_func.func_doc = """GetHeight() -> int



Returns the height of the rectangle.



If the top and bottom sides are coincident, the height is one.

"""
   result["Rect2i"].IsEmpty.im_func.func_doc = """IsEmpty() -> bool



Returns true if the rectangle is empty.


An empty rectangle has its left side strictly greater than its right
side or its top strictly greater than its bottom.

An empty rectangle is not valid.

"""
   result["Rect2i"].GetNormalized.im_func.func_doc = """GetNormalized() -> GF_API GfRect2i



Returns a normalized rectangle, i.e.


one that has a non-negative width and height.

C{GetNormalized()} swaps left and right to ensure a non-negative
width, and similarly for top and bottom.

"""
   result["Rect2i"].GetTop.im_func.func_doc = """GetTop() -> int



Return the Y value of the top edge.

"""
   result["Rect2i"].GetBottom.im_func.func_doc = """GetBottom() -> int



Return the Y value of the bottom edge.

"""
   result["Rect2i"].IsValid.im_func.func_doc = """IsValid() -> bool



Return true if the rectangle is valid (equivalently, not empty).

"""
   result["Rect2i"].GetCenter.im_func.func_doc = """GetCenter() -> Vec2i



Returns the center point of the rectangle.

"""
   result["Rect2i"].SetLower.im_func.func_doc = """SetLower(lower)

lower : Vec2i


Sets the lower corner of the rectangle.

"""
   result["Rect2i"].GetUnion.im_func.func_doc = """GetUnion(that) -> Rect2i

that : Rect2i


Computes the union of two rectangles.

"""
   result["Rect2i"].SetLeft.im_func.func_doc = """SetLeft(x)

x : int


Set the X value of the left edge.

"""
   result["Rect2i"].GetRight.im_func.func_doc = """GetRight() -> int



Return the X value of the right edge.

"""
   result["Quatf"].__doc__ = """
Basic type: a quaternion, a complex number with a real coefficient and
three imaginary coefficients, stored as a 3-vector.

"""
   result["Quatf"].Normalize.im_func.func_doc = """Normalize(eps) -> GF_API float

eps : float


Normalizes this quaternion in place to unit length, returning the
length before normalization.


If the length of this quaternion is smaller than C{eps}, this sets the
quaternion to identity.

"""
   result["Quatf"].GetReal.im_func.func_doc = """GetReal() -> float



Return the real coefficient.

"""
   result["Quatf"].SetReal.im_func.func_doc = """SetReal(real)

real : float


Set the real coefficient.

"""
   result["Quatf"].GetLength.im_func.func_doc = """GetLength() -> float



Return geometric length of this quaternion.

"""
   result["Quatf"].__init__.im_func.func_doc = """__init__()



Default constructor leaves the quaternion undefined.


----------------------------------------------------------------------
__init__(realVal)

realVal : float


Initialize the real coefficient to C{realVal} and the imaginary
coefficients to zero.


Since quaternions typically must be normalized, reasonable values for
C{realVal} are -1, 0, or 1. Other values are legal but are likely to
be meaningless.


----------------------------------------------------------------------
__init__(real, i, j, k)

real : float
i : float
j : float
k : float


Initialize the real and imaginary coefficients.


----------------------------------------------------------------------
__init__(real, imaginary)

real : float
imaginary : Vec3f


Initialize the real and imaginary coefficients.


----------------------------------------------------------------------
__init__(other) -> GF_API

other : class GfQuatd


Construct from GfQuatd.


----------------------------------------------------------------------
__init__(other) -> GF_API

other : class GfQuath


Implicitly convert from GfQuath.

"""
   result["Quatf"].GetConjugate.im_func.func_doc = """GetConjugate() -> Quatf



Return this quaternion's conjugate, which is the quaternion with the
same real coefficient and negated imaginary coefficients.

"""
   result["Quatf"].GetIdentity.func_doc = """**static** GetIdentity() -> Quatf



Return the identity quaternion, with real coefficient 1 and an
imaginary coefficients all zero.

"""
   result["Quatf"].GetInverse.im_func.func_doc = """GetInverse() -> Quatf



Return this quaternion's inverse, or reciprocal.


This is the quaternion's conjugate divided by it's squared length.

"""
   result["Quatf"].GetImaginary.im_func.func_doc = """GetImaginary() -> Vec3f



Return the imaginary coefficient.

"""
   result["Quatf"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Quatf

eps : float


length of this quaternion is smaller than C{eps}, return the identity
quaternion.

"""
   result["Quatf"].SetImaginary.im_func.func_doc = """SetImaginary(imaginary)

imaginary : Vec3f


Set the imaginary coefficients.


----------------------------------------------------------------------
SetImaginary(i, j, k)

i : float
j : float
k : float


Set the imaginary coefficients.

"""
   result["Project"].func_doc = """Project(v) -> Vec3f

v : Vec4f


Projects homogeneous C{v} into Euclidean space and returns the result
as a Vec3f.


----------------------------------------------------------------------
Project(v) -> Vec3d

v : Vec4d


Projects homogeneous C{v} into Euclidean space and returns the result
as a Vec3d.

"""
   result["Abs"].func_doc = """Abs(f) -> double

f : double


Return abs( C{f}).


----------------------------------------------------------------------
Abs(f) -> float

f : float


Return abs( C{f}).


----------------------------------------------------------------------
Abs(f) -> double

f : double


Return abs( C{f}).


----------------------------------------------------------------------
Abs(f) -> float

f : float


Return abs( C{f}).

"""
   result["ConvertLinearToDisplay"].func_doc = """ConvertLinearToDisplay(v) -> GF_API GfVec3f

v : Vec3f


Given a vec, C{v}, representing an energy-linear RGB(A) color, return
a vec of the same type converted to the system's display gamma.


----------------------------------------------------------------------
ConvertLinearToDisplay(v) -> GF_API GfVec3d

v : Vec3d


----------------------------------------------------------------------
ConvertLinearToDisplay(v) -> GF_API GfVec3h

v : Vec3h


----------------------------------------------------------------------
ConvertLinearToDisplay(v) -> GF_API GfVec4f

v : Vec4f


----------------------------------------------------------------------
ConvertLinearToDisplay(v) -> GF_API GfVec4d

v : Vec4d


----------------------------------------------------------------------
ConvertLinearToDisplay(v) -> GF_API GfVec4h

v : Vec4h

"""
   result["Sgn"].func_doc = """Sgn(v) -> T

v : T


Return the signum of C{v} (i.e.


-1, 0, or 1).

The type C{T} must implement the<and>operators; the function returns
zero only if value neither positive, nor negative.


----------------------------------------------------------------------
Sgn(v) -> T

v : T


Return the signum of C{v} (i.e.


-1, 0, or 1).

The type C{T} must implement the<and>operators; the function returns
zero only if value neither positive, nor negative.

"""
   result["Vec3d"].__doc__ = """
Basic type for a vector of 3 double components.


Represents a vector of 3 components of type C{double}. It is intended
to be fast and simple.

"""
   result["Vec3d"].Normalize.im_func.func_doc = """Normalize(eps) -> double

eps : double


Normalizes the vector in place to unit length, returning the length
before normalization.


If the length of the vector is smaller than C{eps}, then the vector is
set to vector/ C{eps}. The original length of the vector is returned.
See also GfNormalize() .

"""
   result["Vec3d"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec3d


----------------------------------------------------------------------
__init__(value)

value : double


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1, s2)

s0 : double
s1 : double
s2 : double


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.


----------------------------------------------------------------------
__init__(other)

other : class GfVec3f


Implicitly convert from GfVec3f.


----------------------------------------------------------------------
__init__(other)

other : class GfVec3h


Implicitly convert from GfVec3h.


----------------------------------------------------------------------
__init__(other)

other : class GfVec3i


Implicitly convert from GfVec3i.

"""
   result["Vec3d"].YAxis.func_doc = """**static** YAxis() -> Vec3d



Create a unit vector along the Y-axis.

"""
   result["Vec3d"].OrthogonalizeBasis.func_doc = """**static** OrthogonalizeBasis(tx, ty, tz, normalize, eps) -> GF_API bool

tx : Vec3d
ty : Vec3d
tz : Vec3d
normalize : bool
eps : double


Orthogonalize and optionally normalize a set of basis vectors.


This uses an iterative method that is very stable even when the
vectors are far from orthogonal (close to colinear). The number of
iterations and thus the computation time does increase as the vectors
become close to colinear, however. Returns a bool specifying whether
the solution converged after a number of iterations. If it did not
converge, the returned vectors will be as close as possible to
orthogonal within the iteration limit. Colinear vectors will be
unaltered, and the method will return false.

"""
   result["Vec3d"].BuildOrthonormalFrame.im_func.func_doc = """BuildOrthonormalFrame(v1, v2, eps) -> GF_API void

v1 : Vec3d
v2 : Vec3d
eps : double


Sets C{v1} and C{v2} to unit vectors such that v1, v2 and *this are
mutually orthogonal.


If the length L of *this is smaller than C{eps}, then v1 and v2 will
have magnitude L/eps. As a result, the function delivers a continuous
result as *this shrinks in length.

"""
   result["Vec3d"].GetLength.im_func.func_doc = """GetLength() -> double



Length.

"""
   result["Vec3d"].ZAxis.func_doc = """**static** ZAxis() -> Vec3d



Create a unit vector along the Z-axis.

"""
   result["Vec3d"].GetComplement.im_func.func_doc = """GetComplement(b) -> Vec3d

b : Vec3d


Returns the orthogonal complement of C{this->GetProjection(b)} .


That is: ::

  *this - this->GetProjection(b)


"""
   result["Vec3d"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Vec3d

eps : double

"""
   result["Vec3d"].GetProjection.im_func.func_doc = """GetProjection(v) -> Vec3d

v : Vec3d


Returns the projection of C{this} onto C{v}.


That is: ::

  v * (*this * v)


"""
   result["Vec3d"].XAxis.func_doc = """**static** XAxis() -> Vec3d



Create a unit vector along the X-axis.

"""
   result["Vec3d"].Axis.func_doc = """**static** Axis(i) -> Vec3d

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 3.

"""
   result["Matrix4f"].__doc__ = """
Stores a 4x4 matrix of C{float} elements.


A basic type.

Matrices are defined to be in row-major order, so C{matrix[i][j]}
indexes the element in the *i* th row and the *j* th column.

3D Transformations
==================

The following methods interpret a GfMatrix4f as a 3D transformation:
SetRotate() , SetScale() , SetTranslate() , SetLookAt() , Factor() ,
ExtractTranslation() , ExtractRotation() , Transform() ,
TransformDir() . By convention, vectors are treated primarily as row
vectors, implying the following:
   - Transformation matrices are organized to deal with row vectors,
     not column vectors. For example, the last row of a matrix contains the
     translation amounts.

   - Each of the Set() methods below completely rewrites the matrix;
     for example, SetTranslate() yields a matrix which does nothing but
     translate.

   - When multiplying two transformation matrices, the matrix on the
     left applies a more local transformation to a row vector. For example,
     if R represents a rotation matrix and T represents a translation
     matrix, the product R*T will rotate a row vector, then translate it.


"""
   result["Matrix4f"].GetRow3.im_func.func_doc = """GetRow3(i) -> Vec3f

i : int


Gets a row of the matrix as a Vec3.

"""
   result["Matrix4f"].IsLeftHanded.im_func.func_doc = """IsLeftHanded() -> bool



Returns true if the vectors in the upper 3x3 matrix form a left-handed
coordinate system.

"""
   result["Matrix4f"].Transform.im_func.func_doc = """Transform(vec) -> Vec3d

vec : Vec3d


Transforms the row vector *vec* by the matrix, returning the result.


This treats the vector as a 4-component vector whose fourth component
is 1.


----------------------------------------------------------------------
Transform(vec) -> Vec3f

vec : Vec3f


Transforms the row vector *vec* by the matrix, returning the result.


This treats the vector as a 4-component vector whose fourth component
is 1. This is an overloaded method; it differs from the other version
in that it returns a different value type.

"""
   result["Matrix4f"].SetZero.im_func.func_doc = """SetZero() -> Matrix4f



Sets the matrix to zero.

"""
   result["Matrix4f"].GetDeterminant3.im_func.func_doc = """GetDeterminant3() -> double



Returns the determinant of the upper 3x3 matrix.


This method is useful when the matrix describes a linear
transformation such as a rotation or scale because the other values in
the 4x4 matrix are not important.

"""
   result["Matrix4f"].ExtractRotation.im_func.func_doc = """ExtractRotation() -> GF_API GfRotation



Returns the rotation corresponding to this matrix.


This works well only if the matrix represents a rotation.

For good results, consider calling Orthonormalize() before calling
this method.

"""
   result["Matrix4f"].Factor.im_func.func_doc = """Factor(r, s, u, t, p, eps) -> GF_API bool

r : Matrix4f
s : Vec3f
u : Matrix4f
t : Vec3f
p : Matrix4f
eps : float


Factors the matrix into 5 components:



   - C{*M* = r * s * -r * u * t} where

   - *t* is a translation.

   - *u* and *r* are rotations, and *-r* is the transpose (inverse) of
     *r*. The *u* matrix may contain shear information.

   - *s* is a scale. Any projection information could be returned in
     matrix *p*, but currently p is never modified.
     Returns C{false} if the matrix is singular (as determined by *eps*).
     In that case, any zero scales in *s* are clamped to *eps* to allow
     computation of *u*.

"""
   result["Matrix4f"].GetHandedness.im_func.func_doc = """GetHandedness() -> GF_API double



Returns the sign of the determinant of the upper 3x3 matrix, i.e.


1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
singular matrix.

"""
   result["Matrix4f"].SetRow.im_func.func_doc = """SetRow(i, v)

i : int
v : Vec4f


Sets a row of the matrix from a Vec4.

"""
   result["Matrix4f"].SetLookAt.im_func.func_doc = """SetLookAt(eyePoint, centerPoint, upDirection) -> GF_API GfMatrix4f

eyePoint : Vec3f
centerPoint : Vec3f
upDirection : Vec3f


Sets the matrix to specify a viewing matrix from parameters similar to
those used by C{gluLookAt(3G)} .


*eyePoint* represents the eye point in world space. *centerPoint*
represents the world-space center of attention. *upDirection* is a
vector indicating which way is up.


----------------------------------------------------------------------
SetLookAt(eyePoint, orientation) -> GF_API GfMatrix4f

eyePoint : Vec3f
orientation : Rotation


Sets the matrix to specify a viewing matrix from a world-space
*eyePoint* and a world-space rotation that rigidly rotates the
orientation from its canonical frame, which is defined to be looking
along the C{-z} axis with the C{+y} axis as the up direction.

"""
   result["Matrix4f"].Orthonormalize.im_func.func_doc = """Orthonormalize(issueWarning) -> GF_API bool

issueWarning : bool


Makes the matrix orthonormal in place.


This is an iterative method that is much more stable than the previous
cross/cross method. If the iterative method does not converge, a
warning is issued.

Returns true if the iteration converged, false otherwise. Leaves any
translation part of the matrix unchanged. If *issueWarning* is true,
this method will issue a warning if the iteration does not converge,
otherwise it will be silent.

"""
   result["Matrix4f"].TransformAffine.im_func.func_doc = """TransformAffine(vec) -> Vec3d

vec : Vec3d


Transforms the row vector *vec* by the matrix, returning the result.


This treats the vector as a 4-component vector whose fourth component
is 1 and ignores the fourth column of the matrix (i.e. assumes it is
(0, 0, 0, 1)).


----------------------------------------------------------------------
TransformAffine(vec) -> Vec3f

vec : Vec3f


Transforms the row vector *vec* by the matrix, returning the result.


This treats the vector as a 4-component vector whose fourth component
is 1 and ignores the fourth column of the matrix (i.e. assumes it is
(0, 0, 0, 1)).

"""
   result["Matrix4f"].GetColumn.im_func.func_doc = """GetColumn(i) -> Vec4f

i : int


Gets a column of the matrix as a Vec4.

"""
   result["Matrix4f"].SetRotateOnly.im_func.func_doc = """SetRotateOnly(rot) -> GF_API GfMatrix4f

rot : Quatf


Sets the matrix to specify a rotation equivalent to *rot*, without
clearing the translation.


----------------------------------------------------------------------
SetRotateOnly(rot) -> GF_API GfMatrix4f

rot : Rotation


Sets the matrix to specify a rotation equivalent to *rot*, without
clearing the translation.


----------------------------------------------------------------------
SetRotateOnly(mx) -> GF_API GfMatrix4f

mx : Matrix3f


Sets the matrix to specify a rotation equivalent to *mx*, without
clearing the translation.

"""
   result["Matrix4f"].SetTransform.im_func.func_doc = """SetTransform(rotate, translate) -> GF_API GfMatrix4f

rotate : Rotation
translate : Vec3f


Sets matrix to specify a rotation by *rotate* and a translation by
*translate*.


----------------------------------------------------------------------
SetTransform(rotmx, translate) -> GF_API GfMatrix4f

rotmx : Matrix3f
translate : Vec3f


Sets matrix to specify a rotation by *rotmx* and a translation by
*translate*.

"""
   result["Matrix4f"].HasOrthogonalRows3.im_func.func_doc = """HasOrthogonalRows3() -> bool



Returns true, if the row vectors of the upper 3x3 matrix form an
orthogonal basis.


Note they do not have to be unit length for this test to return true.

"""
   result["Matrix4f"].GetDeterminant.im_func.func_doc = """GetDeterminant() -> GF_API double



Returns the determinant of the matrix.

"""
   result["Matrix4f"].TransformDir.im_func.func_doc = """TransformDir(vec) -> Vec3d

vec : Vec3d


Transforms row vector *vec* by the matrix, returning the result.


This treats the vector as a direction vector, so the translation
information in the matrix is ignored. That is, it treats the vector as
a 4-component vector whose fourth component is 0.


----------------------------------------------------------------------
TransformDir(vec) -> Vec3f

vec : Vec3f


Transforms row vector *vec* by the matrix, returning the result.


This treats the vector as a direction vector, so the translation
information in the matrix is ignored. That is, it treats the vector as
a 4-component vector whose fourth component is 0. This is an
overloaded method; it differs from the other version in that it
returns a different value type.

"""
   result["Matrix4f"].SetScale.im_func.func_doc = """SetScale(scaleFactors) -> GF_API GfMatrix4f

scaleFactors : Vec3f


Sets the matrix to specify a nonuniform scaling in x, y, and z by the
factors in vector *scaleFactors*.


----------------------------------------------------------------------
SetScale(scaleFactor) -> GF_API GfMatrix4f

scaleFactor : float


Sets matrix to specify a uniform scaling by *scaleFactor*.

"""
   result["Matrix4f"].SetTranslate.im_func.func_doc = """SetTranslate(trans) -> GF_API GfMatrix4f

trans : Vec3f


Sets matrix to specify a translation by the vector *trans*, and clears
the rotation.

"""
   result["Matrix4f"].__init__.im_func.func_doc = """__init__()



Default constructor. Leaves the matrix component values undefined.


----------------------------------------------------------------------
__init__(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33)

m00 : float
m01 : float
m02 : float
m03 : float
m10 : float
m11 : float
m12 : float
m13 : float
m20 : float
m21 : float
m22 : float
m23 : float
m30 : float
m31 : float
m32 : float
m33 : float


Constructor.


Initializes the matrix from 16 independent C{float} values, specified
in row-major order. For example, parameter *m10* specifies the value
in row 1 and column 0.


----------------------------------------------------------------------
__init__(m)

m : float


Constructor.


Initializes the matrix from a 4x4 array of C{float} values, specified
in row-major order.


----------------------------------------------------------------------
__init__(s)

s : float


Constructor.


Explicitly initializes the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
__init__(v)

v : Vec4f


Constructor.


Explicitly initializes the matrix to diagonal form, with the *i* th
element on the diagonal set to C{v[i]} .


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<double>>


Constructor.


Initialize the matrix from a vector of vectors of double. The vector
is expected to be 4x4. If it is too big, only the first 4 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<float>>


Constructor.


Initialize the matrix from a vector of vectors of float. The vector is
expected to be 4x4. If it is too big, only the first 4 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(r0, r1, r2, r3) -> GF_API

r0 : sequence<double>
r1 : sequence<double>
r2 : sequence<double>
r3 : sequence<double>


Constructor.


Initialize the matrix from 4 row vectors of double. Each vector is
expected to length 4. If it is too big, only the first 4 items will be
used. If it is too small, uninitialized elements will be filled in
with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(r0, r1, r2, r3) -> GF_API

r0 : sequence<float>
r1 : sequence<float>
r2 : sequence<float>
r3 : sequence<float>


Constructor.


Initialize the matrix from 4 row vectors of float. Each vector is
expected to length 4. If it is too big, only the first 4 items will be
used. If it is too small, uninitialized elements will be filled in
with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(rotate, translate) -> GF_API

rotate : Rotation
translate : Vec3f


Constructor.


Initializes a transformation matrix to perform the indicated rotation
and translation.


----------------------------------------------------------------------
__init__(rotmx, translate) -> GF_API

rotmx : Matrix3f
translate : Vec3f


Constructor.


Initializes a transformation matrix to perform the indicated rotation
and translation.


----------------------------------------------------------------------
__init__(m) -> GF_API

m : class GfMatrix4d


This explicit constructor converts a "double" matrix to a "float"
matrix.

"""
   result["Matrix4f"].GetRow.im_func.func_doc = """GetRow(i) -> Vec4f

i : int


Gets a row of the matrix as a Vec4.

"""
   result["Matrix4f"].GetTranspose.im_func.func_doc = """GetTranspose() -> GF_API GfMatrix4f



Returns the transpose of the matrix.

"""
   result["Matrix4f"].ExtractTranslation.im_func.func_doc = """ExtractTranslation() -> Vec3f



Returns the translation part of the matrix, defined as the first three
elements of the last row.

"""
   result["Matrix4f"].SetDiagonal.im_func.func_doc = """SetDiagonal(s) -> GF_API GfMatrix4f

s : float


Sets the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
SetDiagonal(arg1) -> GF_API GfMatrix4f

arg1 : Vec4f


Sets the matrix to have diagonal ( C{v[0], v[1], v[2], v[3]} ).

"""
   result["Matrix4f"].GetInverse.im_func.func_doc = """GetInverse(det, eps) -> GF_API GfMatrix4f

det : double
eps : double


Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
matrix is singular.


(FLT_MAX is the largest value a C{float} can have, as defined by the
system.) The matrix is considered singular if the determinant is less
than or equal to the optional parameter *eps*. If *det* is non-null,
C{*det} is set to the determinant.

"""
   result["Matrix4f"].SetIdentity.im_func.func_doc = """SetIdentity() -> Matrix4f



Sets the matrix to the identity matrix.

"""
   result["Matrix4f"].SetTranslateOnly.im_func.func_doc = """SetTranslateOnly(t) -> GF_API GfMatrix4f

t : Vec3f


Sets matrix to specify a translation by the vector *trans*, without
clearing the rotation.

"""
   result["Matrix4f"].Set.im_func.func_doc = """Set(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33) -> Matrix4f

m00 : float
m01 : float
m02 : float
m03 : float
m10 : float
m11 : float
m12 : float
m13 : float
m20 : float
m21 : float
m22 : float
m23 : float
m30 : float
m31 : float
m32 : float
m33 : float


Sets the matrix from 16 independent C{float} values, specified in row-
major order.


For example, parameter *m10* specifies the value in row 1 and column
0.


----------------------------------------------------------------------
Set(m) -> Matrix4f

m : float


Sets the matrix from a 4x4 array of C{float} values, specified in row-
major order.

"""
   result["Matrix4f"].ExtractRotationMatrix.im_func.func_doc = """ExtractRotationMatrix() -> GF_API GfMatrix3f



Returns the rotation corresponding to this matrix.


This works well only if the matrix represents a rotation.

For good results, consider calling Orthonormalize() before calling
this method.

"""
   result["Matrix4f"].SetRow3.im_func.func_doc = """SetRow3(i, v)

i : int
v : Vec3f


Sets a row of the matrix from a Vec3.


The fourth element of the row is ignored.

"""
   result["Matrix4f"].SetColumn.im_func.func_doc = """SetColumn(i, v)

i : int
v : Vec4f


Sets a column of the matrix from a Vec4.

"""
   result["Matrix4f"].SetRotate.im_func.func_doc = """SetRotate(rot) -> GF_API GfMatrix4f

rot : Quatf


Sets the matrix to specify a rotation equivalent to *rot*, and clears
the translation.


----------------------------------------------------------------------
SetRotate(rot) -> GF_API GfMatrix4f

rot : Rotation


Sets the matrix to specify a rotation equivalent to *rot*, and clears
the translation.


----------------------------------------------------------------------
SetRotate(mx) -> GF_API GfMatrix4f

mx : Matrix3f


Sets the matrix to specify a rotation equivalent to *mx*, and clears
the translation.

"""
   result["Matrix4f"].RemoveScaleShear.im_func.func_doc = """RemoveScaleShear() -> GF_API GfMatrix4f



Returns the matrix with any scaling or shearing removed, leaving only
the rotation and translation.


If the matrix cannot be decomposed, returns the original matrix.

"""
   result["Matrix4f"].GetOrthonormalized.im_func.func_doc = """GetOrthonormalized(issueWarning) -> GF_API GfMatrix4f

issueWarning : bool


Returns an orthonormalized copy of the matrix.

"""
   result["Matrix4f"].IsRightHanded.im_func.func_doc = """IsRightHanded() -> bool



Returns true if the vectors in the upper 3x3 matrix form a right-
handed coordinate system.

"""
   result["Matrix4d"].__doc__ = """
Stores a 4x4 matrix of C{double} elements.


A basic type.

Matrices are defined to be in row-major order, so C{matrix[i][j]}
indexes the element in the *i* th row and the *j* th column.

3D Transformations
==================

The following methods interpret a GfMatrix4d as a 3D transformation:
SetRotate() , SetScale() , SetTranslate() , SetLookAt() , Factor() ,
ExtractTranslation() , ExtractRotation() , Transform() ,
TransformDir() . By convention, vectors are treated primarily as row
vectors, implying the following:
   - Transformation matrices are organized to deal with row vectors,
     not column vectors. For example, the last row of a matrix contains the
     translation amounts.

   - Each of the Set() methods below completely rewrites the matrix;
     for example, SetTranslate() yields a matrix which does nothing but
     translate.

   - When multiplying two transformation matrices, the matrix on the
     left applies a more local transformation to a row vector. For example,
     if R represents a rotation matrix and T represents a translation
     matrix, the product R*T will rotate a row vector, then translate it.


"""
   result["Matrix4d"].GetRow3.im_func.func_doc = """GetRow3(i) -> Vec3d

i : int


Gets a row of the matrix as a Vec3.

"""
   result["Matrix4d"].IsLeftHanded.im_func.func_doc = """IsLeftHanded() -> bool



Returns true if the vectors in the upper 3x3 matrix form a left-handed
coordinate system.

"""
   result["Matrix4d"].Transform.im_func.func_doc = """Transform(vec) -> Vec3d

vec : Vec3d


Transforms the row vector *vec* by the matrix, returning the result.


This treats the vector as a 4-component vector whose fourth component
is 1.


----------------------------------------------------------------------
Transform(vec) -> Vec3f

vec : Vec3f


Transforms the row vector *vec* by the matrix, returning the result.


This treats the vector as a 4-component vector whose fourth component
is 1. This is an overloaded method; it differs from the other version
in that it returns a different value type.

"""
   result["Matrix4d"].SetZero.im_func.func_doc = """SetZero() -> Matrix4d



Sets the matrix to zero.

"""
   result["Matrix4d"].GetDeterminant3.im_func.func_doc = """GetDeterminant3() -> double



Returns the determinant of the upper 3x3 matrix.


This method is useful when the matrix describes a linear
transformation such as a rotation or scale because the other values in
the 4x4 matrix are not important.

"""
   result["Matrix4d"].ExtractRotation.im_func.func_doc = """ExtractRotation() -> GF_API GfRotation



Returns the rotation corresponding to this matrix.


This works well only if the matrix represents a rotation.

For good results, consider calling Orthonormalize() before calling
this method.

"""
   result["Matrix4d"].Factor.im_func.func_doc = """Factor(r, s, u, t, p, eps) -> GF_API bool

r : Matrix4d
s : Vec3d
u : Matrix4d
t : Vec3d
p : Matrix4d
eps : double


Factors the matrix into 5 components:



   - C{*M* = r * s * -r * u * t} where

   - *t* is a translation.

   - *u* and *r* are rotations, and *-r* is the transpose (inverse) of
     *r*. The *u* matrix may contain shear information.

   - *s* is a scale. Any projection information could be returned in
     matrix *p*, but currently p is never modified.
     Returns C{false} if the matrix is singular (as determined by *eps*).
     In that case, any zero scales in *s* are clamped to *eps* to allow
     computation of *u*.

"""
   result["Matrix4d"].GetHandedness.im_func.func_doc = """GetHandedness() -> GF_API double



Returns the sign of the determinant of the upper 3x3 matrix, i.e.


1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
singular matrix.

"""
   result["Matrix4d"].SetRow.im_func.func_doc = """SetRow(i, v)

i : int
v : Vec4d


Sets a row of the matrix from a Vec4.

"""
   result["Matrix4d"].SetLookAt.im_func.func_doc = """SetLookAt(eyePoint, centerPoint, upDirection) -> GF_API GfMatrix4d

eyePoint : Vec3d
centerPoint : Vec3d
upDirection : Vec3d


Sets the matrix to specify a viewing matrix from parameters similar to
those used by C{gluLookAt(3G)} .


*eyePoint* represents the eye point in world space. *centerPoint*
represents the world-space center of attention. *upDirection* is a
vector indicating which way is up.


----------------------------------------------------------------------
SetLookAt(eyePoint, orientation) -> GF_API GfMatrix4d

eyePoint : Vec3d
orientation : Rotation


Sets the matrix to specify a viewing matrix from a world-space
*eyePoint* and a world-space rotation that rigidly rotates the
orientation from its canonical frame, which is defined to be looking
along the C{-z} axis with the C{+y} axis as the up direction.

"""
   result["Matrix4d"].Orthonormalize.im_func.func_doc = """Orthonormalize(issueWarning) -> GF_API bool

issueWarning : bool


Makes the matrix orthonormal in place.


This is an iterative method that is much more stable than the previous
cross/cross method. If the iterative method does not converge, a
warning is issued.

Returns true if the iteration converged, false otherwise. Leaves any
translation part of the matrix unchanged. If *issueWarning* is true,
this method will issue a warning if the iteration does not converge,
otherwise it will be silent.

"""
   result["Matrix4d"].TransformAffine.im_func.func_doc = """TransformAffine(vec) -> Vec3d

vec : Vec3d


Transforms the row vector *vec* by the matrix, returning the result.


This treats the vector as a 4-component vector whose fourth component
is 1 and ignores the fourth column of the matrix (i.e. assumes it is
(0, 0, 0, 1)).


----------------------------------------------------------------------
TransformAffine(vec) -> Vec3f

vec : Vec3f


Transforms the row vector *vec* by the matrix, returning the result.


This treats the vector as a 4-component vector whose fourth component
is 1 and ignores the fourth column of the matrix (i.e. assumes it is
(0, 0, 0, 1)).

"""
   result["Matrix4d"].GetColumn.im_func.func_doc = """GetColumn(i) -> Vec4d

i : int


Gets a column of the matrix as a Vec4.

"""
   result["Matrix4d"].SetRotateOnly.im_func.func_doc = """SetRotateOnly(rot) -> GF_API GfMatrix4d

rot : Quatd


Sets the matrix to specify a rotation equivalent to *rot*, without
clearing the translation.


----------------------------------------------------------------------
SetRotateOnly(rot) -> GF_API GfMatrix4d

rot : Rotation


Sets the matrix to specify a rotation equivalent to *rot*, without
clearing the translation.


----------------------------------------------------------------------
SetRotateOnly(mx) -> GF_API GfMatrix4d

mx : Matrix3d


Sets the matrix to specify a rotation equivalent to *mx*, without
clearing the translation.

"""
   result["Matrix4d"].SetTransform.im_func.func_doc = """SetTransform(rotate, translate) -> GF_API GfMatrix4d

rotate : Rotation
translate : Vec3d


Sets matrix to specify a rotation by *rotate* and a translation by
*translate*.


----------------------------------------------------------------------
SetTransform(rotmx, translate) -> GF_API GfMatrix4d

rotmx : Matrix3d
translate : Vec3d


Sets matrix to specify a rotation by *rotmx* and a translation by
*translate*.

"""
   result["Matrix4d"].HasOrthogonalRows3.im_func.func_doc = """HasOrthogonalRows3() -> bool



Returns true, if the row vectors of the upper 3x3 matrix form an
orthogonal basis.


Note they do not have to be unit length for this test to return true.

"""
   result["Matrix4d"].GetDeterminant.im_func.func_doc = """GetDeterminant() -> GF_API double



Returns the determinant of the matrix.

"""
   result["Matrix4d"].TransformDir.im_func.func_doc = """TransformDir(vec) -> Vec3d

vec : Vec3d


Transforms row vector *vec* by the matrix, returning the result.


This treats the vector as a direction vector, so the translation
information in the matrix is ignored. That is, it treats the vector as
a 4-component vector whose fourth component is 0.


----------------------------------------------------------------------
TransformDir(vec) -> Vec3f

vec : Vec3f


Transforms row vector *vec* by the matrix, returning the result.


This treats the vector as a direction vector, so the translation
information in the matrix is ignored. That is, it treats the vector as
a 4-component vector whose fourth component is 0. This is an
overloaded method; it differs from the other version in that it
returns a different value type.

"""
   result["Matrix4d"].SetScale.im_func.func_doc = """SetScale(scaleFactors) -> GF_API GfMatrix4d

scaleFactors : Vec3d


Sets the matrix to specify a nonuniform scaling in x, y, and z by the
factors in vector *scaleFactors*.


----------------------------------------------------------------------
SetScale(scaleFactor) -> GF_API GfMatrix4d

scaleFactor : double


Sets matrix to specify a uniform scaling by *scaleFactor*.

"""
   result["Matrix4d"].SetTranslate.im_func.func_doc = """SetTranslate(trans) -> GF_API GfMatrix4d

trans : Vec3d


Sets matrix to specify a translation by the vector *trans*, and clears
the rotation.

"""
   result["Matrix4d"].SetRow3.im_func.func_doc = """SetRow3(i, v)

i : int
v : Vec3d


Sets a row of the matrix from a Vec3.


The fourth element of the row is ignored.

"""
   result["Matrix4d"].GetRow.im_func.func_doc = """GetRow(i) -> Vec4d

i : int


Gets a row of the matrix as a Vec4.

"""
   result["Matrix4d"].GetTranspose.im_func.func_doc = """GetTranspose() -> GF_API GfMatrix4d



Returns the transpose of the matrix.

"""
   result["Matrix4d"].ExtractTranslation.im_func.func_doc = """ExtractTranslation() -> Vec3d



Returns the translation part of the matrix, defined as the first three
elements of the last row.

"""
   result["Matrix4d"].SetDiagonal.im_func.func_doc = """SetDiagonal(s) -> GF_API GfMatrix4d

s : double


Sets the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
SetDiagonal(arg1) -> GF_API GfMatrix4d

arg1 : Vec4d


Sets the matrix to have diagonal ( C{v[0], v[1], v[2], v[3]} ).

"""
   result["Matrix4d"].GetInverse.im_func.func_doc = """GetInverse(det, eps) -> GF_API GfMatrix4d

det : double
eps : double


Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
matrix is singular.


(FLT_MAX is the largest value a C{float} can have, as defined by the
system.) The matrix is considered singular if the determinant is less
than or equal to the optional parameter *eps*. If *det* is non-null,
C{*det} is set to the determinant.

"""
   result["Matrix4d"].SetIdentity.im_func.func_doc = """SetIdentity() -> Matrix4d



Sets the matrix to the identity matrix.

"""
   result["Matrix4d"].SetTranslateOnly.im_func.func_doc = """SetTranslateOnly(t) -> GF_API GfMatrix4d

t : Vec3d


Sets matrix to specify a translation by the vector *trans*, without
clearing the rotation.

"""
   result["Matrix4d"].__init__.im_func.func_doc = """__init__()



Default constructor. Leaves the matrix component values undefined.


----------------------------------------------------------------------
__init__(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33)

m00 : double
m01 : double
m02 : double
m03 : double
m10 : double
m11 : double
m12 : double
m13 : double
m20 : double
m21 : double
m22 : double
m23 : double
m30 : double
m31 : double
m32 : double
m33 : double


Constructor.


Initializes the matrix from 16 independent C{double} values, specified
in row-major order. For example, parameter *m10* specifies the value
in row 1 and column 0.


----------------------------------------------------------------------
__init__(m)

m : double


Constructor.


Initializes the matrix from a 4x4 array of C{double} values, specified
in row-major order.


----------------------------------------------------------------------
__init__(s)

s : double


Constructor.


Explicitly initializes the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
__init__(v)

v : Vec4d


Constructor.


Explicitly initializes the matrix to diagonal form, with the *i* th
element on the diagonal set to C{v[i]} .


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<double>>


Constructor.


Initialize the matrix from a vector of vectors of double. The vector
is expected to be 4x4. If it is too big, only the first 4 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<float>>


Constructor.


Initialize the matrix from a vector of vectors of float. The vector is
expected to be 4x4. If it is too big, only the first 4 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(r0, r1, r2, r3) -> GF_API

r0 : sequence<double>
r1 : sequence<double>
r2 : sequence<double>
r3 : sequence<double>


Constructor.


Initialize the matrix from 4 row vectors of double. Each vector is
expected to length 4. If it is too big, only the first 4 items will be
used. If it is too small, uninitialized elements will be filled in
with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(r0, r1, r2, r3) -> GF_API

r0 : sequence<float>
r1 : sequence<float>
r2 : sequence<float>
r3 : sequence<float>


Constructor.


Initialize the matrix from 4 row vectors of float. Each vector is
expected to length 4. If it is too big, only the first 4 items will be
used. If it is too small, uninitialized elements will be filled in
with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(rotate, translate) -> GF_API

rotate : Rotation
translate : Vec3d


Constructor.


Initializes a transformation matrix to perform the indicated rotation
and translation.


----------------------------------------------------------------------
__init__(rotmx, translate) -> GF_API

rotmx : Matrix3d
translate : Vec3d


Constructor.


Initializes a transformation matrix to perform the indicated rotation
and translation.


----------------------------------------------------------------------
__init__(m) -> GF_API

m : class GfMatrix4f


This explicit constructor converts a "float" matrix to a "double"
matrix.

"""
   result["Matrix4d"].Set.im_func.func_doc = """Set(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33) -> Matrix4d

m00 : double
m01 : double
m02 : double
m03 : double
m10 : double
m11 : double
m12 : double
m13 : double
m20 : double
m21 : double
m22 : double
m23 : double
m30 : double
m31 : double
m32 : double
m33 : double


Sets the matrix from 16 independent C{double} values, specified in
row-major order.


For example, parameter *m10* specifies the value in row 1 and column
0.


----------------------------------------------------------------------
Set(m) -> Matrix4d

m : double


Sets the matrix from a 4x4 array of C{double} values, specified in
row-major order.

"""
   result["Matrix4d"].ExtractRotationMatrix.im_func.func_doc = """ExtractRotationMatrix() -> GF_API GfMatrix3d



Returns the rotation corresponding to this matrix.


This works well only if the matrix represents a rotation.

For good results, consider calling Orthonormalize() before calling
this method.

"""
   result["Matrix4d"].SetColumn.im_func.func_doc = """SetColumn(i, v)

i : int
v : Vec4d


Sets a column of the matrix from a Vec4.

"""
   result["Matrix4d"].SetRotate.im_func.func_doc = """SetRotate(rot) -> GF_API GfMatrix4d

rot : Quatd


Sets the matrix to specify a rotation equivalent to *rot*, and clears
the translation.


----------------------------------------------------------------------
SetRotate(rot) -> GF_API GfMatrix4d

rot : Rotation


Sets the matrix to specify a rotation equivalent to *rot*, and clears
the translation.


----------------------------------------------------------------------
SetRotate(mx) -> GF_API GfMatrix4d

mx : Matrix3d


Sets the matrix to specify a rotation equivalent to *mx*, and clears
the translation.

"""
   result["Matrix4d"].RemoveScaleShear.im_func.func_doc = """RemoveScaleShear() -> GF_API GfMatrix4d



Returns the matrix with any scaling or shearing removed, leaving only
the rotation and translation.


If the matrix cannot be decomposed, returns the original matrix.

"""
   result["Matrix4d"].GetOrthonormalized.im_func.func_doc = """GetOrthonormalized(issueWarning) -> GF_API GfMatrix4d

issueWarning : bool


Returns an orthonormalized copy of the matrix.

"""
   result["Matrix4d"].IsRightHanded.im_func.func_doc = """IsRightHanded() -> bool



Returns true if the vectors in the upper 3x3 matrix form a right-
handed coordinate system.

"""
   result["Vec2h"].__doc__ = """
Basic type for a vector of 2 GfHalf components.


Represents a vector of 2 components of type C{GfHalf}. It is intended
to be fast and simple.

"""
   result["Vec2h"].Normalize.im_func.func_doc = """Normalize(eps) -> Half

eps : Half


Normalizes the vector in place to unit length, returning the length
before normalization.


If the length of the vector is smaller than C{eps}, then the vector is
set to vector/ C{eps}. The original length of the vector is returned.
See also GfNormalize() .

"""
   result["Vec2h"].YAxis.func_doc = """**static** YAxis() -> Vec2h



Create a unit vector along the Y-axis.

"""
   result["Vec2h"].GetLength.im_func.func_doc = """GetLength() -> Half



Length.

"""
   result["Vec2h"].GetComplement.im_func.func_doc = """GetComplement(b) -> Vec2h

b : Vec2h


Returns the orthogonal complement of C{this->GetProjection(b)} .


That is: ::

  *this - this->GetProjection(b)


"""
   result["Vec2h"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Vec2h

eps : Half

"""
   result["Vec2h"].GetProjection.im_func.func_doc = """GetProjection(v) -> Vec2h

v : Vec2h


Returns the projection of C{this} onto C{v}.


That is: ::

  v * (*this * v)


"""
   result["Vec2h"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec2h


----------------------------------------------------------------------
__init__(value)

value : Half


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1)

s0 : Half
s1 : Half


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.


----------------------------------------------------------------------
__init__(other)

other : class GfVec2d


Construct from GfVec2d.


----------------------------------------------------------------------
__init__(other)

other : class GfVec2f


Construct from GfVec2f.


----------------------------------------------------------------------
__init__(other)

other : class GfVec2i


Implicitly convert from GfVec2i.

"""
   result["Vec2h"].XAxis.func_doc = """**static** XAxis() -> Vec2h



Create a unit vector along the X-axis.

"""
   result["Vec2h"].Axis.func_doc = """**static** Axis(i) -> Vec2h

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 2.

"""
   result["Vec2i"].__doc__ = """
Basic type for a vector of 2 int components.


Represents a vector of 2 components of type C{int}. It is intended to
be fast and simple.

"""
   result["Vec2i"].XAxis.func_doc = """**static** XAxis() -> Vec2i



Create a unit vector along the X-axis.

"""
   result["Vec2i"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec2i


----------------------------------------------------------------------
__init__(value)

value : int


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1)

s0 : int
s1 : int


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.

"""
   result["Vec2i"].YAxis.func_doc = """**static** YAxis() -> Vec2i



Create a unit vector along the Y-axis.

"""
   result["Vec2i"].Axis.func_doc = """**static** Axis(i) -> Vec2i

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 2.

"""
   result["Vec2f"].__doc__ = """
Basic type for a vector of 2 float components.


Represents a vector of 2 components of type C{float}. It is intended
to be fast and simple.

"""
   result["Vec2f"].Normalize.im_func.func_doc = """Normalize(eps) -> float

eps : float


Normalizes the vector in place to unit length, returning the length
before normalization.


If the length of the vector is smaller than C{eps}, then the vector is
set to vector/ C{eps}. The original length of the vector is returned.
See also GfNormalize() .

"""
   result["Vec2f"].YAxis.func_doc = """**static** YAxis() -> Vec2f



Create a unit vector along the Y-axis.

"""
   result["Vec2f"].GetLength.im_func.func_doc = """GetLength() -> float



Length.

"""
   result["Vec2f"].GetComplement.im_func.func_doc = """GetComplement(b) -> Vec2f

b : Vec2f


Returns the orthogonal complement of C{this->GetProjection(b)} .


That is: ::

  *this - this->GetProjection(b)


"""
   result["Vec2f"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Vec2f

eps : float

"""
   result["Vec2f"].GetProjection.im_func.func_doc = """GetProjection(v) -> Vec2f

v : Vec2f


Returns the projection of C{this} onto C{v}.


That is: ::

  v * (*this * v)


"""
   result["Vec2f"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec2f


----------------------------------------------------------------------
__init__(value)

value : float


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1)

s0 : float
s1 : float


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.


----------------------------------------------------------------------
__init__(other)

other : class GfVec2d


Construct from GfVec2d.


----------------------------------------------------------------------
__init__(other)

other : class GfVec2h


Implicitly convert from GfVec2h.


----------------------------------------------------------------------
__init__(other)

other : class GfVec2i


Implicitly convert from GfVec2i.

"""
   result["Vec2f"].XAxis.func_doc = """**static** XAxis() -> Vec2f



Create a unit vector along the X-axis.

"""
   result["Vec2f"].Axis.func_doc = """**static** Axis(i) -> Vec2f

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 2.

"""
   result["Vec2d"].__doc__ = """
Basic type for a vector of 2 double components.


Represents a vector of 2 components of type C{double}. It is intended
to be fast and simple.

"""
   result["Vec2d"].Normalize.im_func.func_doc = """Normalize(eps) -> double

eps : double


Normalizes the vector in place to unit length, returning the length
before normalization.


If the length of the vector is smaller than C{eps}, then the vector is
set to vector/ C{eps}. The original length of the vector is returned.
See also GfNormalize() .

"""
   result["Vec2d"].YAxis.func_doc = """**static** YAxis() -> Vec2d



Create a unit vector along the Y-axis.

"""
   result["Vec2d"].GetLength.im_func.func_doc = """GetLength() -> double



Length.

"""
   result["Vec2d"].GetComplement.im_func.func_doc = """GetComplement(b) -> Vec2d

b : Vec2d


Returns the orthogonal complement of C{this->GetProjection(b)} .


That is: ::

  *this - this->GetProjection(b)


"""
   result["Vec2d"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Vec2d

eps : double

"""
   result["Vec2d"].GetProjection.im_func.func_doc = """GetProjection(v) -> Vec2d

v : Vec2d


Returns the projection of C{this} onto C{v}.


That is: ::

  v * (*this * v)


"""
   result["Vec2d"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec2d


----------------------------------------------------------------------
__init__(value)

value : double


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1)

s0 : double
s1 : double


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.


----------------------------------------------------------------------
__init__(other)

other : class GfVec2f


Implicitly convert from GfVec2f.


----------------------------------------------------------------------
__init__(other)

other : class GfVec2h


Implicitly convert from GfVec2h.


----------------------------------------------------------------------
__init__(other)

other : class GfVec2i


Implicitly convert from GfVec2i.

"""
   result["Vec2d"].XAxis.func_doc = """**static** XAxis() -> Vec2d



Create a unit vector along the X-axis.

"""
   result["Vec2d"].Axis.func_doc = """**static** Axis(i) -> Vec2d

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 2.

"""
   result["Matrix3d"].__doc__ = """
Stores a 3x3 matrix of C{double} elements.


A basic type.

Matrices are defined to be in row-major order, so C{matrix[i][j]}
indexes the element in the *i* th row and the *j* th column.

3D Transformations
==================

Three methods, SetRotate() , SetScale() , and ExtractRotation() ,
interpret a GfMatrix3d as a 3D transformation. By convention, vectors
are treated primarily as row vectors, implying the following:

   - Transformation matrices are organized to deal with row vectors,
     not column vectors.

   - Each of the Set() methods in this class completely rewrites the
     matrix; for example, SetRotate() yields a matrix which does nothing
     but rotate.

   - When multiplying two transformation matrices, the matrix on the
     left applies a more local transformation to a row vector. For example,
     if R represents a rotation matrix and S represents a scale matrix, the
     product R*S will rotate a row vector, then scale it.


"""
   result["Matrix3d"].IsLeftHanded.im_func.func_doc = """IsLeftHanded() -> bool



Returns true if the vectors in matrix form a left-handed coordinate
system.

"""
   result["Matrix3d"].GetTranspose.im_func.func_doc = """GetTranspose() -> GF_API GfMatrix3d



Returns the transpose of the matrix.

"""
   result["Matrix3d"].SetZero.im_func.func_doc = """SetZero() -> Matrix3d



Sets the matrix to zero.

"""
   result["Matrix3d"].SetScale.im_func.func_doc = """SetScale(scaleFactors) -> GF_API GfMatrix3d

scaleFactors : Vec3d


Sets the matrix to specify a nonuniform scaling in x, y, and z by the
factors in vector *scaleFactors*.


----------------------------------------------------------------------
SetScale(scaleFactor) -> GF_API GfMatrix3d

scaleFactor : double


Sets matrix to specify a uniform scaling by *scaleFactor*.

"""
   result["Matrix3d"].GetHandedness.im_func.func_doc = """GetHandedness() -> GF_API double



Returns the sign of the determinant of the matrix, i.e.


1 for a right-handed matrix, -1 for a left-handed matrix, and 0 for a
singular matrix.

"""
   result["Matrix3d"].SetRow.im_func.func_doc = """SetRow(i, v)

i : int
v : Vec3d


Sets a row of the matrix from a Vec3.

"""
   result["Matrix3d"].Orthonormalize.im_func.func_doc = """Orthonormalize(issueWarning) -> GF_API bool

issueWarning : bool


Makes the matrix orthonormal in place.


This is an iterative method that is much more stable than the previous
cross/cross method. If the iterative method does not converge, a
warning is issued.

Returns true if the iteration converged, false otherwise. Leaves any
translation part of the matrix unchanged. If *issueWarning* is true,
this method will issue a warning if the iteration does not converge,
otherwise it will be silent.

"""
   result["Matrix3d"].GetColumn.im_func.func_doc = """GetColumn(i) -> Vec3d

i : int


Gets a column of the matrix as a Vec3.

"""
   result["Matrix3d"].GetDeterminant.im_func.func_doc = """GetDeterminant() -> GF_API double



Returns the determinant of the matrix.

"""
   result["Matrix3d"].ExtractRotation.im_func.func_doc = """ExtractRotation() -> GF_API GfRotation



Returns the rotation corresponding to this matrix.


This works well only if the matrix represents a rotation.

For good results, consider calling Orthonormalize() before calling
this method.

"""
   result["Matrix3d"].SetDiagonal.im_func.func_doc = """SetDiagonal(s) -> GF_API GfMatrix3d

s : double


Sets the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
SetDiagonal(arg1) -> GF_API GfMatrix3d

arg1 : Vec3d


Sets the matrix to have diagonal ( C{v[0], v[1], v[2]} ).

"""
   result["Matrix3d"].GetRow.im_func.func_doc = """GetRow(i) -> Vec3d

i : int


Gets a row of the matrix as a Vec3.

"""
   result["Matrix3d"].GetInverse.im_func.func_doc = """GetInverse(det, eps) -> GF_API GfMatrix3d

det : double
eps : double


Returns the inverse of the matrix, or FLT_MAX * SetIdentity() if the
matrix is singular.


(FLT_MAX is the largest value a C{float} can have, as defined by the
system.) The matrix is considered singular if the determinant is less
than or equal to the optional parameter *eps*. If *det* is non-null,
C{*det} is set to the determinant.

"""
   result["Matrix3d"].SetIdentity.im_func.func_doc = """SetIdentity() -> Matrix3d



Sets the matrix to the identity matrix.

"""
   result["Matrix3d"].Set.im_func.func_doc = """Set(m00, m01, m02, m10, m11, m12, m20, m21, m22) -> Matrix3d

m00 : double
m01 : double
m02 : double
m10 : double
m11 : double
m12 : double
m20 : double
m21 : double
m22 : double


Sets the matrix from 9 independent C{double} values, specified in row-
major order.


For example, parameter *m10* specifies the value in row 1 and column
0.


----------------------------------------------------------------------
Set(m) -> Matrix3d

m : double


Sets the matrix from a 3x3 array of C{double} values, specified in
row-major order.

"""
   result["Matrix3d"].SetColumn.im_func.func_doc = """SetColumn(i, v)

i : int
v : Vec3d


Sets a column of the matrix from a Vec3.

"""
   result["Matrix3d"].__init__.im_func.func_doc = """__init__()



Default constructor. Leaves the matrix component values undefined.


----------------------------------------------------------------------
__init__(m00, m01, m02, m10, m11, m12, m20, m21, m22)

m00 : double
m01 : double
m02 : double
m10 : double
m11 : double
m12 : double
m20 : double
m21 : double
m22 : double


Constructor.


Initializes the matrix from 9 independent C{double} values, specified
in row-major order. For example, parameter *m10* specifies the value
in row 1 and column 0.


----------------------------------------------------------------------
__init__(m)

m : double


Constructor.


Initializes the matrix from a 3x3 array of C{double} values, specified
in row-major order.


----------------------------------------------------------------------
__init__(s)

s : double


Constructor.


Explicitly initializes the matrix to *s* times the identity matrix.


----------------------------------------------------------------------
__init__(s)

s : int


This explicit constructor initializes the matrix to C{s} times the
identity matrix.


----------------------------------------------------------------------
__init__(v)

v : Vec3d


Constructor.


Explicitly initializes the matrix to diagonal form, with the *i* th
element on the diagonal set to C{v[i]} .


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<double>>


Constructor.


Initialize the matrix from a vector of vectors of double. The vector
is expected to be 3x3. If it is too big, only the first 3 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(v) -> GF_API

v : sequence<sequence<float>>


Constructor.


Initialize the matrix from a vector of vectors of float. The vector is
expected to be 3x3. If it is too big, only the first 3 rows and/or
columns will be used. If it is too small, uninitialized elements will
be filled in with the corresponding elements from an identity matrix.


----------------------------------------------------------------------
__init__(rot) -> GF_API

rot : Rotation


Constructor. Initialize matrix from rotation.


----------------------------------------------------------------------
__init__(rot) -> GF_API

rot : Quatd


Constructor. Initialize matrix from a quaternion.


----------------------------------------------------------------------
__init__(m) -> GF_API

m : class GfMatrix3f


This explicit constructor converts a "float" matrix to a "double"
matrix.

"""
   result["Matrix3d"].SetRotate.im_func.func_doc = """SetRotate(rot) -> GF_API GfMatrix3d

rot : Quatd


Sets the matrix to specify a rotation equivalent to *rot*.


----------------------------------------------------------------------
SetRotate(rot) -> GF_API GfMatrix3d

rot : Rotation


Sets the matrix to specify a rotation equivalent to *rot*.

"""
   result["Matrix3d"].GetOrthonormalized.im_func.func_doc = """GetOrthonormalized(issueWarning) -> GF_API GfMatrix3d

issueWarning : bool


Returns an orthonormalized copy of the matrix.

"""
   result["Matrix3d"].IsRightHanded.im_func.func_doc = """IsRightHanded() -> bool



Returns true if the vectors in the matrix form a right-handed
coordinate system.

"""
   result["Ceil"].func_doc = """Ceil(f) -> double

f : double


Return ceil( C{f}).


----------------------------------------------------------------------
Ceil(f) -> float

f : float


Return ceil( C{f}).


----------------------------------------------------------------------
Ceil(f) -> double

f : double


Return ceil( C{f}).


----------------------------------------------------------------------
Ceil(f) -> float

f : float


Return ceil( C{f}).

"""
   result["Vec3i"].__doc__ = """
Basic type for a vector of 3 int components.


Represents a vector of 3 components of type C{int}. It is intended to
be fast and simple.

"""
   result["Vec3i"].XAxis.func_doc = """**static** XAxis() -> Vec3i



Create a unit vector along the X-axis.

"""
   result["Vec3i"].YAxis.func_doc = """**static** YAxis() -> Vec3i



Create a unit vector along the Y-axis.

"""
   result["Vec3i"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec3i


----------------------------------------------------------------------
__init__(value)

value : int


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1, s2)

s0 : int
s1 : int
s2 : int


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.

"""
   result["Vec3i"].ZAxis.func_doc = """**static** ZAxis() -> Vec3i



Create a unit vector along the Z-axis.

"""
   result["Vec3i"].Axis.func_doc = """**static** Axis(i) -> Vec3i

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 3.

"""
   result["Round"].func_doc = """Round(f) -> double

f : double


Return round( C{f}).


----------------------------------------------------------------------
Round(f) -> float

f : float


Return round( C{f}).


----------------------------------------------------------------------
Round(f) -> double

f : double


Return round( C{f}).


----------------------------------------------------------------------
Round(f) -> float

f : float


Return round( C{f}).

"""
   result["IsClose"].func_doc = """IsClose(a, b, epsilon) -> bool

a : double
b : double
epsilon : double


Returns true if C{a} and C{b} are with C{epsilon} of each other.


----------------------------------------------------------------------
IsClose(m1, m2, tolerance) -> GF_API bool

m1 : Matrix2d
m2 : Matrix2d
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
difference between each component of the matrix is less than or equal
to C{tolerance}, or false otherwise.


----------------------------------------------------------------------
IsClose(m1, m2, tolerance) -> GF_API bool

m1 : Matrix2f
m2 : Matrix2f
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
difference between each component of the matrix is less than or equal
to C{tolerance}, or false otherwise.


----------------------------------------------------------------------
IsClose(m1, m2, tolerance) -> GF_API bool

m1 : Matrix3d
m2 : Matrix3d
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
difference between each component of the matrix is less than or equal
to C{tolerance}, or false otherwise.


----------------------------------------------------------------------
IsClose(m1, m2, tolerance) -> GF_API bool

m1 : Matrix3f
m2 : Matrix3f
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
difference between each component of the matrix is less than or equal
to C{tolerance}, or false otherwise.


----------------------------------------------------------------------
IsClose(m1, m2, tolerance) -> GF_API bool

m1 : Matrix4d
m2 : Matrix4d
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
difference between each component of the matrix is less than or equal
to C{tolerance}, or false otherwise.


----------------------------------------------------------------------
IsClose(m1, m2, tolerance) -> GF_API bool

m1 : Matrix4f
m2 : Matrix4f
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
difference between each component of the matrix is less than or equal
to C{tolerance}, or false otherwise.


----------------------------------------------------------------------
IsClose(v1, v2, tolerance) -> bool

v1 : Vec2d
v2 : Vec2d
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
length of the difference vector is less than or equal to C{tolerance}.


----------------------------------------------------------------------
IsClose(v1, v2, tolerance) -> bool

v1 : Vec2f
v2 : Vec2f
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
length of the difference vector is less than or equal to C{tolerance}.


----------------------------------------------------------------------
IsClose(v1, v2, tolerance) -> bool

v1 : Vec2h
v2 : Vec2h
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
length of the difference vector is less than or equal to C{tolerance}.


----------------------------------------------------------------------
IsClose(v1, v2, tolerance) -> bool

v1 : Vec3d
v2 : Vec3d
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
length of the difference vector is less than or equal to C{tolerance}.


----------------------------------------------------------------------
IsClose(v1, v2, tolerance) -> bool

v1 : Vec3f
v2 : Vec3f
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
length of the difference vector is less than or equal to C{tolerance}.


----------------------------------------------------------------------
IsClose(v1, v2, tolerance) -> bool

v1 : Vec3h
v2 : Vec3h
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
length of the difference vector is less than or equal to C{tolerance}.


----------------------------------------------------------------------
IsClose(v1, v2, tolerance) -> bool

v1 : Vec4d
v2 : Vec4d
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
length of the difference vector is less than or equal to C{tolerance}.


----------------------------------------------------------------------
IsClose(v1, v2, tolerance) -> bool

v1 : Vec4f
v2 : Vec4f
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
length of the difference vector is less than or equal to C{tolerance}.


----------------------------------------------------------------------
IsClose(v1, v2, tolerance) -> bool

v1 : Vec4h
v2 : Vec4h
tolerance : double


Tests for equality within a given tolerance, returning C{true} if the
length of the difference vector is less than or equal to C{tolerance}.


----------------------------------------------------------------------
IsClose(a, b, epsilon) -> bool

a : double
b : double
epsilon : double


Returns true if C{a} and C{b} are with C{epsilon} of each other.

"""
   result["Plane"].__doc__ = """
Basic type: 3-dimensional plane.


This class represents a three-dimensional plane as a normal vector and
the distance of the plane from the origin, measured along the normal.
The plane can also be used to represent a half-space: the side of the
plane in the direction of the normal.

"""
   result["Plane"].Project.im_func.func_doc = """Project(p) -> Vec3d

p : Vec3d


Return the projection of C{p} onto the plane.

"""
   result["Plane"].Set.im_func.func_doc = """Set(normal, distanceToOrigin)

normal : Vec3d
distanceToOrigin : double


Sets this to the plane perpendicular to C{normal} and at C{distance}
units from the origin.


The passed-in normal is normalized to unit length first.


----------------------------------------------------------------------
Set(normal, point) -> GF_API void

normal : Vec3d
point : Vec3d


This constructor sets this to the plane perpendicular to C{normal} and
that passes through C{point}.


The passed-in normal is normalized to unit length first.


----------------------------------------------------------------------
Set(p0, p1, p2) -> GF_API void

p0 : Vec3d
p1 : Vec3d
p2 : Vec3d


This constructor sets this to the plane that contains the three given
points.


The normal is constructed from the cross product of ( C{p1} - C{p0}) (
C{p2} - C{p0}). Results are undefined if the points are collinear.


----------------------------------------------------------------------
Set(eqn) -> GF_API void

eqn : Vec4d


This method sets this to the plane given by the equation C{eqn} [0] *
x + C{eqn} [1] * y + C{eqn} [2] * z + C{eqn} [3] = 0.

"""
   result["Plane"].__init__.im_func.func_doc = """__init__()



The default constructor leaves the plane parameters undefined.


----------------------------------------------------------------------
__init__(normal, distanceToOrigin)

normal : Vec3d
distanceToOrigin : double


This constructor sets this to the plane perpendicular to C{normal} and
at C{distance} units from the origin.


The passed-in normal is normalized to unit length first.


----------------------------------------------------------------------
__init__(normal, point)

normal : Vec3d
point : Vec3d


This constructor sets this to the plane perpendicular to C{normal} and
that passes through C{point}.


The passed-in normal is normalized to unit length first.


----------------------------------------------------------------------
__init__(p0, p1, p2)

p0 : Vec3d
p1 : Vec3d
p2 : Vec3d


This constructor sets this to the plane that contains the three given
points.


The normal is constructed from the cross product of ( C{p1} - C{p0}) (
C{p2} - C{p0}). Results are undefined if the points are collinear.


----------------------------------------------------------------------
__init__(eqn)

eqn : Vec4d


This constructor creates a plane given by the equation C{eqn} [0] * x
+ C{eqn} [1] * y + C{eqn} [2] * z + C{eqn} [3] = 0.

"""
   result["Plane"].Reorient.im_func.func_doc = """Reorient(p)

p : Vec3d


Flip the plane normal (if necessary) so that C{p} is in the positive
halfspace.

"""
   result["Plane"].IntersectsPositiveHalfSpace.im_func.func_doc = """IntersectsPositiveHalfSpace(box) -> GF_API bool

box : Range3d


Returns C{true} if the given aligned bounding box is at least
partially on the positive side (the one the normal points into) of the
plane.


----------------------------------------------------------------------
IntersectsPositiveHalfSpace(pt) -> bool

pt : Vec3d


Returns true if the given point is on the plane or within its positive
half space.

"""
   result["Plane"].GetNormal.im_func.func_doc = """GetNormal() -> Vec3d



Returns the unit-length normal vector of the plane.

"""
   result["Plane"].Transform.im_func.func_doc = """Transform(matrix) -> GF_API GfPlane

matrix : Matrix4d


Transforms the plane by the given matrix.

"""
   result["Plane"].GetDistanceFromOrigin.im_func.func_doc = """GetDistanceFromOrigin() -> double



Returns the distance of the plane from the origin.

"""
   result["Plane"].GetEquation.im_func.func_doc = """GetEquation() -> GF_API GfVec4d



Give the coefficients of the equation of the plane.


Suitable to OpenGL calls to set the clipping plane.

"""
   result["Plane"].GetDistance.im_func.func_doc = """GetDistance(p) -> double

p : Vec3d


Returns the distance of point C{from} the plane.


This distance will be positive if the point is on the side of the
plane containing the normal.

"""
   result["Exp"].func_doc = """Exp(f) -> double

f : double


Return exp( C{f}).


----------------------------------------------------------------------
Exp(f) -> float

f : float


Return exp( C{f}).


----------------------------------------------------------------------
Exp(f) -> double

f : double


Return exp( C{f}).


----------------------------------------------------------------------
Exp(f) -> float

f : float


Return exp( C{f}).

"""
   result["Sqrt"].func_doc = """Sqrt(f) -> double

f : double


Return sqrt( C{f}).


----------------------------------------------------------------------
Sqrt(f) -> float

f : float


Return sqrt( C{f}).


----------------------------------------------------------------------
Sqrt(f) -> double

f : double


Return sqrt( C{f}).


----------------------------------------------------------------------
Sqrt(f) -> float

f : float


Return sqrt( C{f}).

"""
   result["Range3f"].__doc__ = """
Basic type: 3-dimensional floating point range.


This class represents a 3-dimensional range (or interval) All
operations are component-wise and conform to interval mathematics. An
empty range is one where max<min. The default empty is
[FLT_MAX,-FLT_MAX]

"""
   result["Range3f"].GetCorner.im_func.func_doc = """GetCorner(i) -> GF_API GfVec3f

i : size_t


Returns the ith corner of the range, in the following order: LDB, RDB,
LUB, RUB, LDF, RDF, LUF, RUF.


Where L/R is left/right, D/U is down/up, and B/F is back/front.

"""
   result["Range3f"].Contains.im_func.func_doc = """Contains(point) -> bool

point : Vec3f


Returns true if the C{point} is located inside the range.


As with all operations of this type, the range is assumed to include
its extrema.


----------------------------------------------------------------------
Contains(range) -> bool

range : Range3f


Returns true if the C{range} is located entirely inside the range.


As with all operations of this type, the ranges are assumed to include
their extrema.

"""
   result["Range3f"].__init__.im_func.func_doc = """__init__()



The default constructor creates an empty range.


----------------------------------------------------------------------
__init__(min, max)

min : Vec3f
max : Vec3f


This constructor initializes the minimum and maximum points.

"""
   result["Range3f"].IntersectWith.im_func.func_doc = """IntersectWith(b) -> Range3f

b : Range3f


Modifies this range to hold its intersection with C{b} and returns the
result.

"""
   result["Range3f"].SetMin.im_func.func_doc = """SetMin(min)

min : Vec3f


Sets the minimum value of the range.

"""
   result["Range3f"].GetSize.im_func.func_doc = """GetSize() -> Vec3f



Returns the size of the range.

"""
   result["Range3f"].SetEmpty.im_func.func_doc = """SetEmpty()



Sets the range to an empty interval.

"""
   result["Range3f"].GetMin.im_func.func_doc = """GetMin() -> Vec3f



Returns the minimum value of the range.

"""
   result["Range3f"].GetMax.im_func.func_doc = """GetMax() -> Vec3f



Returns the maximum value of the range.

"""
   result["Range3f"].UnionWith.im_func.func_doc = """UnionWith(b) -> Range3f

b : Range3f


Extend C{this} to include C{b}.


----------------------------------------------------------------------
UnionWith(b) -> Range3f

b : Vec3f


Extend C{this} to include C{b}.

"""
   result["Range3f"].SetMax.im_func.func_doc = """SetMax(max)

max : Vec3f


Sets the maximum value of the range.

"""
   result["Range3f"].IsEmpty.im_func.func_doc = """IsEmpty() -> bool



Returns whether the range is empty (max<min).

"""
   result["Range3f"].GetIntersection.func_doc = """**static** GetIntersection(a, b) -> Range3f

a : Range3f
b : Range3f


Returns a C{GfRange3f} that describes the intersection of C{a} and
C{b}.

"""
   result["Range3f"].GetMidpoint.im_func.func_doc = """GetMidpoint() -> Vec3f



Returns the midpoint of the range, that is, 0.5*(min+max).


Note: this returns zero in the case of default-constructed ranges, or
ranges set via SetEmpty() .

"""
   result["Range3f"].GetOctant.im_func.func_doc = """GetOctant(i) -> GF_API GfRange3f

i : size_t


Returns the ith octant of the range, in the following order: LDB, RDB,
LUB, RUB, LDF, RDF, LUF, RUF.


Where L/R is left/right, D/U is down/up, and B/F is back/front.

"""
   result["Range3f"].GetDistanceSquared.im_func.func_doc = """GetDistanceSquared(p) -> GF_API double

p : Vec3f


Compute the squared distance from a point to the range.

"""
   result["Range3f"].GetUnion.func_doc = """**static** GetUnion(a, b) -> Range3f

a : Range3f
b : Range3f


Returns the smallest C{GfRange3f} which contains both C{a} and C{b}.

"""
   result["Range3d"].__doc__ = """
Basic type: 3-dimensional floating point range.


This class represents a 3-dimensional range (or interval) All
operations are component-wise and conform to interval mathematics. An
empty range is one where max<min. The default empty is
[FLT_MAX,-FLT_MAX]

"""
   result["Range3d"].GetCorner.im_func.func_doc = """GetCorner(i) -> GF_API GfVec3d

i : size_t


Returns the ith corner of the range, in the following order: LDB, RDB,
LUB, RUB, LDF, RDF, LUF, RUF.


Where L/R is left/right, D/U is down/up, and B/F is back/front.

"""
   result["Range3d"].Contains.im_func.func_doc = """Contains(point) -> bool

point : Vec3d


Returns true if the C{point} is located inside the range.


As with all operations of this type, the range is assumed to include
its extrema.


----------------------------------------------------------------------
Contains(range) -> bool

range : Range3d


Returns true if the C{range} is located entirely inside the range.


As with all operations of this type, the ranges are assumed to include
their extrema.

"""
   result["Range3d"].IntersectWith.im_func.func_doc = """IntersectWith(b) -> Range3d

b : Range3d


Modifies this range to hold its intersection with C{b} and returns the
result.

"""
   result["Range3d"].SetMin.im_func.func_doc = """SetMin(min)

min : Vec3d


Sets the minimum value of the range.

"""
   result["Range3d"].GetSize.im_func.func_doc = """GetSize() -> Vec3d



Returns the size of the range.

"""
   result["Range3d"].SetEmpty.im_func.func_doc = """SetEmpty()



Sets the range to an empty interval.

"""
   result["Range3d"].GetMin.im_func.func_doc = """GetMin() -> Vec3d



Returns the minimum value of the range.

"""
   result["Range3d"].GetMax.im_func.func_doc = """GetMax() -> Vec3d



Returns the maximum value of the range.

"""
   result["Range3d"].UnionWith.im_func.func_doc = """UnionWith(b) -> Range3d

b : Range3d


Extend C{this} to include C{b}.


----------------------------------------------------------------------
UnionWith(b) -> Range3d

b : Vec3d


Extend C{this} to include C{b}.

"""
   result["Range3d"].SetMax.im_func.func_doc = """SetMax(max)

max : Vec3d


Sets the maximum value of the range.

"""
   result["Range3d"].IsEmpty.im_func.func_doc = """IsEmpty() -> bool



Returns whether the range is empty (max<min).

"""
   result["Range3d"].GetIntersection.func_doc = """**static** GetIntersection(a, b) -> Range3d

a : Range3d
b : Range3d


Returns a C{GfRange3d} that describes the intersection of C{a} and
C{b}.

"""
   result["Range3d"].GetMidpoint.im_func.func_doc = """GetMidpoint() -> Vec3d



Returns the midpoint of the range, that is, 0.5*(min+max).


Note: this returns zero in the case of default-constructed ranges, or
ranges set via SetEmpty() .

"""
   result["Range3d"].GetOctant.im_func.func_doc = """GetOctant(i) -> GF_API GfRange3d

i : size_t


Returns the ith octant of the range, in the following order: LDB, RDB,
LUB, RUB, LDF, RDF, LUF, RUF.


Where L/R is left/right, D/U is down/up, and B/F is back/front.

"""
   result["Range3d"].GetDistanceSquared.im_func.func_doc = """GetDistanceSquared(p) -> GF_API double

p : Vec3d


Compute the squared distance from a point to the range.

"""
   result["Range3d"].__init__.im_func.func_doc = """__init__()



The default constructor creates an empty range.


----------------------------------------------------------------------
__init__(min, max)

min : Vec3d
max : Vec3d


This constructor initializes the minimum and maximum points.

"""
   result["Range3d"].GetUnion.func_doc = """**static** GetUnion(a, b) -> Range3d

a : Range3d
b : Range3d


Returns the smallest C{GfRange3d} which contains both C{a} and C{b}.

"""
   result["Dot"].func_doc = """Dot(v1, v2) -> double

v1 : Vec2d
v2 : Vec2d


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> float

v1 : Vec2f
v2 : Vec2f


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> Half

v1 : Vec2h
v2 : Vec2h


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> int

v1 : Vec2i
v2 : Vec2i


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> double

v1 : Vec3d
v2 : Vec3d


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> float

v1 : Vec3f
v2 : Vec3f


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> Half

v1 : Vec3h
v2 : Vec3h


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> int

v1 : Vec3i
v2 : Vec3i


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> double

v1 : Vec4d
v2 : Vec4d


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> float

v1 : Vec4f
v2 : Vec4f


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> Half

v1 : Vec4h
v2 : Vec4h


Returns the dot (inner) product of two vectors.


----------------------------------------------------------------------
Dot(v1, v2) -> int

v1 : Vec4i
v2 : Vec4i


Returns the dot (inner) product of two vectors.

"""
   result["Mod"].func_doc = """Mod(a, b) -> GF_API double

a : double
b : double


The mod function with "correct" behaviour for negative numbers.


If C{a} = C{n} C{b} for some integer C{n}, zero is returned.
Otherwise, for positive C{a}, the value returned is C{fmod(a,b)} , and
for negative C{a}, the value returned is C{fmod(a,b)+b}.


----------------------------------------------------------------------
Mod(a, b) -> GF_API float

a : float
b : float


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.


----------------------------------------------------------------------
Mod(a, b) -> GF_API double

a : double
b : double


The mod function with "correct" behaviour for negative numbers.


If C{a} = C{n} C{b} for some integer C{n}, zero is returned.
Otherwise, for positive C{a}, the value returned is C{fmod(a,b)} , and
for negative C{a}, the value returned is C{fmod(a,b)+b}.

"""
   result["Pow"].func_doc = """Pow(f, p) -> double

f : double
p : double


Return pow( C{f}, C{p}).


----------------------------------------------------------------------
Pow(f, p) -> float

f : float
p : float


Return pow( C{f}, C{p}).


----------------------------------------------------------------------
Pow(f, p) -> double

f : double
p : double


Return pow( C{f}, C{p}).


----------------------------------------------------------------------
Pow(f, p) -> float

f : float
p : float


Return pow( C{f}, C{p}).

"""
   result["GetHomogenized"].func_doc = """GetHomogenized(v) -> GF_API GfVec4f

v : Vec4f


Returns a vector which is C{v} homogenized.


If the fourth element of C{v} is 0, it is set to 1.


----------------------------------------------------------------------
GetHomogenized(v) -> GF_API GfVec4d

v : Vec4d


----------------------------------------------------------------------
GetHomogenized(v) -> GF_API GfVec4f

v : Vec4f


Returns a vector which is C{v} homogenized.


If the fourth element of C{v} is 0, it is set to 1.

"""
   result["Sqr"].func_doc = """Sqr(x) -> double

x : T


Returns the inner product of C{x} with itself: specifically, C{x*x}.


Defined for C{int}, C{float}, C{double}, and all C{GfVec} types.


----------------------------------------------------------------------
Sqr(x) -> double

x : T


Returns the inner product of C{x} with itself: specifically, C{x*x}.


Defined for C{int}, C{float}, C{double}, and all C{GfVec} types.

"""
   result["Ray"].__doc__ = """
Basic type: Ray used for intersection testing.


This class represents a three-dimensional ray in space, typically used
for intersection testing. It consists of an origin and a direction.

Note that by default a C{GfRay} does not normalize its direction
vector to unit length.

Note for ray intersections, the start point is included in the
computations, i.e., a distance of zero is defined to be intersecting.

"""
   result["Ray"].SetEnds.im_func.func_doc = """SetEnds(startPoint, endPoint) -> GF_API void

startPoint : Vec3d
endPoint : Vec3d


Sets the ray by specifying a starting point and an ending point.

"""
   result["Ray"].SetPointAndDirection.im_func.func_doc = """SetPointAndDirection(startPoint, direction) -> GF_API void

startPoint : Vec3d
direction : Vec3d


Sets the ray by specifying a starting point and a direction.

"""
   result["Ray"].Transform.im_func.func_doc = """Transform(matrix) -> GF_API GfRay

matrix : Matrix4d


Transforms the ray by the given matrix.

"""
   result["Ray"].GetPoint.im_func.func_doc = """GetPoint(distance) -> Vec3d

distance : double


Returns the point that is C{distance} units from the starting point
along the direction vector, expressed in parametic distance.

"""
   result["Ray"].FindClosestPoint.im_func.func_doc = """FindClosestPoint(point, rayDistance) -> GF_API GfVec3d

point : Vec3d
rayDistance : double


Returns the point on the ray that is closest to C{point}.


If C{rayDistance} is not C{None}, it will be set to the parametric
distance along the ray of the closest point.

"""
   result["Ray"].__init__.im_func.func_doc = """__init__()



The default constructor leaves the ray parameters undefined.


----------------------------------------------------------------------
__init__(startPoint, direction)

startPoint : Vec3d
direction : Vec3d


This constructor takes a starting point and a direction.

"""
   result["RadiansToDegrees"].func_doc = """RadiansToDegrees(radians) -> double

radians : double


Converts an angle in radians to degrees.


----------------------------------------------------------------------
RadiansToDegrees(radians) -> double

radians : double


Converts an angle in radians to degrees.

"""
   result["Normalize"].func_doc = """Normalize(v, eps) -> double

v : Vec2d
eps : double


Normalizes C{*v} in place to unit length, returning the length before
normalization.


If the length of C{*v} is smaller than C{eps} then C{*v} is set to
C{*v/eps}. The original length of C{*v} is returned.


----------------------------------------------------------------------
Normalize(v, eps) -> float

v : Vec2f
eps : float


Normalizes C{*v} in place to unit length, returning the length before
normalization.


If the length of C{*v} is smaller than C{eps} then C{*v} is set to
C{*v/eps}. The original length of C{*v} is returned.


----------------------------------------------------------------------
Normalize(v, eps) -> Half

v : Vec2h
eps : Half


Normalizes C{*v} in place to unit length, returning the length before
normalization.


If the length of C{*v} is smaller than C{eps} then C{*v} is set to
C{*v/eps}. The original length of C{*v} is returned.


----------------------------------------------------------------------
Normalize(v, eps) -> double

v : Vec3d
eps : double


Normalizes C{*v} in place to unit length, returning the length before
normalization.


If the length of C{*v} is smaller than C{eps} then C{*v} is set to
C{*v/eps}. The original length of C{*v} is returned.


----------------------------------------------------------------------
Normalize(v, eps) -> float

v : Vec3f
eps : float


Normalizes C{*v} in place to unit length, returning the length before
normalization.


If the length of C{*v} is smaller than C{eps} then C{*v} is set to
C{*v/eps}. The original length of C{*v} is returned.


----------------------------------------------------------------------
Normalize(v, eps) -> Half

v : Vec3h
eps : Half


Normalizes C{*v} in place to unit length, returning the length before
normalization.


If the length of C{*v} is smaller than C{eps} then C{*v} is set to
C{*v/eps}. The original length of C{*v} is returned.


----------------------------------------------------------------------
Normalize(v, eps) -> double

v : Vec4d
eps : double


Normalizes C{*v} in place to unit length, returning the length before
normalization.


If the length of C{*v} is smaller than C{eps} then C{*v} is set to
C{*v/eps}. The original length of C{*v} is returned.


----------------------------------------------------------------------
Normalize(v, eps) -> float

v : Vec4f
eps : float


Normalizes C{*v} in place to unit length, returning the length before
normalization.


If the length of C{*v} is smaller than C{eps} then C{*v} is set to
C{*v/eps}. The original length of C{*v} is returned.


----------------------------------------------------------------------
Normalize(v, eps) -> Half

v : Vec4h
eps : Half


Normalizes C{*v} in place to unit length, returning the length before
normalization.


If the length of C{*v} is smaller than C{eps} then C{*v} is set to
C{*v/eps}. The original length of C{*v} is returned.

"""
   result["Range2d"].__doc__ = """
Basic type: 2-dimensional floating point range.


This class represents a 2-dimensional range (or interval) All
operations are component-wise and conform to interval mathematics. An
empty range is one where max<min. The default empty is
[FLT_MAX,-FLT_MAX]

"""
   result["Range2d"].GetCorner.im_func.func_doc = """GetCorner(i) -> GF_API GfVec2d

i : size_t


Returns the ith corner of the range, in the following order: SW, SE,
NW, NE.

"""
   result["Range2d"].Contains.im_func.func_doc = """Contains(point) -> bool

point : Vec2d


Returns true if the C{point} is located inside the range.


As with all operations of this type, the range is assumed to include
its extrema.


----------------------------------------------------------------------
Contains(range) -> bool

range : Range2d


Returns true if the C{range} is located entirely inside the range.


As with all operations of this type, the ranges are assumed to include
their extrema.

"""
   result["Range2d"].IntersectWith.im_func.func_doc = """IntersectWith(b) -> Range2d

b : Range2d


Modifies this range to hold its intersection with C{b} and returns the
result.

"""
   result["Range2d"].SetMin.im_func.func_doc = """SetMin(min)

min : Vec2d


Sets the minimum value of the range.

"""
   result["Range2d"].GetSize.im_func.func_doc = """GetSize() -> Vec2d



Returns the size of the range.

"""
   result["Range2d"].SetEmpty.im_func.func_doc = """SetEmpty()



Sets the range to an empty interval.

"""
   result["Range2d"].GetMin.im_func.func_doc = """GetMin() -> Vec2d



Returns the minimum value of the range.

"""
   result["Range2d"].GetMax.im_func.func_doc = """GetMax() -> Vec2d



Returns the maximum value of the range.

"""
   result["Range2d"].UnionWith.im_func.func_doc = """UnionWith(b) -> Range2d

b : Range2d


Extend C{this} to include C{b}.


----------------------------------------------------------------------
UnionWith(b) -> Range2d

b : Vec2d


Extend C{this} to include C{b}.

"""
   result["Range2d"].SetMax.im_func.func_doc = """SetMax(max)

max : Vec2d


Sets the maximum value of the range.

"""
   result["Range2d"].__init__.im_func.func_doc = """__init__()



The default constructor creates an empty range.


----------------------------------------------------------------------
__init__(min, max)

min : Vec2d
max : Vec2d


This constructor initializes the minimum and maximum points.

"""
   result["Range2d"].IsEmpty.im_func.func_doc = """IsEmpty() -> bool



Returns whether the range is empty (max<min).

"""
   result["Range2d"].GetIntersection.func_doc = """**static** GetIntersection(a, b) -> Range2d

a : Range2d
b : Range2d


Returns a C{GfRange2d} that describes the intersection of C{a} and
C{b}.

"""
   result["Range2d"].GetMidpoint.im_func.func_doc = """GetMidpoint() -> Vec2d



Returns the midpoint of the range, that is, 0.5*(min+max).


Note: this returns zero in the case of default-constructed ranges, or
ranges set via SetEmpty() .

"""
   result["Range2d"].GetDistanceSquared.im_func.func_doc = """GetDistanceSquared(p) -> GF_API double

p : Vec2d


Compute the squared distance from a point to the range.

"""
   result["Range2d"].GetQuadrant.im_func.func_doc = """GetQuadrant(i) -> GF_API GfRange2d

i : size_t


Returns the ith quadrant of the range, in the following order: SW, SE,
NW, NE.

"""
   result["Range2d"].GetUnion.func_doc = """**static** GetUnion(a, b) -> Range2d

a : Range2d
b : Range2d


Returns the smallest C{GfRange2d} which contains both C{a} and C{b}.

"""
   result["Range2f"].__doc__ = """
Basic type: 2-dimensional floating point range.


This class represents a 2-dimensional range (or interval) All
operations are component-wise and conform to interval mathematics. An
empty range is one where max<min. The default empty is
[FLT_MAX,-FLT_MAX]

"""
   result["Range2f"].GetCorner.im_func.func_doc = """GetCorner(i) -> GF_API GfVec2f

i : size_t


Returns the ith corner of the range, in the following order: SW, SE,
NW, NE.

"""
   result["Range2f"].Contains.im_func.func_doc = """Contains(point) -> bool

point : Vec2f


Returns true if the C{point} is located inside the range.


As with all operations of this type, the range is assumed to include
its extrema.


----------------------------------------------------------------------
Contains(range) -> bool

range : Range2f


Returns true if the C{range} is located entirely inside the range.


As with all operations of this type, the ranges are assumed to include
their extrema.

"""
   result["Range2f"].IntersectWith.im_func.func_doc = """IntersectWith(b) -> Range2f

b : Range2f


Modifies this range to hold its intersection with C{b} and returns the
result.

"""
   result["Range2f"].SetMin.im_func.func_doc = """SetMin(min)

min : Vec2f


Sets the minimum value of the range.

"""
   result["Range2f"].GetSize.im_func.func_doc = """GetSize() -> Vec2f



Returns the size of the range.

"""
   result["Range2f"].SetEmpty.im_func.func_doc = """SetEmpty()



Sets the range to an empty interval.

"""
   result["Range2f"].GetMin.im_func.func_doc = """GetMin() -> Vec2f



Returns the minimum value of the range.

"""
   result["Range2f"].GetMax.im_func.func_doc = """GetMax() -> Vec2f



Returns the maximum value of the range.

"""
   result["Range2f"].UnionWith.im_func.func_doc = """UnionWith(b) -> Range2f

b : Range2f


Extend C{this} to include C{b}.


----------------------------------------------------------------------
UnionWith(b) -> Range2f

b : Vec2f


Extend C{this} to include C{b}.

"""
   result["Range2f"].SetMax.im_func.func_doc = """SetMax(max)

max : Vec2f


Sets the maximum value of the range.

"""
   result["Range2f"].__init__.im_func.func_doc = """__init__()



The default constructor creates an empty range.


----------------------------------------------------------------------
__init__(min, max)

min : Vec2f
max : Vec2f


This constructor initializes the minimum and maximum points.

"""
   result["Range2f"].IsEmpty.im_func.func_doc = """IsEmpty() -> bool



Returns whether the range is empty (max<min).

"""
   result["Range2f"].GetIntersection.func_doc = """**static** GetIntersection(a, b) -> Range2f

a : Range2f
b : Range2f


Returns a C{GfRange2f} that describes the intersection of C{a} and
C{b}.

"""
   result["Range2f"].GetMidpoint.im_func.func_doc = """GetMidpoint() -> Vec2f



Returns the midpoint of the range, that is, 0.5*(min+max).


Note: this returns zero in the case of default-constructed ranges, or
ranges set via SetEmpty() .

"""
   result["Range2f"].GetDistanceSquared.im_func.func_doc = """GetDistanceSquared(p) -> GF_API double

p : Vec2f


Compute the squared distance from a point to the range.

"""
   result["Range2f"].GetQuadrant.im_func.func_doc = """GetQuadrant(i) -> GF_API GfRange2f

i : size_t


Returns the ith quadrant of the range, in the following order: SW, SE,
NW, NE.

"""
   result["Range2f"].GetUnion.func_doc = """**static** GetUnion(a, b) -> Range2f

a : Range2f
b : Range2f


Returns the smallest C{GfRange2f} which contains both C{a} and C{b}.

"""
   result["Vec4h"].__doc__ = """
Basic type for a vector of 4 GfHalf components.


Represents a vector of 4 components of type C{GfHalf}. It is intended
to be fast and simple.

"""
   result["Vec4h"].Normalize.im_func.func_doc = """Normalize(eps) -> Half

eps : Half


Normalizes the vector in place to unit length, returning the length
before normalization.


If the length of the vector is smaller than C{eps}, then the vector is
set to vector/ C{eps}. The original length of the vector is returned.
See also GfNormalize() .

"""
   result["Vec4h"].YAxis.func_doc = """**static** YAxis() -> Vec4h



Create a unit vector along the Y-axis.

"""
   result["Vec4h"].WAxis.func_doc = """**static** WAxis() -> Vec4h



Create a unit vector along the W-axis.

"""
   result["Vec4h"].GetLength.im_func.func_doc = """GetLength() -> Half



Length.

"""
   result["Vec4h"].GetComplement.im_func.func_doc = """GetComplement(b) -> Vec4h

b : Vec4h


Returns the orthogonal complement of C{this->GetProjection(b)} .


That is: ::

  *this - this->GetProjection(b)


"""
   result["Vec4h"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Vec4h

eps : Half

"""
   result["Vec4h"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec4h


----------------------------------------------------------------------
__init__(value)

value : Half


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1, s2, s3)

s0 : Half
s1 : Half
s2 : Half
s3 : Half


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.


----------------------------------------------------------------------
__init__(other)

other : class GfVec4d


Construct from GfVec4d.


----------------------------------------------------------------------
__init__(other)

other : class GfVec4f


Construct from GfVec4f.


----------------------------------------------------------------------
__init__(other)

other : class GfVec4i


Implicitly convert from GfVec4i.

"""
   result["Vec4h"].GetProjection.im_func.func_doc = """GetProjection(v) -> Vec4h

v : Vec4h


Returns the projection of C{this} onto C{v}.


That is: ::

  v * (*this * v)


"""
   result["Vec4h"].ZAxis.func_doc = """**static** ZAxis() -> Vec4h



Create a unit vector along the Z-axis.

"""
   result["Vec4h"].XAxis.func_doc = """**static** XAxis() -> Vec4h



Create a unit vector along the X-axis.

"""
   result["Vec4h"].Axis.func_doc = """**static** Axis(i) -> Vec4h

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 4.

"""
   result["Vec4i"].__doc__ = """
Basic type for a vector of 4 int components.


Represents a vector of 4 components of type C{int}. It is intended to
be fast and simple.

"""
   result["Vec4i"].YAxis.func_doc = """**static** YAxis() -> Vec4i



Create a unit vector along the Y-axis.

"""
   result["Vec4i"].WAxis.func_doc = """**static** WAxis() -> Vec4i



Create a unit vector along the W-axis.

"""
   result["Vec4i"].ZAxis.func_doc = """**static** ZAxis() -> Vec4i



Create a unit vector along the Z-axis.

"""
   result["Vec4i"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec4i


----------------------------------------------------------------------
__init__(value)

value : int


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1, s2, s3)

s0 : int
s1 : int
s2 : int
s3 : int


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.

"""
   result["Vec4i"].XAxis.func_doc = """**static** XAxis() -> Vec4i



Create a unit vector along the X-axis.

"""
   result["Vec4i"].Axis.func_doc = """**static** Axis(i) -> Vec4i

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 4.

"""
   result["MultiInterval"].__doc__ = """
GfMultiInterval represents a subset of the real number line as an
ordered set of non-intersecting GfIntervals.

"""
   result["MultiInterval"].Intersect.im_func.func_doc = """Intersect(i) -> GF_API void

i : Interval


----------------------------------------------------------------------
Intersect(s) -> GF_API void

s : MultiInterval

"""
   result["MultiInterval"].GetFullInterval.func_doc = """**static** GetFullInterval() -> MultiInterval



Returns the full interval (-inf, inf).

"""
   result["MultiInterval"].GetSize.im_func.func_doc = """GetSize() -> GF_API size_t



Returns the number of intervals in the set.

"""
   result["MultiInterval"].GetComplement.im_func.func_doc = """GetComplement() -> GF_API GfMultiInterval



Return the complement of this set.

"""
   result["MultiInterval"].Clear.im_func.func_doc = """Clear() -> GF_API void



Clear the multi-interval.

"""
   result["MultiInterval"].Remove.im_func.func_doc = """Remove(i) -> GF_API void

i : Interval


Remove the given interval from this multi-interval.


----------------------------------------------------------------------
Remove(s) -> GF_API void

s : MultiInterval


Remove the given multi-interval from this multi-interval.

"""
   result["MultiInterval"].ArithmeticAdd.im_func.func_doc = """ArithmeticAdd(i) -> GF_API void

i : Interval


Uses the given interval to extend the multi-interval in the interval
arithmetic sense.

"""
   result["MultiInterval"].IsEmpty.im_func.func_doc = """IsEmpty() -> GF_API bool



Returns true if the multi-interval is empty.

"""
   result["MultiInterval"].__init__.im_func.func_doc = """__init__() -> GF_API



----------------------------------------------------------------------
__init__(s) -> GF_API

s : MultiInterval


Constructs an multi-interval by copying the given set.


----------------------------------------------------------------------
__init__(i) -> GF_API

i : Interval


Constructs an multi-interval with the single given interval.


----------------------------------------------------------------------
__init__(intervals) -> GF_API

intervals : sequence< GfInterval >


Constructs an multi-interval containing the given input intervals.

"""
   result["MultiInterval"].Add.im_func.func_doc = """Add(i) -> GF_API void

i : Interval


Add the given interval to the multi-interval.


----------------------------------------------------------------------
Add(s) -> GF_API void

s : MultiInterval


Add the given multi-interval to the multi-interval.


Sets this object to the union of the two sets.

"""
   result["MultiInterval"].GetBounds.im_func.func_doc = """GetBounds() -> GF_API GfInterval



Returns an interval bounding the entire multi-interval.


Returns an empty interval if the multi-interval is empty.

"""
   result["Quaternion"].Normalize.im_func.func_doc = """Normalize(eps) -> GF_API double

eps : double


Normalizes this quaternion in place to unit length, returning the
length before normalization.


If the length of this quaternion is smaller than C{eps}, this sets the
quaternion to identity.

"""
   result["Quaternion"].GetReal.im_func.func_doc = """GetReal() -> double



Returns the real part of the quaternion.

"""
   result["Quaternion"].__init__.im_func.func_doc = """__init__()



The default constructor leaves the quaternion undefined.


----------------------------------------------------------------------
__init__(realVal)

realVal : int


This constructor initializes the real part to the argument and the
imaginary parts to zero.


Since quaternions typically need to be normalized, the only reasonable
values for C{realVal} are -1, 0, or 1. Other values are legal but are
likely to be meaningless.


----------------------------------------------------------------------
__init__(real, imaginary)

real : double
imaginary : Vec3d


This constructor initializes the real and imaginary parts.

"""
   result["Quaternion"].GetLength.im_func.func_doc = """GetLength() -> GF_API double



Returns geometric length of this quaternion.

"""
   result["Quaternion"].GetIdentity.func_doc = """**static** GetIdentity() -> Quaternion



Returns the identity quaternion, which has a real part of 1 and an
imaginary part of (0,0,0).

"""
   result["Quaternion"].GetInverse.im_func.func_doc = """GetInverse() -> GF_API GfQuaternion



Returns the inverse of this quaternion.

"""
   result["Quaternion"].GetImaginary.im_func.func_doc = """GetImaginary() -> Vec3d



Returns the imaginary part of the quaternion.

"""
   result["Quaternion"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> GF_API GfQuaternion

eps : double


Returns a normalized (unit-length) version of this quaternion.


direction as this. If the length of this quaternion is smaller than
C{eps}, this returns the identity quaternion.

"""
   result["Vec4d"].__doc__ = """
Basic type for a vector of 4 double components.


Represents a vector of 4 components of type C{double}. It is intended
to be fast and simple.

"""
   result["Vec4d"].Normalize.im_func.func_doc = """Normalize(eps) -> double

eps : double


Normalizes the vector in place to unit length, returning the length
before normalization.


If the length of the vector is smaller than C{eps}, then the vector is
set to vector/ C{eps}. The original length of the vector is returned.
See also GfNormalize() .

"""
   result["Vec4d"].YAxis.func_doc = """**static** YAxis() -> Vec4d



Create a unit vector along the Y-axis.

"""
   result["Vec4d"].WAxis.func_doc = """**static** WAxis() -> Vec4d



Create a unit vector along the W-axis.

"""
   result["Vec4d"].GetLength.im_func.func_doc = """GetLength() -> double



Length.

"""
   result["Vec4d"].ZAxis.func_doc = """**static** ZAxis() -> Vec4d



Create a unit vector along the Z-axis.

"""
   result["Vec4d"].GetComplement.im_func.func_doc = """GetComplement(b) -> Vec4d

b : Vec4d


Returns the orthogonal complement of C{this->GetProjection(b)} .


That is: ::

  *this - this->GetProjection(b)


"""
   result["Vec4d"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Vec4d

eps : double

"""
   result["Vec4d"].GetProjection.im_func.func_doc = """GetProjection(v) -> Vec4d

v : Vec4d


Returns the projection of C{this} onto C{v}.


That is: ::

  v * (*this * v)


"""
   result["Vec4d"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec4d


----------------------------------------------------------------------
__init__(value)

value : double


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1, s2, s3)

s0 : double
s1 : double
s2 : double
s3 : double


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.


----------------------------------------------------------------------
__init__(other)

other : class GfVec4f


Implicitly convert from GfVec4f.


----------------------------------------------------------------------
__init__(other)

other : class GfVec4h


Implicitly convert from GfVec4h.


----------------------------------------------------------------------
__init__(other)

other : class GfVec4i


Implicitly convert from GfVec4i.

"""
   result["Vec4d"].XAxis.func_doc = """**static** XAxis() -> Vec4d



Create a unit vector along the X-axis.

"""
   result["Vec4d"].Axis.func_doc = """**static** Axis(i) -> Vec4d

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 4.

"""
   result["Vec4f"].__doc__ = """
Basic type for a vector of 4 float components.


Represents a vector of 4 components of type C{float}. It is intended
to be fast and simple.

"""
   result["Vec4f"].Normalize.im_func.func_doc = """Normalize(eps) -> float

eps : float


Normalizes the vector in place to unit length, returning the length
before normalization.


If the length of the vector is smaller than C{eps}, then the vector is
set to vector/ C{eps}. The original length of the vector is returned.
See also GfNormalize() .

"""
   result["Vec4f"].YAxis.func_doc = """**static** YAxis() -> Vec4f



Create a unit vector along the Y-axis.

"""
   result["Vec4f"].WAxis.func_doc = """**static** WAxis() -> Vec4f



Create a unit vector along the W-axis.

"""
   result["Vec4f"].GetLength.im_func.func_doc = """GetLength() -> float



Length.

"""
   result["Vec4f"].ZAxis.func_doc = """**static** ZAxis() -> Vec4f



Create a unit vector along the Z-axis.

"""
   result["Vec4f"].GetComplement.im_func.func_doc = """GetComplement(b) -> Vec4f

b : Vec4f


Returns the orthogonal complement of C{this->GetProjection(b)} .


That is: ::

  *this - this->GetProjection(b)


"""
   result["Vec4f"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Vec4f

eps : float

"""
   result["Vec4f"].GetProjection.im_func.func_doc = """GetProjection(v) -> Vec4f

v : Vec4f


Returns the projection of C{this} onto C{v}.


That is: ::

  v * (*this * v)


"""
   result["Vec4f"].__init__.im_func.func_doc = """__init__()



Default constructor does no initialization.


----------------------------------------------------------------------
__init__(other)

other : Vec4f


----------------------------------------------------------------------
__init__(value)

value : float


Initialize all elements to a single value.


----------------------------------------------------------------------
__init__(s0, s1, s2, s3)

s0 : float
s1 : float
s2 : float
s3 : float


Initialize all elements with explicit arguments.


----------------------------------------------------------------------
__init__(p)

p : Scl


Construct with pointer to values.


----------------------------------------------------------------------
__init__(other)

other : class GfVec4d


Construct from GfVec4d.


----------------------------------------------------------------------
__init__(other)

other : class GfVec4h


Implicitly convert from GfVec4h.


----------------------------------------------------------------------
__init__(other)

other : class GfVec4i


Implicitly convert from GfVec4i.

"""
   result["Vec4f"].XAxis.func_doc = """**static** XAxis() -> Vec4f



Create a unit vector along the X-axis.

"""
   result["Vec4f"].Axis.func_doc = """**static** Axis(i) -> Vec4f

i : size_t


Create a unit vector along the i-th axis, zero-based.


Return the zero vector if C{i} is greater than or equal to 4.

"""
   result["Quatd"].__doc__ = """
Basic type: a quaternion, a complex number with a real coefficient and
three imaginary coefficients, stored as a 3-vector.

"""
   result["Quatd"].Normalize.im_func.func_doc = """Normalize(eps) -> GF_API double

eps : double


Normalizes this quaternion in place to unit length, returning the
length before normalization.


If the length of this quaternion is smaller than C{eps}, this sets the
quaternion to identity.

"""
   result["Quatd"].GetReal.im_func.func_doc = """GetReal() -> double



Return the real coefficient.

"""
   result["Quatd"].SetReal.im_func.func_doc = """SetReal(real)

real : double


Set the real coefficient.

"""
   result["Quatd"].GetLength.im_func.func_doc = """GetLength() -> double



Return geometric length of this quaternion.

"""
   result["Quatd"].__init__.im_func.func_doc = """__init__()



Default constructor leaves the quaternion undefined.


----------------------------------------------------------------------
__init__(realVal)

realVal : double


Initialize the real coefficient to C{realVal} and the imaginary
coefficients to zero.


Since quaternions typically must be normalized, reasonable values for
C{realVal} are -1, 0, or 1. Other values are legal but are likely to
be meaningless.


----------------------------------------------------------------------
__init__(real, i, j, k)

real : double
i : double
j : double
k : double


Initialize the real and imaginary coefficients.


----------------------------------------------------------------------
__init__(real, imaginary)

real : double
imaginary : Vec3d


Initialize the real and imaginary coefficients.


----------------------------------------------------------------------
__init__(other) -> GF_API

other : class GfQuatf


Implicitly convert from GfQuatf.


----------------------------------------------------------------------
__init__(other) -> GF_API

other : class GfQuath


Implicitly convert from GfQuath.

"""
   result["Quatd"].GetConjugate.im_func.func_doc = """GetConjugate() -> Quatd



Return this quaternion's conjugate, which is the quaternion with the
same real coefficient and negated imaginary coefficients.

"""
   result["Quatd"].GetIdentity.func_doc = """**static** GetIdentity() -> Quatd



Return the identity quaternion, with real coefficient 1 and an
imaginary coefficients all zero.

"""
   result["Quatd"].GetInverse.im_func.func_doc = """GetInverse() -> Quatd



Return this quaternion's inverse, or reciprocal.


This is the quaternion's conjugate divided by it's squared length.

"""
   result["Quatd"].GetImaginary.im_func.func_doc = """GetImaginary() -> Vec3d



Return the imaginary coefficient.

"""
   result["Quatd"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Quatd

eps : double


length of this quaternion is smaller than C{eps}, return the identity
quaternion.

"""
   result["Quatd"].SetImaginary.im_func.func_doc = """SetImaginary(imaginary)

imaginary : Vec3d


Set the imaginary coefficients.


----------------------------------------------------------------------
SetImaginary(i, j, k)

i : double
j : double
k : double


Set the imaginary coefficients.

"""
   result["Rotation"].SetRotateInto.im_func.func_doc = """SetRotateInto(rotateFrom, rotateTo) -> GF_API GfRotation

rotateFrom : Vec3d
rotateTo : Vec3d


Sets the rotation to one that brings the C{rotateFrom} vector to align
with C{rotateTo}.


The passed vectors need not be unit length.

"""
   result["Rotation"].GetAngle.im_func.func_doc = """GetAngle() -> double



Returns the rotation angle in degrees.

"""
   result["Rotation"].GetQuat.im_func.func_doc = """GetQuat() -> GF_API GfQuatd



Returns the rotation expressed as a quaternion.

"""
   result["Rotation"].GetAxis.im_func.func_doc = """GetAxis() -> Vec3d



Returns the axis of rotation.

"""
   result["Rotation"].SetQuat.im_func.func_doc = """SetQuat(quat) -> GF_API GfRotation

quat : Quatd


Sets the rotation from a quaternion.


Note that this method accepts GfQuatf and GfQuath since they
implicitly convert to GfQuatd.

"""
   result["Rotation"].RotateOntoProjected.func_doc = """**static** RotateOntoProjected(v1, v2, axis) -> GF_API GfRotation

v1 : Vec3d
v2 : Vec3d
axis : Vec3d

"""
   result["Rotation"].TransformDir.im_func.func_doc = """TransformDir(vec) -> GF_API GfVec3f

vec : Vec3f


Transforms row vector C{vec} by the rotation, returning the result.


----------------------------------------------------------------------
TransformDir(vec) -> GF_API GfVec3d

vec : Vec3d


This is an overloaded member function, provided for convenience. It
differs from the above function only in what argument(s) it accepts.

"""
   result["Rotation"].GetQuaternion.im_func.func_doc = """GetQuaternion() -> Quaternion



Returns the rotation expressed as a quaternion.

"""
   result["Rotation"].__init__.im_func.func_doc = """__init__()



The default constructor leaves the rotation undefined.


----------------------------------------------------------------------
__init__(axis, angle)

axis : Vec3d
angle : double


This constructor initializes the rotation to be C{angle} degrees about
C{axis}.


----------------------------------------------------------------------
__init__(quaternion)

quaternion : Quaternion


This constructor initializes the rotation from a quaternion.


----------------------------------------------------------------------
__init__(quat)

quat : Quatd


This constructor initializes the rotation from a quaternion.


Note that this constructor accepts GfQuatf and GfQuath since they
implicitly convert to GfQuatd.


----------------------------------------------------------------------
__init__(rotateFrom, rotateTo) -> GF_API

rotateFrom : Vec3d
rotateTo : Vec3d


This constructor initializes the rotation to one that brings the
C{rotateFrom} vector to align with C{rotateTo}.


The passed vectors need not be unit length.

"""
   result["Rotation"].DecomposeRotation.func_doc = """**static** DecomposeRotation(rot, TwAxis, FBAxis, LRAxis, handedness, thetaTw, thetaFB, thetaLR, thetaSw, useHint, swShift) -> GF_API void

rot : Matrix4d
TwAxis : Vec3d
FBAxis : Vec3d
LRAxis : Vec3d
handedness : double
thetaTw : double
thetaFB : double
thetaLR : double
thetaSw : double
useHint : bool
swShift : double

"""
   result["Rotation"].SetQuaternion.im_func.func_doc = """SetQuaternion(quat) -> Rotation

quat : Quaternion


Sets the rotation from a quaternion.

"""
   result["Rotation"].SetAxisAngle.im_func.func_doc = """SetAxisAngle(axis, angle) -> Rotation

axis : Vec3d
angle : double


Sets the rotation to be C{angle} degrees about C{axis}.

"""
   result["Rotation"].GetInverse.im_func.func_doc = """GetInverse() -> Rotation



Returns the inverse of this rotation.

"""
   result["Rotation"].SetIdentity.im_func.func_doc = """SetIdentity() -> Rotation



Sets the rotation to an identity rotation.


(This is chosen to be 0 degrees around the positive X axis.)

"""
   result["Rotation"].Decompose.im_func.func_doc = """Decompose(axis0, axis1, axis2) -> GF_API GfVec3d

axis0 : Vec3d
axis1 : Vec3d
axis2 : Vec3d


Decompose rotation about 3 orthogonal axes.


If the axes are not orthogonal, warnings will be spewed.

"""
   result["BBox3d"].ComputeAlignedBox.im_func.func_doc = """ComputeAlignedBox() -> Range3d



Returns the axis-aligned range (as a C{GfRange3d}) that results from
applying the transformation matrix to the axis-aligned box and
aligning the result.


This synonym for C{ComputeAlignedRange} exists for compatibility
purposes.

"""
   result["BBox3d"].HasZeroAreaPrimitives.im_func.func_doc = """HasZeroAreaPrimitives() -> bool



Returns the current state of the zero-area primitives flag".

"""
   result["BBox3d"].Set.im_func.func_doc = """Set(box, matrix)

box : Range3d
matrix : Matrix4d


Sets the axis-aligned box and transformation matrix.

"""
   result["BBox3d"].GetInverseMatrix.im_func.func_doc = """GetInverseMatrix() -> Matrix4d



Returns the inverse of the transformation matrix.


This will be the identity matrix if the transformation matrix is not
invertible.

"""
   result["BBox3d"].SetMatrix.im_func.func_doc = """SetMatrix(matrix)

matrix : Matrix4d


Sets the transformation matrix only.


The axis-aligned box is not modified.

"""
   result["BBox3d"].Transform.im_func.func_doc = """Transform(matrix)

matrix : Matrix4d


Transforms the bounding box by the given matrix, which is assumed to
be a global transformation to apply to the box.


Therefore, this just post-multiplies the box's matrix by C{matrix}.

"""
   result["BBox3d"].SetHasZeroAreaPrimitives.im_func.func_doc = """SetHasZeroAreaPrimitives(hasThem)

hasThem : bool


Sets the zero-area primitives flag to the given value.

"""
   result["BBox3d"].GetBox.im_func.func_doc = """GetBox() -> Range3d



Returns the range of the axis-aligned untransformed box.


This synonym of C{GetRange} exists for compatibility purposes.

"""
   result["BBox3d"].GetRange.im_func.func_doc = """GetRange() -> Range3d



Returns the range of the axis-aligned untransformed box.

"""
   result["BBox3d"].ComputeCentroid.im_func.func_doc = """ComputeCentroid() -> GF_API GfVec3d



Returns the centroid of the bounding box.


The centroid is computed as the transformed centroid of the range.

"""
   result["BBox3d"].Combine.func_doc = """**static** Combine(b1, b2) -> GF_API GfBBox3d

b1 : BBox3d
b2 : BBox3d


Combines two bboxes, returning a new bbox that contains both.


This uses the coordinate space of one of the two original boxes as the
space of the result; it uses the one that produces whe smaller of the
two resulting boxes.

"""
   result["BBox3d"].GetVolume.im_func.func_doc = """GetVolume() -> GF_API double



Returns the volume of the box (0 for an empty box).

"""
   result["BBox3d"].ComputeAlignedRange.im_func.func_doc = """ComputeAlignedRange() -> GF_API GfRange3d



Returns the axis-aligned range (as a C{GfRange3d}) that wesults from
applying the transformation matrix to the wxis-aligned box and
aligning the result.

"""
   result["BBox3d"].__init__.im_func.func_doc = """__init__()



The default constructor leaves the box empty, the transformation
matrix identity, and the zero-area primitives flag" C{false}.


----------------------------------------------------------------------
__init__(rhs)

rhs : BBox3d


Copy constructor.


----------------------------------------------------------------------
__init__(box)

box : Range3d


This constructor takes a box and sets the matrix to identity.


----------------------------------------------------------------------
__init__(box, matrix)

box : Range3d
matrix : Matrix4d


This constructor takes a box and a transformation matrix.

"""
   result["BBox3d"].GetMatrix.im_func.func_doc = """GetMatrix() -> Matrix4d



Returns the transformation matrix.

"""
   result["BBox3d"].SetRange.im_func.func_doc = """SetRange(box)

box : Range3d


Sets the range of the axis-aligned box only.


The transformation matrix is not modified.

"""
   result["Quath"].__doc__ = """
Basic type: a quaternion, a complex number with a real coefficient and
three imaginary coefficients, stored as a 3-vector.

"""
   result["Quath"].Normalize.im_func.func_doc = """Normalize(eps) -> GF_API GfHalf

eps : Half


Normalizes this quaternion in place to unit length, returning the
length before normalization.


If the length of this quaternion is smaller than C{eps}, this sets the
quaternion to identity.

"""
   result["Quath"].GetReal.im_func.func_doc = """GetReal() -> Half



Return the real coefficient.

"""
   result["Quath"].SetReal.im_func.func_doc = """SetReal(real)

real : Half


Set the real coefficient.

"""
   result["Quath"].GetLength.im_func.func_doc = """GetLength() -> Half



Return geometric length of this quaternion.

"""
   result["Quath"].GetConjugate.im_func.func_doc = """GetConjugate() -> Quath



Return this quaternion's conjugate, which is the quaternion with the
same real coefficient and negated imaginary coefficients.

"""
   result["Quath"].GetIdentity.func_doc = """**static** GetIdentity() -> Quath



Return the identity quaternion, with real coefficient 1 and an
imaginary coefficients all zero.

"""
   result["Quath"].GetInverse.im_func.func_doc = """GetInverse() -> Quath



Return this quaternion's inverse, or reciprocal.


This is the quaternion's conjugate divided by it's squared length.

"""
   result["Quath"].GetImaginary.im_func.func_doc = """GetImaginary() -> Vec3h



Return the imaginary coefficient.

"""
   result["Quath"].__init__.im_func.func_doc = """__init__()



Default constructor leaves the quaternion undefined.


----------------------------------------------------------------------
__init__(realVal)

realVal : Half


Initialize the real coefficient to C{realVal} and the imaginary
coefficients to zero.


Since quaternions typically must be normalized, reasonable values for
C{realVal} are -1, 0, or 1. Other values are legal but are likely to
be meaningless.


----------------------------------------------------------------------
__init__(real, i, j, k)

real : Half
i : Half
j : Half
k : Half


Initialize the real and imaginary coefficients.


----------------------------------------------------------------------
__init__(real, imaginary)

real : Half
imaginary : Vec3h


Initialize the real and imaginary coefficients.


----------------------------------------------------------------------
__init__(other) -> GF_API

other : class GfQuatd


Construct from GfQuatd.


----------------------------------------------------------------------
__init__(other) -> GF_API

other : class GfQuatf


Construct from GfQuatf.

"""
   result["Quath"].GetNormalized.im_func.func_doc = """GetNormalized(eps) -> Quath

eps : Half


length of this quaternion is smaller than C{eps}, return the identity
quaternion.

"""
   result["Quath"].SetImaginary.im_func.func_doc = """SetImaginary(imaginary)

imaginary : Vec3h


Set the imaginary coefficients.


----------------------------------------------------------------------
SetImaginary(i, j, k)

i : Half
j : Half
k : Half


Set the imaginary coefficients.

"""
   result["ApplyGamma"].func_doc = """ApplyGamma(v, gamma) -> GF_API GfVec3f

v : Vec3f
gamma : double


Return a new vector with each component of C{v} raised to the power
C{gamma}.


----------------------------------------------------------------------
ApplyGamma(v, gamma) -> GF_API GfVec3d

v : Vec3d
gamma : double


Return a new vector with each component of C{v} raised to the power
C{gamma}.


----------------------------------------------------------------------
ApplyGamma(v, gamma) -> GF_API GfVec3h

v : Vec3h
gamma : double


----------------------------------------------------------------------
ApplyGamma(v, gamma) -> GF_API GfVec4f

v : Vec4f
gamma : double


Return a new vector with the first three components of C{v} raised to
the power C{gamma} and the fourth component unchanged.


----------------------------------------------------------------------
ApplyGamma(v, gamma) -> GF_API GfVec4d

v : Vec4d
gamma : double


Return a new vector with the first three components of C{v} raised to
the power C{gamma} and the fourth component unchanged.


----------------------------------------------------------------------
ApplyGamma(v, gamma) -> GF_API GfVec4h

v : Vec4h
gamma : double

"""
   result["Max"].func_doc = """Max(a1, a2) -> T

a1 : T
a2 : T


Returns the largest of the given C{values}.


----------------------------------------------------------------------
Max(a1, a2, a3) -> T

a1 : T
a2 : T
a3 : T


----------------------------------------------------------------------
Max(a1, a2, a3, a4) -> T

a1 : T
a2 : T
a3 : T
a4 : T


----------------------------------------------------------------------
Max(a1, a2, a3, a4, a5) -> T

a1 : T
a2 : T
a3 : T
a4 : T
a5 : T


----------------------------------------------------------------------
Max(a1, a2) -> T

a1 : T
a2 : T


Returns the largest of the given C{values}.

"""
   result["Transform"].__doc__ = """
Basic type: Compound linear transformation.


This class represents a linear transformation specified as a series of
individual components: a *translation*, a *rotation*, a *scale*, a
*pivotPosition*, and a *pivotOrientation*. When applied to a point,
the point will be transformed as follows (in order):

   - Scaled by the *scale* with respect to *pivotPosition* and the
     orientation specified by the *pivotOrientation*.

   - Rotated by the *rotation* about *pivotPosition*.

   - Translated by *Translation*
     That is, the cumulative matrix that this represents looks like this.
     ::

  M = -P * - O * S * O * R * P * T

where
   - *T* is the *translation* matrix

   - *P* is the matrix that translates by *pivotPosition*

   - *R* is the *rotation* matrix

   - *O* is the matrix that rotates to *pivotOrientation*

   - *S* is the *scale* matrix


"""
   result["Transform"].SetMatrix.im_func.func_doc = """SetMatrix(m) -> GF_API GfTransform

m : Matrix4d


Sets the transform components to implement the transformation
represented by matrix C{m}, ignoring any projection.


This tries to leave the current center unchanged.

"""
   result["Transform"].GetPivotOrientation.im_func.func_doc = """GetPivotOrientation() -> Rotation



Returns the pivot orientation component.

"""
   result["Transform"].SetScale.im_func.func_doc = """SetScale(scale)

scale : Vec3d


Sets the scale component, leaving all others untouched.

"""
   result["Transform"].GetTranslation.im_func.func_doc = """GetTranslation() -> Vec3d



Returns the translation component.

"""
   result["Transform"].GetRotation.im_func.func_doc = """GetRotation() -> Rotation



Returns the rotation component.

"""
   result["Transform"].SetPivotPosition.im_func.func_doc = """SetPivotPosition(pivPos)

pivPos : Vec3d


Sets the pivot position component, leaving all others untouched.

"""
   result["Transform"].GetPivotPosition.im_func.func_doc = """GetPivotPosition() -> Vec3d



Returns the pivot position component.

"""
   result["Transform"].SetRotation.im_func.func_doc = """SetRotation(rotation)

rotation : Rotation


Sets the rotation component, leaving all others untouched.

"""
   result["Transform"].SetIdentity.im_func.func_doc = """SetIdentity() -> GF_API GfTransform



Sets the transformation to the identity transformation.

"""
   result["Transform"].SetTranslation.im_func.func_doc = """SetTranslation(translation)

translation : Vec3d


Sets the translation component, leaving all others untouched.

"""
   result["Transform"].SetPivotOrientation.im_func.func_doc = """SetPivotOrientation(pivotOrient)

pivotOrient : Rotation


Sets the pivot orientation component, leaving all others untouched.

"""
   result["Transform"].GetScale.im_func.func_doc = """GetScale() -> Vec3d



Returns the scale component.

"""
   result["Transform"].GetMatrix.im_func.func_doc = """GetMatrix() -> GF_API GfMatrix4d



Returns a C{GfMatrix4d} that implements the cumulative transformation.

"""
   result["Min"].func_doc = """Min(a1, a2) -> T

a1 : T
a2 : T


Returns the smallest of the given C{values}.


----------------------------------------------------------------------
Min(a1, a2, a3) -> T

a1 : T
a2 : T
a3 : T


----------------------------------------------------------------------
Min(a1, a2, a3, a4) -> T

a1 : T
a2 : T
a3 : T
a4 : T


----------------------------------------------------------------------
Min(a1, a2, a3, a4, a5) -> T

a1 : T
a2 : T
a3 : T
a4 : T
a5 : T


----------------------------------------------------------------------
Min(a1, a2) -> T

a1 : T
a2 : T


Returns the smallest of the given C{values}.

"""
   result["ConvertDisplayToLinear"].func_doc = """ConvertDisplayToLinear(v) -> GF_API GfVec3f

v : Vec3f


Given a vec, C{v}, representing an RGB(A) color in the system's
display gamma space, return an energy-linear vec of the same type.


----------------------------------------------------------------------
ConvertDisplayToLinear(v) -> GF_API GfVec3d

v : Vec3d


----------------------------------------------------------------------
ConvertDisplayToLinear(v) -> GF_API GfVec3h

v : Vec3h


----------------------------------------------------------------------
ConvertDisplayToLinear(v) -> GF_API GfVec4f

v : Vec4f


----------------------------------------------------------------------
ConvertDisplayToLinear(v) -> GF_API GfVec4d

v : Vec4d


----------------------------------------------------------------------
ConvertDisplayToLinear(v) -> GF_API GfVec4h

v : Vec4h

"""
   result["Line"].Set.im_func.func_doc = """Set(p0, dir) -> double

p0 : Vec3d
dir : Vec3d

"""
   result["Line"].__init__.im_func.func_doc = """__init__()



The default constructor leaves line parameters undefined.


----------------------------------------------------------------------
__init__(p0, dir)

p0 : Vec3d
dir : Vec3d


Construct a line from a point and a direction.

"""
   result["Line"].GetPoint.im_func.func_doc = """GetPoint(t) -> Vec3d

t : double


Return the point on the line at C{} ( p0 + t * dir).


Remember dir has been normalized so t represents a unit distance.

"""
   result["Line"].GetDirection.im_func.func_doc = """GetDirection() -> Vec3d



Return the normalized direction of the line.

"""
   result["Line"].FindClosestPoint.im_func.func_doc = """FindClosestPoint(point, t) -> GF_API GfVec3d

point : Vec3d
t : double


Returns the point on the line that is closest to C{point}.


If C{t} is not C{None}, it will be set to the parametric distance
along the line of the returned point.

"""
   result["LineSeg"].GetLength.im_func.func_doc = """GetLength() -> double



Return the length of the line.

"""
   result["LineSeg"].GetPoint.im_func.func_doc = """GetPoint(t) -> Vec3d

t : double


Return the point on the segment specified by the parameter t.


p = p0 + t * (p1 - p0)

"""
   result["LineSeg"].__init__.im_func.func_doc = """__init__()



The default constructor leaves line parameters undefined.


----------------------------------------------------------------------
__init__(p0, p1)

p0 : Vec3d
p1 : Vec3d


Construct a line segment that spans two points.

"""
   result["LineSeg"].GetDirection.im_func.func_doc = """GetDirection() -> Vec3d



Return the normalized direction of the line.

"""
   result["LineSeg"].FindClosestPoint.im_func.func_doc = """FindClosestPoint(point, t) -> GF_API GfVec3d

point : Vec3d
t : double


Returns the point on the line that is closest to C{point}.


If C{t} is not C{None}, it will be set to the parametric distance
along the line of the closest point.

"""
   result["GetDisplayGamma"].func_doc = """GetDisplayGamma() -> GF_API double



Return the system display gamma.

"""
   result["GetComplement"].func_doc = """GetComplement(a, b) -> Vec2d

a : Vec2d
b : Vec2d


Returns the orthogonal complement of C{a.GetProjection(b)} .


That is: ::

  a - a.GetProjection(b)



----------------------------------------------------------------------
GetComplement(a, b) -> Vec2f

a : Vec2f
b : Vec2f


Returns the orthogonal complement of C{a.GetProjection(b)} .


That is: ::

  a - a.GetProjection(b)



----------------------------------------------------------------------
GetComplement(a, b) -> Vec2h

a : Vec2h
b : Vec2h


Returns the orthogonal complement of C{a.GetProjection(b)} .


That is: ::

  a - a.GetProjection(b)



----------------------------------------------------------------------
GetComplement(a, b) -> Vec3d

a : Vec3d
b : Vec3d


Returns the orthogonal complement of C{a.GetProjection(b)} .


That is: ::

  a - a.GetProjection(b)



----------------------------------------------------------------------
GetComplement(a, b) -> Vec3f

a : Vec3f
b : Vec3f


Returns the orthogonal complement of C{a.GetProjection(b)} .


That is: ::

  a - a.GetProjection(b)



----------------------------------------------------------------------
GetComplement(a, b) -> Vec3h

a : Vec3h
b : Vec3h


Returns the orthogonal complement of C{a.GetProjection(b)} .


That is: ::

  a - a.GetProjection(b)



----------------------------------------------------------------------
GetComplement(a, b) -> Vec4d

a : Vec4d
b : Vec4d


Returns the orthogonal complement of C{a.GetProjection(b)} .


That is: ::

  a - a.GetProjection(b)



----------------------------------------------------------------------
GetComplement(a, b) -> Vec4f

a : Vec4f
b : Vec4f


Returns the orthogonal complement of C{a.GetProjection(b)} .


That is: ::

  a - a.GetProjection(b)



----------------------------------------------------------------------
GetComplement(a, b) -> Vec4h

a : Vec4h
b : Vec4h


Returns the orthogonal complement of C{a.GetProjection(b)} .


That is: ::

  a - a.GetProjection(b)


"""
   result["Cross"].func_doc = """Cross(v1, v2) -> Vec3d

v1 : Vec3d
v2 : Vec3d


Returns the cross product of C{v1} and C{v2}.


----------------------------------------------------------------------
Cross(v1, v2) -> Vec3f

v1 : Vec3f
v2 : Vec3f


Returns the cross product of C{v1} and C{v2}.


----------------------------------------------------------------------
Cross(v1, v2) -> Vec3h

v1 : Vec3h
v2 : Vec3h


Returns the cross product of C{v1} and C{v2}.

"""
   result["GetProjection"].func_doc = """GetProjection(a, b) -> Vec2d

a : Vec2d
b : Vec2d


Returns the projection of C{a} onto C{b}.


That is: ::

  b * (a * b)



----------------------------------------------------------------------
GetProjection(a, b) -> Vec2f

a : Vec2f
b : Vec2f


Returns the projection of C{a} onto C{b}.


That is: ::

  b * (a * b)



----------------------------------------------------------------------
GetProjection(a, b) -> Vec2h

a : Vec2h
b : Vec2h


Returns the projection of C{a} onto C{b}.


That is: ::

  b * (a * b)



----------------------------------------------------------------------
GetProjection(a, b) -> Vec3d

a : Vec3d
b : Vec3d


Returns the projection of C{a} onto C{b}.


That is: ::

  b * (a * b)



----------------------------------------------------------------------
GetProjection(a, b) -> Vec3f

a : Vec3f
b : Vec3f


Returns the projection of C{a} onto C{b}.


That is: ::

  b * (a * b)



----------------------------------------------------------------------
GetProjection(a, b) -> Vec3h

a : Vec3h
b : Vec3h


Returns the projection of C{a} onto C{b}.


That is: ::

  b * (a * b)



----------------------------------------------------------------------
GetProjection(a, b) -> Vec4d

a : Vec4d
b : Vec4d


Returns the projection of C{a} onto C{b}.


That is: ::

  b * (a * b)



----------------------------------------------------------------------
GetProjection(a, b) -> Vec4f

a : Vec4f
b : Vec4f


Returns the projection of C{a} onto C{b}.


That is: ::

  b * (a * b)



----------------------------------------------------------------------
GetProjection(a, b) -> Vec4h

a : Vec4h
b : Vec4h


Returns the projection of C{a} onto C{b}.


That is: ::

  b * (a * b)


"""
   result["Camera"].fStop = property(result["Camera"].fStop.fget, result["Camera"].fStop.fset, result["Camera"].fStop.fdel, """type : GF_API float


Returns the lens aperture.

----------------------------------------------------------------------type : GF_API void


Sets the lens aperture, unitless.

""")
   result["Camera"].focusDistance = property(result["Camera"].focusDistance.fget, result["Camera"].focusDistance.fset, result["Camera"].focusDistance.fdel, """type : GF_API float


Returns the focus distance in world units.

----------------------------------------------------------------------type : GF_API void


Sets the focus distance in world units.

""")
   result["Camera"].projection = property(result["Camera"].projection.fget, result["Camera"].projection.fset, result["Camera"].projection.fdel, """type : GF_API Projection


Returns the projection type.

----------------------------------------------------------------------type : GF_API void


Sets the projection type.

""")
   result["Camera"].verticalAperture = property(result["Camera"].verticalAperture.fget, result["Camera"].verticalAperture.fset, result["Camera"].verticalAperture.fdel, """type : GF_API void


Sets the height of the projector aperture in tenths of a world unit
(e.g., mm if the world unit is assumed to be cm).

----------------------------------------------------------------------type : GF_API float


Returns the height of the projector aperture in tenths of a world unit
(e.g., mm if the world unit is assumed to be cm).

""")
   result["Camera"].clippingPlanes = property(result["Camera"].clippingPlanes.fget, result["Camera"].clippingPlanes.fset, result["Camera"].clippingPlanes.fdel, """type : GF_API  sequence< GfVec4f >


Returns additional clipping planes.

----------------------------------------------------------------------type : GF_API void


Sets additional arbitrarily oriented clipping planes.


A vector (a,b,c,d) encodes a clipping plane that clips off points
(x,y,z) with a * x + b * y + c * z + d * 1<0

where (x,y,z) are the coordinates in the camera's space.

""")
   result["Quaternion"].real = property(result["Quaternion"].real.fget, result["Quaternion"].real.fset, result["Quaternion"].real.fdel, """
Sets the real part of the quaternion.

""")
   result["Camera"].aspectRatio = property(result["Camera"].aspectRatio.fget, result["Camera"].aspectRatio.fset, result["Camera"].aspectRatio.fdel, """type : GF_API float


Returns the projector aperture aspect ratio.

""")
   result["Quaternion"].imaginary = property(result["Quaternion"].imaginary.fget, result["Quaternion"].imaginary.fset, result["Quaternion"].imaginary.fdel, """
Sets the imaginary part of the quaternion.

""")
   result["Ray"].startPoint = property(result["Ray"].startPoint.fget, result["Ray"].startPoint.fset, result["Ray"].startPoint.fdel, """type : Vec3d


Returns the starting point of the segment.

""")
   result["Camera"].frustum = property(result["Camera"].frustum.fget, result["Camera"].frustum.fset, result["Camera"].frustum.fdel, """type : GF_API GfFrustum


Returns the computed, world-space camera frustum.


The frustum will always be that of a Y-up, -Z-looking camera.

""")
   result["Camera"].focalLength = property(result["Camera"].focalLength.fget, result["Camera"].focalLength.fset, result["Camera"].focalLength.fdel, """type : GF_API float


Returns the focal length in tenths of a world unit (e.g., mm if the
world unit is assumed to be cm).

----------------------------------------------------------------------type : GF_API void


These are the values actually stored in the class and they correspond
to measurements of an actual physical camera (in mm).


Together with the clipping range, they determine the camera frustum.
Sets the focal length in tenths of a world unit (e.g., mm if the world
unit is assumed to be cm).

""")
   result["Camera"].horizontalAperture = property(result["Camera"].horizontalAperture.fget, result["Camera"].horizontalAperture.fset, result["Camera"].horizontalAperture.fdel, """type : GF_API float


Returns the width of the projector aperture in tenths of a world unit
(e.g., mm if the world unit is assumed to be cm).

----------------------------------------------------------------------type : GF_API void


Sets the width of the projector aperture in tenths of a world unit
(e.g., mm if the world unit is assumed to be cm).

""")
   result["Camera"].clippingRange = property(result["Camera"].clippingRange.fget, result["Camera"].clippingRange.fset, result["Camera"].clippingRange.fdel, """type : GF_API GfRange1f


Returns the clipping range in world units.

----------------------------------------------------------------------type : GF_API void


Sets the clipping range in world units.

""")
   result["Camera"].transform = property(result["Camera"].transform.fget, result["Camera"].transform.fset, result["Camera"].transform.fdel, """type : GF_API GfMatrix4d


Returns the transform of the filmback in world space.


This is exactly the transform specified via SetTransform() .

----------------------------------------------------------------------type : GF_API void


Sets the transform of the filmback in world space to C{val}.

""")
   result["Camera"].horizontalApertureOffset = property(result["Camera"].horizontalApertureOffset.fget, result["Camera"].horizontalApertureOffset.fset, result["Camera"].horizontalApertureOffset.fdel, """type : GF_API float


Returns the horizontal offset of the projector aperture in tenths of a
world unit (e.g., mm if the world unit is assumed to be cm).


In particular, an offset is necessary when writing out a stereo camera
with finite convergence distance as two cameras.

----------------------------------------------------------------------type : GF_API void


Sets the horizontal offset of the projector aperture in tenths of a
world unit (e.g., mm if the world unit is assumed to be cm).

""")
   result["Camera"].verticalApertureOffset = property(result["Camera"].verticalApertureOffset.fget, result["Camera"].verticalApertureOffset.fset, result["Camera"].verticalApertureOffset.fdel, """type : GF_API void


Sets the vertical offset of the projector aperture in tenths of a
world unit (e.g., mm if the world unit is assumed to be cm).

----------------------------------------------------------------------type : GF_API float


Returns the vertical offset of the projector aperture in tenths of a
world unit (e.g., mm if the world unit is assumed to be cm).

""")
   result["Ray"].direction = property(result["Ray"].direction.fget, result["Ray"].direction.fset, result["Ray"].direction.fdel, """type : Vec3d


Returns the direction vector of the segment.


This is not guaranteed to be unit length.

""")