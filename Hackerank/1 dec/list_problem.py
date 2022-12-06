if __name__ == '__main__':
    N = int(input())
    mylist = list()

    for i in range(N):
        input_cmnd = input()
        l = input_cmnd.split()

        if (l[0] == "print"):
            print(mylist)
        elif (l[0] == "reverse"):
            mylist.reverse()
        elif (l[0] == "pop"):
            mylist.pop()
        elif (l[0] == "sort"):
            mylist.sort()
        elif (l[0] == "append"):
            mylist.append(int(l[1]))
        elif (l[0] == "remove"):
            mylist.remove(int(l[1]))
        elif (l[0] == "insert"):
            mylist.insert(int(l[1]), int(l[2]))
