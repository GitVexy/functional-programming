def converted_font_size(font_size):
        
    def multiply_font_size(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("Invalid doc type")
    
    return multiply_font_size


big_parenthesis = (
    "hello",
    "i'd",
    "like",
    "this",
    "for",
    "functions",
    "as",
    "well"
)