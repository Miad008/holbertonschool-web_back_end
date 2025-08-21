#!/usr/bin/env python3
""" Module that returns schools with a specific topic """


def schools_by_topic(mongo_collection, topic):
    """Returns list of schools that have a specific topic"""
    return list(mongo_collection.find({ "topics": topic }))
