class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_seen = {}
        t_seen = {}
        for i in range(len(s)):
            s_character = s[i]
            t_character = t[i]
            if s_character in s_seen:
                s_seen[s_character] += 1
            else:
                s_seen[s_character] = 1

            if t_character in t_seen:
                t_seen[t_character] += 1
            else:
                t_seen[t_character] = 1
        for key in s_seen.keys():
            has_character = key in t_seen
            if not has_character or s_seen[key] != t_seen[key]:
                return False
        return True
