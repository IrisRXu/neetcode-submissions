class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        area = 0

        h = len(grid)
        w = len(grid[0])

        self.area = 0

        def dfs(island):
            i,j = island

            # print(i,j)

            if grid[i][j] == 0:
                return

            grid[i][j] = 0
            self.area += 1
            
            if i+1 < h and grid[i+1][j] == 1: 
                dfs([i+1,j])
            if i-1 >= 0 and grid[i-1][j] == 1: 
                dfs([i-1,j])
            if j+1 < w and grid[i][j+1] == 1: 
                dfs([i,j+1])
            if j-1 >= 0 and grid[i][j-1] == 1 : 
                dfs([i,j-1])

            return

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs([i,j])

                res = max(res, self.area)

        return res

            
            
        