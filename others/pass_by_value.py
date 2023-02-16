# Function definition is here
def changeme(mylist):
    print("Values inside the function before change: ", mylist)
    mylist = [1, 2, 3, 4]  # This would assi new reference in mylist
    print("Values inside the function: ", mylist)


# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)
