class Solution(object):
    def __init__(self):
        self.bases7num=''
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0: return 0
        if num<0:
            ng=True
        else:
            ng=False
        num=abs(num)
        self.bases7num=str(num%7)+self.bases7num
        num=num/7
        if(num>=7):
            self.convertToBase7(num)
        elif num>0:
            self.bases7num=str(num)+self.bases7num
        if ng==True:
            return '-'+self.bases7num
        else:
            return self.bases7num
if __name__=="__main__":
    s=Solution()
    print s.convertToBase7(0)