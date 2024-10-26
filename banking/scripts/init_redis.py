import redis

r = redis.Redis(host='localhost', port=6379, db=0)
r.set('USD', 1.0)
r.set('EUR', 1.2)