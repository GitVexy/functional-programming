def doc_format_checker_and_converter(conversion_function, valid_formats: list):
    
    def convert_if_valid(filename: str, content: str) -> str:
        
        if filename.split(".")[1] in valid_formats:
            return conversion_function(content)
        
        else:
            raise ValueError("Invalid file format")
    
    return convert_if_valid


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
