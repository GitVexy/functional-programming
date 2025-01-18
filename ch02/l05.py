def change_bullet_style(document):
    #lines = document.split("\n")
    #converted_lines = map(convert_line, lines)
    #converted_lines = "\n".join(converted_lines)
    #return converted_lines
    return ("\n".join(map(convert_line, document.split("\n"))))


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line
