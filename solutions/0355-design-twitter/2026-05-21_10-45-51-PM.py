class Twitter:

    def __init__(self):
        self.users = set()
        self.userTweets = defaultdict(list)
        self.following = defaultdict(set)
        self.counter = -1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users.add(userId)
        self.userTweets[userId].append((self.counter, tweetId))
        self.counter -= 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        following = self.following[userId]
        heap = []
        print(following)
        for user in following:
            tweets = self.userTweets[user]
            for tweet in tweets:
                heapq.heappush(heap, tweet)
        
        for tweet in self.userTweets[userId]:
            heapq.heappush(heap, tweet)

        return [x for t, x in heapq.nsmallest(min(10, len(heap)), heap)]
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        return

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
