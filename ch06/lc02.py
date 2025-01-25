def user_words(initial_words: tuple):
    words = initial_words
    def add_word(word: str):
        nonlocal words
        words = words + (word,)
        return words
    
    
    return add_word

add_a_word = user_words(("Hello", "world"))
print(add_a_word("!"))
print(add_a_word("!"))