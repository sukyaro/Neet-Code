
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # Setting the stack (first element of the histogram) and the largest area
        stack = [[0, heights[0]]]
        maxArea = 0

        # Looping through all elements in the list
        for i in range(1, len(heights)):
            if heights[i] < stack[-1][1]: # Poping the value if the current bar is lower than the top of the stack
                while stack and heights[i] < stack[-1][1]: # Checking all previous bars in the stack and popping them if they are lower than the current one
                    top = stack.pop()
                    currArea = (i - top[0]) * top[1]

                    if currArea > maxArea:
                        maxArea = currArea

                stack.append([top[0], heights[i]])
        
            else:
                stack.append([i, heights[i]])

        # Doing the final check with the rest of the bars in the stack
        for i in stack:
            currArea = (len(heights) - i[0]) * i[1]
            if currArea > maxArea:
                maxArea = currArea


        return maxArea



# A little test of the program
solution = Solution()
solution1 = solution.largestRectangleArea([7, 1, 7, 2, 2, 4])
solution2 = solution.largestRectangleArea([1, 3, 7])
solution3 = solution.largestRectangleArea([2, 1, 5, 6, 2, 3])

print(solution1)
print(solution2)
print(solution3)