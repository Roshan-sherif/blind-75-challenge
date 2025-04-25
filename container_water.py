class Solution(object):
    def maxArea(self, heights):
        right=len(heights)-1
        left=0
        areamax=float('-inf')
        while left<right :
            height=min(heights[right],heights[left])
            width=right-left
            area=(height*width)
            areamax=max(areamax,area)
            if heights[right]>heights[left]:
                left+=1
            elif heights[right]<heights[left]:
                right-=1
            else:
                left+=1
        return areamax
            
        