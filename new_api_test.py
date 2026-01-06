import requests
import json

# 1. API'ye GET isteği gönderme (Test API'ıdır)
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# 2. Yanıtın (Status Code) başarılı olup olmadığını kontrol etme
if response.status_code == 200:
    print("API Sorgusu Başarılı! Durum Kodu:", response.status_code)
    
    # 3. JSON verisini Python Sözlüğüne (Dictionary) dönüştürme
    data = response.json()
    
    # 4. Sözlükten spesifik bir veri çekme ve yazdırma
    print("-" * 25)
    print(f"Kullanıcı ID: {data['userId']}")
    print(f"Başlık (Title): {data['title']}")
    print(f"Durum (Completed): {data['completed']}")
    print("-" * 25)

    # Örnek Kontrol
    if data['completed'] == False:
        print("Görev HENÜZ TAMAMLANMAMIŞ.")
        
else:
    print(f"Hata oluştu! Durum Kodu: {response.status_code}")

