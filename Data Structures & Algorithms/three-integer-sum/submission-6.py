class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range(len(nums) - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            r = len(nums) - 1

            while j < r:

                total = nums[i] + nums[j] + nums[r]

                if total == 0:
                    res.append([nums[i], nums[j], nums[r]])

                    j += 1
                    r -= 1

                    # Skip duplicate second elements
                    while j < r and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate third elements
                    while j < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total > 0:
                    r -= 1

                else:
                    j += 1

        return res