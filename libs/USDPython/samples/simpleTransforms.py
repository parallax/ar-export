#!/usr/bin/python

# Builds a scene graph of several objects and sets (animated) translate, rotate, and scale transforms

from pxr import *

filename = 'simpleTransforms'
stage = Usd.Stage.CreateNew('assets/'+filename+'.usd')
stage.SetStartTimeCode(0)
stage.SetEndTimeCode(90)


# set static transform, in the common translate/rotate/scale decomposition
cone = UsdGeom.Cone.Define(stage, '/cone')
cone.AddTranslateOp().Set((0,0,0))
cone.AddRotateXYZOp().Set((0,0,0))
cone.AddScaleOp().Set((1.2,2.0,1.2))

# parent two sphere objects under a common, rotating transform node
xform1 = UsdGeom.Xform.Define(stage, '/xform1')
xform1.AddTranslateOp().Set((0,3,0))
xform1RotateOp = xform1.AddRotateYOp()
for index, value in enumerate(range(90)):
	xform1RotateOp.Set(4*value, Usd.TimeCode(index))

sphere1 = UsdGeom.Sphere.Define(stage, '/xform1/sphere1')
sphere1.AddTranslateOp().Set((2,0,0))

sphere2 = UsdGeom.Sphere.Define(stage, '/xform1/sphere2')
sphere2.AddTranslateOp().Set((-2,0,0))

# print out contents of usd file
print(stage.GetRootLayer().ExportToString())
stage.Save()

# construct .usdz archive from the .usdc file
UsdUtils.CreateNewARKitUsdzPackage('assets/'+filename+'.usd', 'assets/'+filename+'.usdz')
