class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # Pair [Temperature, Index]
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-1, -1, -1):
            print(stack)
            while stack and temperatures[i] >= stack[-1][0]:
                print(f"removing {stack[-1]}")
                stackTemp, stackIndex = stack.pop()
            
            
            res[i] = stack[-1][1] - i if stack else 0
            stack.append([temperatures[i], i])
        
        return res
