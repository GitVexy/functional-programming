"""
This module implements a flexible FizzBuzz-style program.

Functions:
    - get_all_fizzes: Combines all fizz strings and initializes an index list.
    - generate_output: Generates the output string for a given number.
    - process_indices: Updates and processes indices where all rules are satisfied.
    - display_results: Displays indices where all rules were met or indicates no matches.
    - find_buzz: Main function to evaluate and print outputs for numbers based on rules.

Usage:
    Define rules as key-value pairs where keys are divisors (as integers) and values
    are corresponding words to append when divisible. Call `find_buzz` with the range
    limit and rules to see the results.

Example:
    rules = {
        3: "fizz",
        5: "buzz",
    }
    find_buzz(n=100, mapped=True, rules=rules)
"""

from typing import Dict, List, Tuple

def find_buzz(n: int, mapped: bool, rules: Dict[int, str]):
    """
    Generate and print outputs for numbers from 1 to n based on divisibility rules.

    Args:
        n (int): The range of numbers to evaluate (1 to n inclusive).
        mapped (bool): Whether to include the number when rules are met.
        rules (Dict[int, str]): Key-value pairs where keys are divisors (as integers)
            and values are the corresponding words to append when divisible.

    Prints:
        Outputs for each number, and indices where all rules are satisfied.
    """

    print(f"\nRunning find_buzz with n = {n}, mapped = {mapped}\n\nRules: {rules}\n")
    all_fizzes, all_fizzes_indices = get_all_fizzes(rules)

    for i in range(1, n + 1):
        output, num_added = generate_output(i, rules, mapped)

        if not num_added:
            output += str(i)

        output = process_indices(i, output, all_fizzes, all_fizzes_indices)
        print(output)

    display_results(all_fizzes_indices, n, mapped)


def get_all_fizzes(rules: Dict[int, str]) -> Tuple[str, List[int]]:
    """
    Combine all fizz strings and initialize an empty list for indices.

    Args:
        rules (Dict[int, str]): A dictionary where keys are divisors (as integers)
            and values are corresponding words to append.

    Returns:
        Tuple[str, List[int]]: A tuple containing the concatenated fizz strings
            and an empty list to store indices.
    """

    all_fizzes = "".join(rules.values())
    all_fizzes_indices = []
    return all_fizzes, all_fizzes_indices


def generate_output(i: int, rules: Dict[int, str], mapped: bool) -> Tuple[str, bool]:
    """
    Generate the output string for a single number based on divisibility rules.

    Args:
        i (int): The current number being evaluated.
        rules (Dict[int, str]): A dictionary where keys are divisors (as integers)
            and values are corresponding words to append.
        mapped (bool): Whether to include the number in the output string when divisible.

    Returns:
        Tuple[str, bool]: A tuple containing the output string and a boolean indicating
            if any rule was applied.
    """

    output = str(i) if mapped else ""
    fizz_found = False

    for key, value in rules.items():
        if i % key == 0:
            output += ": " + value if mapped and not fizz_found else value
            fizz_found = True

    return output, bool(mapped or fizz_found)


def process_indices(i: int, output: str, all_fizzes: str, all_fizzes_indices: List[int]) -> str:
    """
    Check if the output matches all fizzes and update the indices list.

    Args:
        i (int): The current number being evaluated.
        output (str): The generated output string for the number.
        all_fizzes (str): The concatenated fizz strings.
        all_fizzes_indices (List[int]): The list of indices where all rules are met.

    Returns:
        str: The processed output string, converted to uppercase if all rules are met.
    """

    if all_fizzes in output:
        all_fizzes_indices.append(i)
        return output.upper()
    return output


def display_results(all_fizzes_indices: List[int], n: int, mapped: bool):
    """
    Display the indices where all rules were satisfied or indicate if none were met.

    Args:
        all_fizzes_indices (List[int]): The list of indices where all rules were satisfied.

    Prints:
        The indices where all rules were satisfied, or a message indicating no matches.
    """

    if all_fizzes_indices:
        print(f"\nfind_buzz with n = {n}, mapped = {mapped}\n\nRules: {rules}\n")
        print("\nAll rules met at indices:")
        print("\n".join(map(str, all_fizzes_indices)))

    else:
        print("\nNo indices met all rules...")


rules = {
    3: "fizz",
    5: "buzz",
    7: "bazz",
    9: "fozz",
    11: "bizz",
}

find_buzz(n=10000, mapped=False, rules=rules)
