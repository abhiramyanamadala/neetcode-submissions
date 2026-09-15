class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = []
        for i in range(len(s)):
            if s[i].isalnum():
                s2.append(s[i].lower())
        print (s2)
        if s2 == s2[::-1]:
            return True
        else:
            return False