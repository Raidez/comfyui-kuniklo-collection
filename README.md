# Kuniklo Collection
This is my custom node collection.

## Installation
The collection require **Cairo**, [check the documentation for more information](https://cairosvg.org/documentation/):
- on Windows, you’ll have to install Cairo (with [GTK](https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer) for example);
- on macOS, you’ll have to install cairo and libffi (with Homebrew for example);
- on Linux, you’ll have to install the cairo, python3-dev and libffi-dev packages (names may vary for your distribution).

## Nodes

### Properties
This node is a list of key value pairs.

### ApplySVG2Image
This node is used to apply a SVG to an image :
- images: the images to apply the SVG to (single or batch)
- svg: the SVG to apply
- width: resize the pasted svg to this width
- height: resize the pasted svg to this height
- offset_x: offset the pasted svg to this x position
- offset_y: offset the pasted svg to this y position
- properties: subtitued properties with the dedicated node
