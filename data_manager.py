import json
import os

import redis


def _get_redis_client() -> redis.Redis:
    url = os.getenv('REDIS_URL')
    if not url:
        print("Redis url not set")
        raise ValueError('REDIS_URL is missing')
    client = redis.Redis.from_url(url)
    return client

redis_client = _get_redis_client()

def pull_data() -> dict:
    key = os.getenv("METRICS_KEY", "reservations_metrics")
    value = redis_client.get(key)
    if not value:
        return {"message": f"No data found. Key: {key}"}
    data = json.loads(value)
    return data