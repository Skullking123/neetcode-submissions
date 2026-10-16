class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = [] # elms are (time, userID, tweetID)
        self.following = {} # (userId : set(following))

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, (-self.time, userId, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        processed = []
        while len(newsFeed) < 10 and self.tweets:
            time, posterId, tweetId = heapq.heappop(self.tweets)
            if (userId in self.following and posterId in self.following[userId]) or posterId == userId:
                newsFeed.append(tweetId)
            processed.append((time, posterId, tweetId))
        
        for tweet in processed:
            heapq.heappush(self.tweets, tweet)
        
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following or followeeId not in self.following[followerId]:
            return
        self.following[followerId].remove(followeeId)
