def first_reverse_string(s):
    if s == "": return s
    
    output = list(s).pop()
    print(f"{s}, returning '{output}'")
    output += first_reverse_string(s[:-1])
    return output


print(first_reverse_string("A succulent Chinese meal!"))

def solution_reverse_string(s): # Written after checking solution
    """Recursively reverses a string

    Args:
        s (string)

    Returns:
        reversed string
    """
    print(s)
    
    if s == "":
        return s

    return solution_reverse_string(s[1:]) + s[0]