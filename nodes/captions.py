from io import BytesIO

import torch
from cairosvg import svg2png
from PIL import Image

from .commons import image2tensor, tensor2image


class ApplySVG2Image:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
                "svg": (
                    "STRING",
                    {
                        "multiline": True,
                        "default": """<svg width="1024" height="1024" xmlns="http://www.w3.org/2000/svg">\n\n</svg>""",
                    },
                ),
                "width": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 10000,
                        "step": 1,
                        "display": "number",
                    },
                ),
                "height": (
                    "INT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 10000,
                        "step": 1,
                        "display": "number",
                    },
                ),
                "offset_x": (
                    "INT",
                    {
                        "default": 0,
                        "min": -1000,
                        "max": 1000,
                        "step": 1,
                        "display": "number",
                    },
                ),
                "offset_y": (
                    "INT",
                    {
                        "default": 0,
                        "min": -1000,
                        "max": 1000,
                        "step": 1,
                        "display": "number",
                    },
                ),
            },
            "optional": {
                "properties": ("PROPERTIES",),
            },
        }

    RETURN_TYPES = ("IMAGE", "STRING")
    RETURN_NAMES = ("images", "formated svg")
    FUNCTION = "execute"
    CATEGORY = "kuniklo"

    def execute(self, images, svg, width, height, offset_x, offset_y, **kwargs):
        properties = {}
        if "properties" in kwargs:
            properties = kwargs["properties"]

        output_images = []
        for image in images:
            # interpolate properties
            for key, value in properties.items():
                svg = svg.replace(f"{{{key}}}", str(value))

            # open input image (first batch)
            pil_image01 = tensor2image(image)

            # cast svg to image
            svg_data = svg2png(bytestring=svg)
            pil_image02 = Image.open(BytesIO(svg_data))
            if width and height:
                pil_image02 = pil_image02.resize((width, height))

            # merge images
            pil_image03 = pil_image01.copy()
            pil_image03.paste(pil_image02, (offset_x, offset_y), pil_image02)

            # convert back to tensor
            output_images.append(image2tensor(pil_image03))

        result = torch.stack(output_images, dim=0)
        return (result, svg)
