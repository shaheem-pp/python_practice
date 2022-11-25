n =5
total_rows = n*2
total_cols = (n*4)
for i in range(0,total_rows):
	for j in range(0,total_cols):
		if j<=i :			
			print("*",end=" ")
		elif j>= total_cols/2:
			for _ in range(0,j):
				print((" "*5),"*", end="")
		else:
			print(" ",end=" ")
	print()



# row = (n*2)-1
# for i in range(0,row):
# 	for j in range(0,n):
# 		if j==i or j==row:
# 			print("*",end=" ")
# 		else:
# 			print("|",end=" ")
# 	print('\n')

# for j in range(0,5):
# 	for i in range(0,j):
# 		print("*", end=" | ")
# 	print('\n')

# for j in range(5,0,-1):
# 	for i in range(j,0,-1):
# 		print("*", end=" | ")
# 	print('\n')