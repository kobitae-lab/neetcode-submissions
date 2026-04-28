class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:    
        l = 0
        r = len(numbers) - 1

        while l <= r:
            left = 0
            right = len(numbers) - 1
            while left <= right:
                mid = (left + right) // 2
                complement = target - numbers[l]

                if numbers[mid] == complement:
                    return [l+1, mid+1]
                elif numbers[mid] > complement:
                    right = mid - 1
                else:
                    left = mid + 1
            l += 1