# Python için hafif bir taban imaj kullanıyoruz
FROM python:3.9-slim

# Çalışma dizinini belirliyoruz
WORKDIR /app

# Varsa kütüphane listesini kopyalayıp yüklüyoruz
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || true

# Tüm kodları kopyalıyoruz
COPY . .

# Uygulamayı çalıştırıyoruz (Dosya adın app.py ise)
CMD ["python", "app.py"]