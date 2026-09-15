class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        sorted_values = sorted(dic.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sorted_values[:k]]