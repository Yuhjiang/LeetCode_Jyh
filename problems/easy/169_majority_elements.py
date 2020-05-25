from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        for n in nums:
            nums_dict[n] += 1

        max_k, max_v = None, None
        for k, v in nums_dict.items():
            if not max_k or v > max_v:
                max_k, max_v = k, v

        return max_k


class NewSolution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for i in nums:
            if not count:
                candidate = i
            count += 1 if candidate == i else -1
        return candidate


if __name__ == '__main__':
    s = NewSolution()
    print(s.majorityElement([3, 2, 3]))