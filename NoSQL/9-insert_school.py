#!/usr/bin/env python3
""" Python function that inserts a new document
in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document into the given collection using fields from **kwargs.
    Returns the inserted document's _id.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
