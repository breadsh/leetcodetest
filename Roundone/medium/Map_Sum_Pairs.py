from collections import defaultdict
class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.memdic=defaultdict()
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.memdic[str(key)]=val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sumnum=0
        for key,val in self.memdic.iteritems():
            if str(key).startswith(prefix):
                sumnum+=val
        return sumnum


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("aa",3)
print obj.sum("a")
obj.insert("aa",2)
print obj.sum("a")