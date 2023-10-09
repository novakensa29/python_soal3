def cek(x, y):
    number = str(x)
    jumlah_digit = len(number)
    if y < 1 or y > jumlah_digit:
        return "Posisi tidak valid"
    digit_pada_posisi = int(number[y - 1])
    
    return digit_pada_posisi, jumlah_digit


angka = int(input("Masukkan angka: "))
posisi = int(input("Masukkan posisi digit yang ingin Anda temukan: "))

hasil, jumlah = cek(angka, posisi)
print("Digit pada posisi ke-", posisi, "adalah:", hasil)
print("Jumlah digit dalam angka", angka, "adalah:", jumlah)


