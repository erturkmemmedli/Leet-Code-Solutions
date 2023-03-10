from heapq import heappush, heappop

class Twitter:
    def __init__(self):
        self.followMap = collections.defaultdict(set)
        self.tweetMap = collections.defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        heappush(self.tweetMap[userId], (-self.timestamp, userId, tweetId))
        for person in self.followMap[userId]:
            heappush(self.tweetMap[person], (-self.timestamp, userId, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        answer, stack = [], []
        while len(answer) < 10 and len(self.tweetMap[userId]) > 0:
            time, user, tweet = heappop(self.tweetMap[userId])
            if user == userId or userId in self.followMap[user]:
                answer.append(tweet)
            stack.append((time, user, tweet))
        while stack:
            heappush(self.tweetMap[userId], stack.pop())
        return answer

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followMap[followeeId]:
            self.followMap[followeeId].add(followerId)
            for tweet in self.tweetMap[followeeId]:
                x, user, y = tweet
                if user == followeeId:
                    heappush(self.tweetMap[followerId], tweet)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followeeId].discard(followerId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
