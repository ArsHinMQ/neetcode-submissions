class Twitter:

    def __init__(self):
        self.user_following: Dict[int, Set[int]] = defaultdict(set)
        self.tweets: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        import time
        self.tweets[userId].append((tweetId, time.time()))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        following = self.user_following[userId]
        following.add(userId)
        heap = []
        for f in following:
            idx = len(self.tweets[f]) - 1
            if idx < 0:
                continue
            ti, tt = self.tweets[f][idx]
            heapq.heappush(heap, (-tt, ti, f, idx))

        while heap and len(feed) < 10:
            _, ti, ui, idx = heapq.heappop(heap)
            feed.append(ti)
            nidx = idx - 1
            if nidx < 0:
                continue
            nti, ntt = self.tweets[ui][nidx]
            heapq.heappush(heap, (-ntt, nti, ui, nidx))
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].discard(followeeId)
