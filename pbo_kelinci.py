class Kelinci:

    jumlah_kelinci = 0

    def __init__(self,warna,berat,usia):
        self.warna = warna
        self.berat = berat
        self.usia = usia
        Kelinci.jumlah_kelinci += 1

    def tampilkan_jumlah(self):
        print("Total Kelinci :", Kelinci.jumlah_kelinci)

    def tampilkan_profil(self):
        print("Warna :", self.warna)
        print("Berat :", self.berat)
        print("Usia :", self.usia)

kelinci1 = Kelinci("Hitam", 1.2, 4)
kelinci2 = Kelinci("Putih", 1.5, 3)

kelinci1.tampilkan_profil()
kelinci2.tampilkan_profil()
kelinci1.tampilkan_jumlah()