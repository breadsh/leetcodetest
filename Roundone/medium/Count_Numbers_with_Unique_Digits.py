class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        choice=9
        res=1
        posichoi=1
        for i in range(min(n,10)):
            posichoi*=choice
            res+=posichoi
            if i>=1:
                choice-=1
        return res
