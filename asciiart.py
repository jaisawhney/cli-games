import requests
import random

text = input("ASCII Art Text: ")
font = input("ASCII Art Font: ")


# Get ascii text
def get_ascii_art(text, font):
    req = requests.get(f'http://artii.herokuapp.com/make?text={text}{("&font=%s" % font) if font else ""}')
    print("Font:", font)
    print(req.text)


# Get all available fonts
def get_fonts():
    fonts = requests.get('http://artii.herokuapp.com/fonts_list')
    fonts_array = fonts.text.split('\n')
    return fonts_array


fonts_list = get_fonts()
if font.lower() == "random":
    for i in range(3):
        font = random.choice(fonts_list)
        get_ascii_art(text, font)
elif not font:
    get_ascii_art(text, "")
else:
    if font.lower() not in fonts_list:
        print("Invalid font!")
        quit()
    get_ascii_art(text, font.lower())
