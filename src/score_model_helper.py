from preprocessing import Preprocessing
import numpy as np
import pandas as pd


# This class contains some of the helper functions used in the Model class.

# Returns pandas dataframe, with some dropped columns that are irrelevant for now
def get_dataframe(data_loc):
    df = pd.read_csv(data_loc, sep='\t', encoding='ISO-8859-1')
    df = df.dropna(axis=1)  # Drop columns with 'missing' values
    df = df.drop(columns=['rater1_domain1', 'rater2_domain1'])
    df = df.drop(columns=['essay_id', 'essay_set'])
    return df


# Preprocesses each essays into a word list (where each element of the list is a word). This allows the essay to be
# sequentially processed word-by-word.
def get_clean_essays(essays):
    clean_essays = []
    for essay_v in essays:
        clean_essays.append(Preprocessing.essay_to_wordlist(essay_v, remove_stopwords=True))
    return clean_essays


# Grabs every sentence from each essay in 'essays' and jams them into one array
def get_sentences(essays):
    sentences = []
    for essay in essays:
        sentences += Preprocessing.essay_to_sentences(essay, remove_stopwords=True)
    return sentences


# Turns 'data_vecs' into a np array and then reshapes it into the proper shape for LSTM fitting
def array_and_reshape(data_vecs):
    data_vecs = np.array(data_vecs)
    data_vecs = np.reshape(data_vecs, (data_vecs.shape[0], 1, data_vecs.shape[1]))
    return data_vecs
