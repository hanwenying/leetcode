class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_pos = 0
        nozero_pos = -1
        for i in range(len(nums)):
            if nums[i]:
                nozero_pos += 1
                nums[nozero_pos] = nums[zero_pos]
            zero_pos += 1

        for i in range(nozero_pos + 1, len(nums)):
            nums[i] = 0

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    solution = Solution()
    solution.moveZeroes(nums)
    print nums
