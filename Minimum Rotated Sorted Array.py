class Solution(object):
    def findMin(self, nums):
        low=0
        high= len(nums)-1
        while low<=high:
            if low >= high:
                return nums[low]
            mid=(low+high)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
        return nums[low]
                