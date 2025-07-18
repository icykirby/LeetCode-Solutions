#Done July 17, 2025

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        #create a dictionary and input the keys, the values being the amount of times they appear
        #if it appears more than once, return true. if not then return false
        myDict = {}
    
        for num in nums:
            if num in myDict:
                myDict[num] += 1
                return True
            else:
                myDict[num] = 1
        
        return False
        
       
        