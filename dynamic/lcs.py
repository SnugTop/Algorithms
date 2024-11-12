def lcs(X, Y):
    m = len(X)
    n = len(Y)
    # Create a DP table to store lengths of LCS
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the L table in bottom-up fashion and print the table
    print("LCS table:")
    # Print header row (characters of Y)
    print("    ", end="")
    for char in Y:
        print(f"  {char}", end="")
    print()
    
    for i in range(m + 1):
        # Print header column (characters of X)
        if i == 0:
            print("  ", end="")
        else:
            print(f"{X[i - 1]} ", end="")
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
            # Print the current cell value
            print(f"{L[i][j]:3}", end="")
        print()  # Newline after each row

    # Reconstruct the LCS from the L table
    index = L[m][n]
    lcs_seq = [''] * index  # Create a character array to store the LCS string
    i, j = m, n

    # Start from L[m][n] and work backwards to reconstruct the LCS
    while i > 0 and j > 0:
        # If current characters in X and Y are the same, they are part of LCS
        if X[i - 1] == Y[j - 1]:
            lcs_seq[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        # Move to the direction of the larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Convert the list of characters into a string
    lcs_str = ''.join(lcs_seq)
    return L[m][n], lcs_str

# Example usage:
X = "ELEPHANT"
Y = "RELEVANT"
length, sequence = lcs(X, Y)
print(f"\nLength of LCS: {length}")
print(f"LCS: {sequence}")
