"""Lists exercises"""

__author__ = "730466510"


def all(vals: list[int], num: int) -> bool:
    if len(vals) == 0:  # if list is empty, bool is false
        return False
    for item in vals:
        if item != num:  # test if all list values are equal to num
            return False
    return True


print(all([1, 2, 3], 1))


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_val: int = input[0]  # counting variable
    idx: int = 0  # indexing local variable
    while idx < len(input):
        if input[idx] > max_val:
            max_val = input[idx]  # max_val changes
        else:
            idx += 1
    return max_val


print(max([1, 3, 2]))


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    if len(list_1) != len(list_2):
        return False
    for nums in range(len(list_1)):
        if list_1[nums] != list_2[nums]:
            return False
    return True


print(is_equal([1, 0, 1], [1, 0, 1]))


def extend(a: list[int], b: list[int]) -> None:
    for elem in b:  # elems of second list added to first
        a.append(elem)  # add each elem to end of list


a = [1, 3, 5]
b = [2, 4, 6]
extend(a, b)
print(a)
