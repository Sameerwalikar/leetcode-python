#using dictionary to count the frequency of each number and return the one that appears only once
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic={}
        for i in nums:
            dic[i]=dic.get(i,0)+1
        for key,value in dic.items():
            if(value==1):
                return key