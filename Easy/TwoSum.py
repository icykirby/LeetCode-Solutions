class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force solution
        for i in range(len(nums)):
            for j in range(len(nums)):
                #This is due to the constraint of not using the same element twice
                if i == j:
                    continue
                
                value = nums[i] + nums[j]
        
                if value == target:
                    return i, j

            