#!/usr/bin/env python3
"""
This script defines a class that interface with Redis database for caching data
"""
import redis
import uuid
from typing import Union, Optional, Callable


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

    def get(
        self, key: str, fn: Optional[Callable] = None
    ) -> Optional[Union[str, bytes, int, float]]:
        """
        Retrieves the data associated with the given key from Redis

        if the key does not exist, returns None. if a function is provided,
        it will be applied to the retrieved data before returning

        Args:
            key (str): The key for the data to retrieve
            fn (Optional[Callable]): An optional function to convert
            the retrieved data.

        Returns:
            Optional[Union[str, bytes, int float]]: The retreived data
            and possibly
            converted data, or None if not found
        """

        # Retrieve the data from Redis
        data = self._redis.get(key)
        if data is None:
            # Return None if the key does not exist
            return None
        # Apply the function if provided, else return None
        return fn(data) if fn else data

    def get_str(self, key: str):
        """
        call get with a conversion function for UTF-8 strings
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """
        call get with a conversion function for integers
        """
        return self.get(key, fn=int)
