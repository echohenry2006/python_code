#!/usr/bin/python

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=-1
        while i>-len(nums):
            if nums[i]>nums[i-1]:
                k=i+1
                while k<0:
                    if nums[k]<=nums[i-1]:
                        break
                    k+=1

                nums[k-1],nums[i-1]=nums[i-1],nums[k-1]
                if i<-1:
                    nums[i:]=list(reversed(nums[i:]))
                break
            i-=1
        if i==-len(nums):
            nums.reverse()


if __name__ == "__main__":
    nums=[1,2,3]
    Solution().nextPermutation(nums)
    print nums
            
