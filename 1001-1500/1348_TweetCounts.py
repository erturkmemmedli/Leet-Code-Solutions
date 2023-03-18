from sortedcontainers import SortedList
from collections import defaultdict

class TweetCounts:
    def __init__(self):
        self.tweets = defaultdict(SortedList)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].add(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        time_chunks = []

        if freq == 'minute':
            for i in range(startTime, endTime + 1, 60):
                left = self.tweets[tweetName].bisect_left(i)
                right = self.tweets[tweetName].bisect_left(min(endTime + 1, i + 60))
                time_chunks.append(right - left)

        if freq == 'hour':
            for i in range(startTime, endTime + 1, 3600):
                left = self.tweets[tweetName].bisect_left(i)
                right = self.tweets[tweetName].bisect_left(min(endTime + 1, i + 3600))
                time_chunks.append(right - left)

        if freq == 'day':
            for i in range(startTime, endTime + 1, 86400):
                left = self.tweets[tweetName].bisect_left(i)
                right = self.tweets[tweetName].bisect_left(min(endTime + 1, i + 86400))
                time_chunks.append(right - left)

        return time_chunks

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
