__author__ = 'jiangxiaowei-006'
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if b==0:
            return a
        else:
            return self.getSum(a^b, (a&b)<<1)

if __name__=='__main__':
    s=Solution()
    print s.getSum(5,9)
    #print sum(2,3)