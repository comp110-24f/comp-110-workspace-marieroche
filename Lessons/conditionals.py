"""Practicing my conditionals."""


def less_than_10(num: int) -> bool:
    """Tell us if num < 10."""
    dub: int = num * 2  # 22
    dub = dub - 1  # 21
    print(dub)
    if num < 10:  # check if this is true
        print("Small number")  # "then" block
    else:
        print("Big number")
    print("This is the end of the function!")


less_than_10(num=11)


def wake_up(alarm: bool) -> str:
    """REturn a message based on if alarm is going off."""
    if alarm is True:
        return "Wake up! Go to Comp110!"
    else:
        return "Keep sleeping. You deserve it."


print(wake_up(alarm=False))


def check_first_letter(word: str, letter: str) -> str:
    """Checks if letter is first character of word."""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="s"))
