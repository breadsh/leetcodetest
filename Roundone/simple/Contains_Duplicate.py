class Solution(object):
    def __init__(self):
        self.mem=set()
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for x in nums:
            self.mem.add(x)

        if len(nums)==len(self.mem):
            return True
        else:
            return False