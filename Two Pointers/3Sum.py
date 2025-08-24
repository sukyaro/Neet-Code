
# Brute - Force implementation of the algorithm
# Time Complexity: O(n^5)
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         outputList = []
#         for i in range(len(nums)):
#             target = nums[i]
#             for j in range(len(nums)):
#                 for k in range(len(nums) - 1, -1, -1):
#                     if nums[j] + nums[k] == (-target) and (i != j and i != k and j != k):
#                         if sorted([nums[j], nums[k], target]) not in outputList:
#                             outputList.append(sorted([nums[j], nums[k], target]))
#                     elif nums[j] + nums[k] < (-target):
#                         break
#                     else:
#                         continue

#         return outputList

# Two - pointer approach
# Time complexity: O(n^2)
# Space complexity: O(1)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() # Sorting the list
        outputList = []

        # going through the array choosing the fixed first element
        for i in range(len(nums)):

            # skipping duplicated
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = nums[i]
            left, right = i + 1, len(nums) - 1

            # Using the two-pointer approach for the remaining part
            while left < right:
                threeSum = target + nums[left] + nums[right]

                if threeSum == 0:
                    outputList.append([nums[i], nums[left], nums[right]])
                    
                    # Ignoring the duplicates of the same number for left and right
                    while left < right and nums[left] == nums[left + 1]:
                            left += 1
                    while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                    
                    left += 1
                    right -= 1

                elif threeSum < 0:
                    left += 1 # the sum is too small, need a bigger number
                else: 
                    right -= 1 # the sum is too big, need a smaller number
                    

        return outputList


# A little test of the program
solution = Solution()
solution1 = solution.threeSum([-1, 0, 1, 2, -1, -4])
solution2 = solution.threeSum([0, 0, 0])
solution3 = solution.threeSum([0, 1, 1])
solution4 = solution.threeSum([1, 2, -2, -1])
solution5 = solution.threeSum([3, 0, -2, -1, 1, 2])
solution6 = solution.threeSum([1, -1, -1, 0])

print(solution1)
print(solution2)
print(solution3)
print(solution4)
print(solution5)
print(solution6)