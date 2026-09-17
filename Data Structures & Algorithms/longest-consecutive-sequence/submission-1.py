class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        lis = sorted(nums)

        longest = 1
        current = 1

        for i in range(len(lis) - 1):

            if lis[i] == lis[i + 1]:
                continue

            elif lis[i] + 1 == lis[i + 1]:
                current += 1

            else:
                current = 1

            longest = max(longest, current)

        return longest