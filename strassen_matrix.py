def strassen(A, B):
    n = len(A)
    
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    
    
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    
    M1 = strassen(
        [[A11[i][j] + A22[i][j] for j in range(mid)] for i in range(mid)],
        [[B11[i][j] + B22[i][j] for j in range(mid)] for i in range(mid)]
    )
    M2 = strassen(
        [[A21[i][j] + A22[i][j] for j in range(mid)] for i in range(mid)],
        B11
    )
    M3 = strassen(
        A11,
        [[B12[i][j] - B22[i][j] for j in range(mid)] for i in range(mid)]
    )
    M4 = strassen(
        A22,
        [[B21[i][j] - B11[i][j] for j in range(mid)] for i in range(mid)]
    )
    M5 = strassen(
        [[A11[i][j] + A12[i][j] for j in range(mid)] for i in range(mid)],
        B22
    )
    M6 = strassen(
        [[A21[i][j] - A11[i][j] for j in range(mid)] for i in range(mid)],
        [[B11[i][j] + B12[i][j] for j in range(mid)] for i in range(mid)]
    )
    M7 = strassen(
        [[A12[i][j] - A22[i][j] for j in range(mid)] for i in range(mid)],
        [[B21[i][j] + B22[i][j] for j in range(mid)] for i in range(mid)]
    )


    C11 = [
        [
            M1[i][j] + M4[i][j] - M5[i][j] + M7[i][j] for j in range(mid)
        ]
        for i in range(mid)
    ]
    C12 = [
        [
            M3[i][j] + M5[i][j] for j in range(mid)
        ]
        for i in range(mid)
    ]
    C21 = [
        [
            M2[i][j] + M4[i][j] for j in range(mid)
        ]
        for i in range(mid)
    ]
    C22 = [
        [
            M1[i][j] + M3[i][j] - M2[i][j] + M6[i][j] for j in range(mid)
        ]
        for i in range(mid)
    ]

    
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]

    return C


A = [[6, 3], [2, 5]]
B = [[5, 6], [7, 8]]
result = strassen(A, B)
print(result)
