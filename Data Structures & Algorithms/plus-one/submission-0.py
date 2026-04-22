class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pos = len(digits) - 1
        L = []

        while pos >= 0 and digits[pos] == 9:
            pos -= 1
        
        digits[pos] += 1
        pos += 1
        while pos <= len(digits) - 1:
            digits[pos] = 0
            pos += 1

        if digits[0] == 0:
            L.append(1)
            for digit in digits:
                L.append(digit)
        else:
            return digits
        return L
