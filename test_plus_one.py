from typing import List

import pytest

# Success:
# 	Runtime:28 ms, faster than 92.84% of Python3 online submissions.
# 	Memory Usage:14 MB, less than 7.95% of Python3 online submissions.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        current_index = -1
        while True:
            value = digits[current_index]
            new_value = value + 1
            if new_value == 10:
                digits[current_index] = 0
                current_index = current_index - 1
                if len(digits) < (current_index * -1):
                    digits.insert(0, 0)
            else:
                digits[current_index] = new_value
                break

        return digits


solution = Solution()

cases = (
    ([1], [2]),
    ([9], [1, 0]),
    ([9, 9], [1, 0, 0]),
    ([1, 0], [1, 1]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([1, 2, 3], [1, 2, 4]),
)


@pytest.mark.parametrize(("digits", "expected"), cases)
def test_plus_one(digits: List[int], expected: List[int]):
    assert solution.plusOne(digits) == expected
