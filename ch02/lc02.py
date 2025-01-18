valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def old_pair_document_with_format(doc_names, doc_formats):
    error_handling(doc_names, doc_formats)
    
    return list(                                        # 4. Make product a list and return it
        filter(                                         # 3. Filter all tuples using the lambda function
            lambda format : format[1] in valid_formats, # 2. lambda checks if format is in valid_formats
            zip(doc_names, doc_formats)                 # 1. Merge doc_names and doc_formats into tuples
            )
        )

def pair_document_with_format(doc_names, doc_formats):
    error_handling(doc_names, doc_formats)
    
    zipped = zip(doc_names, doc_formats)
    filtered = filter(lambda format: format[1] in valid_formats, zipped)
    return list(filtered)

    
# Example input:
#   (["Proposal", "Invoice", "Contract"], ["docx", "pdoof", "txt"])

# Example output:
#   [('Proposal', 'docx'), ('Contract', 'txt')]

# Reason:
#   ("Invoice", "pdoof") >> "pdoof" not in valid_formats

def error_handling(x, y):
    
    error_string = f"Expected two populated lists, got {x} and {y}"
    
    if type(x) != list or type(y) != list:
        raise TypeError(error_string)
    
    elif x == [] or y == []:
        print("Soft ValueError:", error_string)
    
    elif not x or not y:
        raise Exception(error_string)

print(pair_document_with_format(["Proposal", "Invoice", "Contract"], ["docx", "pdoof", "txt"]))
