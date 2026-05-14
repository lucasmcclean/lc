class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, [])
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = [userId]
        users.extend(self.follows.get(userId, []))

        allTweets = []
        for uid in users:
            if uid in self.tweets and self.tweets[uid]:
                allTweets.append((len(self.tweets[uid]) -1, self.tweets[uid]))

        heap = []
        for i, (tweetsIdx, userTweets) in enumerate(allTweets):
            time, tweetId = userTweets[tweetsIdx]
            heapq.heappush_max(heap, (time, tweetId, i, tweetsIdx))

        res = []
        while heap and len(res) < 10:
            time, tweetId, i, tweetsIdx = heapq.heappop_max(heap)
            res.append(tweetId)
            if tweetsIdx > 0:
                prevIdx = tweetsIdx - 1
                time, tweetId = allTweets[i][1][prevIdx]
                heapq.heappush_max(heap, (time, tweetId, i, prevIdx))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows.setdefault(followerId, set())
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)
