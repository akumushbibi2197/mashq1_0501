#1-misol
from datetime import datetime

s1 = input("1-sana (YYYY-MM-DD HH:MM): ")
s2 = input("2-sana (YYYY-MM-DD HH:MM): ")

t1 = datetime.strptime(s1, "%Y-%m-%d %H:%M")
t2 = datetime.strptime(s2, "%Y-%m-%d %H:%M")

farq = abs(t2 - t1)
kun = farq.days
soat = farq.seconds // 3600
daq = (farq.seconds % 3600) // 60

print(f"Farq: {kun} kun, {soat} soat, {daq} daqiqa")

#2-misol
import re

raqam = input("Telefon raqam kiriting: ")
faqat_raqam = re.sub(r"\D", "", raqam)

if faqat_raqam.startswith("998"):
    faqat_raqam = "+" + faqat_raqam
elif faqat_raqam.startswith("90") or faqat_raqam.startswith("91"):
    faqat_raqam = "+998" + faqat_raqam

formatlangan = f"{faqat_raqam[:4]} {faqat_raqam[4:6]} {faqat_raqam[6:9]} {faqat_raqam[9:11]} {faqat_raqam[11:]}"
print("Standart format:", formatlangan)

#3-misol
import re

email = input("Email kiriting: ")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("Email to‘g‘ri")
else:
    print("Email noto‘g‘ri")

#4-misol
kurslar = {
    "USD": 12500,
    "EUR": 13500,
    "UZS": 1
}

miqdor = float(input("Miqdor: "))
from_val = input("Qaysi valyutadan: ").upper()
to_val = input("Qaysi valyutaga: ").upper()

uzs = miqdor * kurslar[from_val]
natija = uzs / kurslar[to_val]

print("Natija:", natija, to_val)

#5-misol
balans = 0
tarix = []

def kiritish(summa):
    global balans
    balans += summa
    tarix.append(f"+{summa}")

def chiqarish(summa):
    global balans
    if summa <= balans:
        balans -= summa
        tarix.append(f"-{summa}")
    else:
        print("Balans yetarli emas")

def korish():
    print("Balans:", balans)
    print("Tarix:", tarix)

#5-misol
kutubxona = []

def qoshish(nom):
    kutubxona.append({"nom": nom, "band": False})

def qidirish(nom):
    for k in kutubxona:
        if k["nom"] == nom:
            print(k)

def ijaraga_berish(nom):
    for k in kutubxona:
        if k["nom"] == nom:
            k["band"] = True

def qaytarish(nom):
    for k in kutubxona:
        if k["nom"] == nom:
            k["band"] = False
