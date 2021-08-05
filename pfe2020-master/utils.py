import os 
import sys
import urllib.request
from bs4 import BeautifulSoup as soup
import zipfile
import tarfile
import logging

def maybe_download(file_name, data_path, url):
    """
    Download file from url if not found.

    This function will check if the data_path directory exists otherwise it will create it. it will check if file_name
    exists in data_path directory otherwise it will download it from url.

    Args:
        file_name: string
            The name of file after download
        data_path: string
            The folder where where data should be downloaded
        url: string
            The url of the file to download

    Returns:
        string
            the name of the downloaded file

    """
    logger = logging.getLogger(__name__ + '.maybe_download')

    file_path = data_path + file_name
    logger.debug(('Checking {} into {}'.format(file_name, data_path)))

    # Check data dir exists
    if not os.path.exists(data_path):
        logger.debug('Folder {} not found, creating it'.format(data_path))
        os.makedirs(data_path)

    # Check data file exists
    if os.path.exists(file_path):
        logger.debug('File {} found'.format(file_path))
        return file_path

    # Otherwise download it
    logger.info('Downloading file {} from {}'.format(file_path, url))
    temp_file_name, _ = urllib.request.urlretrieve(url, file_path)
    logger.info('Successfully downloaded file {}, {} bites'.format(temp_file_name, os.stat(temp_file_name).st_size))

    return file_path


def _print_download_progress(count, block_size, total_size):
    """
    Function used for printing the download progress.
    Used as a call-back function in maybe_download_and_extract().
    """

    # Percentage completion.
    pct_complete = float(count * block_size) / total_size

    # Limit it because rounding errors may cause it to exceed 100%.
    pct_complete = min(1.0, pct_complete)

    # Status-message. Note the \r which means the line should overwrite itself.
    msg = "\r- Download progress: {0:.1%}".format(pct_complete)

    # Print it.
    sys.stdout.write(msg)


    sys.stdout.flush()


def maybe_download_and_extract(url, download_dir):
    """
    Download and extract the data if it doesn't already exist.
    Assumes the url is a tar-ball file.
    :param url:
        Internet URL for the tar-file to download.
        Example: "https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"
    :param download_dir:
        Directory where the downloaded file is saved.
        Example: "data/CIFAR-10/"
    :return:
        Nothing.
    """

    # Filename for saving the file downloaded from the internet.
    # Use the filename from the URL and add it to the download_dir.
    filename = url.split('/')[-1]
    filename = filename.split('?')[0]
    file_path = os.path.join(download_dir, filename)

    # Check if the file already exists.
    # If it exists then we assume it has also been extracted,
    # otherwise we need to download and extract it now.
    if not os.path.exists(file_path):
        # Check if the download directory exists, otherwise create it.
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # Download the file from the internet.
        file_path, _ = urllib.request.urlretrieve(url=url,
                                                  filename=file_path,
                                                  reporthook=_print_download_progress)

        print()
        print("Download finished. Extracting files.")

        if file_path.endswith(".zip"):
            # Unpack the zip-file.
            zipfile.ZipFile(file=file_path, mode="r").extractall(download_dir)
        elif file_path.endswith((".tar.gz", ".tgz")):
            # Unpack the tar-ball.
            tarfile.open(name=file_path, mode="r:gz").extractall(download_dir)

        print("Done.")
    else:
        print("Data has apparently already been downloaded and unpacked.")

def getlink(link):
    driver = urllib.request.urlopen(link)
    content = driver.read()
    driver.close()
    page = soup(content, "html.parser")       
    download = page.find("div",{"class":"download_link"}) 
    return download.find("a",{"class":"input"})['href']