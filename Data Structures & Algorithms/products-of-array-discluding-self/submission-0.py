class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        zero_count = 0
        has_zero = False
        if 0 in nums:
            has_zero = True
 
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num
        
        for num in nums:
            if has_zero and num != 0:
                result.append(0)
            elif zero_count >= 2:
                result.append(0)
            else:
                if num == 0:
                    result.append(product)
                else:
                    result.append(product // num)
        return result