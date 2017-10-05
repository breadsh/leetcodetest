import collections
import heapq
class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._twtnews=collections.defaultdict(collections.deque)
        self._followmsg=collections.defaultdict(set)


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        def _postTweet(userId, tweetId,uid):
            if self._twtnews.has_key(userId):
                self._twtnews[userId].append([uid,tweetId])
            else:
                self._twtnews.setdefault(userId,[[uid,tweetId],])

        _postTweet(userId, tweetId,userId)
        if self._followmsg.has_key(userId):
            for us in self._followmsg[userId]:
                _postTweet(us,tweetId,userId)


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if len(self._twtnews.get(userId))>10:
            return [x[1] for x in self._twtnews.get(userId)[:10]]
        else:
            return [x[1] for x in self._twtnews.get(userId)]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if self._followmsg.has_key(followeeId):
            if followerId not in self._followmsg[followeeId]:
                self._followmsg[followeeId].append(followerId)
        else:
            self._followmsg.setdefault(followeeId,[followerId,])


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if self._followmsg.has_key(followeeId):
            if followerId in self._followmsg[followeeId]:
                self._followmsg[followeeId].remove(followerId)
        if self._twtnews.has_key(followerId) and self._twtnews.has_key(followeeId):
                self._twtnews[followerId]=[item for item in self._twtnews[followerId] if item not in self._twtnews[followeeId]]




        # Your Twitter object will be instantiated and called as such:
if __name__=='__main__':
    obj = Twitter()
    #obj.postTweet(userId,tweetId)
    print obj.postTweet(1, 5)
    #param_2 = obj.getNewsFeed(userId)
    param_2 = obj.getNewsFeed(1)
    print param_2
    #obj.follow(followerId,followeeId)
    print obj.follow(1, 2)
    print obj.postTweet(2, 6)
    print obj._followmsg
    print obj._twtnews
    param_3 = obj.getNewsFeed(1)
    print param_3
    print obj.unfollow(1,2)
    param_4=obj.getNewsFeed(1)
    print param_4
    #obj.unfollow(followerId,followeeId)