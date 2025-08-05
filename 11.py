import PIL
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageDraw, ImageFont

img = Image.open("/Users/abhijaypaliwal/PycharmProjects/Pandas_project_1/.venv/abhijay.jpg")

plt.imshow(img)

print(img.format)
print(img.size)
print(img.mode)

resized_ratio = img.resize((300,200))
print(resized_ratio.size)
#resized_ratio.save("abhijay_resized.jpg")

resized = img.resize((img.width //2 , img.height //2))
resized.save("abhijay_resized_half.jpg")
print(resized.size)

#crop(left,upper, right, lower)
cropped = img.crop((100,100,400,400)) #(x1, y1, x2, y2)
print(cropped.size)
cropped.save("abhijay_resized_cropped.jpg")

#rotating and flipping
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
flipped.save("abhijay_flipped.jpg")

# convert to greyscale
gray_img = img.convert('L')
gray_img.save("abhijay-gray.jpg")

r,g,b = img.split()

swapped = Image.merge('RGB',(r,g,b  ))
swapped.save("abhijay-swapped.jpg")

#apply blur
blurred = img.filter(ImageFilter.BLUR)
blurred.save("abhijay-blurred.jpg")

sharpened = img.filter(ImageFilter.SHARPEN)
sharpened.save("abhijay-sharpened.jpg")

edged = img.filter(ImageFilter.FIND_EDGES)
edged.save("abhijay-edged.jpg")

gaussian_blur = img.filter(ImageFilter.GaussianBlur(radius=5))
gaussian_blur.save("abhijay-gaussian-blur.jpg")

draw = ImageDraw.Draw(img)
#draw a rectange xq, yq, x2, y2
draw.rectangle((50,50,150,150), outline='red', width=3)

font = ImageFont.load_default()
draw.text((100,100), "hello pillow", fill='blue', font=font)

plt.imshow(img)
plt.show()


