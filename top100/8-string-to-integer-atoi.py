class Solution:
    def myAtoi(self, str: str) -> int:
        self.MAX = 2**31-1
        self.MIN = -2**31
        self.state_table = {
            #           ''       '+/-'     '0-9'      'other'
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }
        self.state = 'start'
        self.ans = 0
        self.sign = 1

        for c in str:
            self.get(c)

        return self.ans * self.sign

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
            self.ans = min(self.ans, self.MAX) if self.sign == 1 else min(self.ans, -self.MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


if __name__ == '__main__':
    print(Solution().myAtoi("4193 with words"))
    print(Solution().myAtoi("words and 987"))
    print(Solution().myAtoi("-91283472332"))
