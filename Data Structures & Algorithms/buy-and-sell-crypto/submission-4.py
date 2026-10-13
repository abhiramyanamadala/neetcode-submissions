class Solution:
    def maxProfit(self, nums: List[int]) -> int:

        mini = nums[0]
        profit = 0
        for i in range(len(nums)):
            if mini > nums[i]:
                mini = nums[i]
            if nums[i]-mini > profit :
                profit = nums[i]-mini
                
        return profit
       
