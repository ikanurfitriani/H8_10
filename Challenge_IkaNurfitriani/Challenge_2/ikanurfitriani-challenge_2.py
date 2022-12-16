# Challenge 2 - Angka to Terbilang
### Nama: Ika Nurfitriani
### Kode Peserta: PYTN-KS10-008
### Program: Introduction to Python for Data Science

angka=["","Satu","Dua","Tiga","Empat","Lima","Enam","Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
hasil =""
n = int(input("Masukkan angka (0-99) : "))

if n >= 0 and n <= 11:
    hasil = hasil + angka[n]
elif n < 20:
    hasil = angka[n % 10] + " Belas "
elif n < 100:
    hasil = angka[n // 10] + " Puluh " + angka[n % 10]
else :
    print("[WARNING!] Salah masukkan angka")
    print("Angka yang dimasukkan bukan antara 0-99")
print(hasil)