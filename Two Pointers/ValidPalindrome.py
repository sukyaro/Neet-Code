
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Creating a list containing only letters and numbers from the original string
        newString = [i.lower() for i in s.strip() if i not in "?.,;'\][{}!@£$%^&*()_+=- "]

        # Checking if the list is the same if we read it from either side
        if newString == newString[::-1]:
            return True
        else:
            return False

# A little test of the program
solution = Solution()
solution1 = solution.isPalindrome("Was it a car or a cat I saw?")
solution2 = solution.isPalindrome("tab a cat")

print(solution1)
print(solution2)