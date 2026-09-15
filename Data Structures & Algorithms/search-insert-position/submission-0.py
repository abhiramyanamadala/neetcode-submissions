class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[len(nums)-1] < target:
            return len(nums)
        if nums[0] > target :
            return 0
        
        for i in range(len(nums)):
            if target == nums[i]:
                return i
        
        for i in range(len(nums)-1):
            if target > nums[i] and target < nums[i+1]:
                return i+1