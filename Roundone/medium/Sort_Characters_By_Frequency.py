from collections import defaultdict
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        sdict=defaultdict()
        for x in s:
            if sdict.has_key(x):
                sdict[x]+=1
            else:
                sdict[x]=1
        st=sorted(sdict.items(),key=lambda n:n[1],reverse=True)
        res=[]
        for x in st:
            for i in range(x[1]):
                res.append(x[0])
        return ''.join(res)