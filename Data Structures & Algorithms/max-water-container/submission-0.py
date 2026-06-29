class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # go through each item in the heights
        # calc the area and compare it with max
        # keep the highest height and move to right continuously

        left = 0
        right = len(heights) - 1 
        max_area = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area