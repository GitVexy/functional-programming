def remove_invalid_lines(document):
    return "\n".join(
        filter(lambda line : not line.startswith("-"),
               document.split("\n")
               )
    )
