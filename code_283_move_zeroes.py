class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or len(nums) == nums.count(0):
            return

        i=0
        j=1
        while i < len(nums):
            if nums[i] != 0:
                i = i + 1
                j=1
                continue
            while i+j < len(nums):
                if nums[i+j] != 0:
                    nums[i] = nums[i+j]
                    nums[i+j] = 0
                    break
                j=j+1
            i += 1
s = Solution()
arr = [0,1,0,3,12]
s.moveZeroes(arr)
print(arr)
