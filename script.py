class Pelanggan:
    def __init__(self, nama, saldo=0):
        self.nama = nama
        self.saldo = saldo

    def isi_saldo(self, jumlah):
        self.saldo += jumlah
        print(f"Saldo Anda sekarang: {self.saldo}")

def main():
    print("jual beli pulsa Namuy!")

    #Nama Pembeli
    nama_pelanggan = input("Masukkan nama Anda: ")
    pelanggan = Pelanggan(nama_pelanggan)

    while True:
        print("\nMenu:")
        print("1. Isi Saldo")
        print("2. Keluar")

        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "1":
            jumlah_isi_saldo = int(input("Masukkan jumlah saldo: "))
            pelanggan.isi_saldo(jumlah_isi_saldo)
        elif pilihan == "2":
            print("Selesai.")
            break
        else:
            print("Tidak Valid")

if __name__ == "__main__":
    main()
