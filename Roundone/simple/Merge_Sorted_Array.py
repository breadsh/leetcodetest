__author__ = 'jiangxiaowei-006'
import copy
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        a=[]
        if m==0:
            nums1.pop()
            for i in range(n):
                nums1.insert(i,nums2[i])
            return
        while i<n:
            if nums1[j]>nums2[i]:
                nums1.insert(j,nums2[i])
                i+=1
            j+=1
            if j>=m:
                for k in range(i,len(nums2)):
                    nums1.append(nums2[k])
                break

if __name__=='__main__':
    s=Solution()
    nums1=[0]
    m=0
    nums2=[1]
    n=len(nums2)
    s.merge(nums1,m,nums2,n)
    print nums1

