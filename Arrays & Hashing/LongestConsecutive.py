
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        # Checking that the list has any elements
        if len(nums) == 0:
            return 0

        # Sorting the list and setting the starting values for the main and
        # Temporary counters
        nums.sort()
        counter = 1
        maxCounter = 0

        # Going through all the elements in the list and comparing them
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1] - 1: # If the next element is 1 bigger than the current one then adding 1 to the counter
                counter += 1
            elif nums[i] == nums[i + 1]: # If the next element is the same as the current one then the counter remains the same
                counter = counter
            else: # Setting the counter back again to the starting value if the sequence  is not consecutive
                if maxCounter < counter:
                    maxCounter = counter
                counter = 1

        # Checking one more time that the main counter is smaller than the temporarly one
        if maxCounter < counter:
            maxCounter = counter

        return maxCounter


## A little test of the program
solution = Solution()

solution1 = solution.longestConsecutive([2,20,4,10,3,4,5])
solution2 = solution.longestConsecutive([0,3,2,5,4,6,1,1])
solution3 = solution.longestConsecutive([])

print(solution1)
print(solution2)
print(solution3)