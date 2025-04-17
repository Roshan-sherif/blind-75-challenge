class Solution(object):
    def maxSubArray(self, nums):
        maximum = nums[0]
        current =0
        for n in nums:
            if current<0:
                current=0
            current+=n  
            maximum = max(maximum, current)
        return maximum
