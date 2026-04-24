class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        conversion_value_1 = 10 ** (len(num1) - 1)
        int_1 = 0
        for digit in num1:
            int_1 += (ord(digit) - 48) * conversion_value_1
            conversion_value_1 //= 10
        
        conversion_value_2 = 10 ** (len(num2) - 1)
        int_2 = 0
        for digit in num2:
            int_2 += (ord(digit) - 48) * conversion_value_2
            conversion_value_2 //= 10
        
        return str(int_1 * int_2)
        