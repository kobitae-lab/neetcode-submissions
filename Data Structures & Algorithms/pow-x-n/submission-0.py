class Solution:
    def myPow(self, x: float, n: int) -> float:
        power_sum = 1
        i = 1
        while i <= n:
            power_sum *= x
            i += 1

        if n < 0:
            k = -1
            while k >= n:
                power_sum *= x
                k -= 1
            return 1 / power_sum
        else:   
            return power_sum