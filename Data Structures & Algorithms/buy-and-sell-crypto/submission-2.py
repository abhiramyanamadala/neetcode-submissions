class Solution:
    def maxProfit(self, nums: List[int]) -> int:

        mini = nums[0]
        profit = 0

        for i in range(len(nums)):
            if nums[i] - mini > profit:
                profit = nums[i]-mini
            mini = min(nums[i],mini)
        if profit >0:
            return profit
        else :
            return 0
        