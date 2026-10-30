class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = collections.defaultdict(list)
        h = len(grid)
        w = len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                curr = i*w + j
                if grid[i][j] == "1":
                    m[curr]
                    if i+1 < h and grid[i+1][j] == "1":
                        m[curr].append(curr + w)
                    if i-1 >= 0 and grid[i-1][j] == "1":
                        m[curr].append(curr-w)
                    if j+1 < w and grid[i][j+1] == "1":
                        m[curr].append(curr + 1)
                    if j-1 >= 0 and grid[i][j-1] == "1":
                        m[curr].append(curr - 1)
                # grid[i][j] = 0
        # print(m)

        visited = set()

        def dfs(island):
            # print("island: ", island)
            
            if island in visited or island not in m:
                # print("return: ", island)
                return

            visited.add(island)

            for neighbor in m[island]:
                # print("neighbor: ", neighbor)
                dfs(neighbor)


        res = 0
        for island in m:
            if island not in visited:
                
                res += 1
                dfs(island)
                # print(m)

        return res

