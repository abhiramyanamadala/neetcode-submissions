from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}


        for n in nums:
            if n not in count:
                count[n] = 1
            else :
                count[n] += 1

        buckets = [[] for _ in range (len(nums)+1)]

        for num,count in count.items():
            buckets[count].append(num)

        ans = []
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans 
                


