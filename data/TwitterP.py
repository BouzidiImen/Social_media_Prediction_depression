import pandas as pd
import numpy as np
import json
import os
from tqdm import tqdm
from utils import maybe_download_and_extract, getlink

SOURCE_URL = "http://www.mediafire.com/file/xp2jp8ezm3ynpc1/Twitter_Data%25282%2529.zip/file"
DATA_DEFAULT_PATH = '~/.datasets/Crawled-Twitter-Data/'
DEFAULT_TEST_SIZE = .25
DEFAULT_SEED = 2020


def load_data(data_path=DATA_DEFAULT_PATH, link=SOURCE_URL, test_size=DEFAULT_TEST_SIZE):
    """
    load data from website and return train, test and validation data
    :param data_path where data will be saved
    :param link to data
    :param test_size

    """
    data_path = os.path.expanduser(data_path)
    # Download files
    maybe_download_and_extract(getlink(link), data_path)
    # read data
    Twitter_data = pd.read_csv(data_path + "Twitter_data/Profiles.csv")
    L = len(Twitter_data)
    train, val, test = np.split(Twitter_data, [ int(L * (1 - test_size) * (1 - test_size)), int(L * (1 - test_size)) ])
    return train, val, test


def get_username_profile(username, data_path=DATA_DEFAULT_PATH):
    """
    load user's profile for a given username
    :param data_path where data is saved
    :param username 

    """
    timelines = os.listdir(data_path + 'Twitter_data/Timelines')
    clean_usernames = [s.strip('.csv') for s in timelines]
    for i in range(len(clean_usernames)):
        if clean_usernames[i] == username:
            return (pd.read_csv(data_path + 'Twitter_data/Timelines/' + username + '.csv'))
    return (print("user's timeline not found"))
