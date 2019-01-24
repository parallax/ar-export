#!/usr/bin/python

#  Creates a cube mesh and assigns it a PBR material with a diffuse texture

from pxr import *

filename = 'texturedMaterial'
stage = Usd.Stage.CreateNew('assets/'+filename+'.usd')

# create mesh with UVs
mesh = UsdGeom.Mesh.Define(stage, '/cube')
mesh.CreateSubdivisionSchemeAttr().Set(UsdGeom.Tokens.none)
mesh.CreatePointsAttr([(-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5)])
mesh.CreateExtentAttr(UsdGeom.PointBased(mesh).ComputeExtent(mesh.GetPointsAttr().Get()))
mesh.CreateNormalsAttr([(0,0,1), (0,1,0), (0,0,-1), (0,-1,0), (1,0,0), (-1,0,0)])
mesh.SetNormalsInterpolation(UsdGeom.Tokens.uniform)

mesh.CreateFaceVertexCountsAttr([4, 4, 4, 4, 4, 4])
mesh.CreateFaceVertexIndicesAttr([0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 1, 0, 1, 7, 5, 3, 6, 0, 2, 4])
	
uvs = mesh.CreatePrimvar('uv', Sdf.ValueTypeNames.TexCoord2fArray, UsdGeom.Tokens.faceVarying) # a 'faceVarying' mesh attribute is stored per-face per-vertex
uvs.Set([(0.375, 0), (0.625, 0), (0.625, 0.25), (0.375, 0.25), (0.625, 0.5), (0.375, 0.5), (0.625, 0.75), (0.375, 0.75), (0.625, 1), (0.375, 1), (0.875, 0), (0.875, 0.25), (0.125, 0), (0.125, 0.25)])
uvs.SetIndices(Vt.IntArray([0, 1, 2, 3, 3, 2, 4, 5, 5, 4, 6, 7, 7, 6, 8, 9, 1, 10, 11, 2, 12, 0, 3, 13]))

# create PBR material
material = UsdShade.Material.Define(stage, '/cubeMaterial')
pbrShader = UsdShade.Shader.Define(stage, '/cubeMaterial/PBRShader')

pbrShader.CreateIdAttr('UsdPreviewSurface')

# create UV attribute reader node
uvReader = UsdShade.Shader.Define(stage, '/cubeMaterial/uvReader')
uvReader.CreateIdAttr('UsdPrimvarReader_float2')
uvReader.CreateInput('varname',Sdf.ValueTypeNames.Token).Set('uv')
uvReader.CreateOutput('result', Sdf.ValueTypeNames.Float2)

# create texture sampler node
textureSampler = UsdShade.Shader.Define(stage,'/cubeMaterial/diffuseTexture')
textureSampler.CreateIdAttr('UsdUVTexture')
textureSampler.CreateInput('file', Sdf.ValueTypeNames.Asset).Set('textures/soccerBall_BC.png')
textureSampler.CreateInput('uv', Sdf.ValueTypeNames.Float2).ConnectToSource(uvReader, 'result')
textureSampler.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)

pbrShader.CreateInput('diffuseColor', Sdf.ValueTypeNames.Color3f).ConnectToSource(textureSampler, 'rgb')

material.CreateSurfaceOutput().ConnectToSource(pbrShader, 'surface')

# bind material to mesh
UsdShade.MaterialBindingAPI(mesh.GetPrim()).Bind(material)

print(stage.GetRootLayer().ExportToString())
stage.Save()

# construct .usdz archive from the .usdc file
UsdUtils.CreateNewARKitUsdzPackage('assets/'+filename+'.usd', 'assets/'+filename+'.usdz')
