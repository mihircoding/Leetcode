class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s 
        
        rows = [''] * numRows
        add = 0
        inc = 1

        for x in s:
            rows[add] += x
            if add == 0:
                inc = 1
            elif add == numRows -1:
                inc = -1
            add += inc
        return ''.join(rows)

