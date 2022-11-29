from PIL import Image
import time

foo = Image.open(
        "/Users/shaheempp/Developer/python_practice/image_compression/cf_1669706063.595774.png")  # My image is a 200x374 jpeg that is 102kb large
print(foo.size)  # (200, 374)
width, height = foo.size

# if ((width / 3) > 85) and ((height / 3) > 85):
#     if ((width / 4) > 1500) or ((height / 4) > 1500):
#         foo = foo.resize((int(width / 6), int(height / 5)), Image.Resampling.LANCZOS)
#     elif ((width / 4) > 1000) or ((height / 4) > 1000):
#         foo = foo.resize((int(width / 4), int(height / 4)), Image.Resampling.LANCZOS)
#     else:
#         foo = foo.resize((int(width / 3), int(height / 3)), Image.Resampling.LANCZOS)
# foo = foo.resize((int(width / 3), int(height / 3)), Image.Resampling.LANCZOS)

path = '/Users/shaheempp/Developer/python_practice/image_compression/'

filename = "cf_" + str(time.time()) + '.png'

full_path = path + filename

foo.save(full_path, optimize = True, quality = 95)
print(foo.size)
