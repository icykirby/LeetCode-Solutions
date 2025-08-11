#Completed August 11, 2025

class Solution:
    def myAtoi(self, s: str) -> int:
        #create constants
        MININT = -2**31
        MAXINT = 2**31 - 1

        #create list of valid characters
        validChars = ['-']
        validNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

        #conditional to check for a sign (ensures no multiple signs)
        validSignCount = False
        #condtional to check for numbers before a sign (ensures sign in ONLY in the front)
        charBeforeSign = False
        #conditional to check if there is a number in the final answr (ensures not just a sign)
        hasNum = False

        #intialization of empty string
        string = ""

        #loop through string and check for conditionals
        for char in s:
            #ignore leading whitespace (but whitespace that isnt leading leads to the break)
            if char == " " and validSignCount == False and hasNum == False:
                continue
            #check for a plus sign and if a sign has not appeared
            elif char == '+' and validSignCount == False and hasNum == False:
                validSignCount = True
            #check for a plus sign and if another sign already appeared - break if so
            elif char == '+' and validSignCount == True:
                break
            #check if char is valid, if theres been a sign yet, and no chars before the sign
            elif char in validChars and validSignCount == False and charBeforeSign == False:
                string += char
                validSignCount = True
            #check if char is a valid number, turn hasNum conditional to true if so
            elif char in validNums:
                string += char
                charBeforeSign = True
                hasNum = True
            #stop loop is no condition is met
            else:
                break
                
        #turn into an integer or return 0 if nothing was read
        if len(string) > 0 and hasNum == True:
            answer = int(string)

            #check if string is out of bounds for rounding
            if answer < MININT:
                return MININT
            elif answer > MAXINT:
                return MAXINT
            else:
                return answer
        else:
            return 0

        