# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

class TrieNode:
    __slots__ = ('indexes', 'nexts')
    def __init__(self):
            self.indexes = set()
            self.nexts = defaultdict(TrieNode)
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = TrieNode()
        self.suffix = TrieNode()
        words_set = set()
        indexed_words = []
        i = len(words)
        for word in reversed(words):
            i-=1
            if word in words_set:
                continue
            indexed_words.append((i, word))
            words_set.add(word)
        for i, word in indexed_words:
            self._add_to_trie(self.prefix, word, i)
            self._add_to_trie(self.suffix, reversed(word), i)

    def _add_to_trie(self, node, word, index):
        i = node
        for ch in word:
            i = i.nexts[ch]
            i.indexes.add(index)

    def _get_indexes(self, node, word):
        i = node
        for ch in word:
            i = i.nexts.get(ch)
            if i is None:
                return set()
        return i.indexes

    def f(self, pref: str, suff: str) -> int:
        pre = self._get_indexes(self.prefix, pref)
        suf = self._get_indexes(self.suffix, reversed(suff))
        inter = pre.intersection(suf)
        return max(inter) if inter else -1