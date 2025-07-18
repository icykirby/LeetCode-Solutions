class Solution:
    def mySqrt(self, x: int) -> int:
        #brute force approach
        
        #the answer needs to be rounded to the nearest integer
        #thus we can check common square roots to find out answer
        #Our limit is x + 1 (to account for x = 0), thus we can stop when the number's square root is greater than x
        #Once we hit that limit we know that the number previous must be the answer
        #An elif is accounting for integers that are perfect squares
        for i in range(x + 1):
            num = i * i
            if x < num:
                return i - 1
            elif x <= num:
                return i
                