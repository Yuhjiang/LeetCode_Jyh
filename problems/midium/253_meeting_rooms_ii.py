from typing import List
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        left_rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(left_rooms, intervals[0][1])

        for i in intervals[1:]:
            if left_rooms[0] <= i[0]:
                heapq.heappop(left_rooms)

            heapq.heappush(left_rooms, i[1])

        return len(left_rooms)


if __name__ == '__main__':
    print(Solution().minMeetingRooms([[9,10],[4,9],[4,17]]))