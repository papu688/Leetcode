class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0

        for char in s:
            current = d[char]
            if prev_value < current:
                total += current - 2 * prev_value
            else:
                total += current

            prev_value = current

        return total  