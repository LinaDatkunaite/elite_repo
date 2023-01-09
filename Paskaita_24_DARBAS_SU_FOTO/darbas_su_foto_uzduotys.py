import os

from PIL import Image, ImageFilter, ImageEnhance

# Turime logo su peršviečiamu fonu, dydis 128*128. Atsisiųskite, ir perdarykite taip, kad nuo viršaus ir apačios
# nusiimtų po 28 eilutes pikselių. Išsisaugokite, nes naudosime sekančioms užduotims.
# img = Image.open("logo.png")
# # x-min, y-min, x-max, y-max
# crop_box = (0,28,128,100)
# cropped_immage = img.crop(crop_box)
# cropped_immage.show()
# img.save("croped_logo.png")


# sukurkite funkciją, kuri priimtų paveikslėlį
# kontrasto, spalvingumo, aštrumo ir ryškumo reikšmes išsaugoti ar ne reikšmę
# ir atitinkamai pakoreguotų paveikslėlio nustatymus. Parodytų nuotrauką ekrane.
# Priklausomai nuo pasirinkimo, išsaugotų arba ne. Išsaugokite faile,
# prie originalaus pavadinimo pridėję pvz. '_modified', tarkime dog_modified.jpg.


# def picture_edit(picture_name, contrast=1, color=1, sharpness=1, brightness=1, save=0):
#     img = Image.open(f"{picture_name}")
#
#     enh = ImageEnhance.Contrast(img)
#     contrasted = enh.enhance(contrast)
#
#     enh = ImageEnhance.Color(contrasted)
#     colored = enh.enhance(color)
#
#     enh = ImageEnhance.Sharpness(colored)
#     sharpened = enh.enhance(sharpness)
#
#     enh = ImageEnhance.Brightness(colored)
#     brightned = enh.enhance(brightness)
#
#     if save == 1:
#         name = picture_name.split(".")
#         print(f'{name[0]}_modified.{name[1]}')
#         brightned.save(f'{name[0]}_modified.{name[1]}')
#         brightned.show()
#     else:
#         brightned.show()
#
#
# picture_edit("Tiger.jpg", 2, 2, 1.9, 1.9, 0)


# Sukurkite programą, kuri, gavusi nuorodą į katalogą, praiteruos
# visus jame esančius failus, išrinks nuotraukas, pakeis dydį pagal jūsų nurodytą
# aukštį išlaikant proporcijas, ir kiekvienos nuotraukos apatiniame dešiniajame kampe įdės logotipą,
# tą kurį išsisaugojote pirmoje užduotyje. Naudokite .resize, kadangi nuotrauką galbūt reikės padidinti,
# nebūtinai tik sumažinti.
# import os
# link = r"C:\Users\darius\PycharmProjects\Elite\elite_repo\Test_for_pics"
# height = 1000
# logo = Image.open(r"C:\Users\darius\PycharmProjects\Elite\elite_repo\Paskaita_24_DARBAS_SU_FOTO\logo.png")
# logo = logo.convert("RGBA")
# resized_logo = logo.resize((int(height / 15 * 1.5), int(height / 15)))
# resized_logo.show()
#
# os.chdir(link)
# print(os.getcwd())
# print(os.listdir())
#
# for ind, i in enumerate(os.listdir(), 1):
#     if i.split(".")[-1] == "jpg":
#         print(ind, i)
#         img = Image.open(f"{i}")
#         img = img.convert("RGBA")
#         resized_img = img.resize((int(height * 1.5), height))
##         logo_location = (0,0, resized_logo.size[0], resized_logo.size[1])
#         resized_img.paste(resized_logo, logo_location, resized_logo)
#         resized_img.show()



from PIL import Image
import os


def ribos(sk):
    if sk < 0:
        return 0
    elif sk > 255:
        return 255
    return sk


def adjust_colors(img, r, g, b):
    img = Image.open(img)
    data = img.getdata()
    new_data = []
    for pixel in data:
        red = ribos(pixel[0] + r)
        green = ribos(pixel[1] + g)
        blue = ribos(pixel[2] + b)
        new_pixel = (red, green, blue)
        new_data.append(new_pixel)

    img.putdata(new_data)
    return img


new_img = adjust_colors('logo.png', 0, 0, 0)
new_img.show()




from PIL import Image
import os


def ribos(sk):
    if sk < 0:
        return 0
    elif sk > 255:
        return 255
    return sk


def adjust_colors(img, r, g, b):
    img = Image.open(img)
    data = img.getdata()
    new_data = []
    for pixel in data:
        red = ribos(pixel[0] + r)
        green = ribos(pixel[1] + g)
        blue = ribos(pixel[2] + b)
        new_pixel = (red, green, blue)
        new_data.append(new_pixel)

    img.putdata(new_data)
    return img


new_img = adjust_colors('logo.png', 0, 0, 0)
new_img.show()