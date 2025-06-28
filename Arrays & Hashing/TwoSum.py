
## Time Complexity: O(n)
## Space Complexity: O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap = {}

        # Going through the entire list of numbers
        for i in range(len(nums)):

            # Making a new target we'll be looking for
            difference = target - nums[i]

            if difference in hashMap:
                return [hashMap[difference], i]
            hashMap[nums[i]] = i
        
        return []
    

## A little test
solution = Solution()
result1 = solution.twoSum([4, 5, 6], 11)
result2 = solution.twoSum([5, 5], 10)
print(result1)
print(result2)