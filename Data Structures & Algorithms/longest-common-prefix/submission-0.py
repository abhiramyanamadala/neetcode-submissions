class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        strs.sort()
        first = strs[0]
        last = strs[-1]
        prefix = ""
        
        for i in range(len(first)):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break
        
        return prefix
