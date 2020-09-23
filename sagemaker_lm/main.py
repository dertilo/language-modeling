import sagemaker
import wandb
from sagemaker.pytorch import PyTorch

source_dir = "."
wandb.sagemaker_auth(path=source_dir)

sagemaker_session = sagemaker.Session()
s3_path = "s3://tilos-ml-bucket/wikitext-2-raw-v1"

role = "arn:aws:iam::706022464121:role/service-role/AmazonSageMaker-ExecutionRole-20200317T145654"

estimator = PyTorch(
    entry_point="run_espnet.py",
    source_dir=source_dir,
    role=role,
    framework_version="1.6.0",
    py_version="py3",
    instance_count=1,
    instance_type="local",  # 'ml.p2.xlarge',
    # instance_type="ml.c5.xlarge",#"ml.g4dn.xlarge",# 'ml.p2.xlarge',
    # use_spot_instances = True,
    # max_wait = 24 * 60 * 60, # seconds; see max_run
    hyperparameters={},
)

estimator.fit(s3_path)
