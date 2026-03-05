import os  # Sistemi okumak için ekledik
import time
import redis
from flask import Flask, render_template

app = Flask(__name__)
cache = redis.Redis(host='redis-server', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    # 🆔 Konteynerin rengini ve ismini ortam değişkeninden okuyoruz
    app_color = os.environ.get('APP_COLOR', 'blue') # Varsayılan mavi
    app_name = os.environ.get('APP_NAME', 'Bilinmeyen Konteyner')
    
    return render_template('index.html', count=count, color=app_color, version=app_name)

# 3. Uygulamayı dış bağlantılara açık şekilde çalıştırıyoruz
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
