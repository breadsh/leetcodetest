__author__ = 'jiangxiaowei-006'
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        retlst=[]
        for i in range(1,n+1):
            if (i%3==0) and (i%5==0):
                retlst.append('FizzBuzz')
            elif i%3==0:
                retlst.append('Fizz')
            elif i%5==0:
                retlst.append('Buzz')
            else:
                retlst.append(str(i))
        return retlst

