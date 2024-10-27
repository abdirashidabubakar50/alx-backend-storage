#!/usr/bin/env python3

"""
This script defines a function that changes all topics of
a school document based on the name
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document by name

    Args:
        mongo_collection: pymongo collection object
        name (str): The school name to update)
        topics(list): Listt of topics to set for the school

    Returns:
        None
    """
    if mongo_collection is None:
        return

    updated_document = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
