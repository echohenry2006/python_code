#!/usr/bin/python
import copy
class Solution(object):
    def combinationSum3(self,k,n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        intermedia =[]
        result=[]
        for i in xrange(1,10):
            intermedia.append(i)
            self.dfs(k,n,intermedia,1,result)
            intermedia.pop()
        return result
    def dfs(self,k,n,intermedia,level,result):
        if level == k:
            if sum(intermedia) == n:
                result.append(copy.deepcopy(intermedia))
        else:
            for i in xrange(intermedia[-1]+1,10):
                intermedia.append(i)
                self.dfs(k,n,intermedia,level+1,result)
                intermedia.pop()


if __name__ == "__main__":
    ret = Solution().combinationSum3(3,7)
    for s in enumerate(ret):   
        print "%d"*len(s) % tuple(s)    