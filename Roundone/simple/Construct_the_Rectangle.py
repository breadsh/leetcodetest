__author__ = 'jiangxiaowei-006'
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        min=area
        retL=0
        retW=0
        for i in range(1,(area/2)+2):
            if area%i==0:
                L=area/i
                W=area/L
                if L<W:
                    L,W=W,L
                if (L-W)<min:
                    retL=L
                    retW=W
                    min=L-W
        return [retL,retW]

if __name__=="__main__":
    s=Solution()
    print s.constructRectangle(1)