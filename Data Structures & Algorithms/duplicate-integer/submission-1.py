class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = set()

        for i in range(len(nums)):
            if nums[i] not in a:
                a.add(nums[i])
            elif nums[i] in a:
                return True 
        return False
