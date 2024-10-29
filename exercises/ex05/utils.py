"""Practice building list utility functions"""

__author__ = "730466510"


def only_evens(nums: list[int]) -> list[int]:
    idx: int = 0
    even_nums: list[int] = []
    if nums == []:
        return []
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            even_nums.append(nums[idx])
        idx += 1
    return even_nums


print(only_evens(nums=[1, 3, 4, 6, 7, 8]))


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    return_list: list[int] = []
    if start >= len(a_list) or end <= 0:
        return []
    if start < 0:
        start = 0
    if end > len(a_list):
        end = len(a_list)
    while start < end:
        return_list.append(a_list[start])
        start += 1
    return return_list


a_list = [10, 20, 30, 40]
print(sub(a_list, 1, 3))


def add_at_index(list1: list[int], num: int, idx: int) -> None:
    if idx < 0 or idx > len(list1) or list1 == []:
        raise IndexError("Index is out of bounds for the input list")
    else:
        list1.append(0)
        for elem in range(len(list1) - 1, idx, -1):
            list1[elem] = list1[elem - 1]
        list1[idx] = num


list1 = [1, 2, 3, 5]
add_at_index(list1, 4, 3)
print(list1)
