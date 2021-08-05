import cv2
import numpy as np
import os
from tqdm import tqdm

DEFAULT_DATA_NAME = 'data.npz'
DEFAULT_SCALE = .1
DEFAULT_LABEL=np.array([1,0]) #for happiness changed to [0,1] 
DEFALUT_KEY='dep_'

def _resize_to_np(filepath, label, scale):
    src = cv2.imread(filepath, cv2.IMREAD_UNCHANGED)
    width = int(src.shape[1] * scale)
    height = int(src.shape[0] * scale)
    output = cv2.resize(src, (width, height))
    img = np.array([output, label])
    return img.reshape((2, 1))


def create_npz(path,key=DEFALUT_KEY, data_name=DEFAULT_DATA_NAME, scale=DEFAULT_SCALE,label=DEFAULT_LABEL):
    filepath = path + data_name
    if os.path.exists(filepath):
        print('Deleting existing data...')
        os.remove(filepath)
    pictures = os.listdir(path)
    all_imgs = []
    names=[]
    i = 0
    for pic in tqdm(pictures):
        all_imgs.append(_resize_to_np(path + pic, label, scale))
        names.append(key+str(i))
        i += 1
    print('all images were resized ')
    np.savez(filepath, **{name:value for name,value in zip(names,all_imgs)})
    print(f"Data saved into '{filepath}'")
