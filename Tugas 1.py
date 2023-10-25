
sisi1 = float(input("Masukkan panjang sisi pertama: "))
sisi2 = float(input("Masukkan panjang sisi kedua: "))
sisi3 = float(input("Masukkan panjang sisi ketiga: "))

if sisi1 ==  sisi2 == sisi3:
    print("Segitiga Ini Adalah Segitiga Sama Sisi")
elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
    print("Segitiga Ini Adalah Segitiga Sama Kaki")
else:
    print("Segitiga Ini Adalah Segitiga Sembarang")

