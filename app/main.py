"""
Main entry postr of the application consisting of default routes
"""

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

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
    data = store.get(collection_name, key)
    status_code = status.HTTP_200_OK if data else status.HTTP_404_NOT_FOUND

    return JSONResponse(status_code=status_code, content=data)


@app.put("/collection/{collection_name}/key/{key}")
def put_key(collection_name: str, key: str, payload: dict):
    """
        Create a new or replace existing metadata for key

        Note:
            A collection is implicitly part of the key because
            it's used to prevent namespace collisions.
    """
    store = MetaStore()
    return store.put(collection_name, key, data=payload)


@app.delete("/collection/{collection_name}/key/{key}")
def delete_key(collection_name: str, key: str):
    """
        Create a new or replace existing metadata for key
    """
    store = MetaStore()
    data = store.delete(collection_name, key)

    status_code = status.HTTP_200_OK if data else status.HTTP_404_NOT_FOUND
    return JSONResponse(status_code=status_code, content=data)
