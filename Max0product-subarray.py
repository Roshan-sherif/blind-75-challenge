class Solution(object):
    def maxProduct(self, nums):
        res= nums[0]
        current_max=1
        current_min=1
        for num in nums:
            temp= current_max*num
            current_max=max(temp, current_min*num, num)
            current_min= min(temp, current_min*num, num)
            res=max(res,current_max)
        return res
