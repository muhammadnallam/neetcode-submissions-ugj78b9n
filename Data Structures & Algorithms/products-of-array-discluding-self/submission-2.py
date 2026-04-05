class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]*len(nums)

        # Prefixes
        pre = 1
        for i in range(len(nums)-1):
            pre *= nums[i]
            products[i+1] = pre

        # Postfixes
        post = 1
        for i in range(len(nums)-1, 0, -1):
            post *= nums[i]
            products[i-1] *= post

        return products