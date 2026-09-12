class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dictionary = set(wordList)
        if endWord not in dictionary:
            return 0
        if len(endWord) != len(beginWord):
            return 0

        for chunk in dictionary:
            if len(chunk) != len(beginWord):
                dictionary.remove(chunk)

        
        queue = deque([(endWord, 1)])
        table = defaultdict(set)
        while queue:
            chunk, count = queue.popleft()
            for i in range(len(chunk)):
                for j in range(97, 123):
                    rc = chr(j)
                    nchunk = chunk[:i] + rc + chunk[i+1:]
                    if nchunk == beginWord:
                        return count + 1
                    if nchunk not in dictionary:
                        continue
                    elif nchunk == chunk:
                        continue
                    elif nchunk in table[chunk]:
                        continue
                    elif chunk in table[nchunk]:
                        continue
                    table[chunk].add(nchunk)
                    table[nchunk].add(chunk)
                    queue.append((nchunk, count+1))
        return 0

