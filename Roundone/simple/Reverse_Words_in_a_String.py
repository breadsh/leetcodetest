__author__ = 'jiangxiaowei-006'
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=s.split()
        lst.reverse()
        return ' '.join(lst)

if __name__=='__main__':
    tc="the sky is blue"
    s=Solution()
    print s.reverseWords(tc)
