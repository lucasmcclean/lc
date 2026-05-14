class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, [])

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.following.setdefault(userId, set())
        self.following[userId].add(userId)

        heap = []
        for fid in self.following[userId]:
            if fid not in self.tweets:
                continue

            tweets = self.tweets[fid]

            if not tweets:
                continue

            idx = len(tweets) - 1
            time, tid = tweets[idx]

            heapq.heappush_max(
                heap,
                (time, tid, fid, idx - 1)
            )

        feed = []
        while heap and len(feed) < 10:
            _, tid, fid, nxt = heapq.heappop_max(heap)

            feed.append(tid)

            if nxt >= 0:
                time, tid = self.tweets[fid][nxt]

                heapq.heappush_max(
                    heap,
                    (time, tid, fid, nxt - 1)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set())

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
