class Solution:
    def removeDuplicates(self, nums) -> int:
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        prev = nums[0]
        ind = 1
        for i in range(1, len(nums)):
            if nums[i] != prev:
                nums[ind] = nums[i]
                prev = nums[i]
                ind += 1

        return ind


if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))
    print(nums)