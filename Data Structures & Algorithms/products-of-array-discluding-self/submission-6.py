class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        product = 1
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            if num != 0 :
                product *= num 

        if count >= 2:
            for i in range(len(nums)):
                nums[i] = 0
            return nums
        elif count == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = product
                elif nums[i] != 0:
                    nums[i] = 0
            return nums
        elif count == 0 :
            for i in range(len(nums)):
                nums[i] = int(product/nums[i])
            return nums
