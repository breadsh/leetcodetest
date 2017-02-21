__author__ = 'jiangxiaowei-006'
class Solution(object):
    def __init__(self):
        self.memm={}
        self.memr={}
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for x in magazine:
            self.memm[x]=self.memm.get(x,0)+1
        for x in ransomNote:
            self.memr[x]=self.memr.get(x,0)+1
        for key in self.memr:
            if self.memr[key]>self.memm.get(key,0):
                return False
        return True