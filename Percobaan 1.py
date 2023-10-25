nilai = int(input("Masukkan nilai mahasiswa (0-100): "))

if nilai >= 0 and nilai <= 100:
    #Jika nilai berada dalam rentang 0-100, maka melakukan pengecekan status kelulusan
    # if dimodifikasi dari statement and menjadi or
    if nilai >= 90 or nilai <= 100:
        status = "nilai A, EXCELLENT"
    elif nilai >=80 and nilai <= 89:
        status = "nilai B, pertahankan prestasi anda"
    elif nilai >=60 and nilai <= 79:
        status = "nilai C, pertahankan prestasi anda"
    elif nilai >=50 and nilai <= 59:
        status = "nilai D, pertahankan belajar anda"
    else:
        status = "Nilai E, Anda dinyatakan tidak lulus"

    print(f"Nilai mahasiswa: {nilai}")
    print(f"Status kelulusan: {status}")
#===========================================================================================#
#Modifikasi pertanyaan 2
elif nilai < 0:
        print("Nilai yang anda masukkan kurang dari 0")
elif nilai > 100:
        print("Nilai yang anda masukkan lebih dari 100")
#Selesai modifikasi pertanyaan 2
#===========================================================================================#
else:
    # jika nilai di luar rentang 0-100, menampilkan pesan kesalahan
    print("Nilai yang dimasukkan tidak valid, Nilai harus berada dalam rentang 0-100")