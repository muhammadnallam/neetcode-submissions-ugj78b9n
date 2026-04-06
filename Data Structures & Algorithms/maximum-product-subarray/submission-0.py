class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        global_max = max(nums)

        curr_max = curr_min = 1

        for n in nums:
            tmp = curr_max
            curr_max = max(n*curr_max, n*curr_min, n)
            curr_min = min(n*tmp, n*curr_min, n) 

            global_max = max(global_max, curr_max)
        
        return global_max
        