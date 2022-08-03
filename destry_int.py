from random import*
tahmin = ""
parol = input("buziladigan parolni kirgizing>>")
sonlar = ["0","1","2","3","4","5","6","7","8","9"]
while(tahmin !=parol):
    tahmin = ""
    for harf in range(len(parol)):
        tahmin_harf=sonlar[randint(0,9)]
        tahmin=str(tahmin_harf) + str(tahmin)
        print(tahmin)
print("Parol buzildi") 
tugatish = input(f"Parol:<<{tahmin}>>   Dasturdan chiqish uchun istalgan tugmani bosing")   
'''
from random import *
tahmin = ""
parol = input("buziladigan parolni kirgizing>>")
harflar = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","v","z","y","0","1","2","3","4","5","6","7","8","9"]
while(tahmin !=parol):
    tahmin = ""
    for harf in range(len(parol)):
        tahmin_harf = harflar[randint(0,35)]
        tahmin=str(tahmin_harf) + str(tahmin)
        print(tahmin)
print("Parol Muvofiqiyatli buzildi")
Stugatish = input(f"Parol:<<{tahmin}>>")
'''