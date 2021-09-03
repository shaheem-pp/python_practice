f = open("file.txt", "w")

for i in range(1, 100000):
    if i % 2 == 0:
        oe = "Even"
    else:
        oe = "Odd"
    f.writelines("if num == " + str(i) + ":  print(\"It\'s " + oe + "\")\n")

f.close()
