class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        profit = 0
        min_num = nums[0]

        for i in range(len(nums)):
            if nums[i]-min_num > profit :
                profit = nums[i]-min_num
            min_num = min(min_num,nums[i])

        if profit >0:
            return profit
        else :
            return 0
        