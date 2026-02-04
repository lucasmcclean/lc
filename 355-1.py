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
        heap = []
        if userId in self.tweets:
            heap.extend(self.tweets[userId][-10:])

        if userId in self.follows:
            for f in self.follows[userId]:
                if f in self.tweets:
                    heap.extend(self.tweets[f][-10:])
        heapq.heapify_max(heap)

        feed = []
        while heap and len(feed) < 10:
            feed.append(heapq.heappop_max(heap)[1])

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows.setdefault(followerId, set())
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].remove(followeeId)
