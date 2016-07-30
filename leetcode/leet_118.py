#!/usr/bin/python

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret =[]
        tmp=[]
        for row in xrange(numRows):
            last=tmp
            tmp =[]
            for i in xrange(row+1):
                if i==0 or i==row:
                    tmp.append(1)
                else:
                    tmp.append(last[i-1]+last[i])
            ret.append(tmp)
        return ret


if __name__=='__main__':
    ret = Solution().generate(5)
    for i in xrange(len(ret)):
        print "%d "*len(ret[i]) % tuple(ret[i])
