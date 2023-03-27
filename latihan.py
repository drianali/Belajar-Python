class BangunDatar :
    def segitiga() : # method/function
        n = 1
        while(n == 1):
            print("Menghitung Luas Segitiga")
            alas = float(input("Masukkan Alas\t: "))
            tinggi = float(input("Masukkan Tinggi\t: "))
            luas = (alas * tinggi)/2
            print("Luas Segitiga Adalah \t: ",luas, "cm")
            coba = input("Mau itung lagi ga ? [m/g]: ")
            if(coba == "g") :
                break
    def persegipanjang() : # method/function
        n = 1
        while(n == 1) :
            print("Menghitung Luas Persegi Panjang")
            panjang = float(input("Masukkan Panjang\t: "))
            lebar = float(input("Masukkan Lebar\t: "))
            luas = panjang * lebar
            print("Luas Persegi Panjang Adalah \t: ",luas, "cm")
            coba = input("Mau itung lagi ga ? [m/g]: ")
            if(coba == "g") :
                break
    def lingkaran() : # method/function
        n = 1
        while(n == 1) :
            print("Menghitung Luas Lingkaran")
            r = float(input("Masukkan Jari-Jari\t: "))
            luas = (22/7)*r*r
            print("Luas Lingkaran Adalah \t: ",luas, "cm")
            coba = input("Mau itung lagi ga ? [m/g]: ")
            if(coba == "g") :
                break
def menu_awal():
    while(True):
        print("="*60)
        print("Aplikai Hitung Bangun Datar")
        print("="*60)
        print("Pilihan Rumus Bangun Datar :")
        print("[1] Hitung Luas Segitiga")
        print("[2] Hitung Luas Persegi Panjang")
        print("[3] Hitung Luas Lingkaran")
        print("[4] Keluar Dari Aplikasi")
        print("="*35)
        pil = int(input("Masukkan Pilihan Anda\t: "))
        if(pil == 1):
            BangunDatar.segitiga()
        elif(pil == 2):
            BangunDatar.persegipanjang()
        elif(pil == 3):
            BangunDatar.lingkaran()
        elif(pil == 4):
            print("Trimakasih")
            exit()
        else :
            print("Masukkan Pilihan Yang Benar")
menu_awal()