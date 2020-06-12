from typing import List
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adjancent = [[] for _ in range(numCourses)]

        for pre in prerequisites:
            indegrees[pre[0]] += 1
            adjancent[pre[1]].append(pre[0])

        queue = deque()
        for i, nums in enumerate(indegrees):
            if nums == 0:
                queue.append(i)

        while queue:
            q = queue.popleft()
            numCourses -= 1
            for node in adjancent[q]:
                indegrees[node] -= 1
                if not indegrees[node]:
                    queue.append(node)
        return False if numCourses else True




if __name__ == '__main__':
    print(Solution().canFinish(3, [[0,2],[1,2],[2,0]]))