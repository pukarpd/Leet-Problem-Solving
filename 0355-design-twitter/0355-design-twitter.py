class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}      # userId -> list of (time, tweetId)
        self.followers = {}   # followerId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # who we care about
        following = self.followers.get(userId, set())
        following.add(userId)

        # push most recent tweet of each followed user
        for uid in following:
            if uid in self.tweets:
                idx = len(self.tweets[uid]) - 1
                time, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (time, tid, uid, idx))

        # k-way merge (only 10 pops)
        while heap and len(res) < 10:
            time, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)

            # push next older tweet from same user
            if idx > 0:
                next_time, next_tid = self.tweets[uid][idx - 1]
                heapq.heappush(heap, (next_time, next_tid, uid, idx - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set()
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers:
            self.followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)