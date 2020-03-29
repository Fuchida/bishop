"""
Main entry point of the application consisting of default routes
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    """
        Home route will return basic information about the service
    """
    return {"service": "Bishop: API Metadata Service", "version":0.1}


@app.get("/collection/{collection_name}/key/{key_id}")
def get_key(collection_name: str, key_id: int):
    """
        Get information about an existing key
    """
    return {
        "created": "TBD",
        "last_update": "TBD",
        "resource": {"collection_name": collection_name, "key_id": key_id},
        "payload":{}
    }


@app.put("/collection/{collection_name}/key/{key_id}")
def put_key(collection_name: str, key_id: int):
    """
        Create a new or replace existing metadata for key

        Note:
            A collection is implicitly part of the key because
            it's used to prevent namespace collisions.
    """
    return {"status":f"Not Implemented for {collection_name} and {key_id}"}


@app.put("/collection/{collection_name}/key/{key_id}")
def delete_key(collection_name: str, key_id: int):
    """
        Create a new or replace existing metadata for key
    """
    return {"status":f"Not Implemented for {collection_name} and {key_id}"}
