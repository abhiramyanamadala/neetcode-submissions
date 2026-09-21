class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res=[]
        for i in range(len(nums)):
            
            if i>0:
                if nums[i-1] ==nums[i]:
                    continue
            
            l,r=i+1,len(nums)-1

            while l<r:

                su = nums[i]+nums[l]+nums[r]

                if su > 0:
                    r=r-1
                
                elif su<0:
                    l=l+1
                
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1

        return res


        


