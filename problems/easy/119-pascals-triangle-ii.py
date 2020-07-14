from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        if rowIndex <= 0:
            return []

        last = [1]
        for i in range(1, rowIndex):
            tmp = [0 for _ in range(i+1)]
            for j in range(i // 2 + 1):
                tmp[j] = tmp[i-j] = last[j] + (last[j-1] if j >= 1 else 0)
            last = tmp

        return last


if __name__ == '__main__':
    print(Solution().getRow(3))