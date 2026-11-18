class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        n = len(grid)
        m = len(grid[0])

        boxes = []

        q = deque()
        visit = set()
        level = 0

        
        dist = 0


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
                    # print(i,j)
        
        

        while q:
            levelsize = len(q)

            for _ in range(levelsize):
                x,y = q.popleft()

                grid[x][y] = min(grid[x][y], dist)
                for dr,dc in directions:
                    if x+dr < n and x+dr > -1 and y+dc < m and y+dc > -1 and grid[x+dr][y+dc] != -1 and grid[x+dr][y+dc] != 0 and (x+dr,y+dc) not in visit:
                        q.append((x+dr,y+dc))
                        visit.add((x+dr,y+dc))
            dist += 1


                    
