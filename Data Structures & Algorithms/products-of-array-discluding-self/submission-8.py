class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total = 1 
        zeros = 0
        result = []

        for num in nums:
            if num == 0:
                zeros+=1
                if zeros > 1:
                    return [0]*len(nums)
            
            else:
                total *= num
        
        if zeros == 0:
            for num in nums:
                result.append(total//num)
        if zeros == 1:
            for num in nums:
                if num!=0:
                    result.append(0)
                else:
                    result.append(total)


        return result        
        