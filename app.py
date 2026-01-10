import time
import redis
from flask import Flask

# 1. Önce Flask uygulamasını tanımlıyoruz
app = Flask(__name__)

# 2. Redis bağlantısını kuruyoruz (host='redis' olmasına dikkat!)
cache = redis.Redis(host='redis', port=6379)

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
    return f'Selam! Bu sayfa {count} kez görüntülendi.\n'

# 3. EN SONDA uygulamayı çalıştırıyoruz
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
