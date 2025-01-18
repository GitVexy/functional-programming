def convert_case(text, target_format):
    
    if not text or not target_format:
        raise ValueError(f"No text or target format provided")

    if target_format == "uppercase":
        return text.upper()

    elif target_format == "lowercase":
        return text.lower()

    elif target_format == "titlecase":
        return text.title()

    else:
        raise ValueError(f"Unsupported format: {target_format}")
