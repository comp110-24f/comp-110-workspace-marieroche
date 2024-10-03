"""Creating my own Wordle version"""

__author__ = "730466510"


# constants for emojis
WHITE_BOX: str = "\U00002B1C"  # not found
GREEN_BOX: str = "\U0001F7E9"  # correct char and placement
YELLOW_BOX: str = "\U0001F7E8"  # correct char wrong placement


def input_guess(secret_word_len: int) -> str:
    # prompt a guess, continue prompting until correct length
    """Test if user's guess is correct length"""
    guess_word: str = input(f"Enter a {secret_word_len} character word: ")
    # created an input function
    while len(guess_word) != secret_word_len:
        guess_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess_word


def contains_char(guess_word: str, char: str) -> bool:
    """Test each index of word to see if it contains char"""
    assert len(char) == 1
    idx: int = 0
    while idx < len(guess_word):
        if char == guess_word[idx]:
            return True
        idx += 1
    return False


def emojified(secret_word: str, guess_word: str) -> str:
    """Creating the emoji string"""
    assert len(guess_word) == len(secret_word)
    idx: int = 0
    emojis: str = ""  # new variable to add emoji boxes together
    while idx < len(secret_word):
        if guess_word[idx] == secret_word[idx]:  # when first letter is correct
            emojis += GREEN_BOX
        elif contains_char(guess_word, secret_word[idx]):  # when char is found in word
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX  # when letter is not found
        idx += 1  # increase index
    return emojis


def main(secret_word: str) -> None:
    """The entrypoint of the program and the main game loop"""
    turns: int = 1
    while turns <= 6:
        print(f"==Turn {turns}/6==")  # use function instead of concatenation
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            print(f"You won in {turns}/6 turns!")
            return None
        turns += 1
    if turns > 6:  # end turns
        print(f"X/{len(secret_word)+1} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret_word="light")
