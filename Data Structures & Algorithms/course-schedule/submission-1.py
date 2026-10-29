class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for pair in prerequisites:
            adj[pair[0]].append(pair[1])

        visited = set()

        def dfs(course):
            if adj[course] == []:
                return True

            if course in visited:
                # print(course, visited)
                return False

            visited.add(course)
            
            for preq in adj[course]:
                if not dfs(preq):
                    return False

            adj[course] = []
            visited.remove(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True