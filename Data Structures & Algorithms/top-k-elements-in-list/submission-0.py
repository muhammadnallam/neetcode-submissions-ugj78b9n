class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count frequencies
        frequencies = defaultdict(int)
        
        for n in nums:
            frequencies[n] += 1
        
        # Sort elements of hashmap in descending order by value
        sorted_frequencies = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)

        # Select first k elements of list(hashmap.keys())
        topK = []
        for i in range(k):
            topK.append(sorted_frequencies[i][0])
        
        return topK