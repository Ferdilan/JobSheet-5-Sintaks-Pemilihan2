
def hitung_ongkir(total_harga):
    if total_harga < 100000:
        return 20000
    else:
        return 30000

def main():
    print("Selamat datang di Restoran MakanYUK!")
    
    nama_makanan = input("Masukkan nama makanan: ")
    harga_makanan = float(input("Masukkan harga makanan (dalam Rp): "))
    
    pengiriman_expres = input("Apakah Anda ingin pengiriman ekspres? (1 = Ya 0 = Tidak): ").lower()
    
    if pengiriman_expres == "1":
        ongkir = hitung_ongkir(harga_makanan) + 25000
    else:
        ongkir = hitung_ongkir(harga_makanan)
    
    total_harga = harga_makanan + ongkir
    
    print("\n--- Struk Pembayaran ---")
    print("Makanan: " + nama_makanan)
    print("Harga Makanan: Rp " + str(harga_makanan))
    print("Biaya Pengiriman: Rp " + str(ongkir))
    print("Total yang harus dibayar: Rp " + str(total_harga))
    
if __name__ == "__main__":
    main()
