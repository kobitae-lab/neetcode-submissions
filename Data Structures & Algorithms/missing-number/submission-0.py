class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        for i in range(len(nums)):
            s ^= i ^ nums[i]
        return s