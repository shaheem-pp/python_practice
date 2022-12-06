from PIL import Image
import time

foo = Image.open(
        "/Users/shaheempp/Downloads/lulumall-cochin.jpg")
print(foo.size)  # (200, 374)
width, height = foo.size

if height >= 250 and width >= 250:
    if height == width:
        foo = foo.resize((250, 250), Image.Resampling.LANCZOS)
    elif height > width:
        aspect_ratio = height / width
        new_width = 250
        new_height = new_width * aspect_ratio
        foo = foo.resize((int(new_width), int(new_height)), Image.Resampling.LANCZOS)
    else:
        aspect_ratio = width / height
        new_height = 250
        new_width = new_height * aspect_ratio
        foo = foo.resize((int(new_width), int(new_height)), Image.Resampling.LANCZOS)

path = '/Users/shaheempp/Developer/python_practice/image_compression/'

filename = "cf_" + str(time.time()) + '.png'

full_path = path + filename

foo.save(full_path, optimize = True, quality = 100)
print(foo.size)
