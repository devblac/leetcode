class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #edge cases
        # Empty List
        # Equals numbers
        # Negative numbers = Covered in the constraints, so we don't have to take into account. 
        result = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    result[i] += 1
        return result