user_data = {
    "mahasiswa": "RaHaSia",
    "ferdilan": "parako",
    "adedira": "cakra",
}

# Memeriksa username 
def validasi_username(username):
    #mengubah username menjadi kecil
    return username.lower() in user_data

# Memeriksa password
def chek_password(username, password):
    return user_data.get(username.lower()) == password

#program utama
while True:
    username = input("Masukkan username: ")

    if validasi_username(username):
        password = input("Masukkan password: ")
        if chek_password(username, password):
            print("Login berhasil. Selamat datang, " + username + "!")
            break
        else:
            print("Password salah. Silakan coba lagi.")
    else:
        print("Username tidak ditemukan. Silakan coba lagi.")
