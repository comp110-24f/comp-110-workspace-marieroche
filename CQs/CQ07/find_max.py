__author__ = "730466510"


def find_and_remove_max(a: list[int]) -> int:
    if len(a) == 0:
        return -1
    max_val: int = a[0]  # counting variable
    for num in a:
        if num > max_val:
            max_val = num
    idx: int = 0
    while idx < len(a):
        if a[idx] == max_val:
            a.remove(max_val)
        else:
            idx += 1
    return max_val


a: list[int] = [10, 9, 8, 7, 10]
print(find_and_remove_max(a))
print(a)
