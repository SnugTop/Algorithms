def edit_distance(first_string, second_string):
    len1, len2 = len(first_string), len(second_string)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    
    #Base Case
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j
                     
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if first_string[i - 1] == second_string[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1] [j] + 1, 
                    dp[i][j - 1] + 1,
                    dp[i - 1] [j - 1] + 1)
    return dp[len1][len2]
                     
if __name__ == "__main__":
    print(edit_distance(input(), input()))