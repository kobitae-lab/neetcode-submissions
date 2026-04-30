class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while 1 < len(stones):
            stones.sort(reverse = True)
            if stones[0] == stones[1]:
                stones.pop(0)
                stones.pop(0)
            else:
                stones[0] = stones[0] - stones[1]
                stones.pop(1)
        
        if len(stones) == 1:
            return stones[0]
        return 0