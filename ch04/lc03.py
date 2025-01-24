def find_longest_word(document, longest_word=""):
    if len(document) == 0: return longest_word # Base case
    
    words = document.split(" ")
    if len(words[0]) > len(longest_word):
        longest_word = words[0]
    
    return find_longest_word(" ".join(words[1:]), longest_word)

print(f"\n{find_longest_word("This right here is the longest: Thingamabob")}\n")


""" Longest Word

In Doc2Doc, we have a search function to find the longest word in a document.
Assignment

Complete the find_longest_word function without a loop. It accepts string inputs, document, and optional longest_word, which is the current longest word and defaults to an empty string.

    Check if the first word is longer than the current longest_word, then recur for the rest of the document.
    Ensure there are no potential index errors.

 """