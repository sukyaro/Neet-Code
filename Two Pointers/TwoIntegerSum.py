
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:

        # Brute-force approach: try every pair of numbers until we find one that sums to target
        for i in range(len(numbers)):  # start index
            for j in range(len(numbers) - 1, 0, -1):  # end index

                # Check if numbers[i] and numbers[j] form the target sum
                if numbers[i] + numbers[j] == target and numbers[i] != numbers[j]:
                    # Return 1-based indices as required by the problem
                    return [i + 1, j + 1]


# A little test of the program
solution = Solution()
solution1 = solution.twoSum([1, 2, 3, 4], 3)
solution2 = solution.twoSum([2, 3, 4], 6)

print(solution1)
print(solution2)