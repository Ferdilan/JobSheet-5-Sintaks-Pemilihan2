menu = input("Pilih salah satu menu berikut 1.Luas 2.Volume (1/2) ")

#Menu luas persegi & segitiga
if menu == "1":
    pilih1 =  input("Pilih salah satu a.Persegi b.Segitiga (a/b) ")
    if pilih1 == "a":
        sisipersegi = float(input("Masukkan Sisi Persegi: "))
        luaspersegi = sisipersegi * sisipersegi
        print(f"Luas dari persegi adalah: {int(luaspersegi)}")
    else:
        alassegitiga = float(input("Masukkan Alas Segitiga: "))
        tinggisegitiga = float(input("Masukkan Tinggi Segitiga: "))
        luassegitiga = 0.5 * alassegitiga * tinggisegitiga
        print(f"Luas dari segitiga adalah: {int(luassegitiga)}")
#Menu Volume kubus & tabung
else:
    pilih2 =  input("Pilih salah satu a.Kubus b.Tabung (a/b) ")
    if pilih2 == "a":
        sisikubus = float(input("Masukkan Sisi Kubus: "))
        volumekubus =  6 * sisikubus * sisikubus
        print(f"Volume dari kubus adalah: {int(volumekubus)}")
    else:
        jarijari = float(input("Masukkan jari - jari tabung: "))
        tinggitabung = float(input("Masukkan Tinggi Tabung: "))
        volumetabung = 3.14 * jarijari * jarijari * tinggitabung
        print(f"Volume dari kubus adalah: {int(volumetabung)}")