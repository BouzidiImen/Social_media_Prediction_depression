import pathlib
import requests as requests
from urllib.request import urlretrieve
from tqdm import trange
import time
from socket import error as socket_error
import errno

DEFAULT_KEY_WORD = 'depression'
DEFAULT_PATH = "Unsplash/Depression/"

def get_unsplash_images(token, key_word=DEFAULT_KEY_WORD, path_to_folder=DEFAULT_PATH):
    """
    Using Unsplash API to save url of photos in a csv
    :param path_to_folder: Path there images will be saved
    :param browser: webdriver
    :param key_word: key word to be searched
    :param token

    """
    r = requests.get(f'https://api.unsplash.com/search/photos?query={key_word}&client_id={token}')
    infos = r.json()
    total_pages = infos['total_pages']
    total_images = infos['total']
    links = []
    num_per_page = 200
    for pg in range(1, total_pages + 1):
        new_r = requests.get(f'https://api.unsplash.com/search/photos?query={key_word}' +
                             f'&page={pg}&per_page={num_per_page}&client_id={token}')
        data = new_r.json()
        for img_data in data['results']:
            img_url = img_data['urls']['raw']
            links.append(img_url)
    if len(links) == total_images:
        print('Links for all images')
    else:
        print('Missing links')
    Clean_links = []
    for l in links:
        Clean_links.append(l.split('?')[0])
    pathlib.Path(path_to_folder).mkdir(parents=True, exist_ok=True)
    try:
        for i in trange(len(Clean_links)):
            name = 'Unsplash_' + key_word + '_' + str(i)
            time.sleep(5)
            urlretrieve(links[i], path_to_folder+ name + "." + 'jpeg')
    except socket_error as e:
        if e.errno != errno.ECONNRESET:
            raise
        pass
