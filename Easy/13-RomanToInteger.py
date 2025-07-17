#Completed July 17, 2025

class Solution:
    def romanToInt(self, s: str) -> int:
        #create a dictionary - key being string and value being number
        myDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        #loop over the string and save the answer (the value of the roman numerals) into an array
        romNumArr = []
        for char in s:
            romNum = myDict.get(char)
            romNumArr.append(romNum)
        
        #loop through the array of the values. If index i is less than index i+1, i needs to be subtracted. In this case it is multiplied by -1 to make it negative for easy calculations        
        for i in range(len(romNumArr) - 1):
            if romNumArr[i] < romNumArr[i+1]:
                romNumArr[i] *= -1
        
        #Add the values of all the roman numerals and return
        ans = 0
        for i in range(len(romNumArr)):
            ans += romNumArr[i]

        return ans
        