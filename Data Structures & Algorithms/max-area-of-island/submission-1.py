class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        area = 0

        h = len(grid)
        w = len(grid[0])


        def dfs(island):
            i,j = island
            if (i >= h or i < 0 or j >= w or j < 0 or grid[i][j] == 0):
                return 0

            # print(i,j)

            grid[i][j] = 0
            
            return (1 + dfs([i+1,j]) + dfs([i-1,j]) + dfs([i,j+1]) + dfs([i,j-1]))


        for i in range(h):
            for j in range(w):
                # if grid[i][j] == 1:
                area = dfs([i,j])
                res = max(res, area)

        return res

            
            
        