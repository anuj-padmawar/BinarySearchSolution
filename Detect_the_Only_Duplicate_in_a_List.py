class Solution:
    def solve(self, nums):
        l = len(nums)
        temp = l*(l-1)/2
        temp_sum = sum(nums)
        return temp_sum-temp
        
