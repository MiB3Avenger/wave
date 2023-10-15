from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class StaticS3Boto3Storage(S3Boto3Storage):
    """
    Static files storage
    """
    file_overwrite = True
    location = getattr(settings, 'S3_STATIC_LOCATION', "static")


class MediaS3Boto3Storage(S3Boto3Storage):
    """
    S3 storage for media files, we want to make sure that overwriting files is
    set to false in case someone uploads file with same name.
    """
    file_overwrite = False
    location = 'media'
