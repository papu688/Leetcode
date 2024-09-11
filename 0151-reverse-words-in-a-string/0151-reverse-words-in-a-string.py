class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()

        reversed_word = s[::-1]

        return (' '.join(reversed_word))
            