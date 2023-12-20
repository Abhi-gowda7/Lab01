def min_steps_to_empty(s):
    n = len(s)
    if n <= 1:
        return 0

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

# Example usage:
input_str = input()
result = min_steps_to_empty(input_str)
print(f"Minimum steps to delete characters: {result}")
