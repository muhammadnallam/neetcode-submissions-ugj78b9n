class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        longest = 1
        nums_hash = set(nums)

        for n in nums:
            curr_max = 1
            if n-1 not in nums_hash:
                next = n+1
                while next in nums_hash:
                    curr_max += 1
                    next += 1
            longest = max(curr_max, longest)
        
        return longest
        