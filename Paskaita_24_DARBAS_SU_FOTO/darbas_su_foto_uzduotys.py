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
# # C:/Users/darius/PycharmProjects/Elite/elite_repo/Test_for_pics
# folder=input("Input folder path like C:/Users/...: ")
# os.chdir(os.path.join(folder))
# while True:
#     inp=int(input("Choose action: 1 - show images, 2 - resize images, 3 - exit"))
#
#     if inp == 1:
#         for ind, i in enumerate(os.listdir(os.path.join(folder)), 1):
#             if i.endswith(('.png', '.jpg')):
#                 print(ind, i)
#
#     if inp == 2:
#         pic = input("Input picture name: ")
#         img = Image.open(f"{pic}")
#         img = img.convert("RGBA")
#         height = int(input("Input desirable picture height: "))
#         width = round(img.size[1] / img.size[0] * height)
#         img = img.resize((height, width))
#         logo = Image.open(r'C:\Users\darius\PycharmProjects\Elite\elite_repo\Paskaita_24_DARBAS_SU_FOTO\tree.png')
#         logo = logo.convert("RGBA")
#         logo_height = height/10
#         logo_width = round(logo.size[1] / logo.size[0] * logo_height)
#         logo = logo.resize((int(logo_height), int(logo_width)))
#         logo_location = (
#                         img.size[0]-logo.size[0],
#                         img.size[1]-logo.size[1],
#                         img.size[0],
#                         img.size[1])
#         img.paste(logo, logo_location, logo)
#         img.show()
#         img.save(f'{folder}/modified_{pic.split(".")[0]}.png')
#
#     if inp == 3:
#         print("Bye")
#         break



# Parašykite programą, kuriai padavus nuotrauką ir R G B reikšmes, ji pakoreguotų kiekvieną pikselį atitinkamai.
# T.y. jeigu reikšmė teigiama - pridėtų, jeigu neigiama - atimtų. Neleiskite galutinėms
# reikšmėms būti mažesnėmis už nulį ir didesnėmis už 255!
#
from PIL import Image
import os

# def ribos(sk):
#     if sk < 0:
#         return 0
#     elif sk > 255:
#         return 255
#     return sk
#
#
# def adjust_colors(img, r, g, b):
#     img = Image.open(img)
#     data = img.getdata()
#     new_data = []
#     for pixel in data:
#         red = ribos(pixel[0] + r)
#         green = ribos(pixel[1] + g)
#         blue = ribos(pixel[2] + b)
#         new_pixel = (red, green, blue)
#         new_data.append(new_pixel)
#
#     img.putdata(new_data)
#     return img
#
#
# new_img = adjust_colors('logo.png', 0, 0, 0)
# new_img.show()



# Parašykite programą, kuriai padavus nuotrauką, ir nurodžius pikselio R G B reikšmes, visi pikseliai,
# kurių nors viena reikšmė viršija jūsų nurodytą ribą, būtų pakeisti juodais, o likusieji baltais.
# def turn_binary(img, r, g, b):
#     img = Image.open(img)
#     data = img.getdata()
#     new_data = []
#     black = 0, 0, 0
#     white = 255, 255, 255
#     for pixel in data:
#         if pixel[0] >= r or pixel[1] >= g or pixel[2] >= b:
#             new_data.append(black)
#         else:
#             new_data.append(white)
#
#     img.putdata(new_data)
#     img.show()
#     return img
#
# turn_binary("Tiger.jpg", 200, 200, 200 )