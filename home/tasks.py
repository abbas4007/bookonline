from celery import shared_task
from . import bucket


def all_bucket_objects():
    return bucket.get_objects()


@shared_task
def delete_object_task(key):
    bucket.delete_object(key)
