
# 0, 1
CountNumber = lambda N, X: N - sum(X % -~i > 0 or X / -~i > N for i in range(N))

print(CountNumber(6, 12))
