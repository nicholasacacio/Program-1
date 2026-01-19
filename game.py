import random
import time

# ============================================
#     🎮 GAME TEBAK ANGKA SERU 🎮
# ============================================

def tampilkan_banner():
    print("\n" + "="*50)
    print("       🎯 SELAMAT DATANG DI GAME TEBAK ANGKA 🎯")
    print("="*50)
    print("📌 Angka rahasianya tersembunyi antara 1 - 100")
    print("📌 Anda hanya punya 10 kesempatan untuk menebak")
    print("📌 Semakin cepat menebak = Score semakin tinggi")
    print("="*50 + "\n")

def tampilkan_progress(tebakan_ke, max_tebakan):
    print(f"🔹 Tebakan ke: {tebakan_ke}/{max_tebakan} ", end="")
    print("█" * tebakan_ke + "░" * (max_tebakan - tebakan_ke))

def main():
    tampilkan_banner()
    
    secret_number = random.randint(1, 100)
    tebakan_ke = 0
    max_tebakan = 10
    waktu_mulai = time.time()
    history_tebakan = []
    
    while tebakan_ke < max_tebakan:
        try:
            guess_number = int(input("\n🎲 Masukkan tebakan Anda: "))
            
            # Validasi input
            if guess_number < 1 or guess_number > 100:
                print("❌ Angka harus di antara 1 - 100!")
                continue
            
            tebakan_ke += 1
            history_tebakan.append(guess_number)
            
            tampilkan_progress(tebakan_ke, max_tebakan)
            
            if guess_number == secret_number:
                waktu_akhir = time.time()
                waktu_tempuh = round(waktu_akhir - waktu_mulai, 2)
                score = max(0, 1000 - (tebakan_ke * 50) - int(waktu_tempuh * 10))
                
                print("\n" + "🎉" * 25)
                print("✨✨✨ SELAMAT! TEBAKAN ANDA BENAR! ✨✨✨")
                print("🎉" * 25)
                print(f"\n📊 STATISTIK PERMAINAN:")
                print(f"   ➤ Angka rahasia: {secret_number}")
                print(f"   ➤ Jumlah tebakan: {tebakan_ke} kali")
                print(f"   ➤ Waktu tempuh: {waktu_tempuh} detik")
                print(f"   ➤ Riwayat tebakan: {history_tebakan}")
                print(f"   ➤ SCORE AKHIR: 🏆 {score} poin! 🏆\n")
                break
            
            elif guess_number < secret_number:
                selisih = secret_number - guess_number
                if selisih > 20:
                    print(f"🔥 JAUH BANGET! Tebakan Anda terlalu KECIL! ({guess_number})")
                elif selisih > 10:
                    print(f"📈 Tebakan Anda terlalu kecil ({guess_number}), naik lagi!")
                else:
                    print(f"🔥 DEKAT! Tebakan Anda masih kurang ({guess_number})")
            
            else:  # guess_number > secret_number
                selisih = guess_number - secret_number
                if selisih > 20:
                    print(f"🔥 JAUH BANGET! Tebakan Anda terlalu BESAR! ({guess_number})")
                elif selisih > 10:
                    print(f"📉 Tebakan Anda terlalu besar ({guess_number}), turun lagi!")
                else:
                    print(f"🔥 DEKAT! Tebakan Anda masih lebih besar ({guess_number})")
            
            sisa = max_tebakan - tebakan_ke
            if sisa > 0:
                print(f"⏰ Sisa kesempatan: {sisa} {'kali' if sisa > 1 else 'kali'}")
        
        except ValueError:
            print("❌ Input tidak valid! Masukkan angka bulat antara 1 - 100!")
            continue
    
    if tebakan_ke == max_tebakan:
        print("\n" + "💔" * 25)
        print("☠️  GAME OVER! KESEMPATAN HABIS! ☠️")
        print("💔" * 25)
        print(f"\n😭 Maaf, Anda tidak berhasil menebak!")
        print(f"   ➤ Angka rahasia adalah: {secret_number}")
        print(f"   ➤ Tebakan Anda: {history_tebakan}\n")
    
    ulang = input("🎮 Ingin bermain lagi? (ya/tidak): ").lower()
    if ulang in ['ya', 'y', 'yes']:
        main()
    else:
        print("\n👋 Terima kasih telah bermain! Sampai jumpa lagi!\n")

if __name__ == "__main__":
    main()