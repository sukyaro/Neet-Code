class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Setting the starting values for buy, sell, and profit
        buy, sell = (float('inf'), -1), float('-inf')
        profit = -1
        
        # Going through the list
        for i in range(len(prices)):
            # If the current price is less than current buy, update the buy price
            if prices[i] < buy[0]:
                buy = (prices[i], i) # Updating the new buy price
                sell = float('-inf') # Resetting the sell price cus we cant sell it for the outdated price
            
            # If the current price is bigger than the previous sell price and the day is past the buy day, update the sell price
            if prices[i] > sell and i > buy[1]:
                sell = prices[i]
            
            # Updating the max profit
            if (sell - buy[0]) > profit:
                profit = sell - buy[0]

        # Returning the max profit or 0 if the purchase was not made
        if profit == -1:
            return 0
        else:
            return int(profit)
        
        
    
solution = Solution()
solution1 = solution.maxProfit([10, 1, 5, 6, 7, 1])    # Expected: 6 
solution2 = solution.maxProfit([10, 8, 7, 5, 2])       # Expected: 0
solution3 = solution.maxProfit([7, 1, 5, 3, 6, 4])     # Expected: 5
solution4 = solution.maxProfit([7, 6, 4, 3, 1])        # Expected: 0
solution5 = solution.maxProfit([1, 2, 3, 4, 5])        # Expected: 4
solution6 = solution.maxProfit([5])                    # Expected: 0
solution7 = solution.maxProfit([2, 4])                 # Expected: 2
solution8 = solution.maxProfit([3, 4, 1])              # Expected: 1

print(solution1)
print(solution2)
print(solution3)
print(solution4)
print(solution5)
print(solution6)
print(solution7)
print(solution8)