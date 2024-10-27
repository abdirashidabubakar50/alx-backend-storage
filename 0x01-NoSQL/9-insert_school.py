#!/usr/bin/env python3

"""
This script defines a function insert-school that inserts
a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in the collection based on kwargs.

    Args:
        mongo_collection: pymongo collection object
        **kwargs: Key-value pairs representing the document fields

    Returns:
        The _id of the inserted document
    """
    if mongo_collection is None:
        return []
    documents = mongo_collection.insert_one(kwargs)
    return documents.inserted_id
