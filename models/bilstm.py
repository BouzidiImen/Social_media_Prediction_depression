import numpy as np

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, Dropout, Bidirectional
from keras.utils.np_utils import to_categorical
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping, ModelCheckpoint
import os

DEFAULT_MAX_FEATURES = 2000
DEFAULT_MAX_LENGTH = 28
DEFAULT_EMBED = 128
DEFAULT_LSTM_UNITS = 400
DEFAULT_BATCH = 300
DEFAULT_EPOCHS = 200
DEFAULT_LR = .001
DEFAULT_PATIENCE=10


def _preprocess_data(train,validation, test, max_features=DEFAULT_MAX_FEATURES, max_len=DEFAULT_MAX_LENGTH):
    """
    Prepare data sequentially to feed it to the neural network
    :param train:
        train data
    :param test:
        test data
    :param max_features:
        maximum number that sentence may contain
    :param max_len:
        padding size
    :return:
        train and test, features and their labels
    """
    train_tokenizer = Tokenizer(num_words=max_features, split=' ')
    train_tokenizer.fit_on_texts(train.features)
    x_train = train_tokenizer.texts_to_sequences(train.features)
    x_train = pad_sequences(x_train, maxlen=max_len)

    test_tokenizer = Tokenizer(num_words=max_features, split=' ')
    test_tokenizer.fit_on_texts(test.features)
    x_test = test_tokenizer.texts_to_sequences(test.features)
    x_test = pad_sequences(x_test, maxlen=max_len)

    validation_tokenizer = Tokenizer(num_words=max_features, split=' ')
    validation_tokenizer.fit_on_texts(validation.features)
    x_validation = validation_tokenizer.texts_to_sequences(validation.features)
    x_validation = pad_sequences(x_validation, maxlen=max_len)

    y_train = to_categorical(train.labels)
    y_test = to_categorical(test.labels)
    y_validation = to_categorical(validation.labels)

    return x_train, y_train, x_test, y_test, x_validation, y_validation


def model(train, validation, test, embed_dim=DEFAULT_EMBED, lstm_units=DEFAULT_LSTM_UNITS, batch_size=DEFAULT_BATCH,
          lr=DEFAULT_LR,patience=DEFAULT_PATIENCE,epochs=DEFAULT_EPOCHS, max_features=DEFAULT_MAX_FEATURES, max_len=DEFAULT_MAX_LENGTH):
    """
    LSTM MODEL FOR BINARY CLASSIFICATION
    :param train:
        train data
    :param validation
        validation data
    :param test:
        test data
    :param embed_dim:
        embedding dimension
    :param lstm_units:
        number of units in an lstm cell
    :param batch_size:
        batch size
    :param epochs:
        number of epochs
    :param max_features:
        maximum number that sentence may contain
    :param max_len:
        padding size
    :return:
    """
    adam = Adam(lr=lr, beta_1=0.9, beta_2=0.999, epsilon=None, decay=0.0, amsgrad=False)

    file_path = "weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"

    check_point = ModelCheckpoint(file_path, monitor='val_loss', verbose=1, save_best_only=True,
                                  save_weights_only=True, mode='auto', period=1)
    early_stop = EarlyStopping(monitor='val_loss', patience=patience, verbose=1,
                               mode='auto', restore_best_weights=True)

    out_dim = len(np.unique(train.labels))
    x_train, y_train, x_test, y_test,  x_validation, y_validation = _preprocess_data(train, validation, test, max_features, max_len)
    loss = 'binary_crossentropy'
    if y_train.shape[1]>2:
        loss = 'categorical_crossentropy'

    model = Sequential()
    model.add(Embedding(max_features, embed_dim, input_length=x_train.shape[1]))
    model.add(Dropout(.2))
    model.add(Bidirectional(LSTM(lstm_units, dropout=.8, recurrent_dropout=.8))=
    model.add(Dropout(.8))
    model.add(Dense(out_dim, activation='softmax'))
    model.compile(loss=loss, optimizer=adam, metrics=['accuracy'])
    model.fit(x_train, y_train, batch_size,epochs, verbose=True,
              validation_data=(x_validation,y_validation),
              callbacks=[check_point,early_stop])
    loss, train_accuracy = model.evaluate(x_train, y_train, verbose=False)
    print("Training Accuracy: {:.4f}".format(train_accuracy))
    loss, test_accuracy = model.evaluate(x_test, y_test, verbose=False)
    print("Testing Accuracy:  {:.4f}".format(test_accuracy))
    return train_accuracy,test_accuracy
