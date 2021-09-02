import requests
import random

text = input("ASCII Art Text: ")
font = input("ASCII Art Font: ")


def getAsciiArt(text, font):
    req = requests.get(f'http://artii.herokuapp.com/make?text={text}{("&font=%s" % font) if font else ""}')
    print("Font:", font)
    print(req.text)


if font.lower() == "random":
    fonts = requests.get('http://artii.herokuapp.com/fonts_list')
    fontsArray = fonts.text.split('\n')
    random_font = random.choice(fontsArray)
    for i in range(3):
        font = random.choice(fontsArray)
        getAsciiArt(text, font)
elif not font:
    getAsciiArt(text, "")
else:
    getAsciiArt(text, font.lower())
