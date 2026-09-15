class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lis = []
        r = max(len(word1),len(word2))
        for i in range(r):
            if i < len(word1):
                lis.append(word1[i])
            if i < len(word2):
                lis.append(word2[i])
        return ("".join(lis))