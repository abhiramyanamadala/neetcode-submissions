class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = {}

        for i in range(len(strs)):
            t = tuple(sorted(strs[i]))

            if t not in dic:
                dic[t] = [strs[i]]
            else:
                dic[t].append(strs[i])

        return list(dic.values())