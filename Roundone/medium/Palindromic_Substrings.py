class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=0
        for i in range(len(s)+1):
            for j in range(i):
                if s[j:i]==s[j:i][::-1]:
                    n+=1
        return n