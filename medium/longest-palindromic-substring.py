
#my solution to https://leetcode.com/problems/zigzag-conversion/description/
#i used the simulation approach

class Solution:
    def longestPalindrome(self, s):
        #Base case
        if len(s) <= 1:
            return s
        #initialize 
        start = 0
        max_len = 0
        #helper function to expand around the center
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left -1
        
        for i in range(len(s)):
            len1 = expand(i, i) #Odd Length
            len2 = expand(i, i + 1) #Even Length
            
            length = max(len1, len2)
            
            if (length > max_len):
                max_len = length
                start = i - (length - 1) // 2
        return s[start:start + max_len]
    
    
print(Solution().longestPalindrome("racecar"))
print(Solution().longestPalindrome("cbbd"))
