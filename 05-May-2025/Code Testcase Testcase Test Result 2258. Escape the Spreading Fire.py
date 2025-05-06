class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        orQue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    orQue.append((i, j, 1))

        def check(t):
            time = 0
            que = deque(orQue)  # Create a new deque to avoid modifying the original
            visit = deepcopy(grid)
            # print(grid)

            def isBound(x, y):
                if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]):
                    return False
                if visit[x][y] == 3:
                    return -1
                return visit[x][y] == 0

            added = False
            if not que:
                que.append((0, 0, -1))
            while que:
                n = len(que)

                if time == t:
                    added = True
                    que.append((0, 0, -1))

                for _ in range(n):

                    # print(que)
                    i, j, id = que.popleft()

                    if i == len(grid) - 1 and j == len(grid[0]) - 1:
                        # print(visit, id)
                        if visit[i][j] == -1:
                            return time
                        else:
                            return False

                    for u, v in directions:
                        if isBound(i + u, j + v) == True or (
                            id == -1 and isBound(i + u, j + v) == -1
                        ):
                            if (
                                i + u == len(grid) - 1
                                and j + v == len(grid[0]) - 1
                                and id == 1
                            ):
                                que.append((i + u, j + v, 3))
                                visit[i + u][j + v] = 3
                                continue
                            que.append((i + u, j + v, id))
                            visit[i + u][j + v] = id
                if not added and len(que) == 0:
                    added = True
                    que.appendleft((0, 0, -1))

                time += 1
            return False

        # return check(0)
        # ans2 = check(3)
        # return [ans1, ans2]
        left = 1
        right = 10**9
        while left <= right:
            md = (right + left) // 2
            if check(md):
                left = md + 1
            else:
                right = md - 1
        ans = check(right)
        # if right
        # print(left, right)
        if ans:
            return right
        return -1
