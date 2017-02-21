__author__ = 'jiangxiaowei-006'
class Solution(object):
    def __init__(self):
        self.countnum=0
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(reverse=True)
        s.sort()
        while g:
            if len(s)==0:
                return self.countnum
            child=g.pop()
            for x in s:
                if x>=child:
                    self.countnum+=1
                    s.remove(x)
                    break
        return self.countnum


if __name__=='__main__':
    greed=[1,2,3]
    size=[1,1]
    s=Solution()
    print s.findContentChildren(greed,size)
