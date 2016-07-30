#!/usr/bin/python

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lookup = {}
        for i, num in enumerate(nums):
            if num in lookup:
                return True
            lookup[num] = i
        return False
if __name__ == '__main__':
    print "%s" % Solution().containsDuplicate([1, 1, 2, 3, 4])
