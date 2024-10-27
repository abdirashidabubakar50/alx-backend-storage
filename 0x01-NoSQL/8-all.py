#!/usr/bin/env python3
"""
This script defines a function that lists all documents in a collection
"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    This function returns lists of all documents in a collection

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents or an empty list if no documents exist
    """
    if mongo_collection is None:
        return []

    documents = list(mongo_collection.find())
    return documents
