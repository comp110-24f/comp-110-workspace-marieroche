def remove_chars(msg: str, char: str) -> str:
    """Return copy of message with all instances of char removed."""
    copy: str = ""  # set up empty string to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
        index += 1
    return copy


# if (
# __name__ == "__main__"
# adding this means it won't be run when importing into another file
# word: str = "yoyo"  # global variable
# print(remove_chars(word, char="y"))
# print(remove_chars(word, char="o"))
