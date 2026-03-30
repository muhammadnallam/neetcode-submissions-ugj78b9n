class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in hashtable:
                return [hashtable[m], i]
            hashtable[n] = i