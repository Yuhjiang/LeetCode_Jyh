"""
字符串转整数
1. 整数前只能有多个空格，或者'+','-'，但不能重复
2. 整数后的非整数值要忽略
3. 整数范围在-2**31-2**31-1，超过的数，则定位极值
"""


class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        num = ''
        number_num = 0
        minus = 1
        number_minus = 0        # 正负号不能重复
        str_int = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for s in str:
            if number_num == 0:
                if number_minus == 0:
                    if s == '-':            # 判断正负情况，且符号只能出现一次
                        minus = -1
                        number_minus += 1
                        continue
                    elif s == '+':
                        number_minus += 1
                        continue
                    elif s == ' ':          # 在未出现正负号和数字前的空格都忽略
                        continue
                    elif s not in str_int:
                        break
                else:                       # 已经出现了正负号，说明数字开始了，后续不能有其他字符
                    if s not in str_int:
                        break
            else:
                if s not in str_int:
                    break

            number_num += 1
            num += s
            if minus * int(num) > INT_MAX:
                return INT_MAX
            elif minus * int(num) < INT_MIN:
                return INT_MIN
        if num == '':
            num = 0
        return minus * int(num)


if __name__ == '__main__':
    test = ['42', '   -42', '4193 with words', 'words and 987', '-91283472332', '+-2', '- 234', '0-1']
    s = Solution()
    for t in test:
        print(s.myAtoi(t))