__author__ = 'jiangxiaowei-006'
class Solution(object):
    def __init__(self):
        self.ret=''
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        sa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        i=(n-1)%26
        self.ret=sa[i]+self.ret
        x=(n-1)/26
        if x!=0:
            self.convertToTitle(x)
        return self.ret
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        sa='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ret=0
        for x in s:
           ret=ret*26+(sa.index(x)+1)
        return ret
if __name__=='__main__':
    s=Solution()
    print s.convertToTitle(728)
    print s.titleToNumber('AAZ')

