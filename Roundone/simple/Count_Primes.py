__author__ = 'jiangxiaowei-006'
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        ret=[True for i in range(n)]
        ret[0]=False
        ret[1]=False
        for i in range(2,int(n**0.5)+1):
            if ret[i]:
                ret[i*i:n:i]=[False] * len(ret[i*i:n:i])
        return ret.count(True)

if __name__=='__main__':
    s=Solution()
    print s.countPrimes(10)
