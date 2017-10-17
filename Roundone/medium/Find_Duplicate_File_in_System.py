from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        filedict=defaultdict(list)
        for x in paths:
            data=x.split()
            dirname=data[0]
            fldata=data[1:]
            for fl in fldata:
                filename,_,content=fl.partition('(')
                filedict[content[:-1]].append('/'.join([dirname,filename]))
        return [x for x in filedict.values() if len(x)>1]
