from redis import Redis
import time
import logging

logging.basicConfig(level=logging.INFO,format='%(asctime)s: %(message)s')

redis = Redis(host='', port=6379, decode_responses=True, ssl=True, username='default', password='')

if redis.ping():
    logging.info("Connected to Redis")


key = 'testing'
current = time.ctime(time.time())

# Set the key 'testing' with the current date and time as value.
# The Key will expire and removed from cache in 60 seconds.

redis.set(key, current, ex=60)

keyValue = redis.get(key)
keyTTL = redis.ttl(key)

logging.info("Key {} was set at {} and has {} seconds until expired".format(key, keyValue, keyTTL))

