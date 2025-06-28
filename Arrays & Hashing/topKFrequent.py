
## Time Complexity: O(n^2)
## Space Complexity: O(n)


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        mainList = []

        # Making nested list where the first element is the element
        # And the second element is the number of occurrences of this element in the list
        counter = [[i, nums.count(i)] for i in set(nums)]

        # Sorting the list by the second elements values in descending order
        counter.sort(key=lambda x: x[1], reverse=True) 

        # Creating a new list consisting of the first elements of the list counter
        mainList = [counter[i][0] for i in range(k)] 

        return mainList


## A little test of the algorithm
solution = Solution()
solution1 = solution.topKFrequent([1, 2, 2, 3, 3, 3], 2)
solution2 = solution.topKFrequent([7, 7], 1)
solution3 = solution.topKFrequent([1, 2], 2)

print(solution1)
print(solution2)
print(solution3)