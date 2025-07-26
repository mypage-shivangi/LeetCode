class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arrsum=sum(nums)
        leftsum=0
        for i in range(len(nums)):
            rightsum=arrsum-nums[i]-leftsum
            if leftsum==arrsum-nums[i]-leftsum:
                return i
            leftsum+=nums[i]
        return -1
