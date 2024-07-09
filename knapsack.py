
def knapsack(capacity, weights, values):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

if __name__ == "__main__":
    capacity = 37
    weights = [10, 20, 30]
    values = [60, 100, 120]
    print("Maximum value:", knapsack(capacity, weights, values))