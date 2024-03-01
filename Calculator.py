class Kalkulator:
    def plus(self, a,b):
        hasil = a+b
        print(f"Hasilnya Adalah {hasil}")
    def kurang(self, a,b):
        hasil = a-b
        print(f"Hasilnya Adalah {hasil}")
    def kali(self, a,b):
        hasil = a*b
        print(f"Hasilnya Adalah {hasil}")
    def bagi(self, a,b):
        if b ==0:
            print(f"Tidak ada hasil")
        else:
            hasil = a/b
            print(f"Hasilnya Adalah {hasil}")
        
def main():
    Kalk = Kalkulator()
    while True:
        print("================================================")
        print("-----SELAMAT DATANG DI APLIKASI KAlKULATOR------")
        print("================================================")
        print("Arvian Nur Hidayat")
        print("-------------------")
        print("Aplikasi Kalkulator")
        print("1. Kalkulator")
        print("2. Keluar")
        print("================================================")
        pil1 = int(input("Masukkan Pilihan (1,2): "))
        if pil1 ==1:
            a = float(input("Masukkan Angka Pertama: "))
            b = float(input("Masukkan Angka Kedua: "))
            print("================================================")
            print("Pilih Fitur")
            print("1. Penambahan")
            print("2. Pengurangan")
            print("3. Perkalian")
            print("4. Pembagian")
            print("================================================")
            operasi = str(input("Silahkan masukkan pilihan fitur di atas: "))
            if operasi =='1':
                Kalk.plus(a,b)
            elif operasi =='2':
                Kalk.kurang(a,b)
            elif operasi =='3':
                Kalk.kali(a,b)
            elif operasi =='4':
                Kalk.bagi(a,b)
            else:
                print("Pilihan Tidak Tersedia")
        elif pil1 ==2:
            print("Anda Telah Keluar")
            print("Terimakasih Sudah Memakai Aplikasi ini")
            break
        
        else:
            print("Pilihan Tidak Tersedia")
            
if __name__=="__main__":
    main()