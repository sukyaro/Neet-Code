
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len1, len2 = len(nums1), len(nums2) # Getting the length of the both arrays
        
        merged = nums1 + nums2 # Merging the 2 arrays
        merged.sort() # Sorting the new big array
        
        totalLength = len1 + len2
        
        if totalLength % 2 == 0:
            return (merged[totalLength // 2 - 1] + merged[totalLength // 2]) / 2 # If the new array's length is even returning the average of the 2 elements in the middle
        else:
            return merged[totalLength // 2] # if the new array's length is odd returning the middle element
        
        
    
# A little test of the program
solution = Solution()
solution1 = solution.findMedianSortedArrays([1, 2], [3])
solution2 = solution.findMedianSortedArrays([1, 2], [3, 4])
solution3 = solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5])
solution4 = solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4])

print(solution1)
print(solution2)
print(solution3)
print(solution4)