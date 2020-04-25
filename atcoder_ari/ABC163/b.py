N, M = map(int, input().split())
day = sum(map(int, input().split()))

(print(N - day) if (N - day) >= 0 else print(-1))
