class Solution(object):
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
    st='AAZ'
    s=Solution()
    print s.titleToNumber(st)