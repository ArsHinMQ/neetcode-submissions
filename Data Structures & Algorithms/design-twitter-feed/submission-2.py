class Twitter:

    def __init__(self):
        self.user_following: Dict[int, Set[int]] = defaultdict(set)
        self.tweets: List[Tuple(int, int)] = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        following = self.user_following[userId]
        for i in range(len(self.tweets) -1, -1, -1):
            ti, ui = self.tweets[i]
            if ui != userId and ui not in following:
                continue
            feed.append(ti)
            if len(feed) >= 10:
                break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].discard(followeeId)
