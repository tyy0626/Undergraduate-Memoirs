import sys

def dp_method(tasks):
    # dp: list of (d, p)
    #0-1 bag,state transition equation
    #dp[t] = max(dp[t],dp[t-1]+pi
    tasks.sort(key=lambda x: x[0])  # By deadline ascending
    max_d = max(d for d, _ in tasks)
    total_p = sum(p for _, p in tasks)

    dp = [0] * (max_d + 1)  # dp[t] = maximum benefit that can be obtained in t time slots
    for d, p in tasks:
        # Only allow the current task to be placed in slots 1..d, and traverse in reverse order to avoid reusing the same task
        for t in range(d, 0, -1):
            dp[t] = max(dp[t], dp[t - 1] + p)

    max_profit = max(dp)
    return total_p - max_profit

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    tasks = []
    idx = 1
    for i in range(n):
        d = int(data[idx])
        p = int(data[idx+1])
        idx += 2
        tasks.append((d, p))
    print(dp_method(tasks))

if __name__ == '__main__':
    main()
