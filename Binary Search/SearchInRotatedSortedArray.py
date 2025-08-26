
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # Implementing Binary Search
        while left <= right:
            middle = (left + right) // 2
            
            # If the middle is the target return the index
            if nums[middle] == target:
                return middle
            
            elif nums[left] <= nums[middle]: # If the left half is sorted
                if nums[left] <= target <= nums[middle]: # If target is withing the left side
                    right = middle - 1 # Searching the left side
                else:
                    left = middle + 1 # Searching the right side
                
            elif nums[middle] < nums[right]: # If the right half is sorted
                if nums[middle] <= target <= nums[right]: # If the target is withing the right side
                    left = middle + 1 # Search the right side 
                else:
                    right = middle - 1 # Search the left side

        # Returning -1 if the target is not in the array
        return -1
        
        
# A little test of the program
solution = Solution()
solution1 = solution.search([3, 4, 5, 6, 1, 2], 1)    # Expected 4
solution2 = solution.search([3, 5, 6, 0, 1, 2], 4)    # Expected -1
solution3 = solution.search([4, 5, 6, 7, 0, 1, 2], 0) # Expected 4
solution4 = solution.search([4, 5, 6, 7, 0, 1, 2], 3) # Expected -1

print(solution1)
print(solution2)
print(solution3)
print(solution4)