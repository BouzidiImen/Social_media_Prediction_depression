import pandas as pd
import numpy as np
import json
import os
from tqdm import tqdm
import logging
from utils import maybe_download_and_extract
from data import DataSet, DataSets
from utils import maybe_download_and_extract, getlink

SOURCE_URL = "http://www.mediafire.com/file/33gw4n73pyoa2ea/data.zip/file"
DATA_DEFAULT_PATH = '~/.datasets/Cross-Domain_Depression_Detection_via Harvesting_Social_Media/'
DEFAULT_TEST_SIZE=.25
DEFAULT_SEED=2020

def _read_data(data_path):
    '''
    Read downloaded data
    :param data_path: path for the dataset json files
    :return: tweets and labels
    '''
    # Import data
    tweets=[]
    labels=[]
    labels_path = data_path+'data/'
    for cathegory in os.listdir(labels_path):
        data_files=labels_path+cathegory
        files = os.listdir(data_files)
        for file in tqdm(files):
            with open(data_files+'/'+file) as json_d:
                tmp = json.load(json_d)
            tweets.append(tmp['text'])
            if cathegory=='negative':
                labels.append(0)
            if cathegory=='positive':
                labels.append(0)
    x, y = np.array(tweets), np.array(labels)
    return x, y


def load_data(data_path=DATA_DEFAULT_PATH, test_size=DEFAULT_TEST_SIZE, seed=DEFAULT_SEED):
    """
    Loads dataset.

    Args:
        data_path: string
            the path of the directory that contains the dataset
        test_size: float
            Value between 0 and 1 that indicated the proportion to use for the test set. This is calculated from
              the train set.
        seed: integer
            initialization of  the random number generator
    Returns:
        DataSets object
            A named tuple of type Datasets containing the train and test sets all of them of type dataset.
    """

    data_path = os.path.expanduser(data_path)

    # Download files
    maybe_download_and_extract(getlink(SOURCE_URL), data_path)

    # read data to memory
    x, y = _read_data(data_path)

    data = DataSet(x, y, seed=seed)
    train, test = data.split(split_size=test_size)
    train, validation= train.split(split_size=test_size)
    return DataSets(train,validation,test)
