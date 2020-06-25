from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if not people:
            return []
        people.sort(key=lambda x: (x[1], -x[0]))

        queue = []
        for p in people:
            count = p[1]
            if count == 0:
                queue.insert(0, p)
                continue
            for i in range(len(queue)):
                if p[0] <= queue[i][0]:
                    count -= 1
                if count == 0:
                    queue.insert(i+1, p)
        return queue


class NewSolution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))

        result = []
        for i in range(len(people)):
            result.insert(people[i][1], people[i])

        return result


if __name__ == '__main__':
    print(NewSolution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
    # print(Solution().reconstructQueue([[7, 0], [5, 1]]))