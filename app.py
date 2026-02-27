import time
import redis
from flask import Flask

# 1. Flask uygulamasını tanımlıyoruz
app = Flask(__name__)

# 2. Redis bağlantısını kuruyoruz (host='redis' docker-compose'daki servis adıdır)
# 'redis' yerine 'redis-server' yazıyoruz
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
    return f'<h1>Selam! Bu sayfa {count} kez görüntülendi.</h1>\n'

# 3. Uygulamayı dış bağlantılara açık şekilde çalıştırıyoruz
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
