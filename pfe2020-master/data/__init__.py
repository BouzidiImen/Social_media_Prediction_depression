import logging
import collections
import numpy as np
from sklearn.model_selection import train_test_split

DataSets = collections.namedtuple('DataSets', ['train', 'validation', 'test'])
class DataSet(object):
    def __init__(self, features, labels, seed=None, name=None):
        if name is None:
            name = self.__class__.__name__
        self._logger = logging.getLogger(self.__class__.__name__)
        self._features = features
        self._labels = labels
        self._seed = seed
        self._name = name

        self._epoch_completed = 0
        self._index_in_epoch = 0


    @property
    def features(self):
        return self._features

    @property
    def labels(self):
        return self._labels

    @property
    def num_examples(self):
        return len(self._features)

    @property
    def input_dim(self):
        if len(self._features.shape) == 2:
            return self._features.shape[1]
        else:
            return self._features.shape[1:]

    @property
    def output_dim(self):
        return self.n_classes

    @property
    def n_classes(self):
        if len(self.labels.shape) == 1:
            _n_classes = len(np.unique(self.labels))
        else:
            _n_classes = self.labels.shape[1]
        return _n_classes

    def split(self, split_size):
        assert split_size > 0 and not split_size > 1
        features_train, features_test, labels_train, labels_test = train_test_split(self._features, self._labels,
                                                                                    test_size=split_size,
                                                                                    random_state=self._seed)

        train = DataSet(features_train, labels_train, seed=self._seed)
        test = DataSet(features_test, labels_test, seed=self._seed)
        return train, test

    def shuffle(self):
        idx = np.arange(0, self.num_examples)
        np.random.seed(self._seed)
        np.random.shuffle(idx)
        self._features = self.features[idx]
        self._labels = self.labels[idx]