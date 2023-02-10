import pytest


def helper(index: int, value: list[str]):
    if index >= len(value) / 2:
        return

    opposite_index = -1 - index
    value[index], value[opposite_index] = value[opposite_index], value[index]
    helper(index + 1, value)


class Solution:
    def reverseString(self, s: list[str]) -> None:
        s[:] = s[::-1]


solution = Solution()


@pytest.mark.parametrize("s", (
        "Hello",
))
def test_recursive_reverse_print(s: str):
    array = list(s)
    expected = "".join(reversed(array))
    solution.reverseString(array)
    assert expected == "".join(array)


if __name__ == '__main__':
    Solution().reverseString(
        ["A", " ", "m", "a", "n", ",", " ", "a", " ", "p", "l", "a", "n", ",", " ", "a", " ", "c", "a", "n", "a", "l",
         ":", " ", "P", "a", "n", "a", "m", "a"]
    )

    print(["a", "m", "a", "n", "a", "P", " ", ":", "l", "a", "n", "a", "c", " ", "a", " ", ",", "n", "a", "l", "p", " ",
           "a", " ", ",", "n", "a", "m", " ", "A"])
