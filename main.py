import warnings
warnings.filterwarnings('ignore')

# import os
# os.environ['TRANSFORMERS_CACHE'] = 'pretrain_model_files/'
#
#
# from transformers import AutoModel, AutoTokenizer
#
# tokenizer = AutoTokenizer.from_pretrained('bert-base-chinese')
# model = AutoModel.from_pretrained('bert-base-chinese')

from datasets import load_dataset
datasets = load_dataset("csv", data_files= {"train": 'train.csv',
                                            "validation": 'dev.csv'}, cache_dir='weibo_senti_100k')