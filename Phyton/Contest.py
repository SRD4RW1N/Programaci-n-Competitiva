n, k = map(int, input().split())
d, s = map(int, input().split())
x = (n*d - s*k) / (n-k)
if x < 0 or x > 100:
    print("impossible")
else:
    print("{:.6f}".format(x))