class Solution:
    INT_MAX = 2**31-1
    INT_MIN = -2**31

    def myAtoi(self, s: str) -> int:

        self.state_table = {
            #          ''        '+/-'      '0-9'      'other'
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }
        self.state = 'start'
        self.sign = 1
        self.ans = 0

        for c in s:
            self.get(c)

        return self.ans

    @staticmethod
    def get_next_state(c: str):
        if c.isspace():
            return 0
        elif c in ['+', '-']:
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def get(self, c: str):
        self.state = self.state_table[self.state][self.get_next_state(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, self.INT_MAX) if self.sign == 1 else min(self.ans, -self.INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


if __name__ == '__main__':
    print(Solution().myAtoi("4193 with words"))
    print(Solution().myAtoi("words and 987"))
    print(Solution().myAtoi("-91283472332"))