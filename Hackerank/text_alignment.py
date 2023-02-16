# #     H
# #    HHH
# #   HHHHH
# #  HHHHHHH
# # HHHHHHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #   HHHHHHHHHHHHHHHHHHHHHHHHH
# #   HHHHHHHHHHHHHHHHHHHHHHHHH
# #   HHHHHHHHHHHHHHHHHHHHHHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #   HHHHH               HHHHH
# #                     HHHHHHHHH
# #                      HHHHHHH
# #                       HHHHH
# #                        HHH
# #                         H
# def left_pad_string(string, length, char):
# 	padded_string = string.ljust(length, char)
# 	print(padded_string)
#
#
# def right_pad_string(string, length, char):
# 	padded_string = string.rjust(length, char)
# 	# return (padded_string)
# 	print(padded_string)
#
#
# def center_pad_string(string, length, char):
# 	padded_string = string.center(length, char)
# 	print(padded_string)
#
# chars="a"
# left_pad_string(chars, 9, "*")
# right_pad_string(chars, 9, "*")
# center_pad_string(chars, 9, "*")
#
#
# def top_left_cone():
# 	for i in range(1, 10, 2):
# 		chars = "H" * i
# 		center_pad_string(chars, 9, " ")
#
# top_left_cone()
#
# def vertical_left_bar():
# 	for i in range(6):
# 		chars = "HHHHH"
# 		right_pad_string(chars, 7, " ")
# 		left_pad_string(chars, 7, " ")
#
# vertical_left_bar()
#
# def vertical_right_bar():
# 	for i in range(6):
# 		chars = "HHHHH"
# 		right_pad_string(chars, 20, " ")
#
# vertical_right_bar()
#
# print(len("HHHHHHHHHHHHHHHHHHHHHHHHH"))


# Replace all ______ with rjust, ljust or center.

thickness = 5  # This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
	print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))
#
# # Top Pillars
for i in range(thickness + 1):
	print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
#
# # Middle Belt
for i in range((thickness + 1) // 2):
	print((c * thickness * 5).center(thickness * 6))
#
# # Bottom Pillars
for i in range(thickness + 1):
	print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))
#
# # Bottom Cone
for i in range(thickness):
	print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(
			thickness * 6))
