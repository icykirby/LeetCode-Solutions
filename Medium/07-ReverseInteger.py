#Completed August 11, 2025

class Solution:
    def reverse(self, x: int) -> int:

        #create constants for conditionals
        MININT = -2**31
        MAXINT= 2**31 - 1
        
        #stringify and reverse the int (add - sign to the front and remove it from the end for negatives)
        if x >= 0:
            string = str(x)[::-1]
        else:
            string = '-' + str(x)[::-1][:-1]
        

        #turn string to integer
        answer = int(string)

        #check if answer is in valid range
        if answer > MAXINT or answer < MININT:
            return 0
        else:
            return answer
