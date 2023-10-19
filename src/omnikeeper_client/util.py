import webcolors
import json

from typing import (
    Any
)

def hexString2RGBColor(hex: str) -> int:
    (r,g,b) = webcolors.hex_to_rgb(hex)
    return (r << 16) | (g << 8) | (b)

def json_pretty(data : Any) -> None:
    return json.dumps(data, indent=2)
