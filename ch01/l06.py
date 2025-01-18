def get_median_font_size(font_sizes):
    return (
        None if not font_sizes 
        else 
            sorted(font_sizes)[len(font_sizes) // 2] if len(font_sizes) % 2 == 1 
        else 
            sorted(font_sizes)[len(font_sizes) // 2 - 1]
        )
