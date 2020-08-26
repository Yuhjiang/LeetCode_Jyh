class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip(' ')
        if not s:
            return False
        self.pos = 0

        ans = self.scan_integer(s)
        if self.pos < len(s) and s[self.pos] == '.':
            self.pos += 1
            ans = self.scan_unsigned_integer(s) or ans
        if self.pos < len(s) and (s[self.pos] == 'e' or s[self.pos] == 'E'):
            self.pos += 1
            ans = ans and self.scan_integer(s)

        return ans and self.pos == len(s)

    def scan_unsigned_integer(self, s: str):
        before = self.pos
        for i in s[self.pos:]:
            if i.isdigit():
                self.pos += 1
            else:
                break

        return self.pos > before

    def scan_integer(self, s: str):
        if self.pos >= len(s):
            return False
        if s[self.pos] == '+' or s[self.pos] == '-':
            self.pos += 1
        return self.scan_unsigned_integer(s)


if __name__ == '__main__':
    print(Solution().isNumber("0e"))