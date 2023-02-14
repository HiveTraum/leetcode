import pytest


# Success:
# 	Runtime:38 ms, faster than 30.78% of Python3 online submissions.
# 	Memory Usage:13.9 MB, less than 31.81% of Python3 online submissions.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        i = 0

        previous_was_space = True

        for symbol in s:
            if symbol == " ":
                previous_was_space = True
                continue

            if previous_was_space:
                previous_was_space = False
                i = 0

            i += 1

        return i


solution = Solution()

cases = (
    ("word", 4),
    (" fly me to the moon ", 4),
    ("luffy is still joyboy", 6)
)


@pytest.mark.parametrize(("s", "expected"), cases)
def test_length_of_last_word(s: str, expected: int):
    assert solution.lengthOfLastWord(s) == expected
