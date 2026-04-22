class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        new_sum = 0
        for digit in str(n):
            new_sum += int(digit) ** 2
        
        while new_sum != 1:
            if new_sum in d:
                return False
            d.add(new_sum)
            newer_sum = 0
            for digit in str(new_sum):
                newer_sum += int(digit) ** 2

            new_sum = newer_sum
        
        return True