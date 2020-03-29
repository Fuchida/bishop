"""
Provide various settings, confuration options and constants
"""
from dataclasses import dataclass
from envparse import Env

@dataclass
class EnvironmentSettings:
    """
        Provide constants configured in environment variables
    """
    def __init__(self):
        env = Env(S3_BUCKET_NAME=str)
        self.s3_bucket_name = env('S3_BUCKET_NAME')
