class Solution(object):
    def getint(self,a):
        anum = a.split('+')
        x1 = anum[0]
        y1 = anum[1][:-1]
        return int(x1),int(y1)
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x1,y1=self.getint(a)
        x2,y2=self.getint(b)
        x=x1*x2+(-1*y1*y2)
        y=x1*y2+x2*y1
        return str(x)+'+'+str(y)+'i'

if __name__=='__main__':
    a="1+1i"
    b="1+1i"
    s=Solution()
    print s.complexNumberMultiply(a,b)
