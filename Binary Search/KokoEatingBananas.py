
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # If the length of the array equals to the number of house then return the largest element of the array
        if h == len(piles):
            return max(piles)
        
        # Setting the maximum possible k and the lower and upper boundary for the binary search
        k = max(piles)
        lower, upper = 1, max(piles)
        
        while lower <= upper:
            middle = (lower + upper) // 2
            summ = 0
            
            # Adding up the time that it will take to eat all the bananas given the current guessing time
            for i in piles:
                summ += ceil(i / middle)
            
            # Updating the boundaries
            if summ <= h:
                k = middle
                upper = middle - 1
            else:
                lower = middle + 1
                
        return k
        
    
    
    
solution = Solution()
solution1 = solution.minEatingSpeed([1, 4, 3, 2], 9) # Expecting 2
solution2 = solution.minEatingSpeed([25, 10, 23, 4], 4) # Expecting 25

print(solution1)
print(solution2) 