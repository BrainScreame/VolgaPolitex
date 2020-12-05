def form_list(N, K):
    res = []

    items = [*range(1, N + 1)]
    while len(items) != 0:
        if K > len(items):
            tmp = items[K % len(items) - 1]
        else:
            tmp = items[K - 1]

        items = items[items.index(tmp):] + items[:items.index(tmp)]
        items.remove(tmp)
        res.append(tmp)

    return res


N = int(input())
K = int(input())
print(form_list(N, K))
