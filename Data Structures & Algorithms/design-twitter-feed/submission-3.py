class Twitter:

    def __init__(self):
        self.user_following: Dict[int, Set[int]] = defaultdict(set)
        self.tweets: Dict[int, List[Tuple[int, int, int]]] = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        import time
        self.tweets[userId].append((tweetId, time.time(), userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        following = self.user_following[userId]
        following.add(userId)
        following_index = {idx: len(self.tweets[idx]) - 1 for idx in following}
        while len(feed) < 10:
            recent_twt = None
            for fi in following:
                most_recent = None
                uts = self.tweets[fi]
                fidx = following_index[fi]
                if fidx < 0:
                    continue
                twt = self.tweets[fi][fidx]
                if recent_twt is None or twt[1] > recent_twt[1]:
                    recent_twt = twt
            if recent_twt is None:
                break
            ti, tt, ui = recent_twt
            following_index[ui] -= 1
            feed.append(ti)
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].discard(followeeId)
