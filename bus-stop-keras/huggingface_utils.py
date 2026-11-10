"""
Hugging Face model configurations.
Using BERT for the BUS-stop SST-2 experiment.
"""

from transformers import TFBertModel, BertTokenizer, BertConfig

MODELS = [
    (TFBertModel, BertTokenizer, BertConfig)
]