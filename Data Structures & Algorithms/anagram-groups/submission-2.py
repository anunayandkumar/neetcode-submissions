class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            if d.get(sorted_word,0) == 0:
                d[sorted_word] = [strs[i]]
            else:
                k = d[sorted_word]
                k.append(strs[i])
                d[sorted_word] = k    
        return list(d.values())