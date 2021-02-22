from googletrans import Translator
with open('Translate.txt', 'r+', encoding='utf-8') as pf:
    with open('Translate.txt', 'r+', encoding='utf-8') as tf:
        tr = Translator()
        text = {line.split()[0]: int(line.split()[2]) for line in tf}
        translated = [el[0] + tr.translate(text.keys()) for el in text.items()]
        print(translated)
