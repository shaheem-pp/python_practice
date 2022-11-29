from PIL import Image
import time

from variables import IMAGE_COMPRESSION_DIR, IMAGE_COMPRESSION_SAVE_PATH

foo = Image.open(IMAGE_COMPRESSION_DIR)  # My image is a 200x374 jpeg that is 102kb large
print(foo.size)  # (200, 374)

# downsize the image with an ANTIALIAS filter (gives the highest quality)
foo = foo.resize((160, 300), Image.ANTIALIAS)

path = IMAGE_COMPRESSION_SAVE_PATH

filename = "cf_" + str(time.time()) + '.jpg'

full_path = path + filename

foo.save(full_path, quality = 95)  # The saved downsized image size is 24.8kb
print(foo.size)  # (200, 374)

foo.save(full_path, optimize = True, quality = 95)  # The saved downsized image size is 22.9kb
