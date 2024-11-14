def compute_operations(n):
    dp = [0] * (n + 1)
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
    
    sequence = []
    while n > 1:
        sequence.append(n)
        if dp[n] == dp[n - 1] + 1:
            n -= 1
        elif n % 2 == 0 and dp[n] == dp[n // 2] + 1:
            n //= 2
        elif n % 3 == 0 and dp[n] == dp[n // 3] + 1:
            n //= 3
    
    sequence.append(1)
    sequence.reverse()
    return sequence

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(" ".join(map(str, output_sequence)))
