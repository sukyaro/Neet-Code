
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Setting the flag and boundaries
        found = False
        left, right = 0, len(nums) - 1
        
        # Going through the list while the target is not found and we have not checked all the element
        while not found and left <= right:
            middPoint = (left + right) // 2 # Setting the midpoint
            
            if nums[middPoint] == target:
                found = False
                return middPoint
            elif nums[middPoint] < target:
                left = middPoint + 1
            else:
                right = middPoint - 1
                
        # If the element is not in the list returning -1
        return -1


# A little test of the program
solution = Solution()
solution1 = solution.search([-1, 0, 2, 4, 6, 8], 4)
solution2 = solution.search([-1, 0, 2, 4, 6, 8], 3)
 
print(solution1)
print(solution2)
