#!/usr/bin/python

# Creates a cube mesh and assigns it a simple PBR material 

from pxr import *

filename = 'simpleMaterial'
stage = Usd.Stage.CreateNew('assets/'+filename+'.usd')

# create mesh
mesh = UsdGeom.Mesh.Define(stage, '/cube')
mesh.CreateSubdivisionSchemeAttr().Set(UsdGeom.Tokens.none)
mesh.CreatePointsAttr([(-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5)])
mesh.CreateExtentAttr(UsdGeom.PointBased(mesh).ComputeExtent(mesh.GetPointsAttr().Get()))
mesh.CreateNormalsAttr([(0,0,1), (0,1,0), (0,0,-1), (0,-1,0), (1,0,0), (-1,0,0)])
mesh.SetNormalsInterpolation(UsdGeom.Tokens.uniform)

mesh.CreateFaceVertexCountsAttr([4, 4, 4, 4, 4, 4])
mesh.CreateFaceVertexIndicesAttr([0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 1, 0, 1, 7, 5, 3, 6, 0, 2, 4])

# create PBR material
material = UsdShade.Material.Define(stage, '/cubeMaterial')
pbrShader = UsdShade.Shader.Define(stage, '/cubeMaterial/PBRShader')

pbrShader.CreateIdAttr('UsdPreviewSurface')
pbrShader.CreateInput('diffuseColor', Sdf.ValueTypeNames.Color3f).Set(Gf.Vec3f(0.84, 0.65, 0.65))
pbrShader.CreateInput('metallic', Sdf.ValueTypeNames.Float).Set(0.9)
pbrShader.CreateInput('roughness', Sdf.ValueTypeNames.Float).Set(0.2)

material.CreateSurfaceOutput().ConnectToSource(pbrShader, 'surface')

# bind material to mesh
UsdShade.MaterialBindingAPI(mesh.GetPrim()).Bind(material)

print(stage.GetRootLayer().ExportToString())
stage.Save()

# construct .usdz archive from the .usdc file
UsdUtils.CreateNewARKitUsdzPackage('assets/'+filename+'.usd', 'assets/'+filename+'.usdz')
