from typing import List
import heapq


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        queue = []

        result = [0 for _ in range(len(T))]
        for i, item in enumerate(T):
            if not queue:
                heapq.heappush(queue, (item, i))
            else:
                while queue and queue[0][0] < item:
                    top = heapq.heappop(queue)
                    result[top[1]] = i - top[1]
                heapq.heappush(queue, (item, i))

        return result


class NewSolution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(T))]

        for i, item in enumerate(T):
            if stack:
                while stack and item > T[stack[-1]]:
                    top = stack[-1]
                    result[top] = i-top
                    stack.pop()
            stack.append(i)
        return result


if __name__ == '__main__':
    print(NewSolution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
    print(NewSolution().dailyTemperatures([73, 74]))