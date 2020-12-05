def convert_list(str):
    if len(str) > 2:
        return str[1:-1].split(", ")
    else:
        return list()


def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


fst_list = input()
sec_list = input()

fst_list = convert_list(fst_list)
sec_list = convert_list(sec_list)

fst_list = fst_list + sec_list
fst_list = [int(item) for item in fst_list]

print(merge_sort(fst_list))
