def remove_emphasis_from_word(word):
    return word.strip("*")                              # Simply strip "*" from word


def remove_emphasis_from_line(line):
    words = line.split()                                # Split line into words
    output = map(remove_emphasis_from_word, words)      # Iterate on words with function above
    return " ".join(output)                             # Join the output with spaces


def remove_emphasis(doc_content):
    lines = doc_content.split("\n")                     # Split content into lines
    output = map(remove_emphasis_from_line, lines)      # Iterate on lines with function above
    return "\n".join(output)                            # Join the ouput with newlines



# First try under here

def first_try_at_remove_emphasis_from_word(word: str):
    return word.strip("*")

def first_try_at_remove_emphasis_from_line(line: str):
    output_list = []
    line = line[:-1]
    
    for word in line.split(" "):
        output_list.append(remove_emphasis_from_word(word))
    
    return " ".join(output_list)

def first_try_at_remove_emphasis(doc_content: str):
    lines_list = doc_content.split("\n")
    punctuation_list = []
    
    for line in lines_list:
        punctuation_list.append(line[-1:] if not line[-1:] == "*" else "")
    
    emphasis_removed = []
    
    for line in lines_list:
        emphasis_removed.append(remove_emphasis_from_line(line))
    
    output = []
    
    for i in range(0, len(emphasis_removed)):
        output.append(f"{emphasis_removed[i] + punctuation_list[i]}")
        
    return "\n".join(output)