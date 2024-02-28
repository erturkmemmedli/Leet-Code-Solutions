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

# Alternative solution

class TweetNode:
    def __init__(self, userId, tweetId, next = None, prev = None):
        self.userId = userId
        self.tweetId = tweetId
        self.next = next
        self.prev = prev

class TweetList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addTweet(self, tweet):
        if not self.head:
            self.head = tweet
            self.tail = tweet

        else:
            self.tail.next = tweet
            tweet.prev = self.tail
            self.tail = self.tail.next

class Twitter:

    def __init__(self):
        self.userTweetMap = defaultdict(set)
        self.userFollowMap = defaultdict(set)
        self.tweetList = TweetList()

    def postTweet(self, userId: int, tweetId: int) -> None:
        tweet = TweetNode(userId, tweetId)
        self.tweetList.addTweet(tweet)
        self.userTweetMap[userId].add(tweetId)
        self.userFollowMap[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        mostRecentTweets = []
        current = self.tweetList.tail

        while current and len(mostRecentTweets) < 10:
            if current.userId in self.userFollowMap[userId]:
                mostRecentTweets.append(current.tweetId)
            current = current.prev

        return mostRecentTweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollowMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.userFollowMap[followerId].discard(followeeId)

# Alternative solution

class ListNode:
    def __init__(self, tweet_id, time, prev=None, next=None):
        self.tweet_id = tweet_id
        self.time = time
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, node):
        if not self.head:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = self.tail.next


class Twitter:
    def __init__(self):
        self.follow_map = defaultdict(set)
        self.user_tweet_map = defaultdict(LinkedList)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        node = ListNode(tweetId, self.timestamp)
        self.user_tweet_map[userId].insert(node)
        self.timestamp += 1
        self.follow_map[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        print(self.user_tweet_map)
        print(self.follow_map)
        heap = []
        output = []

        if userId not in self.follow_map:
            return []

        for user in self.follow_map[userId]:
            if user in self.user_tweet_map:
                node = self.user_tweet_map[user].tail
                time = node.time
                heappush(heap, (-time, node))
        
        while heap and len(output) < 10:
            _, node = heappop(heap)
            id = node.tweet_id
            if node.prev:
                time = node.prev.time
                heappush(heap, (-time, node.prev))
            output.append(id)
        
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
