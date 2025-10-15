# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26) ]
        self.is_end=False
        self.val=0

# class Trie:

#     def __init__(self):
#         self.root=TrieNode()

#     def insert(self, word: str) -> None:
#         cur=self.root
#         for char in word:
#             idx=ord(char)-ord("a")
#             if cur.children[idx] is None:
#                 cur.children[idx]=TrieNode()
#             cur=cur.children[idx]
#         cur.is_end=True
        

#     def search(self, word: str) -> bool:
#         cur=self.root
#         for char in word:
#             idx=ord(char)-ord("a")
#             if cur.children[idx] is None:
#                 return False
#             cur=cur.children[idx]
#         return cur.is_end

class MapSum:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, key: str, val: int) -> None:
        cur=self.root
        for char in key:
            idx=ord(char)-ord("a")
            if cur.children[idx] is None:
                cur.children[idx]=TrieNode()
            cur=cur.children[idx]
            # cur.val+=val
        cur.is_end=True
        cur.val=val
        

    def sum(self, prefix: str) -> int:
        cur=self.root
        for char in prefix:
            idx=ord(char)-ord("a")
            if cur.children[idx] is None:
                return 0
            cur=cur.children[idx]
        ans=0
        stack=[cur]
        while stack:
            cur=stack.pop()
            ans+=cur.val
            for child in cur.children:
                if child:
                    stack.append(child)
        return ans
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)