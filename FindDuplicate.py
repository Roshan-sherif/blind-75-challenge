class Solution(object):
    def containsDuplicate(self, nums):
        hashmap={}
        for index,num in enumerate(nums):
            if num in hashmap:
                return True;
            else:
                hashmap[num]=index
        return False