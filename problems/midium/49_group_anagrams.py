from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for s in strs:
            tmp = ''.join(sorted(s))

            if tmp in memo:
                memo[tmp].append(s)
            else:
                memo[tmp] = [s]
        return list(memo.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))