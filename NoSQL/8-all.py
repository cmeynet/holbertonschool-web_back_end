#!/usr/bin/env python3
""" Python function that lists all documents in a collection """


def list_all(mongo_collection):
    """
    Return a list of all documents in the collection.
    If the collection is empty (or None), return an empty list.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
