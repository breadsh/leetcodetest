__author__ = 'jiangxiaowei-006'
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        mem=[]
        mem.append(1)
        mem.append(2)
        for i in range(2,n):
            mem.append(mem[i-1]+mem[i-2])
        return mem[n-1]



if __name__=='__main__':
    s=Solution()
    print s.climbStairs(35)