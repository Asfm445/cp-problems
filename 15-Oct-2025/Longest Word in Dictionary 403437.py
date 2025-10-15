# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26) ]
        self.is_end=False

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
        cur.is_end=True
        

    def find(self):
        return self.find_helper(self.root)

    def find_helper(self,root):
        if not root:
            return ''
        ans=""
        for i in range(len(root.children)):
            child=root.children[i]
            if child and child.is_end:
                child_ans=chr(ord('a')+i)+self.find_helper(root.children[i])

                if len(child_ans)>len(ans):
                    ans=child_ans
                elif len(child_ans)==len(ans):
                    ans=min(ans,child_ans)
        return ans

        



    


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie=Trie()

        for word in words:
            trie.insert(word)
        return trie.find()