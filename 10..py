#PILLOW
# IT IS A PYTHON IMAGE LIBRARY FORK THAT ADDS SUPPORTS TO MODERN IMAGE FORMATS
#SUPPORTS OPENING, EDITING AND SAVING IMAGE FORMAT SUCH AS JPEG, PNG, GIF, BMP, TIFF

import PIL
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageDraw, ImageFont

img = Image.open("/Users/abhijaypaliwal/PycharmProjects/Pandas_project_1/.venv/dan-MdTtpxGlrz8-unsplash.jpg")
plt.imshow(img)
plt.axis('off')
#img.save("./test.jpg")
img.save("abhijay.jpg", quality=2000)
plt.show()
