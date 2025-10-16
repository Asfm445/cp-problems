# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [ None for _ in range(26) ]
        self.is_end=False


class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        cur=self.root
        for char in word:
            idx=ord(char)-ord("a")
            if cur.children[idx] is None:
                cur.children[idx]=TrieNode()
            cur=cur.children[idx]
        cur.is_end=True
        

    def search(self, word: str) -> bool:
        cur=self.root
        i=0
        que=deque()
        que.append(cur)
        while que:
            n=len(que)
            
            for _ in range(n):
                cur=que.popleft()
                char=word[i]
                if i==len(word)-1:
                    if char==".":
                        for child in cur.children:
                            if child and child.is_end:
                                return True
                        continue
                    idx=ord(char)-ord("a")
                    if cur.children[idx] and cur.children[idx].is_end:
                        return True
                    continue
                    
                if char==".":
                    for child in cur.children:
                        if child:
                            # if i==len(word)-1 and 
                            que.append(child)
                else:
                    idx=ord(char)-ord("a")
                    if cur.children[idx] is None:
                        continue
                    que.append(cur.children[idx])
            i+=1
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)