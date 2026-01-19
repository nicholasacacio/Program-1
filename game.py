# Aplikasi game secret number

secret_number = 777
guess_number = int(input("Masukkan Tebak Angka:"))

while guess_number != secret_number:
    print("Tebakan salah, silakan coba lagi")
    print("Anda terjebak dalam perputaran abadi") # modify
    guess_number = int(input("Masukkan Tebak Angka:"))

print("Selamat.., tebakan Anda benar")
print("Kode ini saya buat di codespace")