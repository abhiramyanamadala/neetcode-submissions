class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dics1 = {}
        dics2 = {}

        for i in range(len(s1)):
            if s1[i] not in dics1:
                dics1[s1[i]] = 1
            else :
                dics1[s1[i]] += 1
        print(dics1)
        
        x= (len(s2)-len(s1))

        for i in range(x+1):
            if s2[i] in dics1 :
                dics2 = {}
                for j in range(i,i+len(s1)):
                    if s2[j] not in dics2:
                        dics2[s2[j]] = 1
                    else :
                        dics2[s2[j]] += 1
                print(dics2)
                if dics2 == dics1:
                    return True 
        
        return False