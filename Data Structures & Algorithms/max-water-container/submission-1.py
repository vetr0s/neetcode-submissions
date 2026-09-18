class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = 0

        l,r = 0,len(heights) - 1

        while l<r:
            width = r-l
            height = min(heights[l], heights[r])
            vol = width*height
            ret = max(ret, vol)
            if height == heights[l]:
                l+= 1
            else:
                r-=1
        return ret