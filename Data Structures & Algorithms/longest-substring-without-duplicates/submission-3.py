class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        k = set()
        left = 0
        maxi = 0

        for right in range(len(s)):
            while s[right] in k:
                k.remove(s[left])
                left += 1

            k.add(s[right])
            maxi = max(maxi, right - left + 1)

        return maxi