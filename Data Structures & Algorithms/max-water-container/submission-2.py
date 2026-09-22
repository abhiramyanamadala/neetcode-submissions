class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1
        maxi = 0
        while i<j:
            temp = min(height[i],height[j])*(j-i)
            maxi = max(temp,maxi)

            if height[i] < height[j]:
                i += 1
            elif height[j] <= height[i]:
                j -= 1
        
        return maxi