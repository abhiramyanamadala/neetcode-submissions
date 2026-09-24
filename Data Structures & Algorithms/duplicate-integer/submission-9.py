class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        empty_set = set()
        for i in range(len(nums)):
            if nums[i] not in empty_set:
                empty_set.add(nums[i])
            else :
                return True
        return False
       
