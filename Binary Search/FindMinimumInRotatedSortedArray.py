
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # Implementing Binary Search
        while left <= right:
            middle = (left + right) // 2
            
            # Changing the normal Binary search
            if nums[middle] > nums[right]: # If the middle is bigger than the most right, the solution is in the left segment
                nums = nums[middle + 1:]
                left = 0
                right = len(nums) - 1
            elif nums[middle] < nums[right]: # If middle is smaller than the most right, the solution is in the right segment
                nums = nums[:middle + 1]
                left = 0 
                right = len(nums) - 1
            else:
                return nums[middle]
                
            
    
# A little test of the program
solution = Solution()
solution1 = solution.findMin([3, 4, 5, 6, 1, 2]) # Expected 1
solution2 = solution.findMin([4, 5, 0, 1, 2, 3]) # Expected 0
solution3 = solution.findMin([4, 5, 6, 7])       # Expected 4
solution4 = solution.findMin([3, 4, 5, 1, 2])    # Expected 1

print(solution1)
print(solution2)
print(solution3)
print(solution4)