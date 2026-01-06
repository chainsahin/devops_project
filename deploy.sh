#!/bin/bash

# Değişkenler (Yarın bir gün değiştirmek kolay olsun diye)
APP_NAME="cihan-app-v3"
IMAGE_NAME="yeni-devops-app:v3"

echo "--- Operasyon Başlıyor: $APP_NAME ---"

# 1. Eski çöpleri temizle (Eğer varsa)
docker stop $APP_NAME 2>/dev/null
docker rm $APP_NAME 2>/dev/null

# 2. Yeni imajı build et
echo "--- Build alınıyor... ---"
docker build -t $IMAGE_NAME .

# 3. Konteyneri çalıştır
echo "--- Konteyner ateşleniyor... ---"
docker run -d -p 8080:5000 --name $APP_NAME $IMAGE_NAME

echo "--- Durum Kontrolü: ---"
docker ps | grep $APP_NAME

echo "--- Test Ediliyor: ---"
sleep 2 # Uygulamanın uyanması için 2 saniye bekle
curl http://localhost:8080
