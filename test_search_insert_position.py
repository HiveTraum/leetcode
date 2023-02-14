from typing import List

import pytest


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_bound = 0
        right_bound = len(nums) - 1

        while left_bound <= right_bound:
            center = (left_bound + right_bound) // 2

            if nums[center] == target:
                return center
            elif nums[center] < target:
                left_bound = center + 1
            else:
                right_bound = center - 1

        return left_bound


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
