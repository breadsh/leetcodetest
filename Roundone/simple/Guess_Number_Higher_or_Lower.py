# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    if num==6:
        return 0
    if num<6:
        return 1
    if num>6:
        return -1

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        maxnum=n
        minnum=1
        while 1:
            i=n//2
            res=guess(i)
            if res==0:
                return i
            elif res==-1:
                maxnum=i
                n=i+minnum
            else:
                if i>minnum:
                    minnum=i
                n=i+1+maxnum

if __name__=='__main__':
    s=Solution()
    print s.guessNumber(20)