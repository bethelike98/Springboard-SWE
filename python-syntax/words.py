def print_upper_words(words):
    """
    Prints out each words in all uppercase.
    """
    for word in words:
        print(greeting.upper())

def print_upper_words_e(words):
    """
    Prints out each words in all uppercase that begin with e.
    """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())

def print_upper_words_all(words, must_start_with):
    """
    Prints out each words in all uppercase that begin with a set of letters passed in.
    """
    for word in words:
        for letter in must_start_with:
            if word.lower().startswith(letter.lower()):
                print(word.upper())

print_upper_words_all(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})