from selenium import webdriver
import time
from tqdm import trange
import urllib.request
from socket import error as socket_error
import errno
import pathlib


DEFAULT_key_word = "Depression"
DEFAULT_PATH_FOLDER = "Pexels/Happy/"
DEFAULT_WEB_DRIVER = webdriver.Firefox()
DEFAULT_TIME_SLEEP_SCROLL = 5


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.69 " \
              "Safari/537.36 "


def _choose(messy):
    clean = []
    for elt in messy:
        link = elt.get_attribute('src')
        if not (link.find('https://images.pexels.com/photos/')):
            clean.append(link.split("?")[0])
    return clean
def _scroll_down(browser, time_sleep):
    """A method for scrolling the page."""
    # Get scroll height.
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to the bottom.
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load the page, this depends on the speed of internet connection
        time.sleep(time_sleep)
        # Calculate new scroll height and compare with last scroll height.
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def get_pexels_images(key_word=DEFAULT_key_word, browser=DEFAULT_WEB_DRIVER, path_to_folder=DEFAULT_PATH_FOLDER, time_sleep_for_scroll = DEFAULT_TIME_SLEEP_SCROLL):
    """
    Crawl Pexel Website and download all images with a key word
    :param path_to_folder: Path there images will be saved
    :param browser: webdriver
    :param key_word: key word to be searched

    """
    pathlib.Path(path_to_folder).mkdir(parents=True, exist_ok=True)
    browser.get("https://www.pexels.com/search/" + key_word)
    _scroll_down(browser, time_sleep_for_scroll)
    browser.implicitly_wait(10)  # seconds
    columns = browser.find_elements_by_class_name('photos__column')
    all_imgs = []
    for column in columns:
        all_imgs.append(column.find_elements_by_tag_name("img"))
    imgs = []
    for col in all_imgs:
        for img in col:
            imgs.append(img)
    img_links = _choose(imgs)
    try:  # Because an exception occurred while running the code (three times)
        urllib_urlopener = AppURLopener()
        for i in trange(len(img_links)):
            extension = img_links[i].split('.')[-1]
            name = key_word + str(i)
            time.sleep(5)
            urllib_urlopener.retrieve(img_links[i], path_to_folder + name + "." + extension)
    except socket_error as e:
        if e.errno != errno.ECONNRESET:
            raise
        pass
    browser.close()
