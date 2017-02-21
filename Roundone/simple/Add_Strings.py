class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def _adds(num1,num2):
            carry=0
            ret = ''
            onelen=len(num1)
            twolen=len(num2)
            for i in range(len(num2)-1,-1,-1):
                s=int(num2[i])+int(num1[i+onelen-twolen])+carry
                carry=0
                if s>=10:
                    ret=str(s)[1]+ret
                    carry=1
                else:
                    ret=str(s)+ret
            if onelen==twolen:
                if carry!=0:
                    ret=str(carry*10**onelen+int(ret))
                    carry=0
            else:
                for i in range(len(num1)-len(num2)-1,-1,-1):
                    if carry!=0:
                        if int(num1[i])+carry>=10:
                            ret=str(int(num1[i])+carry)[1]+ret
                            carry=1
                        else:
                            ret = str(int(num1[i]) + carry) + ret
                            carry=0
                    else:
                        ret=num1[i]+ret
                if carry!=0:
                    ret=str(carry*10**onelen+int(ret))
                    carry=0
            return ret
        if len(num1)>len(num2):
            return _adds(num1,num2)
        else:
            return _adds(num2,num1)
if __name__=="__main__":
    s=Solution()
    num1='9'
    num2='99'
    print s.addStrings(num2,num1)