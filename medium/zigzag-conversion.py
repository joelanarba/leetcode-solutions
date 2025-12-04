#my solution to https://leetcode.com/problems/zigzag-conversion/description/
#i used the simulation approach

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        #Base case
        if numRows == 1 or numRows >= len(s):
            return s
        
        #creating the rows
        rows = [""] * numRows
        #setting the controls
        row = 0 #start at the top
        direction = 1 # go down
        for char in s:
            rows[row] += char #place current char in the current row
            
            #changing directon when we hit top or bottom
            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1
            #movew to the next row    
            row += direction
        #join all rows together
        return "".join(rows)
        

        
        
