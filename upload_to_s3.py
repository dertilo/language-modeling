from sagemaker.s3 import S3Uploader
from util.util_methods import exec_command
import os

if __name__ == '__main__':
    local_path = f"{os.environ['HOME']}/data"
    file_to_upload = f"{local_path}/wikitext-2-raw-v1.zip"
    if not os.path.isfile(file_to_upload):
        os.system(f"cd {local_path} && wget --trust-server-names https://s3.amazonaws.com/research.metamind.io/wikitext/{file_to_upload}")

    s3_prefix = "s3://tilos-ml-bucket/wikitext-2-raw-v1"
    S3Uploader.upload(file_to_upload, f"{s3_prefix}")