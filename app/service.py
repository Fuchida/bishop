"""
    Provide interface between external services
"""
import json

import bucketstore
from settings import EnvironmentSettings

class MetaStore:
    """
        Provide a key value interface to store and retrieve metadata.
    """

    def __init__(self):
        self.env = EnvironmentSettings()
        self.store = bucketstore.get(self.env.s3_bucket_name, create=True)

    def get(self, collection: str, key: str) -> dict:
        """
            Retrive data based on existing key.

            Raises:
                NoSuchKey when key does not exists
        """
        if self.key_exists(collection, key):
            data = json.loads(self.store.get(f'{collection}/{key}'))
        else:
            data = {}

        return data

    def put(self, collection: str, key: str, data: dict) -> dict:
        """
            Provided a key and value store data in the datastore
        """
        return self.store.set(f'{collection}/{key}', json.dumps(data, default=str))

    def key_exists(self, collection: str, key: str) -> bool:
        """
            Provided a key determine if it exists in the datastore.
        """
        return f'{collection}/{key}' in self.store