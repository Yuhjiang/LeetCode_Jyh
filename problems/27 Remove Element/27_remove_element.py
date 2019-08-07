class Solution:
    def removeElement(self, nums, val: int) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        left = 0
        right = nums_len - 1
        while left <= right:
            # print('left: {}, right: {}'.format(left, right))
            if nums[left] == val:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
            else:
                left += 1

        return left


if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    print(s.removeElement(nums, 2))
    print(nums)