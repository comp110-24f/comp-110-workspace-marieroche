"""Practice writing unit tests for functions"""

__author__ = "730466510"


# only_evens tests
from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


# expected outcome
def test_only_evens() -> None:
    nums: list[int] = [1, 3, 4, 6, 7, 8]
    result = only_evens(nums)
    assert result == [4, 6, 8]


# edge case
def test_only_evens_edge() -> None:
    nums: list[int] = []
    result = only_evens(nums)
    assert result == []
    assert nums == []


# show expected mutation
def test_only_evens_mutation() -> None:
    nums: list[int] = [1, 3, 4, 6, 7, 8]
    result = only_evens(nums)
    assert result == [4, 6, 8]
    assert nums == [1, 3, 4, 6, 7, 8]


# sub tests
# expected outcome
def test_sub() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    result = sub(a_list, start, end)
    assert result == [20, 30]


# edge case
def test_sub_edge() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 4
    end: int = 3
    result = sub(a_list, start, end)
    assert result == []


# show expected mutation
def test_sub_mutation() -> None:
    a_list: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    result = sub(a_list, start, end)
    assert result == [20, 30]
    assert a_list == [10, 20, 30, 40]


# add_at_index tests
# expected outcome
def test_add_at_index() -> None:
    list1 = [1, 2, 3, 5]
    num = 4
    idx = 3
    result = add_at_index(list1, num, idx)
    assert result == [1, 2, 3, 4, 5]


# show expected mutation
def test_add_at_index_mutation() -> None:
    list1 = [1, 2, 3, 5]
    num = 4
    idx = 3
    result = add_at_index(list1, num, idx)
    assert result == [1, 2, 3, 4, 5]
    assert list1 == [1, 2, 3, 4, 5]


# edge case/raise index error
def test_add_at_index_raises_indexerror():
    """Test that add_at_index raises an IndexError for an invalid index."""
    # your object to pass to add_at_index function
    list1 = [1, 2, 3, 5]
    num = 4
    idx = -1
    with pytest.raises(IndexError):
        add_at_index(list1, idx, num)
        # an IndexError is raised for the case when the add_at_index is given an idx
        # that is greater than the length of our num


if __name__ == "__main__":
    test_only_evens()
    test_only_evens_edge()
    test_only_evens_mutation()
    test_sub()
    test_sub_edge()
    test_sub_mutation()
    test_add_at_index()
    test_add_at_index_raises_indexerror()
    test_add_at_index_mutation()
    print("All tests passed!")
