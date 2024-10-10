"""EX03 - Wordle - Creating my own Wordle."""

__author__ = "730672220"


def input_guess(secret_word_len: int) -> str:
    input_guess: str = input(f"Enter a {secret_word_len}-character word: ")
    while (
        len(input_guess) != secret_word_len
    ):  # while statement gets skipped over if false and just returns
        if len(input_guess) != secret_word_len:
            input_guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return input_guess


def contains_char(secret_word: str, char_search: str) -> bool:
    """search for a character in the word."""
    assert len(char_search) == 1
    index = 0
    while index <= len(secret_word) - 1:
        if secret_word[index] == char_search:
            return True
        else:
            index += 1
    return False  # return false if while loop never returns true


def emojified(guessed_word: str, real_word: str) -> str:
    """compare user guess and secret word"""
    assert len(guessed_word) == len(real_word)
    index = 0
    blocks: str = ""  # need something to concatenate boxes together
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index <= len(real_word) - 1:
        if contains_char(real_word, guessed_word[index]) is False:
            blocks += WHITE_BOX
        if contains_char(real_word, guessed_word[index]) is True:
            if real_word[index] == guessed_word[index]:
                blocks += GREEN_BOX
            if real_word[index] != guessed_word[index]:
                blocks += YELLOW_BOX
        index += 1
    return blocks


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn_number: int = 1
    while turn_number <= 6:  # don't need to create max_turns = 6 variable
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(
            len(secret)
        )  # needed to make a new variable and then use it to call emojified
        print(emojified(guessed_word=guess, real_word=secret))
        if guess == secret:
            return print(f"You won in {turn_number}/6 turns!")
        turn_number += 1
    if turn_number > 6:  # this if statement must be outside while loop
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
