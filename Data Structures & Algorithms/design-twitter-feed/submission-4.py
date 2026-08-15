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
            for t in self.tweets[f]:
                ti, tt = t
                heap.append((-tt, ti))
        heapq.heapify(heap)
        for _ in range(10):
            if len(heap) == 0:
                break
            _, ti = heapq.heappop(heap)
            feed.append(ti)
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_following[followerId].discard(followeeId)
