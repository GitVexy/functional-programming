def convert_tuple_value_to_txt(tup: tuple):
    return (tup[0], convert_md_to_txt(tup[1]))


def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        plain_text_args = list(map(convert_md_to_txt, args))
        plain_text_kwargs = dict(map(convert_tuple_value_to_txt, kwargs.items()))
        
        return func(*plain_text_args, **plain_text_kwargs)

    return wrapper


# don't touch below this line

def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
