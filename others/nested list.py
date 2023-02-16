number_of_students = int(input())
student_list = []
mark_list = []
for _ in range(number_of_students):
	a =[]
	name = input()
	score = float(input())
	a.append(name)
	a.append(score)
	student_list.append(a)
	mark_list.append(score)
sorted_mark = sorted(mark_list)
student_list = sorted(student_list)
mark_set = [*set(sorted_mark)]
mark_list = list(mark_set)
search_word = mark_list[1]
results = [sub_list[0] for sub_list in student_list if sub_list[1] == search_word]
for r in results:
	print(r)