def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D array to store lengths of longest common subsequence
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the L matrix in bottom-up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Length of LCS
    lcs_length = L[m][n]

    # Backtrack to find the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()  # Reverse the list to get the correct order
    return ''.join(lcs), L
