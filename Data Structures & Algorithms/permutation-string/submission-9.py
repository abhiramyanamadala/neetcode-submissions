class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        dics1 = {}
        dics2 = {}

        if (len(s1)>len(s2)):
            return False

        for c in alphabets:
            dics1[c] = 0
            dics2[c] = 0
        
        for c in s1 :
            dics1[c] += 1

        
        for i in range(len(s1)):
            dics2[s2[i]] += 1
        
        for i in range(len(s2)-len(s1)):
            if dics2 == dics1:
                return True
            temp = i+len(s1)
            dics2[s2[i]] -= 1
            dics2[s2[temp]] += 1

        if dics1 == dics2:
            return True
        
        return False
        
        