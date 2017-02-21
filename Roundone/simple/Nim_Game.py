class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=3: return True
        ret=n-(n/3)*4
        if ret>0 and ret<=3:
            return True
        else:
            return False