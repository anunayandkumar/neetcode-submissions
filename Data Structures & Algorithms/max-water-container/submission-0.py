class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        water = 0
        while left<right:
            min_height = min(heights[left],heights[right])
            width = right - left 
            water = max(water, min_height*width)
            if min_height==heights[left]:
                left += 1
            else:
                right -= 1
        return water
        