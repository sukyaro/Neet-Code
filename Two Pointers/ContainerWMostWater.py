
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        # Setting the largest area and the 2 pointers to go through the list
        largestArea = 0
        left, right = 0, len(heights) - 1     

        # Going through the list (from each side) until the poiners meet
        while left < right:
            currArea = min(heights[left], heights[right]) * (right - left)

            if currArea > largestArea:
                largestArea = currArea
            
            # Choosing which pointer to increment depending on which one of them is smaller
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            

        return largestArea


# A little test of the program
solution = Solution()
solution1 = solution.maxArea([1, 7, 2, 5, 4, 7, 3, 6])
solution2 = solution.maxArea([2, 2, 2])
solution3 = solution.maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6])
solution4 = solution.maxArea([1,7,1,1,1,1,2,5,12,3,500,50,7,8,4,7,38,9,10,12,6])

print(solution1)
print(solution2)
print(solution3)
print(solution4)