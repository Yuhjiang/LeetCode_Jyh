class TrieNode:
    def __init__(self):
        self._links = [None for _ in range(26)]
        self.end = False

    def __contains__(self, item):
        return self._links[ord(item)-ord('a')] is not None

    def __getitem__(self, item):
        return self._links[ord(item) - ord('a')]

    def __setitem__(self, key, value):
        self._links[ord(key)-ord('a')] = value

    def set_end(self):
        self.end = True

    def is_end(self):
        return self.end


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if w not in node:
                node[w] = TrieNode()
            node = node[w]
        node.set_end()

    def search_prefix(self, word: str) -> TrieNode:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i, w in enumerate(word):
            if w in node:
                node = node[w]
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.search_prefix(prefix)
        return node is not None


class NewTrie:
    def __init__(self):
        self.node = {'#': False}

    def insert(self, word: str) -> None:
        node = self.node
        for w in word:
            if w not in node:
                node[w] = {'#': False}
            node = node[w]
        node['#'] = True

    def search_prefix(self, word: str):
        node = self.node
        for w in word:
            if w in node:
                node = node[w]
            else:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node['#']

    def startsWith(self, prefix: str) -> bool:
        node = self.search_prefix(prefix)
        return node is not None


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    word = 'hello'
    obj = NewTrie()
    # obj.insert('a')
    print(obj.search('a'))
    # param_2 = obj.search(word)
    # print(param_2)
    # param_3 = obj.startsWith('held')
    # print(param_3)