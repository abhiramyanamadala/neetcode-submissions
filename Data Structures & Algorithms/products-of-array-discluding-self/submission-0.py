class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr =[1]

        for i in range(len(nums)) :
            if i == 0:
                pass
            else :
                pr.append(pr[i-1]*nums[i-1])

        sr = [1]
        m = len(nums)-1

        for j in range(len(nums)-1,0,-1):
            sr.append(sr[m-j]*nums[j])
        
        res = []
        
        for k in range(len(sr)):
            res.append(pr[k]*sr[m-k])
        
        return(res)