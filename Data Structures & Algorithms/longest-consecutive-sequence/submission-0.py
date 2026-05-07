class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)

        def count_sequence(i):
            count = 1
            while i+1 in hashSet:
                count += 1
                i += 1
            return count
            
        longest = 0    
        for i in nums:
            if i-1 not in hashSet:
                longest = max(count_sequence(i), longest)
        return longest