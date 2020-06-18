from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = len(nums)
        dp = [1] * length
        max_length = dp[-1]
        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                if nums[j] > nums[i]:
                    dp[i] = dp[i] if dp[i] > dp[j]+1 else dp[j]+1

            max_length = max_length if max_length > dp[i] else dp[i]
        return max_length


class NewSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []

        for n in nums:
            if not dp or dp[-1] < n:
                dp.append(n)
            else:
                l, r = 0, len(dp) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if dp[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                dp[loc] = n
        return len(dp)


if __name__ == '__main__':
    # print(NewSolution().lengthOfLIS([10,9,2,5,3,7,101,18,19]))
    print(Solution().lengthOfLIS([4,10,4,3,8,9]))