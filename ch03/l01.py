global_valid_extensions = ["docx", "pdf", "txt", "pptx", "ppt", "md"]
global_valid_conversions = {
    "docx": ["pdf", "txt", "md"],
    "pdf": ["docx", "txt", "md"],
    "txt": ["docx", "pdf", "md"],
    "pptx": ["ppt", "pdf"],
    "ppt": ["pptx", "pdf"],
    "md": ["docx", "pdf", "txt"],
}


def convert_file_format(filename, target_format):
    global global_valid_extensions
    global global_valid_conversions
    
    current_format = filename.split(".")[-1]
    if (
        current_format in global_valid_extensions
        and target_format in global_valid_conversions[current_format]
    ):
        return filename.replace(current_format, target_format)
    return None

file = "hex.txt"
target = "pdf"
print(convert_file_format(file, target))
print(file)
print(convert_file_format(file, target))