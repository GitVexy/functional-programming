def first_reverse_string(s):
    if s == "": return s
    
    output = list(s).pop()
    print(f"{s}, returning '{output}'")
    output += first_reverse_string(s[:-1])
    return output



def solution_reverse_string(s: str) -> str:
    """Recursively reverses a string
    Args:     string
    Returns:  string
    """
    print(s)
    if s == "":
        return s
    return solution_reverse_string(s[1:]) + s[0]

print(first_reverse_string("A succulent Chinese meal!"))