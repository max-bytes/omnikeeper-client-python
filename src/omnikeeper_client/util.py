import webcolors
import json

from typing import (
    Any
)

def hex_string_to_rgb_color(hex: str) -> int:
    """
    Converts a hex color string to an RGB integer

    Parameters
    ----------
    hex : str
        A string representing the hex color (e.g., '#FFFFFF')

    Returns
    -------
    int
        An integer representing the RGB color
    """
    (r,g,b) = webcolors.hex_to_rgb(hex)
    return (r << 16) | (g << 8) | (b)

def json_pretty(data : Any) -> None:
    return json.dumps(data, indent=2)

# utility function that converts an arbitrary class object into a dict, recursively
# taken from https://gist.github.com/sungitly/3f75cb297572dace2937
def to_dict(item):
    """
    Converts an arbitrary class object into a dict, recursively

    Parameters
    ----------
    item
        The input item to be converted. This can be a dictionary, list, tuple, or an arbitrary class object

    Returns
    -------
    result
        A dictionary representation of the input item
    """
    match item:
        case dict():
            data = {}
            for k, v in item.items():
                data[k] = to_dict(v)
            return data
        case list() | tuple():
            return [to_dict(x) for x in item]
        case object(__dict__=_):
            data = {}
            for k, v in item.__dict__.items():
                if not k.startswith("_"):
                    data[k] = to_dict(v)
            return data
        case _:
            return item
