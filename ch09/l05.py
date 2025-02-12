from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line

def convert_format(content: str, from_format, to_format):
    if not from_format or not to_format:
        raise Exception("Invalid type")
    
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML): # MD to HTML
            return f"<h1>{content.lstrip('# ')}</h1>"
        
        case (DocFormat.TXT, DocFormat.PDF): # TXT to PDF
            return f"[PDF] {content} [PDF]"
        
        case (DocFormat.HTML, DocFormat.MD): # HTML to MD
            return f"# {content.lstrip('<h1>').rstrip('</h1>')}"
        
        case _:
            raise Exception("Invalid type")
