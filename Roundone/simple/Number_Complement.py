__author__ = 'jiangxiaowei-006'

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret=''
        for i in bin(num)[2:]:
            if i!=None:
                if i=='1':
                    ret=ret+'0'
                else:
                    ret=ret+'1'
        i=len(ret)-1
        retnum=0
        for j in ret:
            #print j
            if j=='1':
                retnum=retnum+2**i
            i-=1
        return retnum
if __name__=="__main__":
    s=Solution()
    print s.findComplement(5)
