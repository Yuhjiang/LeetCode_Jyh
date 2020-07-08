class Solution:
    def countAndSay(self, n: int) -> str:
        pre = '1'
        cnt = 2

        while cnt <= n:
            tmp = ''
            last = None
            count = 0
            for i in pre:
                if not last:
                    last = i
                    count = 1
                    continue
                if i == last:
                    count += 1
                else:
                    tmp += '{}{}'.format(count, last)
                    last = i
                    count = 1
            pre = tmp + '{}{}'.format(count, last)
            cnt += 1

        return pre


if __name__ == '__main__':
    for i in range(1, 6):
        print(Solution().countAndSay(i))
