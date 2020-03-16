class Solution:
    def countAndSay(self, n: int) -> str:
        result = self.say("1", 1, n)
        return result

    def say(self, n, curr, max):
        if curr == max:
            return n
        else:
            res = self.say_next_seq(n)
            return self.say(res, curr+1, max)

    def say_next_seq(self, s: str) -> str:
        curr_num = 0
        curr = ""

        res = ""

        for i in s:
            if curr == "":
                curr = i
                curr_num += 1
                continue
            if curr == i:
                curr_num += 1
            else:
                res += (str(curr_num) + curr)
                curr_num = 1
                curr = i

        res += (str(curr_num) + curr)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(1))
    print(s.countAndSay(2))
    print(s.countAndSay(3))
    print(s.countAndSay(4))
    print(s.countAndSay(5))