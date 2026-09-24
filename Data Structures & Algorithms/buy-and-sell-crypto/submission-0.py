class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        temp =0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[j] - nums[i] >temp:
                    temp = nums[j]-nums[i]
        return temp