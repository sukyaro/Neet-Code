
## Time Complexity: O(n)
## Space Complexity: O(n)


class Solution:

    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # Getting the length of the array,
        # Creating a new array and filling it with 1s
        n = len(nums)
        newArray = [1] * n

        # Calculating prefix products
        prefix = 1
        for i in range(n):
            newArray[i] = prefix
            prefix *= nums[i]

        # Calculating suffix products and multiplying with the prefix
        suffix = 1
        for i in range(n - 1, -1, -1):
            newArray[i] *= suffix
            suffix *= nums[i]

        return newArray
    

## A little program test
solution = Solution()

solution1 = solution.productExceptSelf([1, 2, 4, 6])

print(solution1)
        