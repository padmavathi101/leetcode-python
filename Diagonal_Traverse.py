class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        d=[]
        rows=0
        columns=0
        if matrix:
            for i in matrix:
                rows=rows+1
            for i in matrix[0]:
                columns=columns+1
        if rows!=0 or columns!=0:
            i = 0
            j = 0
            k = 0
            # Direction is initially from down to up 
            isUp = True
  
            # Traverse the matrix till all elements get traversed 
            while k<rows * columns: 
            # If isUp = True then traverse from downward 
            # to upward 
                if isUp:
                    while i >= 0 and j<columns : 
                        d.append(matrix[i][j])
                        k += 1
                        j += 1
                        i -= 1
                    if i < 0 and j <= columns - 1: 
                        i = 0
                    if j == columns: 
                        i = i + 2
                        j -= 1
                else:
                    while j >= 0 and i<rows : 
                        d.append(matrix[i][j])
                        k += 1
                        i += 1
                        j -= 1
                    if j < 0 and i <= rows - 1: 
                        j = 0
                    if i == rows: 
                        j = j + 2
                        i -= 1
            
                isUp = not isUp 
        else:
            return []
                
        return d
