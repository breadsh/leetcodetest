class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return [(x,y) for x in nums1 for y in nums2 if x==y]

if __name__=='__main__':
    s=Solution()
    nums1=[1]
    nums2=[1,1]
    print s.intersect(nums1,nums2)