n = int(input())

if (n < 10):
    sum = 0
    for i in range(0, n):
        sum += i
    print(sum)
elif 10 <= n < 20:
    print("used numbers= ", end="")
    print(*range(0, n), sep=", ")
else:
    print("very big number")
