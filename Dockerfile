# 1. Taban imaj: Senin listende zaten olan hafif Python'u kullanıyoruz
FROM python:3.9-slim

# 2. Çalışma dizini: Konteyner içindeki 'evimiz'
WORKDIR /app

# 3. Dosyaları kopyala: Mevcut klasördeki her şeyi konteynerin içine at
COPY . .

# 4. Bağımlılıkları kur: requirements.txt içindeki flask'ı yükle
RUN pip install --no-cache-dir -r requirements.txt

# 5. Çalıştırma komutu: Konteyner uyanınca ne yapacak?
CMD ["python", "app.py"]
