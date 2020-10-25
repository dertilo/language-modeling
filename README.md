# language-modeling

### [huggingface-transformers]
* [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/dertilo/language-modeling/blob/master/language_modeling.ipynb)
* get data from [wikitext-long-term-dependency-language-modeling-dataset](https://blog.einstein.ai/the-wikitext-long-term-dependency-language-modeling-dataset/)

```shell script
wget --trust-server-names https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-2-raw-v1.zip
unzip wikitext-2-raw-v1.zip
export TRAIN_FILE=$HOME/data/wikitext-2-raw/wiki.train.raw
export TEST_FILE=$HOME/data/wikitext-2-raw/wiki.test.raw

export WANDB_PROJECT=language-modeling
```
* train
```shell script
python run_language_modeling.py \
    --output_dir=output \
    --run_name=debug \
    --logging_steps=3 \
    --model_type=gpt2 \
    --model_name_or_path=gpt2 \
    --do_train \
    --do_eval \
    --train_data_file=$TRAIN_FILE \
    --eval_data_file=$TEST_FILE 
```
* results: `perplexity = 19.756381741458434` after 30 min on Tesla G4, see [wandb](https://wandb.ai/dertilo/language-modeling/runs/11wv8bfb/overview) and [jupyter-notebook](language_modeling.ipynb)

* rsync to google colab
```shell script
rclone sync -P --exclude ".git/**" --exclude ".idea/**" --exclude "build/**" --exclude "*.pyc" --max-size 100k $HOME/code/NLP/language-modeling dertilo-googledrive:language-modeling
```
