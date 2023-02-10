from typing import List

import pytest


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0

        for letters in zip(*strs):
            if len(set(letters)) == 1:
                i += 1
            else:
                break

        return strs[0][:i]


solution = Solution()


@pytest.mark.parametrize(("strs", "expected"), (
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        ([""], ""),
        (["a"], "a"),
))
def test_longest_common_prefix(strs: list[str], expected: str):
    assert solution.longestCommonPrefix(strs) == expected
