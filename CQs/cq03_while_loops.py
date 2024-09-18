"""Using a  while loop to iterate over a string"""

__author__ = "730466510"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index: int = 0
    while index < len(phrase):  # while loop to iterate over each character in phrase
        if phrase[index] == search_char:  # if current char = search_car, count increase
            count = count + 1
            index = index + 1
    return count


if __name__ == "__main__":
    print(num_instances(phrase="Hello", search_char="l"))
