# 1. Aşama: Derleme (Ağır araçlar burada)
FROM gcc:latest AS builder
WORKDIR /app
COPY . .
RUN gcc -o myapp main.c

# 2. Aşama: Çalıştırma (Sadece çalışan dosya burada)
FROM alpine:latest  
WORKDIR /root/
COPY --from=builder /app/myapp .
CMD ["./myapp"]