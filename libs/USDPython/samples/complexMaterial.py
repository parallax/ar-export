#!/usr/bin/python

# Creates a cube mesh and assigns it a more complex PBR material with textures for normal, roughness and diffuse channels

from pxr import *

filename = 'complexMaterial'
stage = Usd.Stage.CreateNew('assets/' + filename + '.usd')

# create mesh with UVs
mesh = UsdGeom.Mesh.Define(stage, '/cube')
mesh.CreateSubdivisionSchemeAttr().Set(UsdGeom.Tokens.none)
mesh.CreatePointsAttr([(-0.5, -0.5, 0.5), (0.5, -0.5, 0.5), (-0.5, 0.5, 0.5), (0.5, 0.5, 0.5), (-0.5, 0.5, -0.5), (0.5, 0.5, -0.5), (-0.5, -0.5, -0.5), (0.5, -0.5, -0.5)])
mesh.CreateExtentAttr(UsdGeom.PointBased(mesh).ComputeExtent(mesh.GetPointsAttr().Get()))
mesh.CreateNormalsAttr([(0,0,1), (0,1,0), (0,0,-1), (0,-1,0), (1,0,0), (-1,0,0)])
mesh.SetNormalsInterpolation(UsdGeom.Tokens.uniform)

mesh.CreateFaceVertexCountsAttr([4, 4, 4, 4, 4, 4])
mesh.CreateFaceVertexIndicesAttr([0, 1, 3, 2, 2, 3, 5, 4, 4, 5, 7, 6, 6, 7, 1, 0, 1, 7, 5, 3, 6, 0, 2, 4])

textureCoordinates = mesh.CreatePrimvar('uv', Sdf.ValueTypeNames.TexCoord2fArray, UsdGeom.Tokens.faceVarying)
textureCoordinates.Set([(0.375, 0), (0.625, 0), (0.625, 0.25), (0.375, 0.25), (0.625, 0.5), (0.375, 0.5), (0.625, 0.75), (0.375, 0.75), (0.625, 1), (0.375, 1), (0.875, 0), (0.875, 0.25), (0.125, 0), (0.125, 0.25)])
textureCoordinates.SetIndices(Vt.IntArray([0, 1, 2, 3, 3, 2, 4, 5, 5, 4, 6, 7, 7, 6, 8, 9, 1, 10, 11, 2, 12, 0, 3, 13]))

# create PBR material
material = UsdShade.Material.Define(stage, '/cubeMaterial')
uvInput = material.CreateInput('frame:stPrimvarName', Sdf.ValueTypeNames.Token)
uvInput.Set('uv')

pbrShader = UsdShade.Shader.Define(stage, '/cubeMaterial/PBRShader')
pbrShader.CreateIdAttr('UsdPreviewSurface')

# create UV attribute reader node
uvReader = UsdShade.Shader.Define(stage, '/cubeMaterial/uvReader')
uvReader.CreateIdAttr('UsdPrimvarReader_float2')
uvReader.CreateInput('varname',Sdf.ValueTypeNames.Token).ConnectToSource(uvInput)
uvReader.CreateOutput('result', Sdf.ValueTypeNames.Float2)

# diffuse texture
diffuseTextureSampler = UsdShade.Shader.Define(stage,'/cubeMaterial/diffuseTexture')
diffuseTextureSampler.CreateIdAttr('UsdUVTexture')
diffuseTextureSampler.CreateInput('file', Sdf.ValueTypeNames.Asset).Set('textures/soccerBall_BC.png')
diffuseTextureSampler.CreateInput('uv', Sdf.ValueTypeNames.Float2).ConnectToSource(uvReader, 'result')
diffuseTextureSampler.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)
pbrShader.CreateInput('diffuseColor', Sdf.ValueTypeNames.Color3f).ConnectToSource(diffuseTextureSampler, 'rgb')

# set metalness = 0
pbrShader.CreateInput('metallic', Sdf.ValueTypeNames.Float).Set(0.0)

# roughness texture
roughnessTextureSampler = UsdShade.Shader.Define(stage,'/cubeMaterial/roughnessTexture')
roughnessTextureSampler.CreateIdAttr('UsdUVTexture')
roughnessTextureSampler.CreateInput('file', Sdf.ValueTypeNames.Asset).Set('textures/soccerBall_R.png')
roughnessTextureSampler.CreateInput('uv', Sdf.ValueTypeNames.Float2).ConnectToSource(uvReader, 'result')
roughnessTextureSampler.CreateOutput('r', Sdf.ValueTypeNames.Float)
pbrShader.CreateInput('roughness', Sdf.ValueTypeNames.Float).ConnectToSource(roughnessTextureSampler, 'r')

# normal texture
normalTextureSampler = UsdShade.Shader.Define(stage,'/cubeMaterial/normalTexture')
normalTextureSampler.CreateIdAttr('UsdUVTexture')
normalTextureSampler.CreateInput('file', Sdf.ValueTypeNames.Asset).Set('textures/soccerBall_N.png')
normalTextureSampler.CreateInput('uv', Sdf.ValueTypeNames.Float2).ConnectToSource(uvReader, 'result')
normalTextureSampler.CreateInput('scale', Sdf.ValueTypeNames.Float4).Set((2.0, 2.0, 2.0, 2.0))
normalTextureSampler.CreateInput('bias', Sdf.ValueTypeNames.Float4).Set((-1.0, -1.0, -1.0, -1.0))
normalTextureSampler.CreateOutput('rgb', Sdf.ValueTypeNames.Float3)
pbrShader.CreateInput('normal',Sdf.ValueTypeNames.Normal3f).ConnectToSource(normalTextureSampler, 'rgb')

material.CreateSurfaceOutput().ConnectToSource(pbrShader, 'surface')

# bind material to mesh
UsdShade.MaterialBindingAPI(mesh.GetPrim()).Bind(material)

print(stage.GetRootLayer().ExportToString())
stage.Save()

# construct .usdz archive from the .usdc file
UsdUtils.CreateNewARKitUsdzPackage('assets/'+filename+'.usd', 'assets/'+filename+'.usdz')
