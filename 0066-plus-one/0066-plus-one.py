class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ls = []

        str_nums = "".join(map(str, digits))

        result = str(int(str_nums) + 1)

        for num in result:
            ls.append(int(num))
        return ls