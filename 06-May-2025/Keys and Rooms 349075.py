# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False for i in range(len(rooms))]
        que=deque()
        que.append(0)
        while que:
            room=que.pop()
            visited[room]=True
            for lock in rooms[room]:
                if not visited[lock]:
                    que.append(lock)
        for i in visited:
            if not i:
                return False
        return True



        