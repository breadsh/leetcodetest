__author__ = 'jiangxiaowei-006'
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:return True
        if num<=0:return False
        for x in [2,3,5]:
            while num%x==0:
                num=num/x
        return num==1

if __name__=='__main__':
    num=-2147483648
    s=Solution()
    print s.isUgly(num)

