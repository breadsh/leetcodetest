class Solution(object):
    def __init__(self):
        self.hexdict={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        self.hexnum=''
        self.max=4294967295
    def getHexchar(self,num):
        if num>=10:
            ret=self.hexdict.get(num)
        else:
            ret=str(num)
        return ret
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num<0:
            numz=self.max+num+1
            return self.toHex(numz)
        if num<16:
            return self.hexnum+self.getHexchar(num)
        n=num/16
        if n<16:
            self.hexnum=self.hexnum+self.getHexchar(n)
        else:
            self.toHex(n)
        m=num%16
        if m<16:
            self.hexnum=self.hexnum+self.getHexchar(m)
            return self.hexnum
        else:
            self.toHex(m)

if __name__=="__main__":
    s=Solution()
    print s.toHex(-2)
