from collections import defaultdict
class MagicDictionary(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.datadict=defaultdict()
    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for x in dict:
            self.datadict.setdefault(x,len(x))
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        for k,v in self.datadict.iteritems():
            diff=0
            res=False
            if v==len(word):
                for i in range(v):
                    if k[i]!=word[i]:
                        diff+=1
                        res=True
                        if diff>1:
                            res=False
                            break
                if res:
                    return res
        return False






        # Your MagicDictionary object will be instantiated and called as such:
        # obj = MagicDictionary()
        # obj.buildDict(dict)
        # param_2 = obj.search(word)