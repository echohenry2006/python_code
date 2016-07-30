#!/usr/bin/python
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for i in xrange(0,len(nums)):
            if nums[i]:
                nums[i],nums[pos]= nums[pos],nums[i]
                pos+=1


if __name__=='__main__':
    nums=[ 0, 1, 0, 3, 2]
    Solution().moveZeroes(nums)
    print "%d "*len(nums) % tuple(nums)
