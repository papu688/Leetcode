class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        new_digits = [str(num) for num in digits ]
        str_num = ''.join(new_digits)

        res = int(str_num) +1

        return [int(num) for num in str(res)]
            
