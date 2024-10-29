"""Practice with Dictionary Functions"""

__author__ = "730466510"


def invert(my_dict: dict[str, str]) -> dict[str, str]:
    """Inverting keys and values."""
    inverted_dict: dict[str, str] = {}
    for key in my_dict:
        if my_dict[key] in inverted_dict:
            raise KeyError("You cannot have two identical values in your list!")
        inverted_dict[my_dict[key]] = key
    return inverted_dict


print(invert({"a": "z", "b": "y", "c": "x"}))


def favorite_color(favs: dict[str, str]) -> str:
    """Finding the color most people pick as their favorite in a dictionary"""
    most_popular: str = ""
    colors: list[str] = []
    for key in favs:
        colors.append(favs[key])
    frequencies: dict[str, int] = count(colors)
    a: int = 0
    for key in frequencies:
        if frequencies[key] > a:
            a = frequencies[key]
            most_popular = key
    return most_popular


def count(x: list[str]) -> dict[str, int]:
    """Finding the count of words in a dictionary"""
    amount: dict[str, int] = {}
    for key in x:
        if key in amount:
            amount[key] += 1
        else:
            amount[key] = 1
    return amount


def alphabetizer(x: list[str]) -> dict[str, list[str]]:
    """alphabetizing a list of strings"""
    result: dict[str, list[str]] = {}
    for word in x:
        key = word[0].lower()
        if key not in result:
            result[key] = []
        result[key].append(word)
    return result


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, name: str
) -> None:
    """updates the attendance record with days and corresponding names"""
    if day not in attendance_log:
        attendance_log[day] = []
    if name not in attendance_log[day]:
        attendance_log[day].append(name)
