__author__ = "730466510"

from CQs.CQ07.find_max import find_and_remove_max


# use case test
def test_return_value() -> None:  # should return the largest number in the list
    a: list[int] = [1, 2, 5, 6, 9]
    result = find_and_remove_max(a)
    assert result == 9


# use case test 2
def test_mutate_list() -> None:  # should remove the largest number in the list
    a: list[int] = [1, 2, 5, 6, 9]
    find_and_remove_max(a)
    assert a == [1, 2, 5, 6]


# edge case
def test_empty_list() -> None:  # should return -1 for an empty list
    a: list[int] = []
    result = find_and_remove_max(a)
    assert result == -1
    assert a == []  # expect empty list to remain unchanged


if __name__ == "__main__":
    test_return_value()
    test_mutate_list()
    test_empty_list()
    print("All tests passed!")
