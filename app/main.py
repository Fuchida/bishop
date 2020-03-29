"""
Main entry postr of the application consisting of default routes
"""
from datetime import datetime

from fastapi import FastAPI
from service import MetaStore

app = FastAPI()

@app.get("/")
def root():
    """
        Home route will return basic information about the service
    """
    return {"service": "Bishop: API Metadata Service", "version":0.1}


@app.get("/collection/{collection_name}/key/{key}")
def get_key(collection_name: str, key: str):
    """
        Get information about an existing key
    """
    store = MetaStore()

    # TODO if metadata is not found, return status should be 404
    return store.get(collection_name, key)


@app.put("/collection/{collection_name}/key/{key}")
def put_key(collection_name: str, key: str):
    """
        Create a new or replace existing metadata for key

        Note:
            A collection is implicitly part of the key because
            it's used to prevent namespace collisions.
    """
    store = MetaStore()
    data = {'created': datetime.utcnow(),
            'created_by':'Bishop',
            'payload':{'collection':collection_name,
                       'key':key}
            }

    return store.put(collection_name, key, data=data)


@app.delete("/collection/{collection_name}/key/{key}")
def delete_key(collection_name: str, key: str):
    """
        Create a new or replace existing metadata for key
    """
    return {"status":f"Not Implemented for {collection_name} and {key}"}
