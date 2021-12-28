def array_sum(array, size):
    sum = 0
    for i in array:
        sum = sum + i
    return sum


size = int(input("Enter size of list: "))
myList = []
for i in range(size):
    num = int(input("Enter element {}: ".format(i + 1)))
    myList.append(num)

sum = array_sum(myList, size)
print("Sum : {}".format(sum))
