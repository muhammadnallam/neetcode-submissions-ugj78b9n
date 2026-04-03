# Time Complexity: O(n x m)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = defaultdict(list) # from collections library

        for s in strs:
            frequency = [0]*26 
            for c in s:
                frequency[ord(c) - ord('a')] += 1
            
            hashtable[tuple(frequency)].append(s)
        
        return list(hashtable.values())
