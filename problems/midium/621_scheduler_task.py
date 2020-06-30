from typing import List
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        times = [0] * 26

        for i in tasks:
            times[ord(i)-ord('A')] += 1

        times.sort()
        duration = 0
        while times[25] > 0:
            i = 0
            while i <= n:
                if times[25] == 0:
                    break
                if i < 26 and times[25-i] > 0:
                    times[25-i] -= 1
                duration += 1
                i += 1
            times.sort()

        return duration


class NewSolution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        times = [0] * 26

        for i in tasks:
            times[ord(i)-ord('A')] += 1

        queue = []
        for i in times:
            if i:
                queue.append(-i)
        heapq.heapify(queue)

        duration = 0
        while queue:
            temp = []
            i = 0
            while i <= n:
                if queue:
                    if queue[0] != -1:
                        temp.append(-heapq.heappop(queue)-1)
                    else:
                        heapq.heappop(queue)
                duration += 1
                i += 1
                if not queue and not temp:
                    break
            for i in temp:
                heapq.heappush(queue, -i)

        return duration


if __name__ == '__main__':
    print(NewSolution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
