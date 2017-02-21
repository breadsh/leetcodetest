__author__ = 'jiangxiaowei-006'
class Solution(object):
    def __init__(self):
        self.rowone='qwertyuiop'
        self.rowtwo='asdfghjkl'
        self.rowthree='zxcvbnm'
        self.mem=set()
    def _findWords(self,word):
        if len(word)==1:
            return word
        def f(x):
            if x in self.rowone:
                return 1
            elif x in self.rowtwo:
                return 2
            else:
                return 3
        flag=False
        self.mem.clear()
        for w in word.lower():
            ret=f(w)
            if len(self.mem)==0:
                self.mem.add(ret)
            elif ret in self.mem:
                flag=True
                continue
            else:
                flag=False
                break
        if flag==True:
            return word
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        return filter(self._findWords,words)

if __name__=="__main__":
    s=Solution()
    testcase=["Hello", "Alaska", "Dad", "Peace"]
    print s.findWords(testcase)