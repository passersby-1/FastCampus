def solution(words, queries):
    class Node:
        def __init__(self, key):
            self.key = key
            self.dp = dict()
            self.children = dict()

    class Trie:
        def __init__(self):
            self.head = Node(None)
        
        def insert(self, word):
            length = len(word)

            curr = self.head
            while length > 0:
                for c in word:
                    if c not in curr.children:
                        curr.children[c] = Node(c)
                    if length not in curr.dp:
                        curr.dp[length] = 0
                    
                    curr.dp[length] += 1
                    length -= 1
                    curr = curr.children[c]
            curr.children['*'] = Node('*')

        def search_count(self, prefix):
            length = len(prefix)

            curr = self.head
            for c in prefix:
                if c == '?':
                    return curr.dp[length] if length in curr.dp else 0
                elif c in curr.children:
                    curr = curr.children[c]
                    length -= 1
                else:
                    return 0

            return 1 if '*' in curr.children else 0

    trie = Trie()
    reverse_trie = Trie()
    for word in words:
        trie.insert(word)
        reverse_trie.insert(word[::-1])

    ans = []
    for query in queries:
        if query[0] == '?':
            ans.append(reverse_trie.search_count(query[::-1]))
        else:
            ans.append(trie.search_count(query))

    return ans

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))