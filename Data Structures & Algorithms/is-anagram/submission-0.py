class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for i in s:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for k in t:
            if k not in d2:
                d2[k] = 1
            else:
                d2[k] += 1

        return d1 == d2
        