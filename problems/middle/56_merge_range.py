from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda _: _[0])
        final_intervals = []

        for interval in intervals:
            if not final_intervals:
                final_intervals.append(interval)
            else:
                if interval[0] > final_intervals[-1][-1]:
                    # 下个区间最小值大于已有区间最大值，放弃合并
                    final_intervals.append(interval)
                else:
                    final_intervals[-1][-1] = max(interval[-1], final_intervals[-1][-1])
        return final_intervals


if __name__ == '__main__':
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(s.merge([[1, 4], [4, 5]]))
    print(s.merge([[1, 4], [0, 0]]))
