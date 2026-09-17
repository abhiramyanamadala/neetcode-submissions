class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        e = ""

        for i in s:
            if i.isalnum():
                e += i.lower()

        return e == e[::-1]
        