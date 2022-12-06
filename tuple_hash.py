n = int(input())  # how many numbers to accept
numbers = [int(num) for num in input().split(" ", n - 1)]
t = tuple(numbers)
print(hash(t))
