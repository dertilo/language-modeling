from sagemaker.s3 import S3Uploader
from util import data_io
from util.util_methods import exec_command
import os

if __name__ == '__main__':
    local_path = f"{os.environ['HOME']}/data"
    data_io.download_data("https://s3.amazonaws.com/research.metamind.io/wikitext","wikitext-2-raw-v1.zip",local_path,unzip_it=True,remove_zipped=True)
    folder_name = "wikitext-2-raw-v1"
    file_to_upload = f"/tmp/{folder_name}.tar.gz"
    exec_command(f"cd {local_path} && tar -czvf {file_to_upload} {folder_name}")
    s3_prefix = "s3://tilos-ml-bucket/wikitext-2-raw-v1"
    S3Uploader.upload(file_to_upload, f"{s3_prefix}")