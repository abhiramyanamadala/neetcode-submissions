class Solution(object):
    def isAnagram(self, s, t):
      
        if len(s) != len(t) :
            return False

        temp1 = sorted(list(s))
        temp2 = sorted(list(t))

        if temp1 == temp2:
            return True
        return False

