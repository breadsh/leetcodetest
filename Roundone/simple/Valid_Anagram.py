class Solution(object):
    def __init__(self):
        self.mems={}
        self.memt={}
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ##AC but need to make more faster
        if len(s)!=len(t): return False
        for x in s:
            self.mems[x]=self.mems.get(x,0)+1
        for x in t:
            self.memt[x]=self.memt.get(x,0)+1
        for key in self.mems:
            if self.mems[key]!=self.memt.get(key,0):
                return False
        return True
