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


def recommend_exercise_by_bmi():
	"""Rekomendasi olahraga berdasarkan BMI (menggunakan berat dan tinggi).
	Jika tinggi tidak diberikan, gunakan rentang berat sebagai fallback.
	"""
	try:
		weight = float(input("Berat (kg): ").strip())
	except Exception:
		print("Berat tidak valid.")
		return

	height_input = input("Tinggi (cm) [opsional, tekan Enter jika tidak tahu]: ").strip()
	bmi = None
	if height_input:
		try:
			height_cm = float(height_input)
			if height_cm <= 0:
				raise ValueError()
			height_m = height_cm / 100.0
			bmi = weight / (height_m * height_m)
			print(f"BMI Anda: {bmi:.1f}")
		except Exception:
			print("Tinggi tidak valid, menggunakan rekomendasi berdasarkan berat saja.")
			bmi = None

	print("\nRekomendasi olahraga:")
	if bmi is not None:
		if bmi < 18.5:
			print("- Kategori: Kurang berat (underweight). Fokus pada latihan kekuatan ringan dan peningkatan massa otot.")
			print("  Contoh: latihan beban tubuh 2-3x/minggu, 2-3 set x 8-12 repetisi; jalan santai 3x/minggu 20-30 menit.")
		elif bmi < 25:
			print("- Kategori: Normal. Kombinasikan kardio dan kekuatan untuk pemeliharaan kebugaran.")
			print("  Contoh: jalan cepat/bersepeda 30-45 menit, 3-5x/minggu; latihan kekuatan 2x/minggu.")
		elif bmi < 30:
			print("- Kategori: Kelebihan berat (overweight). Prioritaskan aktivitas kardiovaskular berdampak rendah dan latihan kekuatan.")
			print("  Contoh: jalan cepat 30-45 menit 5x/minggu, berenang/sepeda; latihan kekuatan 2x/minggu untuk menjaga massa otot.")
		else:
			print("- Kategori: Obesitas. Mulai dengan aktivitas berdampak rendah, tingkatkan durasi secara bertahap.")
			print("  Contoh: jalan ringan 20-30 menit 4-6x/minggu, berenang atau aerobik air; konsultasi medis jika ada kondisi penyerta.")
	else:
		# fallback berdasarkan berat saja
		if weight < 50:
			print("- Berat <50kg: latihan campuran (kekuatan + kardio ringan). Perhatikan asupan kalori jika ingin menambah berat.)")
		elif weight < 70:
			print("- Berat 50-70kg: latihan campuran, 150 menit kardio moderat/minggu + 2 sesi kekuatan.")
		elif weight < 90:
			print("- Berat 70-90kg: fokus pada kardio berdampak rendah (jalan, sepeda) dan latihan kekuatan moderat.")
		else:
			print("- Berat >=90kg: mulai dengan kardio berdampak rendah, jaga intensitas rendah sampai adaptasi; konsultasi medis disarankan jika ada keluhan.")

	print("Catatan: Mulai perlahan jika belum aktif, naikkan intensitas bertahap, dan konsultasi tenaga kesehatan jika perlu.")


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
		print("6. Rekomendasi olahraga sesuai berat/BMI")
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
		elif choice == "6":
			recommend_exercise_by_bmi()
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

