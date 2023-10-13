import webcolors

def hexString2RGBColor(hex: str) -> int:
    (r,g,b) = webcolors.hex_to_rgb(hex)
    return (r << 16) | (g << 8) | (b)