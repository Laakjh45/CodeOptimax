def knapsack_solution(weights, values, capacity):
    n = len(values)
    K = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weights[i - 1] <= w:
                K[i][w] = max(values[i - 1] + K[i - 1][w - weights[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    # Backtrack to find the items included in the optimal solution
    res = K[n][capacity]
    w = capacity
    items_included = []

    for i in range(n, 0, -1):
        if res != K[i - 1][w]:
            items_included.append((weights[i - 1], values[i - 1]))
            res -= values[i - 1]
            w -= weights[i - 1]

    items_included.reverse()  # Reverse to maintain the original order
    return K[n][capacity], items_included