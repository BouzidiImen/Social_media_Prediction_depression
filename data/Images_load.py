import numpy as np
import os
from tqdm import trange
from utils import maybe_download_and_extract, getlink
from data import DataSet, DataSets

SOURCE_NEGATIVE_URL = "http://www.mediafire.com/file/17l0aqdbqhbvlfu/negative.npz/file"
SOURCE_POSITIVE_URL = "http://www.mediafire.com/file/v1s3tqqzriuuq61/positive.npz/file"
DATA_DEFAULT_PATH = '~/.datasets/Images_From_Unsplash_And_Pexels/'
DEFAULT_TEST_SIZE = .25
DEFAULT_SEED=2020


def _extract(Pdata, Ndata):
    '''
        Extract features and labels of images
        :param Pdata: data for depressed users' images
        :param Ndata: data for non depressed users' images
        :return: features and labels
    '''
    # Extract features and labels 
    features = list(Pdata[ Pdata.files[ 0 ] ][ 0 ])
    labels = list(Pdata[ Pdata.files[ 0 ] ][ 1 ])
    for i in trange(1,len(Pdata)):
        features.append(Pdata[ Pdata.files[ i ] ][ 0 ][ 0 ])
        labels.append(Pdata[ Pdata.files[ i ] ][ 1 ][ 0 ])
    for i in trange(len(Ndata)):
        features.append(Ndata[ Ndata.files[ i ] ][ 0 ][ 0 ])
        labels.append(Ndata[ Ndata.files[ i ] ][ 1 ][ 0 ])
    return features, labels


def load_data(data_path=DATA_DEFAULT_PATH, seed=DEFAULT_SEED, test_size=DEFAULT_TEST_SIZE):
    """
    Loads dataset.
    :param data_path: string
            the path of the directory that contains the dataset  
    """

    data_path = os.path.expanduser(data_path)

    # Download files
    maybe_download_and_extract(getlink(SOURCE_NEGATIVE_URL), data_path)
    maybe_download_and_extract(getlink(SOURCE_POSITIVE_URL), data_path)
    # read data
    P = np.load(data_path + 'positive.npz',allow_pickle=True)  # load data for depressed users
    N = np.load(data_path + 'negative.npz',allow_pickle=True)  # load data for not depressed users
    features, labels = _extract(P, N)

    data = DataSet(features, labels, seed=seed)
    train, test = data.split(split_size=test_size)
    train, validation = train.split(split_size=test_size)
    return DataSets(train, validation, test)
