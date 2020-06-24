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


if __name__ == '__main__':
    # print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
    print(Solution().reconstructQueue([[7, 0], [5, 1]]))