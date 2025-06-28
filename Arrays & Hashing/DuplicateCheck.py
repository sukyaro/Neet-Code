
## Time Complexity: O(n)
## Space Complexity: O(n)


class Solution:
    #Adding the datatypes (not required in Python)
    def hasDuplicate(self, nums: list[int]) -> bool:

        # Creating a new set where were gonna store the elements
        seen = set()
        flag = False

        # Going through all the elements in the given list and adding them to a set
        # If the element has been previosly added changing the flag and terminating the program
        for num in nums:
           if num in seen:
               flag = True
               break
           seen.add(num)
        return flag
    

## A little program check
solution = Solution()
result = solution.hasDuplicate([1, 2, 3, 4, 5])
result2 = solution.hasDuplicate([1, 2, 3, 3, 5])
print(result)
print(result2)