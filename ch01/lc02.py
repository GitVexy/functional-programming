def hex_to_rgb(hex_color):
    if (
        len(str(hex_color)) != 6 or
        not is_hexadecimal(hex_color)
        ): raise Exception("not a hex color string")
    
    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    
    return r, g, b


# Don't edit below this line


def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False