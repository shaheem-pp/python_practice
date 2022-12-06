import re

string = "product/f1130124140odwgrc.png"

my_new_string = re.sub('[^a-zA-Z0-9 \n\.]', ' ', string)
dir_name = my_new_string.split(" ")[0]
file_name = my_new_string.split(" ")[-1]
print(dir_name)
print(file_name)
