__author__ = 'jiangxiaowei-006'
class Solution(object):
    def __init__(self):
        self._mem=set()
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            if s[i] not in self._mem:
                self._mem.add(s[i])
                if s[i] not in s[i+1:]:
                    return i
        return -1



if __name__=='__main__':
    tests='cc'
    #print tests[0:2]+tests[3:]
    #print tests.find('c')
    s=Solution()
    print s.firstUniqChar(tests)