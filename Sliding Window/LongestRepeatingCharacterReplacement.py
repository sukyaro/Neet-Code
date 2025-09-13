
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Setting the needed variables
        result = 0 # Final result
        charFrequency = {} # A hashmap to store the frequences of each char
        mostFreqCharCount = 0 # The most frequent char count
        left, right = 0, 0 # The left and right pointers
        
        # Going thorugh the string
        while right < len(s):
            # Updating the hashmap
            currCharFreq = charFrequency[s[right]] = charFrequency.get(s[right], 0) + 1
            
            # Updating the maximal frequency of the chars
            if currCharFreq > mostFreqCharCount:
                mostFreqCharCount = currCharFreq

            # Checking the formula: sliding window - most freq char should be less or equal to k
            # So that we can replace the chars and still have a valid string
            if (right - left + 1) - mostFreqCharCount > k:
                charFrequency[s[left]] -= 1 # If the window is not valid we decrement the frequence of the first char in the window
                left += 1 # And increment the left pointer to move the window
            
            # Updating the result
            result = max(result, right - left + 1)
                
            # Incrementing the right pointer
            right += 1
                

        return result
    
    
# A little test of the program
solution = Solution()
solution1  = solution.characterReplacement("XYYX", 2)          # Expected 4
solution2  = solution.characterReplacement("AAABABB", 1)       # Expected 5
solution3  = solution.characterReplacement("ABAB", 2)          # Expected 4
solution4  = solution.characterReplacement("AABABBA", 1)       # Expected 4
solution5  = solution.characterReplacement("AAAA", 2)          # Expected 4
solution6  = solution.characterReplacement("ABCDE", 1)         # Expected 2
solution7  = solution.characterReplacement("ABCDE", 4)         # Expected 5
solution8  = solution.characterReplacement("ABBB", 2)          # Expected 4
solution9  = solution.characterReplacement("BAAAB", 2)         # Expected 5
solution10 = solution.characterReplacement("XYZXYZ", 2)        # Expected 3
solution11 = solution.characterReplacement("CCCCCC", 3)        # Expected 6
solution12 = solution.characterReplacement("ABCDABCD", 3)      # Expected 4
solution13 = solution.characterReplacement("AABBC", 2)         # Expected 4
solution14 = solution.characterReplacement("Z", 5)             # Expected 1
solution15 = solution.characterReplacement("ABBAAAAB", 2)      # Expected 6

print(solution1)
print(solution2)
print(solution3)
print(solution4)
print(solution5)
print(solution6)
print(solution7)
print(solution8)
print(solution9)
print(solution10)
print(solution11)
print(solution12)
print(solution13)
print(solution14)
print(solution15)