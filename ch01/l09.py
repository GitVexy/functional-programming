def format_line(line):
    return f"{line.strip(' ').upper().replace('.', '')}..."

print(format_line("  Hello, world  "))