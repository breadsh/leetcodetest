class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        ss = (s + s)[1:-1]
        print ss
        return ss.find(s)!= -1


if __name__=='__main__':
    st='aaa'
    s=Solution()
    print s.repeatedSubstringPattern(st)

