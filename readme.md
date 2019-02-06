# ARexport

## Description

Converts Blender3D .blend files into .dae (collada), .gltf and .usdz files for use with AR viewers.

## Requirements

- Blender 2.8
- Xcode 11
- Node.js

## Setup

The converter script will need know where to find the Blender executable and USD python libraries.
To do this is to create a `.env` file in this directory and enter the following values...

```
PYTHONPATH=path_to_usd_python
BLENDER=path_to_blender
```

On OSX Blender is usually in the applications folder `/Applications/blender/blender.app/Contents/MacOS/blender`
USD python can be found in the libs directory of this repo if you don't have it already installed.s

## Usage

`node converter.js input_file.blend -o output_directory`

Opens the target .blend file and exports a gltf, dae and usdz files in the output directory.

# TODO

- Collada doesn't seem to export textures for all channels, only colour
- Multiple source file input / watch folder
