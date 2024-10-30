#!/usr/bin/env python3
"""
This script defines a class that interface with Redis database for caching data
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    class to interface with a redis database for caching data
    """
    def __init__(self) -> None:
        """
        initializes cache instance

        creates a redis client instance and flushes the database to remove
        all existing keys
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores a given data in Redis and returns unique key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
