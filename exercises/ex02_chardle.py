"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730672220"


def input_word() -> str:
    input_word: str = input("Enter a 5-character word: ")
    if len(input_word) == 5:
        print("'" + input_word + "'")
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        print("'" + input_word + "'")

    return input_word


def input_letter() -> str:
    input_letter: str = input("Enter a single character: ")
    if len(input_letter) == 1:
        print("'" + input_letter + "'")
    else:
        print("Error: Character must be a single character.")
        exit()
        print("'" + input_letter + "'")
    return input_letter


def contains_char(word: str, letter: str) -> None:
    count: int = 0  # this counts instances
    print("Searching for " + letter + " in " + word)
    # parameters don't need def, keep contain_char parameters different to input funcs
    # was using indices as if loop but it's not
    # must manually check each index
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    if count >= 2:
        print(str(count) + " instances of " + letter + " found in " + word)
    if count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    # by adding these statements I can make sure it's gramatically correct
    if count == 0:
        print(str(count) + "No instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


# automatically handles function calls
if __name__ == "__main__":
    main()
# lets me run file as module and allows other modules to import function
