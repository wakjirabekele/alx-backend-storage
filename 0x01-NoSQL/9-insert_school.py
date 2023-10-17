#!/usr/bin/env python3

"""
Function that inserts a new document in a collection based on kwargs.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    """
    if mongo_collection is None:
        return None
    return mongo_collection.insert_one(kwargs).inserted_id
