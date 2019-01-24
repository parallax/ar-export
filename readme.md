# Requirements

Blender 2.8
Xcode 11
Nodejs

The converter script will need know where to find the blender executable and USD python libraries. 
To do this is to create a `.env` file in this directory and enter the following values...

```
PYTHONPATH=path_to_usd_python
BLENDER=path_to_blender
```

On OSX Blender is usally in the applications folder `/Applications/blender/blender.app/Contents/MacOS/blender`.


# Usage

`converter.js input_file.blend -o output_directory`

Opens the target .blend file and exports a gltf, dae and usdz files in the output directory.


