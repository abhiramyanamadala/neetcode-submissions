class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_set = set(nums)
        for num in my_set:
            x = target-num
            if x in my_set:
                arr = [num,target-num]
                break
        arr1 = []
        for i in range(len(nums)):
            if nums[i] == arr[0] or nums[i] == arr[1]:
                arr1.append(i)
        
        return(arr1)