"""EX02 - Chardle - A cute step in toward Wordle."""

__author__ = "730466510"


def input_word() -> str:
    pick_word: str = input("Enter a 5-character word: ")  # created an input function
    if len(pick_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()  # exited the program when the condition was not met
    return pick_word


def input_letter() -> str:
    pick_letter: str = input("Enter a single character: ")
    if len(pick_letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    return pick_letter


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0  # created variable to keep track of letter occurrence
    if word[0] == letter:  # used boolean to see if indexed letter = letter
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
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    if count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
