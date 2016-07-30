#!/usr/bin/python
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count =1
        for i in xrange(1,len(nums)):
            if count!=0:
                if nums[i]==major:
                    count+=1
                else:
                    count-=1
            else:
                count+=1
                major=nums[i]
        return major




if __name__=='__main__':
    nums = [2,3,1,1,2]
    print "%d" % Solution().majorityElement(nums)

