from enum import Enum
from lc02 import (
    EditType,
    handle_edit
)

"""
Doc2Doc should be able to track changes in documents.
Tracking changes is important for undoing and redoing edits.
Some editors save changes and some file formats do as well.

Assignment:
  Complete the handle_edit function.
  Create functions for the following operations:

    NEWLINE:
      Use the edit dict to modify and return a copy of the doc.

      The edit dict will only contain:
       a line_number key and integer value (zero-indexed!)

      Add a newline at the end of the line of the document corresponding
      to the line_number.

    SUBSTITUTE:
      Use the edit dict to modify and return a copy of the doc.

      The edit dict will contain:
        a insert_text key and string value,
        a line_number key and integer value,
        a start key and integer value,
        and an end key and integer value.

      Substitute the insert_text into the line of the doc corresponding
      to the line_number between the start and end indexes.

    INSERT:
      Use the edit dict to modify and return a copy of the doc.

      The edit dict will contain:
        a insert_text key and string value,
        a line_number key and integer value,
        and a start key and integer value.

      Insert the insert_text into the line of the document
      corresponding to the line_number at the start index.

    DELETE:
      Use the edit dict to modify and return a copy of the doc.

      The edit dict will contain:
        a line_number key and integer value,
        a start key and integer value,
        and an end key and integer value.

      Remove the substring of the line of the document corresponding to
      the line_number between the start and end indexes.

    Exceptions:
      If the edit_type is none of the above, raise Exception
      with the string "unknown edit type".
"""


try:
    (EditType.SUBSTITUTE
     and EditType.INSERT
     and EditType.DELETE
     and EditType.NEWLINE)
except Exception as error:
    print(f"Error: Missing attribute {error} from enum")

    class EditType(Enum):
        SUBSTITUTE = None
        INSERT = None
        DELETE = None
        NEWLINE = None


run_cases = [
    (
        """Dear Manager,

I’m outraged!
My car warranty is
an total disaster.
Fix this immediately now!

Sincerely,""",
        EditType.SUBSTITUTE,
        {
            "insert_text": "right",
            "line_number": 5,
            "start": 9,
            "end": 20,
        },
        """Dear Manager,

I’m outraged!
My car warranty is
an total disaster.
Fix this right now!

Sincerely,""",
    ),
    (
        """Dear Manager,

I’m outraged!
My car warranty is
an total disaster.
Fix this right now!

Sincerely,""",
        EditType.NEWLINE,
        {
            "line_number": 7,
        },
        """Dear Manager,

I’m outraged!
My car warranty is
an total disaster.
Fix this right now!

Sincerely,
""",
    ),
    (
        """Dear Manager,

I’m outraged!
My car warranty is
an total disaster.
Fix this right now!

Sincerely,
""",
        EditType.INSERT,
        {
            "insert_text": "Karen",
            "line_number": 8,
            "start": 0,
        },
        """Dear Manager,

I’m outraged!
My car warranty is
an total disaster.
Fix this right now!

Sincerely,
Karen""",
    ),
    (
        """Dear Manager,

I’m outraged!
My car warranty is
an total disaster.
Fix this right now!

Sincerely,
Karen""",
        EditType.DELETE,
        {
            "line_number": 4,
            "start": 1,
            "end": 2,
        },
        """Dear Manager,

I’m outraged!
My car warranty is
a total disaster.
Fix this right now!

Sincerely,
Karen""",
    ),
]

submit_cases = run_cases + [
    (
        "test string",
        "unknown edit type",
        {},
        "unknown edit type",
    ),
]


def test(document, edit_type, edit, expected_output):
    print("---------------------------------")
    print(f"Change Type: {edit_type}")
    print("Inputs:")
    for key, val in edit.items():
        print(f"* {key}: {val}")
    print("Expected:")
    print(expected_output)
    try:
        result = handle_edit(document, edit_type, edit)
    # catch expected error or else raise unexpected error again
    except Exception as e:
        result = str(e)
    print("Actual:")
    print(result)
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
