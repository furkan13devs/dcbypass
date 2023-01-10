#!/bin/bash

RED='\033[1;31m'
NC='\033[0m'

printf "${RED}LINUX INSTALL SCRIPT${NC}\n"
sleep 2

echo '[*] gereksinimler yükleniyor...'

pip install --upgrade pip
pip install -r requirements.txt

echo '[*] yükleniyor...'

chmod +x bypassblacklist.py
shopt -s expand_aliases
alias bypass='python3 ~/dcbypass/bypassblacklist.py'

sleep 2
printf "${RED}[*] yükleme tamamlandı (veya gereksinimler zaten karşılandı)${NC}\n"
echo 'Do you want to run the program? y/n'
read launch
if [ $launch == "y" ]
then
echo '[*] açılıyor...'
python3 bypassblacklist.py
elif [ $launch ==  "n" ]
then
echo '[!] çıkış....'
sleep 2
exit
else
echo '[!] Söz diziminizi kontrol edin, yanlış girdi! (Büyük/küçük harfe duyarlı "y" veya "n")'
sleep 1
echo '[!] ÇIKIŞ YAPILIYOR!'
sleep 2
exit
fi
