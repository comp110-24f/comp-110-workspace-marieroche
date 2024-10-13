"""Mutating functions."""

__author__ = "730466510"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(list_1: list[int], value: int) -> None:
    list_1.append(value)


manual_append(list_1, value=2)
print(list_1)


def double(list_2: list[int]) -> None:
    idx: int = 0
    while idx < len(list_2):
        list_2[idx] *= 2
        idx += 1


print(double(list_2))
print(list_1)
print(list_2)
