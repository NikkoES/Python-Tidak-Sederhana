def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Pilih Operasi : ")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

pilihan = input("Masukkan pilihan : ")

a = int(input("Masukkan bilangan satu : "))
b = int(input("Masukkan bilangan kedua : "))

if pilihan == '1':
    print(a, " + ", b, " = ", add(a, b))
elif pilihan == '2':
    print(a, " + ", b, " = ", subtract(a, b))
elif pilihan == '3':
    print(a, " + ", b, " = ", multiply(a, b))
elif pilihan == '4':
    print(a, " + ", b, " = ", divide(a, b))
else:
    print("Masukkan salah !")
