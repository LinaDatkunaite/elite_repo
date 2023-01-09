from PIL import Image, ImageFilter, ImageEnhance

img = Image.open("Tiger.jpg")
# atidaryti foto
# img.show()
# issisaugot nauja paredaguota foto
# img.save("new_dog.jpg")


# size - width and hight (dimensions in picksels)
# print(img.format, img.size, img.mode)

# thumbnails - mini foto - pakeisti dydi pikseliu
# size = (128,128)
# img.thumbnail(size)
# img.show()

# nuotraukos apkarpymas (upper-left and down-right)
# x min x max y min y max - parametrai
# crop_box = (100,100,200,200)
# cropped_immage = img.crop(crop_box)
# cropped_immage.show()
# cropped_immage.save("tigro_plaukas.jpg")


# pasukti image su transpose
# img.transpose(Image.FLIP_TOP_BOTTOM).show()
# img.transpose(Image.ROTATE_90).show()
# img.transpose(Image.ROTATE_180).show()


# resize image priima viena tuple elementa
# img.resize((250,150)).show()

# iskraipytas (nes neproporcingai ivesti parametrai)
# img.resize((300,300)).show()

# proporcingai reikia sumazinti krastine - ziurim i W 6000 and H 4000  6K/4K = 1.5 santykis kad gautusi neiskraipyta foto
# img.resize((int(100*1.5),100)).show()

# png overlap:
# img2 = Image.open("tree.png")
# print(img2.size, img.size[1], img.size[0])
# 0,0 koordinate pats kairinis kampas, img2.size[0] - x max, img2.size[1] - y max().
# logo_location = (0,0, img2.size[0], img2.size[1])

# 3 - parametras  img2transparency - chanellis
# img.paste(img2, logo_location, img2)
# img.show()

# blurred=img.filter(ImageFilter.BLUR).show()
# blurred=img.filter(ImageFilter.EDGE_ENHANCE_MORE).show()

data=img.getdata()
# for ind, i in enumerate(data):
#     print(i)
# print(ind)



# prideti balta juosta nuo virsaus
# 3 parametrai - Red Green Blu
# for i in range(5):
#     print(data[i])
# new_data = []
# # spalva nurodoma - 255 visur yra balta, 0 butu juoda
# white_pixel = (255,255,255)
# for i in range(100000000):
#     new_data.append(white_pixel)
# img.putdata(new_data)
# img.show()

# L - juoda balta, SMYC
# img.convert("L").show()
# new_img = img.convert("RGB")
# new_img.show()



# Sharpness, brightness, contrast
# enh=ImageEnhance.Contrast(img)
# enh.enhance(1.9).show()
# enh.enhance(1.9).save("tiger_contrast".jpg)


# enh=ImageEnhance.Color(img)
# enh.enhance(1.9).show()

# img3 = Image.open('C:\\Users\\darius\\Desktop\\tigro_plaukas.jpg')
# img3.show()