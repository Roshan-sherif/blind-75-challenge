class Solution(object):
    def productExceptSelf(self, nums):
        prefix=1
        postfix=1
        result=[1]*len(nums)
        for i in range(len(result)):
            result[i]=prefix
            prefix *= nums[i]
        for i in range(len(result)-1,-1,-1):
            result[i] *=postfix
            postfix *= nums[i]
        return result