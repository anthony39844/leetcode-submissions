class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list)
        self.following = defaultdict(set)
        self.counter = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId].append((self.counter, tweetId))
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId]
        following.add(userId)
        heap = []
        idx = -1

        while len(heap) <= 10:
            max_len = 0
            for user in following:
                tweets = self.userTweets[user]
                max_len = max(max_len, len(tweets))
                if len(tweets) < abs(idx):
                    continue
                heapq.heappush(heap, tweets[idx])
            if abs(idx) >= max_len:
                break
            idx -= 1
        
        out = []
        for i in range(min(10, len(heap))):
            out.append(heapq.heappop(heap)[1])

        return out
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
