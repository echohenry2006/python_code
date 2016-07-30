#!/usr/bin/python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums , result, min_diff,i = sorted(nums), float("inf"), float("inf"), 0
        while i < len(nums)-2:
            j=i+1
            k=len(nums)-1
            while k>j:
                
                diff = nums[i]+nums[k]+nums[j] - target
                if abs(diff) < abs(min_diff):
                    min_diff = diff
                    result = nums[i]+nums[k]+nums[j]
                if diff < 0:
                    j+=1
                    while j<k and nums[j]==nums[j-1]: 
                        j+=1
                else:
                    k-=1
                    while k>j and nums[k]==nums[k+1]:
                        k-=1
            i+=1
            while i < len(nums)-2 and nums[i]==nums[i-1]:
                i+=1

        return result






if __name__=='__main__':
    print "%d" % Solution().threeSumClosest([1,1,1,0],-100)
