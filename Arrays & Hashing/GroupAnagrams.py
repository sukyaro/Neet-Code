
## Time Complexity: O(n^2 * k) - where n is the number of words and k is the number of chars
## Space Complexity: O(n * k) - where n is the number of words and k is the number of chars


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        listOfLists = []
        unique = []
        mainList = []
        counter = 0
        been = set()

        # Going through every word and creating a dictionary of how many different letters its got
        for i in strs:
            englishDictionary = {}
            for char in i:
                englishDictionary[char] = englishDictionary.get(char, 0) + 1
            
            unique.append([i, englishDictionary])
        

        # Creating sublists of all the pairs (at this step there could be the exactly same sublists)
        for i in range(len(unique)):
            listOfLists.append([unique[i][0]])
            for j in range(len(unique)):
                if unique[i][1] == unique[j][1] and i != j:
                    listOfLists[counter].append(unique[j][0])
            
            listOfLists[counter].sort()
            counter += 1


        # Getting rid of the duplicates and leave the unique sublists only
        for i in listOfLists:
            key = tuple(sorted(i))
            if key not in been:
                been.add(key)
                mainList.append(i)
            
        
        return mainList
            
            
## Small test of the program
solution = Solution()
print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(solution.groupAnagrams((["",""])))
print(solution.groupAnagrams(["ddddddddddg","dgggggggggg"]))

