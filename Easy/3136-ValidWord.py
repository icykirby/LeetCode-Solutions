#Done July 15, 2025

class Solution:
    def isValid(self, word: str) -> bool:
        #first check the length of the string
        n = len(word)
        if n < 3:
            return False

        #second, check if it has only numbers and letters
        nums = "0123456789"
        consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        vowels = "aeiouAEIOU"

        consonantCount = 0
        vowelCount = 0

        for char in word:
            if char not in (nums + consonants + vowels):
                return False 

        #third check and see if it has at least one vowel and non vowel
            elif char in vowels and char not in nums:
                vowelCount += 1
            elif char in consonants and char not in nums:
                consonantCount += 1
        
        if vowelCount == 0 or consonantCount == 0:
            return False
        else:
            return True