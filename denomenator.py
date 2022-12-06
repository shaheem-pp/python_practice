import math

# width = 4088
# height = 8852
#
#
# width = math.ceil(width / 100)
# print(width)
# w_mult = math.ceil(100 / width)
# height = math.ceil(height / width)
# print(height)
# print(w_mult)
# h_mult = math.ceil(100 / height)
# print(width * w_mult, height * h_mult)
# if height <= width:
#     h_to_100_diff = height - 100
#     print(h_to_100_diff)
#     new_height = height - h_to_100_diff
#     print('height', height)
#     print('new_height', new_height)
#     new_width = width - h_to_100_diff
#     print('width', width)
#     print('new_width', new_width)
# else:
#     w_to_100_diff = width - 100
#     new_width = width - w_to_100_diff
#     print('width', width)
#     print('new_width', new_width)
#     new_height = height - w_to_100_diff
#     print('height', height)
#     print('new_height', new_height)


width = 216
height = 100
w2 = width * width
h2 = height * height
diagonal = math.sqrt(w2 + h2)
aspect_ratio = width/height
print(diagonal)
print(aspect_ratio)
print(diagonal / aspect_ratio)
print(100*aspect_ratio)
# aspect_ratio1 = height/width
# aspect_ratio2 = width/height
# print(aspect_ratio1)
# print(aspect_ratio2)
# print(100*aspect_ratio1)
# print(100*aspect_ratio2)

# a = 4088
# b = 8852
# ratio = b/a
#
# # a=100
# # b=216
# # ratio=b/a
# print(ratio)
# print(100*ratio)
