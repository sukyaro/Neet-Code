class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Setting up the string and the length of the longest string
        longestString = ""
        longestStringLen = 0
        
        # Going through the original string
        for i in s:
            # If the char is not in the new string, adding it
            if i not in longestString:
                longestString += i
            else:
                # Checking if the length of the current substring is bigger than the max length
                if longestStringLen < len(longestString):
                    longestStringLen = len(longestString)
                
                # If the current letter is at the front of the substring we delete it and keep the substring
                if i == longestString[0]:
                    longestString = longestString[1:] + i
                else:
                    # Else we start a new string
                    longestString = i
        
        # Double checking that the length of the substring is less than the max length
        if longestStringLen < len(longestString):
            longestStringLen = len(longestString)
                
        # Returning the max length
        return longestStringLen
                
    

solution = Solution()
solution1 = solution.lengthOfLongestSubstring("zxyzxyz")   # expected 3 ("zxy" or "xyz")
solution2 = solution.lengthOfLongestSubstring("abcabcbb")  # expected 3 ("abc")
solution3 = solution.lengthOfLongestSubstring("bbbbb")     # expected 1 ("b")
solution4 = solution.lengthOfLongestSubstring("pwwkew")    # expected 3 ("wke")
solution5 = solution.lengthOfLongestSubstring("")          # expected 0 (empty string)
solution6 = solution.lengthOfLongestSubstring("au")        # expected 2 ("au")
solution7 = solution.lengthOfLongestSubstring("dvdf")      # expected 3 ("vdf")
solution8 = solution.lengthOfLongestSubstring("anviaj")    # expected 5 ("nviaj")
solution9 = solution.lengthOfLongestSubstring("abcdef")    # expected 6 ("abcdef")
solution10 = solution.lengthOfLongestSubstring("abba")     # expected 2 ("ab" or "ba")
solution11 = solution.lengthOfLongestSubstring("xxxxx")    # expected 1 ("x")
solution12 = solution.lengthOfLongestSubstring(s="nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM")

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