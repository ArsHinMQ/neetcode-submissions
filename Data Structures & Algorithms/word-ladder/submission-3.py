class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary = set(wordList)
        if endWord not in dictionary:
            return 0
        if len(endWord) != len(beginWord):
            return 0

        
        queue = deque([(beginWord, 1)])
        while queue:
            chunk, count = queue.popleft()
            for i in range(len(chunk)):
                for j in range(97, 123):
                    rc = chr(j)
                    nchunk = chunk[:i] + rc + chunk[i+1:]
                    if nchunk == endWord:
                        return count + 1
                    if nchunk not in dictionary:
                        continue
                    queue.append((nchunk, count+1))
                    dictionary.remove(nchunk)
        return 0

