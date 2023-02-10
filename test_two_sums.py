from typing import List

import pytest as pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            expected_value = target - num
            for j, second_value in enumerate(nums[i + 1:]):
                if expected_value == second_value:
                    return [i, i + j + 1]


@pytest.mark.parametrize(("nums", "target", "expected"), (
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
))
def test_two_sums_solution(nums: List[int], target: int, expected: List[int]):
    assert Solution().twoSum(nums, target) == expected
