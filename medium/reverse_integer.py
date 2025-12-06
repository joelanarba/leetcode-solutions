"""
this is my solution to https://leetcode.com/problems/reverse-integer/description/ leetcode challenge
"""
class Solution(object):
    def reverse(self, x):
        #Check sign of x
        sign = -1 if x < 0 else 1
        
        #make x positive
        x = abs(x)
        #convert x to string, reverse it and convert it back to int
        reversed_x = int(str(x)[::-1])
        #Add sign to the reversed val
        reversed_x = sign * reversed_x
        
        if reversed_x < -2**31 or reversed_x > 2**31 -1:
            return 0
        else:
            return reversed_x

