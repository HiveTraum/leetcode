import pytest
from line_profiler_pycharm import profile


class Solution:
    opening_parenthesis = {
        "{": "}",
        "(": ")",
        "[": "]"
    }

    @profile
    def isValid(self, s: str) -> bool:
        stack = []
        for token in s:
            if token in self.opening_parenthesis:
                stack.append(token)
            else:
                if len(stack) == 0:
                    return False

                if self.opening_parenthesis.get(stack.pop()) != token:
                    return False

        return len(stack) == 0


solution = Solution()

cases = (
    ("[]", True),
    ("[)", False),
    ("[(", False),
    ("[((((]]", False),
    ("[({})]", True),
    ("[{(})]", False),
    ("]", False)
)


@pytest.mark.parametrize(("s", "expected"), cases)
def test_valid_parenthesis(s: str, expected: bool):
    assert solution.isValid(s) == expected


if __name__ == '__main__':
    for data, _ in cases:
        solution.isValid(data)
