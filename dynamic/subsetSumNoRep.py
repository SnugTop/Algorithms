from sys import stdin, stdout


def maximum_gold(capacity, weights):
    dp = [0] * (capacity + 1)
   
    for weight in weights:
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + weight)
    return dp[capacity]


if __name__ == '__main__':
    input_data = stdin.read().strip().split()
    input_capacity = int(input_data[0])
    n = int(input_data[1])
    input_weights = list(map(int, input_data[2:2 + n]))

    result = maximum_gold(input_capacity, input_weights)
    
    stdout.write(f"{result}\n")