from enum import Enum


class EditType(Enum):
    NEWLINE = 1
    SUBSTITUTE = 2
    INSERT = 3
    DELETE = 4


def handle_edit(document: str,
                edit_type: EditType,
                edit: dict) -> str:
    match edit_type:

        case EditType.NEWLINE:
            return doc_newline(document, edit)

        case EditType.SUBSTITUTE:
            return doc_substitute(document, edit)

        case EditType.INSERT:
            return doc_insert(document, edit)

        case EditType.DELETE:
            return doc_delete(document, edit)

        case _:
            raise Exception("unknown edit type")


def line_number_check(doc: str = None,
                      edit: dict = None) -> None:
    if (
        edit["line_number"] >= len(doc.split("\n")) or
        edit["line_number"] < 0
    ):
        raise IndexError("line_number is out of range")

    return edit["line_number"]


def doc_newline(document: str,
                edit: dict = {"line_number": int}
                ) -> str:
    line_number = line_number_check(document, edit)
    split_lines = document.split("\n")
    split_lines.insert(line_number + 1, "")

    return "\n".join(split_lines)


def doc_substitute(document: str,
                   edit: dict = {"insert_text": str,
                                 "line_number": int,
                                 "start": int,
                                 "end": int}
                   ) -> str:
    line_number = line_number_check(document, edit)
    split_lines = document.split("\n")
    edited_line = (
        split_lines[line_number][:edit["start"]] +
        edit["insert_text"] +
        split_lines[line_number][edit["end"]:]
    )
    split_lines[line_number] = edited_line

    return "\n".join(split_lines)


def doc_insert(document: str,
               edit: dict = {"insert_text": str,
                             "line_number": int,
                             "start": int}
               ) -> str:
    line_number = line_number_check(document, edit)
    split_lines = document.split("\n")
    edited_line = (
        split_lines[line_number][:edit["start"]] +
        edit["insert_text"] +
        split_lines[line_number][edit["start"]:]
    )
    split_lines[line_number] = edited_line

    return "\n".join(split_lines)


def doc_delete(document: str,
               edit: dict = {"line_number": int,
                             "start": int,
                             "end": int}
               ) -> str:
    line_number = line_number_check(document, edit)
    split_lines = document.split("\n")
    edited_line = (
        split_lines[line_number][:edit["start"]] +
        split_lines[line_number][edit["end"]:]
    )
    split_lines[line_number] = edited_line

    return "\n".join(split_lines)
