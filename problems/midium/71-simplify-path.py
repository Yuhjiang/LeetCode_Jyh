class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ''
        stack = []
        path_list = path.split('/')

        for p in path_list:
            if not p:
                continue
            if p == '..':
                if stack:
                    stack.pop()
            elif p == '.':
                continue
            else:
                stack.append(p)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    print(Solution().simplifyPath('/home/'))
    print(Solution().simplifyPath('/../'))
    print(Solution().simplifyPath('/home//foo/'))
    print(Solution().simplifyPath('/a/./b/../../c/'))
    print(Solution().simplifyPath('/a/../../b/../c//.//'))
    print(Solution().simplifyPath('/a//b////c/d//././/..'))
