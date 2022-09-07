
#Menghitung Luas Persegi Panjang
def luasPersegiPanjang():
    print("Menghitung Luas Persegi Panjang")

    panjang = input("Masukkan panjang : ")
    lebar   = input("masukkan Lebar : ")
    luas    = int(panjang)*int(lebar)

    print("Luas Persegi Panjang :", luas )

#Menghitung Luas Persegi
def luasPersegi():
    print("Menghitung Luas Persegi ")

    panjang = input("Masukkan panjang Sisi: ")
    luas    = int(panjang)*int(panjang)

    print("Luas Persegi  :", luas )

#Menghitung Luas Segitiga
def luasSegitiga():
    print("Menghitung Luas Segitiga")

    alas = input("Masukkan Alas : ")
    tinggi   = input("masukkan Tinggi : ")
    luas    = (float(alas)*float(tinggi))/2

    print("Luas Persegi Panjang :", luas )

#Menghitung Luas Lingkaran
def luasLingkaran():
    print("Menghitung Luas Lingkaran")

    rusuk = float(input("Masukkan panjang jari-jari : "))
    if rusuk%7 == 0:
        luas    = (rusuk*rusuk*22)/7
    elif rusuk%7 != 0:
        luas    = rusuk*rusuk*3.14
    
    print("Luas Persegi Panjang :", luas )

i = 1
while i == 1:
    print("1. Menghitung Luas Persegi Panjang")
    print("2. Menghitung Luas Persegi")
    print("3. Menghitung Luas Segitiga")
    print("4. Menghitung Luas Lingkaran")
    print("5. Keluar")
    pilihan = int(input("Silahkan pilih salah satu : "))
    if pilihan == 1:
        luasPersegiPanjang()
    elif pilihan == 2:
        luasPersegi()
    elif pilihan == 3:
        luasSegitiga()
    elif pilihan == 4:
        luasLingkaran()
    elif pilihan == 5:
        print("Terima kasih Telah Berhitung")
        break



