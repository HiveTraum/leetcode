import pytest


class Solution:
    digits = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        summ = 0
        enumeration = enumerate(s)
        for i, character in enumeration:
            value = self.digits.get(s[i:i + 2])
            try:
                if value is None:
                    value = self.digits.get(s[i])
                else:
                    next(enumeration)
            except StopIteration:
                pass

            summ += value

            i += 1

        return summ


@pytest.mark.parametrize(("x", "expected"), (
        ("I", 1),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
))
def test_roman_to_integer(x: str, expected: bool):
    assert Solution().romanToInt(x) == expected
