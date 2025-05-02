import torch
import torchvision.transforms
from PIL import Image


def tensor2image(tensor: torch.Tensor) -> Image.Image:
    return torchvision.transforms.ToPILImage()(
        torch.permute(tensor, (2, 0, 1))
    ).convert("RGBA")


def image2tensor(pil_image: Image.Image) -> torch.Tensor:
    return torch.permute(torchvision.transforms.ToTensor()(pil_image), (1, 2, 0))


class Properties:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "key_0": ("STRING",),
                "value_0": ("STRING",),
                "key_1": ("STRING",),
                "value_1": ("STRING",),
                "key_2": ("STRING",),
                "value_2": ("STRING",),
                "key_3": ("STRING",),
                "value_3": ("STRING",),
                "key_4": ("STRING",),
                "value_4": ("STRING",),
                "key_5": ("STRING",),
                "value_5": ("STRING",),
                "key_6": ("STRING",),
                "value_6": ("STRING",),
                "key_7": ("STRING",),
                "value_7": ("STRING",),
                "key_8": ("STRING",),
                "value_8": ("STRING",),
                "key_9": ("STRING",),
                "value_9": ("STRING",),
            }
        }

    RETURN_TYPES = ("PROPERTIES",)
    FUNCTION = "execute"
    CATEGORY = "kuniklo"

    def execute(self, **kwargs):
        properties = {}

        for key, value in kwargs.items():
            if key.startswith("key_") and value:
                properties[value] = kwargs[key.replace("key_", "value_")]

        return (properties,)
