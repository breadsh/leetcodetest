__author__ = 'jiangxiaowei-006'
import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num - 1) % 3 == 0 and bin(num).count('1')==1 and num>0