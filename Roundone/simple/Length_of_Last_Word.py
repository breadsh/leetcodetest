__author__ = 'jiangxiaowei-006'
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.split()[-1:])==0:
            return 0
        return len(s.split()[-1:][0])

if __name__=='__main__':
    s=Solution()
    print s.lengthOfLastWord(' ')