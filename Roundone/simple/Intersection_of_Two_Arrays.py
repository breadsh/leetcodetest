__author__ = 'jiangxiaowei-006'
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)==0:
            return []
        return [x for x in set([x for x in nums1 if x in nums2])]

if __name__=="__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    s=Solution()
    print s.intersection(nums1,nums2)