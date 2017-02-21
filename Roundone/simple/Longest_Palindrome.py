class Solution(object):
    def __init__(self):
        self.mem={}
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i in s:
            self.mem[i]=1+self.mem.get(i,0)
        for key in self.mem:
            res+=self.mem[key]-self.mem[key]/2
        if res>=len(s):
            return res
        return res+1
