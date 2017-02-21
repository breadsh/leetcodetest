__author__ = 'jiangxiaowei-006'
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tmp=s+t
        beginone=ord(tmp[0])
        for i in range(1,len(tmp)):
            beginone^=ord(tmp[i])
        return chr(beginone)


