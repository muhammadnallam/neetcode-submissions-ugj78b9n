class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}

        for s in strs:
            s_sorted = ''.join(sorted(s))
            if not s_sorted in hashtable:
                hashtable[s_sorted] = [s]
            else:
                hashtable[s_sorted].append(s)
        
        anagrams = []
        for v in hashtable.values():
            anagrams.append(v)
        
        return anagrams
