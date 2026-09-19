class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        lis = []

        for i in range(len(nums)):
            if target-nums[i] not in dic:
                dic[nums[i]] = i
            elif target-nums[i] in dic:
                value = target-nums[i]
                lis.append(dic.get(value)) 
                lis.append(i)
        return lis

