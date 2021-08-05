import pandas as pd
from requests import get
from tqdm import trange
import time
from socket import error as socket_error
import errno
import pathlib
from random import randint
from urllib.request import urlcleanup

DEFAULT_FILE_NAME = 'Suicide'
DEFAULT_FOLDER_PATH = 'Unsplash/Depression/'
DEFAULT_NAME = 'Unsplash_'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'}


def _save_image(website_name,Name, Extension, Link, path_to_folder):
    try:
        name = website_name + Name
        pic = get(Link, headers=headers)
        with open(path_to_folder + name + "." + Extension, 'wb') as photo:
            photo.write(pic.content)
    except socket_error as e:
        if e.errno != errno.ECONNRESET:
            raise
    urlcleanup()


def save_images(website_name=DEFAULT_NAME,file_name=DEFAULT_FILE_NAME, folder_path=DEFAULT_FOLDER_PATH):
    missed = []
    data = pd.read_csv(file_name + ".csv")
    pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)
    for i in trange(len(data)):
        wait = randint(5, 15)
        time.sleep(wait)
        print(f'\nWaiting {wait}s...')
        try:
            _save_image(website_name,data['Name'].iloc[i], data['Extension'].iloc[i], data['Links'].iloc[i], folder_path)
        except:
            missed.append(data['Links'].iloc[i])
    missed_data = pd.DataFrame({'Missed_Links': missed}, index=None)
    missed_data.to_csv('MissedData.csv')
