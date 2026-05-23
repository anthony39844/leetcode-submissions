class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1
        if userId not in self.tweets:
            self.tweets[userId] = []

        if len(self.tweets[userId]) == 10:
            self.tweets[userId].pop(0)
        
        self.tweets[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        jus_tweets = []
        tweets = []
        if userId in self.tweets:
            tweets = self.tweets[userId].copy()

        # For every follower of this userId, get their tweets too
        if userId in self.followers:
            for i in self.followers[userId]:
                tweets.extend(self.tweets.get(i, []))

        count = 0
        heapq.heapify_max(tweets)
        while count < 10 and len(tweets) > 0:
            jus_tweets.append(heapq.heappop_max(tweets)[1])
            count +=1
        
        return jus_tweets
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            if followerId not in self.followers:
                self.followers[followerId] = set()
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)

