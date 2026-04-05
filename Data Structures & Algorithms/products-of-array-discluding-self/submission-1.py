class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]*len(nums)
        for i in range(len(nums)):
            for j, n in enumerate(nums):
                if i == j:
                    continue
                products[i]*=n
        return products

            