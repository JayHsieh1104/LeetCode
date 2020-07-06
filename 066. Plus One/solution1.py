class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits:
            return [1]
        
        carry = 0
        if digits[-1] == 9:
            digits[-1] = 0
            carry = 1
            for i in range(len(digits)-2, -1, -1):
                if carry == 0:
                    break
                elif digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] = digits[i] + 1
                    carry = 0
            if carry == 1:
                digits = [1] + digits
        else:
            digits[-1] = digits[-1] + 1
        return digits