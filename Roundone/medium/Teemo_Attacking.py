class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        n=len(timeSeries)
        if n==0:
            return 0
        ressum=duration
        for i in xrange(n-1,0,-1):
            drtime=timeSeries[i]-timeSeries[i-1]
            if drtime<duration:
                ressum+=drtime
            else:
                ressum+=duration
        return ressum