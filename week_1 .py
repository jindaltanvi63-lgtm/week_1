def solve_psne(p1_matrix, p2_matrix):
    rows=len(p1_matrix)
    cols=len(p1_matrix[0])
    lst=[]
    for i in range(rows):
         for j in range(cols):
             if all(p1_matrix[i][j] >= p1_matrix[r][j] for r in range(rows)):
                 if all(p2_matrix[i][j]>= p2_matrix[i][c] for c in range(cols)):
                     lst.append((i,j))
    return lst                 