#!/usr/bin/env python3
""" Python function that changes all topics of a school document
based on the name """


def update_topics(mongo_collection, name, topics):
    """ Update the 'topics' field of all school documents
    matching the given name. """
    result = mongo_collection.update_many({"name": name},
                                          {"$set": {"topics": topics}})
    return result
