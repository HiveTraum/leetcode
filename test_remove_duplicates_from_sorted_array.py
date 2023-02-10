from typing import List

import pytest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        current = None
        i = 0
        for num in nums:
            if num == current:
                continue

            current = num
            nums[i] = num
            i += 1

        return i


cases = (
    ([0, 1, 2], [0, 1, 2], 3),
    ([0, 1, 1], [0, 1], 2),
    ([], [], 0),
    ([1, 1, 1], [1], 1)
)

solution = Solution()


@pytest.mark.parametrize(("nums", "expected_nums", "expected_k"), cases)
def test_remove_duplicates_from_sorted_array(nums: List[int], expected_nums: List[int], expected_k: int):
    assert solution.removeDuplicates(nums) == expected_k
    assert nums[:expected_k] == expected_nums
