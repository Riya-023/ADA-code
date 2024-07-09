import sys
def Matrix_chain(p):
    
    n = len(p) - 1

    m=[[0] * n for _ in range(n)]

    for i in range(n):
        m[i][i] = 0

    for chain_length in range(2, n+1):
        for i in range(n - chain_length + 1):
            j = i+ chain_length - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]* p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
    
    return m[0][n-1]

if __name__ == "__main__":
    matrix_dimensions = [5,10,3,5,20,15]

    mininmum_scalar_multiplication = Matrix_chain(matrix_dimensions)

    print("Minimum number od scalar multiplication needed:", mininmum_scalar_multiplication)