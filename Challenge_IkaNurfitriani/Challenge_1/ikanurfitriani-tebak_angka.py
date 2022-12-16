# Challenge 1 - Game sederhana dengan Python
### Nama: Ika Nurfitriani
### Kode Peserta: PYTN-KS10-008
### Program: Introduction to Python for Data Science

import random
print('='*48)
print("\t\tGAME TEBAK ANGKA")
print('='*48)
print()

angka = random.randint(0,9)
kesempatan = 3
percobaan = 0
skor = 100

print("Komputer telah memilih sebuah angka dari 0 - 9")
print("Tebaklah angka yang komputer pilih")
print("Input HARUS berupa ANGKA!!!")
print("Score Anda saat ini adalah 100")
print()

while percobaan < kesempatan:
    jawab = input("Masukkan tebakkan angka: ")
    if jawab.isnumeric():
        jawab = eval(jawab)
        if jawab > angka:
            skor -= 10
            print("Tebakkan Anda terlalu besar, score dikurangi 10")
            print(f'Score Anda saat ini adalah {skor}')
        elif jawab < angka:
            skor -= 10
            print("Tebakkan Anda terlalu kecil, score dikurangi 10")
            print(f'Score Anda saat ini adalah {skor}')
        else:
            print("ANDA MENANG")
            print(f'Jumlah percobaan menebak {percobaan+1}x!')
            print(f'Score Anda adalah {skor}')
            break
        print()
    else:
        skor -= 20
        print("[WARNING!] Tebakkan harus berupa ANGKA")
        print("Penalty!, Score Anda dikurangi 20")
        print(f'Score Anda saat ini adalah {skor}')
    print()
    
    if percobaan == 2:
        print("=== GAME OVER ===")
        print(f'Score Anda adalah {skor}')
        print()
        break

    percobaan += 1