from random import *
tahmin = ""
parol = input("buziladigan parolni kirgizing>>")
harflar = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","W","X","V","Z","Y","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","w","x","v","z","y"]
while(tahmin !=parol):
    tahmin = ""
    for harf in range(len(parol)):
        tahmin_harf = harflar[randint(0,35  )]
        tahmin=str(tahmin_harf) + str(tahmin)
        print(tahmin)
print("Parol Muvofiqiyatli buzildi")
Tugatish = input(f"Parol:<<{tahmin}>>")























