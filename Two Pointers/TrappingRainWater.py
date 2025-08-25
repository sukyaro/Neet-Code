
# First approach
# Time Complexity: O(n)
# Space Complexity: O(n)
# class Solution:
#     def trap(self, height: list[int]) -> int:
#         maxLeft, maxRight = [0 for i in range(len(height))], [0 for i in range(len(height))]
#         maxLeftBound, maxRightBound = 0, 0
#         sumTrap = 0

#         for i in range(len(height)):
#             maxLeft[i] = maxLeftBound
#             if height[i] > maxLeftBound:
#                 maxLeftBound = height[i]
            
#         for i in range(len(height) - 1, -1, -1):
#             maxRight[i] = maxRightBound
#             if height[i] > maxRightBound:
#                 maxRightBound = height[i]
            
#         for i in range(len(height)):
#             currTrap = min(maxLeft[i], maxRight[i]) - height[i]
            
#             if currTrap < 0:
#                 currTrap = 0
            
#             sumTrap += currTrap

#         return sumTrap


# Second Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def trap(self, height: list[int]) -> int:
        maxLeft, maxRight = 0, 0           # Tracking the highest bars from the left and the right
        left, right = 0, len(height) - 1. 
        sumTrap = 0                        # Accumulating the total trapped water 

        while left < right:
            # Deciding which side to process, the smaller boundary limits the water level
            if maxLeft <= maxRight:
                currHeight = height[left]
            else:
                currHeight = height[right]

            # Watter trapped at this position
            currTrap = min(maxLeft, maxRight) - currHeight
            if currTrap < 0:
                currTrap = 0

            sumTrap += currTrap

            # Updating the highest bar
            if height[left] > maxLeft:
                maxLeft = height[left]
            
            if height[right] > maxRight:
                maxRight = height[right]

            # Move the pointer from the smaller boundary inward
            if maxLeft <= maxRight:
                left += 1
            else:
                right -= 1

        return sumTrap


# A little test of the program
solution = Solution()
solution1 = solution.trap([0,2,0,3,1,0,1,3,2,1])
solution2 = solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])

print(solution1)
print(solution2)