class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        longest = 1
        count = 1

        lis = sorted(set(nums))

        for i in range(len(lis)-1):
            if lis[i] +1 == lis[i+1]:
                count += 1

            else :
                longest = max(longest,count)
                count =1
                
        return max(longest,count)