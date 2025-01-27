from typing import Callable, Tuple

# FUNCTION 1
def new_resizer(max_width: int, max_height: int) -> Callable[[int, int], Callable[[int, int], Tuple[int, int]]]:
    "Returns declare_size()"
    
    # FUNCTION 2
    def declare_size(min_width: int = 0, min_height: int = 0) -> Callable[[int, int], Tuple[int, int]]:
        "Checks if minimum sizes are within bounds. Returns resize()"
        nonlocal max_width, max_height
        
        if min_width > max_width or min_height > max_height:
            raise ValueError("minimum size cannot exceed maximum size")
        
        # FUNCTION 3
        def resize(width: int = 0, height: int = 0) -> Tuple[int, int]:
            "Adjusts width and height, and returns new values"
            
            nonlocal max_width, max_height, min_width, min_height
            
            if min_width <= width <= max_width:
                new_width = width
            
            elif width < min_width:
                new_width = min_width
            
            else:
                new_width = max_width
            
            if min_height <= height <= max_height:
                new_height = height
            
            elif height < min_height:
                new_height = min_height
            
            else:
                new_height = max_height
            
            # FINAL OUTPUT
            return (new_width, new_height)
        
        # RETURN FUNCTION 3
        return resize
    
    # RETURN FUNCTION 2
    return declare_size

print(f"Mine: {new_resizer(1000, 1000)(100, 100)(420, 69)}")



#################################################
def CHATGPT_resizer(max_width: int, max_height: int) -> Callable[[int, int], Callable[[int, int], Tuple[int, int]]]:
    return lambda min_width=0, min_height=0: (
        lambda w=0, h=0: (
            max(min_width, min(max_width, w)), 
            max(min_height, min(max_height, h))
        )
        if min_width <= max_width and min_height <= max_height 
        else ValueError("minimum size cannot exceed maximum size")
    )

print(f"ChatGPT: {CHATGPT_resizer(1000, 1000)(100, 100)(420, 69)}")  # Output: (420, 100)

