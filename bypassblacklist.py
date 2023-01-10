#Report any issue on Github.

import os
import sys
import time
import pyfiglet

# Note : the str "word" is only the raw input by user, it will not change...
word = ""
banner = pyfiglet.figlet_format("DISCORD BLACKLISTED WORDS BYPASS 2023")

print(banner)
print("A tool by Xprogrammer777 \n")
word = str(input("[*] BYPASS ETMEK İSTEDİĞİNİZ KELİMEYİ YAZIN: "))

def startprocess():

    if "a" in word:
        bypassed = word.replace('a', '\u0430') 

    elif "c" in word:
        bypassed = word.replace('c', '\u03F2')

    elif "e" in word:
        bypassed = word.replace('e', '\u0435')

    elif "o" in word:
        bypassed = word.replace('o', '\u043E')

    elif "p" in word:
        bypassed = word.replace('p', '\u0440')

    elif "s" in word:
        bypassed = word.replace('s', '\u0455')

    elif "d" in word:
        bypassed = word.replace('d', '\u0501')
    
    elif "q" in word:
        bypassed = word.replace('q', '\u051B')

    elif "w" in word:
        bypassed = word.replace('w', '\u051D')
        
    else:
        print("[!]Üzgünüm, bu kelimeyi atlayamıyoruz, tüm kelimeleri atlamak için yeni bir güncelleme yayınlayacağız.")
        time.sleep(1)
        print("[!] çıkış yapılıyor!")
        quit()
        
    print("[*] işlem başarıyla tamamlandı!")
    
    time.sleep(1)

    print("[*] BU SÖZCÜĞÜ KOPYALAYIP YAPIŞTIRIN: ", bypassed)
        
    #print the result


if word == "":
    time.sleep(1)
    print("[!] bir kelime yazın")
    time.sleep(1)
else:
    print("[*] işte benim sıram başlıyoruz...")
    time.sleep(1)
    startprocess()
