# Fonksiyonun tanımı: 'sayi' adında bir girdi alacak.
def yarisini_hesapla(sayi):
    # Fonksiyonun tek görevi sayıyı 2'ye bölüp sonucu geri döndürmek.
    # Bash'teki 'echo' yerine, sonucu dışarı aktarmak için 'return' kullanılır.
    sonuc = sayi / 2
    return sonuc

# Ana Program
sayi_1 = 42
sayi_2 = 100

# Fonksiyonu çağırıyoruz ve geri dönen sonucu bir değişkende tutuyoruz
cevap_1 = yarisini_hesapla(sayi_1)
cevap_2 = yarisini_hesapla(sayi_2)

print(f"42'nin yarısı: {cevap_1}")
print(f"100'ün yarısı: {cevap_2}")