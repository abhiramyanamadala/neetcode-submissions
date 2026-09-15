class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nus = sorted(nums)
        for i in range(0,len(nus)-1):
            if nus[i] == nus[i+1]:
                return True

        return False