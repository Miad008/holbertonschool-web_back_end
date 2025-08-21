#!/usr/bin/env python3
""" Module that updates the topics of a school document """


def update_topics(mongo_collection, name, topics):
    """Updates all topics of a school document based on the name"""
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
