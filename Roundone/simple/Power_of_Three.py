__author__ = 'jiangxiaowei-006'
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        if (math.log10(n)/math.log10(3))%1==0:
            return True
        return False

if __name__=='__main__':
    s=Solution()
    print s.isPowerOfThree(0)