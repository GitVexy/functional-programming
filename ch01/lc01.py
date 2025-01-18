def toggle_case(line):
    if not line or line == None:
        return ""
    
    elif line.istitle():
        return line.upper() + "!!!"
    
    elif line.isupper():
        return line[0] + line[1:].lower().replace("!", "")
    
    elif len(line) > 0 and line[1:].islower():
        return line.title()
    
    return line