numbers = input().split(", ")

numbers = [bin(round(float(item))).count("1") for item in numbers]
numbers.sort()
print(*numbers, sep=", ")
