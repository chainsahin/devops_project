import os
import redis
from flask import Flask, jsonify
import socket

app = Flask(__name__)

# Değişkenleri dış dünyadan (Environment) alıyoruz
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')

cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)

def get_hit_count():
    return cache.incr('hits')

@app.route('/')
def get_info():
    count = get_hit_count()
    return jsonify({
        "mesaj": "Environment Variables Aktif!",
        "ziyaret_sayisi": count,
        "baglanilan_redis": REDIS_HOST,
        "hostname": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
