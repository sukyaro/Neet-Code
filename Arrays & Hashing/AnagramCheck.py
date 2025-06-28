
## Time Compexity: O(n)
## Space Complexity: O(1)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Checking if the length of the two strings is the same, if not they are deffo not anagrams
        if len(s) != len(t):
            return False
        
        dict_s, dict_t = {}, {}

        # Adding every single letter in every word to a dictionary
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        # Checking that the 2 dictionaries are the same
        return dict_s == dict_t
    

## A little test of the program
solution = Solution()
result1 = solution.isAnagram("hello", "lelho")
result2 = solution.isAnagram("hello", "lol")
print(result1)
print(result2)