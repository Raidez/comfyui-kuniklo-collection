from .nodes.commons import Properties
from .nodes.captions import ApplySVG2Image

NODE_CLASS_MAPPINGS = {
    "Properties": Properties,
    "ApplySVG2Image": ApplySVG2Image,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Properties": "Properties",
    "ApplySVG2Image": "Apply SVG to Image",
}
