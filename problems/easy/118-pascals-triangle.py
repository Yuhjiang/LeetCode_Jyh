from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []

        ans = [[1]]
        for i in range(1, numRows):
            last = ans[i-1]
            tmp = [0 for _ in range(i+1)]
            for j in range(i // 2 + 1):
                tmp[j] = tmp[i-j] = last[j] + (last[j-1] if j >= 1 else 0)
            ans.append(tmp)

        return ans


if __name__ == '__main__':
    # print(Solution().generate(1))
    print(Solution().generate(2))
    print(Solution().generate(3))
    print(Solution().generate(5))
