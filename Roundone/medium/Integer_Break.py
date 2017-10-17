class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1 for i in range(n+1)]
        dp[1]=1
        for i in range(2,n+1):

            for j in range(1,i):

                dp[i]=max(dp[i],max(j,dp[j])*max(i-j,dp[i-j]))
                print i
                print dp[i]
                print '-------------'
        print dp

        return dp[n]

if __name__=='__main__':
    n=9
    s=Solution()
    print s.integerBreak(n)