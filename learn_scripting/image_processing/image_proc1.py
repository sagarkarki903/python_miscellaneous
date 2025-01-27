from PIL import Image, ImageFilter

img = Image.open('./nobita.jpg')
# filtered_img = img.filter(ImageFilter.BLUR)
# grey_scaled_img = img.convert('L')

#format below in the parameter is optional but is  a good practice
# grey_scaled_img.save("grey_scaled_img.png", "png")
img2 = Image.open('./earth.webp')
# print(img2)
#
# img2.save("earth.png")
# img2.show()

#...............................................
#Reduce the size of an image
img3 = Image.open('./cafe.jpg')
print(img3.size)
new_img3 = img3.resize((600, 600))
print(new_img3.size)

new_img3.save("reduced_img3.jpg")




