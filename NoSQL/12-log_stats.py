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
    collection = client.logs.nginx

    print(f"{collection.count_documents({})} logs")
    print(f"""Methods:
    \tmethod GET: {collection.count_documents({"method": "GET"})}
    \tmethod POST: {collection.count_documents({"method": "POST"})}
    \tmethod PUT: {collection.count_documents({"method": "PUT"})}
    \tmethod PATCH: {collection.count_documents({"method": "PATCH"})}
    \tmethod DELETE: {collection.count_documents({"method": "DELETE"})}""")
    print(f"""{collection.count_documents
               ({"method": "GET", "path": "/status"})} status check""")
