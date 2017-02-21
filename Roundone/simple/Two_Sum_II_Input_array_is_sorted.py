__author__ = 'jiangxiaowei-006'
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i in range(len(numbers)):
            y=target-numbers[i]
            if y in dic:
                return [dic[y]+1, i+1]
            dic[numbers[i]] = i





if __name__=='__main__':
    numbers=[2,3,4]
    s=Solution()
    print s.twoSum(numbers,6)