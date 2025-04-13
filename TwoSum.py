class Solution(object):
    def twoSum(self, nums, target):
        seen={}

        for index,num in enumerate(nums): 
            complement=target-num
            if complement in seen:
                return [seen[complement],index]
            else :
                seen[num]= index   
        return []    
