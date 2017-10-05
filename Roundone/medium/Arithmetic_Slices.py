class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        j=0
        if len(A)<=2:
            return 0
        sum=A[1]-A[0]
        count=0
        for i in range(2,len(A)):
            if A[i]-A[i-1]==sum:
                j+=1
                count+=j
            else:
                sum=A[i]-A[i-1]
                j=0

        return count
