class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        L = []
        current_index = 0

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in d:
                L[d[sorted_word]].append(word)
            else:
                L.append([word])
                d[sorted_word] = current_index
                current_index += 1

        return L


