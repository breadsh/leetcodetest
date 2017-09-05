class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [bin(i)[2:].count('1') for i in xrange(num+1)]

if __name__=='__main__':
    s=Solution()
    print s.countBits(5)