"""
    Provide an interface between external services
"""
import json
from exceptions import IllegalArgumentError

import bucketstore
from logzero import logger

from bucketstore import S3Bucket
from botocore.exceptions import EndpointConnectionError
import backoff
from settings import EnvironmentSettings

class MetaStore:
    """
        Provide a key value interface to store and retrieve metadata.
    """

    def __init__(self):
        self.env = EnvironmentSettings()
        self.store = self.__get_store_instance()

    @backoff.on_exception(backoff.expo, EndpointConnectionError,
                          max_time=15, jitter=backoff.full_jitter)
    def __get_store_instance(self) -> S3Bucket:
        """
            Connect to S3 and provide an instance of S3Bucket
        """
        return bucketstore.get(self.env.s3_bucket_name, create=True)

    @backoff.on_exception(backoff.expo, EndpointConnectionError,
                          max_time=15, jitter=backoff.full_jitter)
    def get(self, collection: str, key: str) -> dict:
        """
            Retrive data based on existing key.
        """
        if self.key_exists(collection, key):
            data = json.loads(self.store.get(f'{collection}/{key}'))
        else:
            data = {}

        return data

    @backoff.on_exception(backoff.expo, EndpointConnectionError,
                          max_time=15, jitter=backoff.full_jitter)
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

    @backoff.on_exception(backoff.expo, EndpointConnectionError,
                          max_time=15, jitter=backoff.full_jitter)
    def delete(self, collection: str, key: str) -> dict:
        """
            Provided a collection and key delete the key from the data store

            throws: IllegalArgumentError when key is not
        """
        # NOTE: What do we do when an attempt to delete a key is made ?
        #       right not it's idempotent and no harm is done
        if not all([collection, key]):
            raise IllegalArgumentError("Collection or key are both required.")

        if collection is None or key is None:
            raise IllegalArgumentError("Collection or key cannot be None.")

        # If we try to delete a key that does not exist, we should provide
        # appropriate messaging.
        if not self.key_exists(collection, key):
            logger.warning("key: %s not found", key)
            data = {}
        else:
            data = self.store.delete(f'{collection}/{key}')

        return data
