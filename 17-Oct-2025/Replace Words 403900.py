# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
        

    def search(self, word: str) -> bool:
        cur=self.root
        ans=[]
        for char in word:
            idx=ord(char)-ord("a")
            if cur.children[idx] is None:
                return ans if cur.is_end else []
            ans.append(char)
            cur=cur.children[idx]
            if cur.is_end:
                return ans
        return []



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie=Trie()
        for word in dictionary:
            trie.insert(word)
        
        ans=[]
        for word in sentence.split():
            re=trie.search(word)
            if re:
                ans.append("".join(re))
                # print(re)
            else:
                ans.append(word)
        return " ".join(ans)
        