class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = []
        post = []
        fin =[]

        for _ in range(len(nums)):
            pre.append("_")
            post.append("_")
            fin.append("_")

        for i in range(len(nums)-1):
            if i == 0:
                pre[0] = nums[0]
            pre[i+1] = pre[i]*nums[i+1]
        
        for j in range(len(nums)-1,0,-1):
            if j == len(nums)-1:
                post[j] = nums[len(nums)-1]
            post[j-1] = post[j]*nums[j-1]
        


        for i in range(len(nums)):
            if i == 0:
                fin[i] = post[i+1]
            elif i == len(nums)-1:
                fin[i] = pre[i-1]
            else:
                fin[i] = pre[i-1]*post[i+1]

        return fin

    

