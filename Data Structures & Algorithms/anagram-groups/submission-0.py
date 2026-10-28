class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        seen = {}

        for string in strs:
            key = frozenset(Counter(string).items())

            if key not in seen:
                seen[key] = string
                anagrams[string] = []

            anagrams[seen[key]].append(string)

        return list(anagrams.values())
            

            
        