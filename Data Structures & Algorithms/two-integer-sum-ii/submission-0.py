class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)) :
            if target-numbers[i] in dic:
                lis = []
                lis.append(dic.get(target-numbers[i]))
                lis.append(i+1)
                return lis
            else :
                dic[numbers[i]] = i+1
