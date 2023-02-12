from typing import List

import pytest


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num is val:
                continue

            nums[i] = num
            i += 1

        return i


solution = Solution()


@pytest.mark.parametrize(("nums", "val", "expected_k", "expected_nums"), (
        ([1], 1, 0, []),
        ([0, 1, 2], 3, 3, [0, 1, 2]),
        ([0, 0, 0], 0, 0, []),
        ([2, 1, 5, 2, 1], 2, 3, [1, 5, 1]),
        ([], 1, 0, []),
))
def test_longest_common_prefix(nums: List[int], val: int, expected_k: int, expected_nums: List[int]):
    result = solution.removeElement(nums, val)
    assert result == expected_k
    assert nums[:result] == expected_nums
