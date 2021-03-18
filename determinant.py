def get_minor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def determinant(m):

    if(len(m) == 1):
        return m[0][0]
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    det = 0
    for c in range(len(m)):
        det += ((-1)**c)*m[0][c]*determinant(get_minor(m,0,c))
    return det

print(determinant([[5]]))