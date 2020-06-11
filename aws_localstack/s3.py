import boto3

BUCKET_NAME = 'xananana'

folder = 's3-xanana'


def get_matching_s3_objects(prefix, suffix=""):
    s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")

    kwargs = {'Bucket': f"{BUCKET_NAME}"}

    if isinstance(prefix, str):
        prefixes = (prefix,)
    else:
        prefixes = prefix

    for key_prefix in prefixes:
        kwargs["Prefix"] = key_prefix

        for page in paginator.paginate(**kwargs):
            try:
                contents = page["Contents"]
            except KeyError:
                break

            for obj in contents:
                key = obj["Key"]
                if suffix in key and key != f"{key_prefix}/":
                    yield obj


def get_matching_s3_keys(prefixes, suffixes):
    if not suffixes:
        suffixes = ''

    for obj in get_matching_s3_objects(prefixes, suffixes):
        yield obj["Key"]


prefixes = ['']
suffixes= 'a'
keys = get_matching_s3_keys(prefixes, suffixes)
s3_keys = [key for key in keys]