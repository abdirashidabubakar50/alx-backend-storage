#!/usr/bin/env python3

"""
This script defines a function that returns the list
of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have a specific topic.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The MongoDB
    collection object.
    topic (str): The topic to search for.

    Returns:
    list: A list of schools matching the topic.
    """
    if mongo_collection is None:
        return

    results = mongo_collection.find_many({"topic": topic})

    schools = list(results)

    return schools
