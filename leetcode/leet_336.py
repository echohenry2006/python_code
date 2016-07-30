#!/usr/bin/python
class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(len(words)):
            for j in xrange(len(words)):
                if i==j:
                    continue
                if self.ispalind(i,j,words):
                    result.append([i,j])
        return result
    def ispalind(self,i,j,words):
        
        s = words[i]+words[j]
        i,j=0,len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            i+=1
            j-=1
        return True



if __name__ == "__main__":
    words = ["bat", "tab", "cat"]
    print Solution().palindromePairs(words)
    words = ["abcd", "dcba", "lls", "s", "sssll"]
    print Solution().palindromePairs(words)

        
