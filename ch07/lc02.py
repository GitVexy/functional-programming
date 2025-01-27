# Syntax: ![alt text](url "title")
# alt text:
#    a brief description for screen readers and web scrapers. Required for accessibility.
# url:
#    url or relative path to image.
# title:
#    shown on mouse hover. Optional.

from typing import Callable

def create_markdown_image(alt_text: str) -> Callable[[str, str], str]:
    markdown_image = f"![{alt_text}]"
    
    def create_markdown_url(url: str) -> Callable[[str], str]:
        url = f"({url.replace('(', '%28').replace(')', '%29')})"
        nonlocal markdown_image
        markdown_image += url
        
        def create_markdown_title(title:str = None) -> Callable[[str], str]:
            nonlocal markdown_image
            if title:
                markdown_image = f'{markdown_image[:-1]} "{title}")'
                
            return markdown_image
        return create_markdown_title
    return create_markdown_url


print(str(
    create_markdown_image
          ("Deeply curried function")
          ("https://revistavelvet.cl/wp-content/uploads/2022/08/IMG_8053.jpg")
          ("")
          )
      )
