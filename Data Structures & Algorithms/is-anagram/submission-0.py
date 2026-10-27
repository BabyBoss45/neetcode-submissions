class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tempS = {}
        tempT = {}


        for letter in s:
            tempS[letter] = tempS.get(letter, 0) + 1

        for letter in t:
            tempT[letter] = tempT.get(letter, 0) + 1 

            
        return tempS == tempT

       