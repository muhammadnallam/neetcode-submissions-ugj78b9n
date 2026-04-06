class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_number = lambda i, j: (i//3)*3 + (j//3)
        locations = {} 

        for i, row in enumerate(board):
            for j, n in enumerate(row):
                try:
                    n = int(n)
                except ValueError:
                    continue

                digit = locations.setdefault(n, [set(), set(), set()])

                if i in digit[0]:
                    return False
                elif j in digit[1]:
                    return False
                elif box_number(i, j) in digit[2]:
                    return False
                else:
                    locations[n][0].add(i)
                    locations[n][1].add(j)
                    locations[n][2].add(box_number(i, j))
        
        return True