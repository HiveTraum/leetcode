import math

import pytest


class Solution:
    @staticmethod
    def count_digits(x: int):
        count = 0

        while x != 0:
            x //= 10
            count += 1

        return count

    def get_reversed_decomposed_value(self, x: int, digits_count: int):
        for i in range(digits_count):
            expected_digits_count = digits_count - i
            minimum = 10 ** (expected_digits_count - 1)

            if x > minimum:
                a = 10 ** int(math.log10(x))
                b = x // a
                yield b
                x = x - a * b
            elif self.count_digits(x) == expected_digits_count:
                yield x
            else:
                yield 0

    @staticmethod
    def get_decomposed_value(x: int, digits_count: int):

        for _ in range(digits_count):
            if x < 10:
                yield x
                break
            else:
                yield x % 10
                x //= 10

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = self.count_digits(x)
        decomposed = self.get_decomposed_value(x, digits)
        reversed_decomposed = self.get_reversed_decomposed_value(x, digits)
        for first, second in zip(decomposed, reversed_decomposed):
            if first != second:
                return False
        return True


@pytest.mark.parametrize(("x", "expected"), (
        (121, True),
        (10, False),
        (-121, False),
        (313, True),
        (1001, True),
        (1000021, False),
        (11, True),
))
def test_palindrome_number(x: int, expected: bool):
    assert Solution().isPalindrome(x) == expected


@pytest.mark.parametrize(("x", "expected"), (
        (11, [1, 1]),
        (1001, [1, 0, 0, 1]),
        (1000021, [1, 0, 0, 0, 0, 2, 1]),
))
def test_palindrome_number_reversed_decomposed_number(x: int, expected: list[int]):
    solution = Solution()
    assert list(solution.get_reversed_decomposed_value(x, solution.count_digits(x))) == expected


@pytest.mark.parametrize(("x", "expected"), (
        (11, [1, 1]),
        (1001, [1, 0, 0, 1]),
        (1000021, [1, 2, 0, 0, 0, 0, 1])
))
def test_palindrome_number_decomposed_number(x: int, expected: list[int]):
    solution = Solution()
    assert list(solution.get_decomposed_value(x, solution.count_digits(x))) == expected
