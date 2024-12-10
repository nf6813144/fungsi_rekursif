def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

def fibonacci(x):
    if x <= 1:
        return x
    else:
        return fibonacci(x - 1) + fibonacci(x - 2)

print("Pilih fungsi yang ingin dijalankan:")
print("1. Faktorial")
print("2. Fibonacci")

pilihan = int(input("Masukkan pilihan (1 atau 2): "))

if pilihan == 1:
    a = int(input("Masukkan nilai yang akan dicari faktorialnya: "))
    cari_faktorial = faktorial(a)
    print("Nilai dari", a, "! adalah", cari_faktorial)

elif pilihan == 2:
    x = int(input("Masukkan batas untuk deret Fibonacci: "))
    print("Deret Fibonacci hingga", x, ":")
    for i in range(x):
        print(fibonacci(i), end=" ")
    print()

else:
    print("Pilihan tidak valid. Silakan pilih 1 atau 2.")