class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_lis = sorted(set(nums))
        nums[:] = new_lis
        return len(new_lis)