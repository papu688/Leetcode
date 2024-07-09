class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = lambda num1, num2 : int(num1) * int(num2)
        result = res(num1, num2)
        return str(result)