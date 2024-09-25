def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:  # if letter is not char, or if not(msg[index]) == char
            copy += msg[index]  # add it to copy, or can write copy = copy + msg[index]
        index += 1  # index = index + 1
    return copy


# create a variable with the variable word and value yoyo
word: str = "yoyo"  # GLOBAL VARIABLE
# print result of function with word and y
print(remove_chars(msg=word, char="y"))  # using keyword arguments
# print result of fucntion with word and o
print(remove_chars(word, "o"))  # using positional arguments

# remove_char (msg="football", char="o") -> ftball
# print(remove_char(msg="football", char="o"))
# red dot on side is breakpoint which stops code from running. arrow in trailhead takes
# -you through memory diagram on the left side.
