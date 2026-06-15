class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        queue = deque()
        queue.append(beginWord)

        words = set(wordList)
        if beginWord in words:
            words.remove(beginWord)

        path = 0
        while queue:
            print(queue, words)
            for i in range(len(queue)):
                w = queue.popleft()
                if w == endWord:
                    return path+1
                print(w, words)
                for l in range(len(w)):
                    for c in "abcdefghhijklmnopqrstuvwxyz":
                        new_word = w[:l]+c+w[l+1:]
                        if new_word in words:
                            queue.append(new_word)
                            words.remove(new_word)
            path += 1
        return 0