"""Summing the elements of a list using different loops"""

__author__ = "730466510"


def w_sum(vals: list[float]) -> float:
    total = 0.0
    idx: int = 0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


print(w_sum([0.1, 3.2, 4.5]))


def f_sum(vals: list[float]) -> float:
    total = 0.0
    for elem in vals:
        total += elem
    return total


print(f_sum([0.1, 3.2, 4.5]))


def f_range_sum(vals: list[float]) -> float:
    total = 0.0
    for elem in range(0, len(vals)):
        total += vals[elem]
    return total


print(f_range_sum([0.1, 3.2, 4.5]))
