# Python program to interchange first and last elements in a list

def swap(size,user_list):
	print(user_list)
	user_list[0], user_list[size-1] = user_list[size-1],user_list[0]
	print(user_list)

user_list=[]
size=int(input("Ener the size of the list: ",))
for i in range(size):
	user_list.append(int(input("Enter Element: ")))


swap(size,user_list)
