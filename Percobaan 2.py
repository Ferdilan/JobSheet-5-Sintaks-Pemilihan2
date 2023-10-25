kategori = input("Apakah anda seorang pekerja atau pebisnis (Pekerja/Pebisnis): ")
penghasilan = float(input("Masukkan penghasilan Anda (Rp.) "))

#Modifikasi pertanyaan 3
if penghasilan <= 0:
    print("Penghasilan yang dimasukkan tidak valid.")
else:
#Akhir modifikasi
    if kategori.lower() == "pekerja":
        # Memeriksa besarnya pajak berdasarkan penghasilan
        if penghasilan <= 5000000:
            pajak = penghasilan * 0.05
        elif penghasilan <= 10000000:
            pajak = penghasilan * 0.1
        else:
            pajak = penghasilan * 0.2

        # Menghitung gaji bersih
        gaji_bersih = penghasilan - pajak

        # Menampilkan hasil 
        print(f"Kategori: Pekerja")
        print(f"Penghasilan anda: RP {int(penghasilan)}")
        print(f"Pajak yang harus dibayar: Rp {int(pajak)}")
        print(f"Gaji bersih yang diterima: Rp {int(gaji_bersih)}")

    elif kategori.lower() == "pebisnis":
        # Memeriksa besarnya pajak berdasarkan penghasilan bisnis
        if penghasilan <= 10000000:
            pajak = penghasilan * 0.1
        else:
            pajak = penghasilan * 0.2

        # Menghitung gaji bersih (penghasilan bisnis setelah dipotong pajak)
        gaji_bersih = penghasilan - pajak

        # Menampilkan hasil
        print(f"Kategori: Pebisnis")
        print(f"Penghasilan anda: RP {int(penghasilan)}")
        print(f"Pajak yang harus dibayar: Rp {int(pajak)}")
        print(f"Gaji bersih yang diterima: Rp {int(gaji_bersih)}")

    else:
        print("Kategori yang dimasukkan tidak valid. Harap masukkan 'pekerja' atau 'pebisnis'.")
