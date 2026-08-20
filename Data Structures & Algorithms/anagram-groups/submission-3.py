class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if d.get(sorted_word,0) == 0:
                d[sorted_word] = [strs[i]]
            else:
                d[sorted_word].append(strs[i])
        return list(d.values())