from typing import List

import pytest


# TODO: Переделать т.к. плохие результаты
#  Success:
# 	Runtime:60 ms, faster than 26.56% of Python3 online submissions.
# 	Memory Usage:14.8 MB, less than 32.20% of Python3 online submissions.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_bound = 0
        right_bound = len(nums) - 1

        if target < nums[left_bound]:
            return 0

        if target > nums[right_bound]:
            return right_bound + 1

        while True:
            if (right_bound - left_bound) <= 1:
                if nums[left_bound] == target:
                    return left_bound
                else:
                    return right_bound

            center = (right_bound - left_bound) // 2 + left_bound
            if nums[center] >= target:
                right_bound = center
            else:
                left_bound = center


solution = Solution()

cases = (
    ([1], 1, 0),
    ([0, 1, 2], 1, 1),
    ([1, 3, 5, 6], 7, 4),
    ([1, 3, 5, 6], 0, 0),
    ([0, 1, 2, 4, 7, 100], 4, 3),
    ([1, 5, 7, 10, 12, 16, 19], 19, 6),
)


@pytest.mark.parametrize(("nums", "target", "expected"), cases)
def test_search_insert_position(nums: List[int], target: int, expected: int):
    assert solution.searchInsert(nums, target) == expected
