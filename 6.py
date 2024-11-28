data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

#No 1
no1 = data_panen
print(f"1. {no1}")

#No 2
no2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"2. Jumlah jagung lokasi 2: {no2}")

#No3
no3 = data_panen['lokasi3']['nama_lokasi']
print(f"3. Nama lokasi 3: {no3}")

#No 4 & No 5
hasil_padi = {}
hasil_kedelai = {}
hasil_jagung = {}
for i,j in data_panen.items():
    hasil_padi[i] = j['hasil_panen']['padi']
    hasil_kedelai[i] = j['hasil_panen']['kedelai']
    hasil_jagung[i] = j['hasil_panen']['jagung']
print(f"4. Hasil panen padi: {hasil_padi}")
print(f"   Hasil panen kedelai: {hasil_kedelai}")

#No 6
for j in hasil_padi.keys() and hasil_jagung.keys():
    if hasil_padi[j] > 1300 or hasil_jagung[j] > 800:
        print("memerlukan perhatian khusus")
    else:
        print("lokasi tersebut dalam kondisi baik")
        
#No 7_
