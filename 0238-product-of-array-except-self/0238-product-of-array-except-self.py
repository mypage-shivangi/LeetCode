class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n

        # Left pass
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # Right pass
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        print(output)
        return output
