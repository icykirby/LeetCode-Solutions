#Completed on July 18, 2025

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        #create a dtionary, assign n its length, and the limit
        myDict = {}
        n = len(nums)
        limit = n/2
        
        #iterate over the list and add numbers to the dictionary. 
        #If its in the dictionary check if its over the limit and return it if so
        for num in nums:
            if num not in myDict:
                myDict[num] = 1
            else:
                myDict[num] += 1
            if myDict[num] >= limit:
                return num
