#Completed July 15, 2025

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #We know that negative numbers cannot be palindromes due to their sign, so disqualify them immediately
        if x < 0:
            return False

        #convert the int into a string for comparison purposes
        string = str(x)

        #Split the string into two halves
        stringFirstHalf = string[:len(string)//2]
        stringSecondHalf = string[len(string)//2:]

        #if the number is odd the second string will have an extra number in its front. That is the center number. Get rid of it as it is unnecessary for the comparisons since both halves "share" it.
        if len(stringFirstHalf) < len(stringSecondHalf):
            newSecondStringHalf = stringSecondHalf[1:]
        
            #reverse that new string half and compare it to the first
            newRvrsdStringHalf = newSecondStringHalf[::-1]

            if stringFirstHalf == newRvrsdStringHalf:
                return True
            else:
                return False
        else:
            rvrsdStringHalf = stringSecondHalf[::-1]

            if stringFirstHalf == rvrsdStringHalf:
                return True
            else:
                return False
        
        
