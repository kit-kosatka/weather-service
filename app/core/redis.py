import redis.asyncio as aioredis
from app.core.config import settings

client = aioredis.from_url(settings.REDIS_URL)