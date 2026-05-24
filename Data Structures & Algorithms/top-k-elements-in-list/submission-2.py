class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        result = []

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        print(d)
        for i in range(k):
            most_freq = max(d, key=d.get)
            result.append(most_freq)
            d.pop(most_freq)

        return result
