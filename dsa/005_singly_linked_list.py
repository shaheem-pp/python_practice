# Create a linked list that has the following capabilities:
#
# 1 - Add an element to the beginning of the list
# 2 - Add an element to the end of the list
# 3 - Add an element after a specific value in the list
# 4 - Add multiple elements to the end of the list at once
# 5 - Delete the first occurrence of a specific value in the list
# 6 - Check if a specific value exists in the list
# 7 - Return the total number of elements in the list
# 8 - Display all the elements in the list


class Node():

	def __int__(self, data = None):
		self.data = data
		self.next = None


class LinkedList():
	def __int__(self):
		self.head = None
