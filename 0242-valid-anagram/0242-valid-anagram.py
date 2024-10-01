class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_char = {}

        for char in s:
            if char in count_char:
                count_char[char] += 1
            else:
                count_char[char] = 1

        for char in t:
            if char in count_char:
                count_char[char] -= 1
            else:
                return False

        for count in count_char.values():
            if count != 0:
                return False
            
        return True
