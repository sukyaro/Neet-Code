
## Time Complexity: O(n)
## Space Complexity: O(n)


class Solution:

    # A function for encoding a list into a string
    # So far the algorithm has a problem because instead of
    # The spaces, the words are separated by a £ symbol
    def encode(self, strs: list[str]) -> str:
        string = ""

        for i in strs:
            string += i + "£"

        print(string)
        print(self.decode(string))
        return string


    # Decoding the string back into a list
    def decode(self, s: str) -> list[str]:
        strs = s.split("#")
        del strs[-1]
        return strs


# A little test of the algorithm
solution = Solution()

solution1 = solution.encode(["neet","code","love","you"])
solution2 = solution.encode([""])
solution3 = solution.encode([])
solution4 = solution.encode(["The quick brown fox","jumps over the","lazy dog","1234567890","abcdefghijklmnopqrstuvwxyz"])

#print(solution1)
#print(solution2)
#print(solution3)