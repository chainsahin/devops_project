# 1. Temel imaj olarak Python'ın hafif bir sürümünü kullanıyoruz
FROM python:3.9-slim

# 2. Konteyner içinde çalışacağımız klasörü oluşturuyoruz
WORKDIR /app

# 3. Kütüphane listesini kopyalayıp yüklüyoruz 📦
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Projedeki tüm dosyaları (app.py vb.) konteynere kopyalıyoruz
COPY . .

# 5. Uygulamanın 5000 portunda çalışacağını belirtiyoruz ⚓
EXPOSE 5000

# 6. Uygulamayı başlatan komut
CMD ["python", "app.py"]
