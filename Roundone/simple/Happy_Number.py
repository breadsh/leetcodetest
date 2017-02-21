class Solution(object):
    def __init__(self):
        self.mem=set()
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sumnum=0
        for n in str(n):
            sumnum=sumnum+int(n)**2
        if sumnum==1:
            return True
        elif sumnum in self.mem:
            return False
        else:
            self.mem.add(sumnum)
            return self.isHappy(sumnum)

if __name__=="__main__":
    s=Solution()
    a= s.isHappy(2)
    print a