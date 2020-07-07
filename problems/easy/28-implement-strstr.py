class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack:
            if not needle:
                return 0
        else:
            if not needle:
                return 0
        kmp = self.get_kmp(needle)
        count = 0

        for i in range(len(haystack)):
            while count > 0 and haystack[i] != needle[count]:
                count = kmp[count-1]
            if needle[count] == haystack[i]:
                count += 1
            if count == len(needle):
                return i - len(needle) + 1
        return -1

    def get_kmp(self, needle):
        kmp = [0 for _ in range(len(needle))]
        kmp[0] = 0
        max_length = 0

        for i in range(1, len(needle)):
            while max_length > 0 and needle[i] != needle[max_length]:
                max_length = kmp[max_length-1]
            if needle[max_length] == needle[i]:
                max_length += 1

            kmp[i] = max_length
        return kmp


if __name__ == '__main__':
    # print(Solution().strStr('hello', 'll'))
    # print(Solution().strStr('a', 'a'))
    print(Solution().strStr("mississippi", 'pi'))
