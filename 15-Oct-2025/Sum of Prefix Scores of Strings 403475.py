# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26) ]
        self.is_end=False
        self.count=0

class Trie:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for char in word:
            idx=ord(char)-ord("a")
            if cur.children[idx] is None:
                cur.children[idx]=TrieNode()
            cur=cur.children[idx]
            cur.count+=1
        cur.is_end=True
        

    def search(self, word: str) -> int:
        ans=0
        cur=self.root
        for char in word:
            idx=ord(char)-ord("a")
            if cur.children[idx] is None:
                return False
            cur=cur.children[idx]
            ans+=cur.count
        return ans






class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie=Trie()

        for word in words:
            trie.insert(word)
        ans=[]
        for word in words:
            ans.append(trie.search(word))
        return ans
        