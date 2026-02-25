#!/usr/bin/env python3
"""
Program rekomendasi hidup sehat — ringkas dan praktis (bahasa Indonesia).
Fitur:
- Tips hidup sehat umum
- Rekomendasi pola makan harian dengan takaran
- Rekomendasi olahraga dan air/tidur
- Hitung kebutuhan kalori sederhana (BMR + faktor aktivitas)
"""
import sys


def print_header():
	print("\n=== Program Hidup Sehat — Rekomendasi Singkat ===\n")


def general_tips():
	tips = [
		"Makan beragam: sayur, buah, biji-bijian, protein tanpa lemak.",
		"Kurangi gula tambahan dan makanan olahan berlemak tinggi.",
		"Pilih metode memasak yang lebih sehat: kukus, panggang, rebus.",
		"Tidur 7-9 jam per malam untuk dewasa.",
		"Beraktivitas fisik minimal 150 menit moderat tiap minggu.",
		"Perhatikan porsi: gunakan piring lebih kecil supaya porsi terkontrol.",
	]
	print("Tips Umum:")
	for i, t in enumerate(tips, 1):
		print(f"{i}. {t}")


def meal_plan_examples():
	print("\nRekomendasi Pola Makan Harian (contoh, untuk 3 kali makan + 2 camilan):")
	print("- Sarapan:")
	print("  * 1 porsi karbohidrat (nasi 1/2 piring atau 2 roti gandum)")
	print("  * 1 porsi protein (telur 1-2 butir / tahu tempe 100g)")
	print("  * Sayur atau buah (1 porsi buah atau sayur 1 genggam)")
	print("- Makan siang:")
	print("  * 1 porsi karbohidrat (nasi 1/2 piring)")
	print("  * 1 porsi protein (ayam ikan 100-150g)")
	print("  * Sayur sebanyak 1 piring sayur berwarna")
	print("- Makan malam (lebih ringan):")
	print("  * Karbohidrat lebih kecil (1/3 piring)")
	print("  * Protein + sayur, hindari makan berat dekat waktu tidur")
	print("- Camilan (pilih sehat): yogurt rendah gula, buah, kacang 20-30g")


def exercise_and_recovery():
	print("\nRekomendasi Olahraga & Pemulihan:")
	print("- Latihan aerobik 150 menit/minggu (jalan cepat, bersepeda, berenang)")
	print("- Latihan kekuatan 2x seminggu (bobot tubuh atau beban ringan)")
	print("- Peregangan setiap hari, dan istirahat aktif bila duduk lama")
	print("- Tidur 7-9 jam; pertahankan rutinitas tidur yang konsisten")


def hydration_sleep():
	print("\nAir & Tidur:")
	print("- Target minum ~2-3 liter per hari (sesuaikan aktivitas dan cuaca)")
	print("- Minum secara bertahap, bukan sekaligus banyak")
	print("- Kurangi kafein sore/malam agar tidur lebih baik")


def calc_calories():
	try:
		sex = input("Jenis kelamin (l/p): ").strip().lower()
		age = int(input("Usia (tahun): ").strip())
		weight = float(input("Berat (kg): ").strip())
		height = float(input("Tinggi (cm): ").strip())
	except Exception:
		print("Input tidak valid — kembali ke menu.")
		return

	if sex not in ("l", "p"):
		print("Jenis kelamin harus 'l' (laki) atau 'p' (perempuan).")
		return

	# Mifflin-St Jeor
	if sex == "l":
		bmr = 10 * weight + 6.25 * height - 5 * age + 5
	else:
		bmr = 10 * weight + 6.25 * height - 5 * age - 161

	print("Pilih level aktivitas:")
	print("1. Tidak aktif (sedikit/tiada olahraga)")
	print("2. Ringan (1-3 hari/minggu)")
	print("3. Sedang (3-5 hari/minggu)")
	print("4. Aktif (6-7 hari/minggu)")
	print("5. Sangat aktif (kerja fisik berat/latihan ganda)")
	level = input("Pilihan (1-5): ").strip()
	factors = {"1":1.2, "2":1.375, "3":1.55, "4":1.725, "5":1.9}
	factor = factors.get(level, 1.2)
	need = int(bmr * factor)

	print(f"\nEstimasi kebutuhan kalori harian: {need} kcal (perkiraan)")
	print("Distribusi makro (contoh): 45-55% karbo, 15-25% protein, 25-35% lemak")
	print("Contoh pembagian porsi untuk 2000 kcal:")
	print("- Karbohidrat: 225-275 g | Protein: 75-125 g | Lemak: 55-78 g")


def menu():
	while True:
		print_header()
		print("Pilih opsi:")
		print("1. Tips umum hidup sehat")
		print("2. Pola makan dan takaran contoh")
		print("3. Olahraga & istirahat")
		print("4. Air & tidur")
		print("5. Hitung kebutuhan kalori (personal)")
		print("0. Keluar")
		choice = input("Masukkan pilihan: ").strip()
		if choice == "1":
			general_tips()
		elif choice == "2":
			meal_plan_examples()
		elif choice == "3":
			exercise_and_recovery()
		elif choice == "4":
			hydration_sleep()
		elif choice == "5":
			calc_calories()
		elif choice == "0":
			print("Terima kasih — semoga hidup sehat!")
			break
		else:
			print("Pilihan tidak dikenal, coba lagi.")


if __name__ == "__main__":
	try:
		menu()
	except KeyboardInterrupt:
		print("\nDibatalkan. Sampai jumpa.")

