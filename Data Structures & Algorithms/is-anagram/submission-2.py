class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Checking frequency is O(n), while sorting is O(nlogn) 
        s_freq = [0]*26
        t_freq = [0]*26

        for c in s:
            s_freq[ord(c) - ord('a')] += 1
        for c in t:
            t_freq[ord(c) - ord('a')] += 1
    
        return s_freq == t_freq