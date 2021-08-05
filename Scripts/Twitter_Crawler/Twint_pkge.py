import twint
import pandas as pd
from tqdm import trange
import sys, os

DEFAULT_KEYWORD = "I suffer from depression"
DEFAULT_KEYWORDS = [ "I am diagnosed with depression", 'I am fighting depression', 'I suffer from depression' ]
DEFAULT_LIMIT = 3000
DEFAULT_USERNAME = 'Imen'
DEFAULT_LIMIT_PROFILE_STATUS = 100


def clean_data(key_words=DEFAULT_KEYWORDS):
    data = pd.DataFrame()
    for key in key_words:
        data = data.append(pd.read_csv(key + ".csv"))
    data = data.drop_duplicates(subset=['user_id'], keep='first')
    return data


def get_keywords_tweets(keyword=DEFAULT_KEYWORD, limit=DEFAULT_LIMIT):
    """
    This function returns a csv data set with tweets containing the keyword
    :param keyword is the key word to search for
    :param limit number of tweets to retrieve
    """
    c = twint.Config()
    c.Search = keyword
    c.Limit = limit
    c.Store_csv = True
    c.Output = keyword + ".csv"
    sys.stdout = open(os.devnull, 'w')
    twint.run.Search(c)


def get_profile_infos(user_name=DEFAULT_USERNAME):
    """
           This function returns a csv file with users pesonal information (bio/location/followers/following)
           :param  user_name Username of a twitter user
    """
    c = twint.Config()
    c.Username = user_name
    c.Store_csv = True
    c.Output = ("Profileinfos.csv")
    sys.stdout = open(os.devnull, 'w')
    twint.run.Lookup(c)


def get_timeline_by_username(user_name=DEFAULT_USERNAME, limit=DEFAULT_LIMIT_PROFILE_STATUS):
    """
           This function returns csv files each contain 100 recent post of a user
           :param  user_name user_name Username of a twitter user
    """
    c = twint.Config()
    c.Username = user_name
    c.Profile = True
    c.Retweets = True
    c.Limit = limit
    c.Store_csv = True
    c.Output = ('Timelines/' + user_name + ".csv")
    sys.stdout = open(os.devnull, 'w')
    twint.run.Search(c)
