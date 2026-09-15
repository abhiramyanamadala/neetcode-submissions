class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dic = {}

        for num in nums :
            if num not in dic.keys() :
                dic[num] = 1
            else :
                dic[num] += 1
        


        sorted_values = dict(sorted(dic.items(), key=lambda item: item[1],reverse = True))

        lis = list(sorted_values.keys())[:k]
        return lis
        

        
