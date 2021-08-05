from npz import create_npz
import numpy as np
create_npz(path='Data/Unsplash_Pexels_Data/Depression/')
create_npz(path='Data/Unsplash_Pexels_Data/Happiness/',label=np.array([0,1]))
