from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 0

        nums_list = [(key, count) for key, count in nums_dict.items()]
        nums_list.sort(key=lambda x: x[1], reverse=True)

        res = nums_list[:k]
        return [r[0] for r in res]


if __name__ == '__main__':
    print(Solution().topKFrequent([1], 1))