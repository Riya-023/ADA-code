def lcs(X, Y):
    
    m = len(X)
    n = len(Y)

    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    lcs_length = L[m][n]

    
    lcs = [''] * (lcs_length + 1)
    lcs[lcs_length] = ''

    i, j = m, n
    while i > 0 and j > 0:

        if X[i - 1] == Y[j - 1]:
            lcs[lcs_length - 1] = X[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1

        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)

X = "AGGTAB"
Y = "GXTXAYB"
print("String X:", X)
print("String Y:", Y)
print("Longest Common Subsequence:", lcs(X, Y))
