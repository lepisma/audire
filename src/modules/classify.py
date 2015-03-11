"""
Classifier stuff for audio event detection
"""

import numpy as np
from features import mfcc
from sklearn import svm


def train(features, target):
    """Train a classifier on given dataset.

    Args:
        features (array): features.
        target (array): target values of classes.
    Returns:
        clf: Classifier
    """
    
    clf = svm.LinearSVC()
    clf.fit(features, target)

    return clf


def preprocess(data, sr):
    """Preprocess the data and find features
    """

    features = np.mean(mfcc(np.array(data), samplerate=sr), axis=0)

    return features
