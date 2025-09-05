
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            # Flip the sign of the number at the index corresponding to nums[i]
            # Use abs() because nums[i] may already be negative from a previous step
            nums[abs(nums[i]) - 1] *= -1
            
            # If after flipping, the value is equal to its absolute value,
            # it means the number at this index was already negative before,
            # so nums[i] is the duplicate number
            if nums[abs(nums[i]) - 1] == abs(nums[abs(nums[i]) - 1]):
                return abs(nums[i])
            
        # Return -1 if there are no duplicates
        return -1

    
# A little test of the program
solution = Solution()
solution1 = solution.findDuplicate([1, 2, 3, 2, 2])
solution2 = solution.findDuplicate([1, 2, 3, 4, 4])
solution3 = solution.findDuplicate([1, 3, 4, 2, 2])
solution4 = solution.findDuplicate([3, 2, 2, 2, 4])

print(solution1)
print(solution2)
print(solution3)
print(solution4)