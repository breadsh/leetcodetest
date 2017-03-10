__author__ = 'jiangxiaowei-006'
import random
class Codec:
    def __init__(self):
        self.mem={}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        s='abcdefghijklmnopqrstuvwxyz0123456789'
        tiny=''
        for i in range(6):
            tiny+=random.choice(s)
        if tiny not in self.mem:
            self.mem[tiny]=longUrl
        return 'http://tinyurl.com/'+tiny
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        for key in self.mem:
            if key==shortUrl[-6:]:
                return self.mem[key]

if __name__=='__main__':
    c=Codec()
    tiny=c.encode('https://leetcode.com/problems/design-tinyurl')
    print tiny
    print c.decode(tiny)
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))