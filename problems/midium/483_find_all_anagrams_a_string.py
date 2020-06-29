from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import defaultdict
        need = defaultdict(int)
        window = defaultdict(int)

        for c in p:
            need[c] += 1

        left = right = 0
        valid = 0

        total_size = len(s)
        p_size = len(p)
        need_size = len(need)
        result = []
        while right < total_size:
            c = s[right]
            right += 1
            if need.get(c):     # c是p内的字符串
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= p_size:
                if valid == need_size:
                    result.append(left)

                c = s[left]
                left += 1

                if need.get(c):
                    if need[c] == window[c]:
                        valid -= 1
                    window[c] -= 1
        return result


if __name__ == '__main__':
    print(Solution().findAnagrams("baa", "aa"))