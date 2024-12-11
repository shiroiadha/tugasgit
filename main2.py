import numpy as np

sampah_wilayah1 = np.array([1.2, 1.5, 1.3, 1.7, 1.6, 1.4, 1.1, 1.8, 1.5, 1.9,
                            1.3, 1.6, 1.7, 1.4, 1.2, 1.5, 1.3, 1.9, 1.8, 1.7,
                            1.5, 1.3, 1.2, 1.4, 1.6, 1.5, 1.9, 1.8, 1.6, 1.7])

sampah_wilayah2 = np.array([1.1, 1.3, 1.4, 1.6, 1.5, 1.7, 1.2, 1.6, 1.7, 1.8,
                            1.4, 1.5, 1.6, 1.3, 1.1, 1.4, 1.5, 1.8, 1.7, 1.6,
                            1.4, 1.2, 1.3, 1.5, 1.7, 1.6, 1.8, 1.5, 1.9, 1.8])

print("Soal 1")
total_sw1 = np.sum(sampah_wilayah1) # Total sampah wilayah 1
total_sw2 = np.sum(sampah_wilayah2) # Total sampah wilayah 2
print(f"Total sampah wilayah 1 = {total_sw1:.2f}\nTotal sampah wilayah 2 = {total_sw2:.2f}")

print("\nSoal 2")
for gacor in range(sampah_wilayah1.shape[0]): # Perulangan berdasarkan panjang array di dimensi 0
    if sampah_wilayah1[gacor] > sampah_wilayah2[gacor]: # Percabangan untuk menentukan wilayah mana yang bakalan banjir duluan (:
        print(f"Sampah di wilayah 1 lebih banyak dari sampah di wilayah 2 di hari ke-{gacor+1}")
    else:
        print(f"Sampah di wilayah 2 lebih banyak dari sampah di wilayah 1 di hari ke-{gacor+1}")

print("\nSoal 3")
for i in range(sampah_wilayah1.shape[0]):
    tpd = np.add(sampah_wilayah1[i], sampah_wilayah2[i]) # Total sampah yang dikumpulkan di kedua wilayah setiap harinya
    print(f"Total sampah di kedua wilayah di hari ke-{i+1} = {tpd:.2f}")