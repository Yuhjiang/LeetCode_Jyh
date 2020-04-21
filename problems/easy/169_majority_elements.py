from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = {}

        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 1
            else:
                nums_dict[n] += 1

        max_k, max_v = None, None
        for k, v in nums_dict.items():
            if not max_k or v > max_v:
                max_k, max_v = k, v

        return max_k


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))