default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands: dict, new_command: str, function: str) -> dict:
    local_commands = commands.copy()
    local_commands[new_command] = function
    return local_commands


def add_format(formats: list, format: str) -> list:
    local_formats = formats.copy()
    local_formats.append(format)
    return local_formats


def save_document(docs: dict, file_name: str, doc: str) -> dict:
    local_docs = docs.copy()
    local_docs[file_name] = doc
    return local_docs


def add_line_break(line: str) -> str:
    return line + "\n\n"
