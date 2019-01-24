# Precompiled macOS Python Modules for Pixar's USD Library (Version 18.09)

This archive contains precompiled macOS Python modules for Pixar's USD library, and a set of sample scripts that demonstrate how to generate usd files.

## Python Bindings

This binary library was compiled using version 18.09 of [the public USD Github repository](http://openusd.org) with the following build script arguments (see USDPython/README.md for further details):

    python USD/build_scripts/build_usd.py --build-args TBB,extra_inc=big_iron.inc --python --no-imaging --docs --no-usdview --build-monolithic USDPython

To start using USD in Python, set your PATH and PYTHONPATH variables as follows (replace `<PATH_TO_USDPYTHON>` with the path to this USDPython folder):

    export PATH=$PATH:<PATH_TO_USDPYTHON>/USD
    export PYTHONPATH=$PYTHONPATH:<PATH_TO_USDPYTHON>/USD

You should then be able to easily inspect the content of any text or binary .usd file or a .usdz archive usding `usdcat`, e.g.:

	usdcat samples/assets/island.usdz


## Samples

The `samples` folder contains a set of simple scripts that focus on different aspects of writing USD data, such as geometry, materials, skinning and animation. 
Each script generates a .usdc and a .usdz file in the `assets` subfolder, and also prints the generated .usd file's content.

| Script | Purpose |
| ------ | --- |
| `simpleMesh.py` | creates a cube mesh |
| `simpleTransforms.py` |  builds a scene graph of several objects and sets (animated) translate, rotate, and scale transforms |
| `simpleMaterial.py` | creates a simple PBR material |
| `meshGroups.py` | creates a cube mesh with two mesh groups and assigns each a separate material |
| `texturedMaterial.py` | creates a cube mesh and assigns it a PBR material with a diffuse texture |
| `complexMaterial.py` | creates a cube mesh and assigns it a more complex PBR material with textures for normal, roughness and diffuse channels |
| `skinnedMeshAnimation.py` | creates an animated skinned cube |


