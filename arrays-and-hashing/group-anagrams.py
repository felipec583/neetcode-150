from typing import List



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        alphabet_length = 26
        for word in strs:
            anagram_key = [0 for i in range(alphabet_length)]
            for char in word:
                alphabet_index = ord(char) - ord("a")
                anagram_key[alphabet_index] += 1
            key = "#".join(str(i) for i in anagram_key)
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        return [groups.values()]
