#!/usr/bin/env python3
"""
Stats about Nginx logs stored in MongoDB
Database: logs
Collection: nginx

Display:
- "logs: X"  where X is the number of documents in this collection
- "Methods:"
-   methods in this order:
        method GET: <count>
        method POST: <count>
        method PUT: <count>
        method PATCH: <count>
        method DELETE: <count>
- "status check: <count>" for documents with method=GET and path=/status
"""
from pymongo import MongoClient

if __name__ == "__main__":
    # Create a MongoDB client
    client = MongoClient("mongodb://127.0.0.1:27017")
    # Select the 'logs' database then the 'nginx' collection
    col = client.logs.nginx

    print("{} logs".format(col.count_documents({})))
    print("Methods:")
    print("\tmethod GET: {}".format(col.count_documents({'method': 'GET'})))
    print("\tmethod POST: {}".format(col.count_documents({'method': 'POST'})))
    print("\tmethod PUT: {}".format(col.count_documents({'method': 'PUT'})))
    print("\tmethod PATCH: {}".format(col.count_documents({'method': 'PATCH'})))
    print("\tmethod DELETE: {}".format(col.count_documents({'method': 'DELETE'})))
    print("{} status check".format(col.count_documents({'method': 'GET', 'path': '/status'})))
