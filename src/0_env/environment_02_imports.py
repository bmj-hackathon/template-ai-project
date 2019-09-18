

#%%
import os
from pathlib import Path

#%% ===========================================================================
# Standard imports
# =============================================================================
import os
from pathlib import Path
import sys
import zipfile
import gc
import time
from pprint import pprint
from functools import reduce
from collections import defaultdict
import json
import yaml
import inspect

#%% ===========================================================================
# ML imports
# =============================================================================
import numpy as np
print('numpy {} as np'.format(np.__version__))
import pandas as pd
print('pandas {} as pd'.format(pd.__version__))
import sklearn as sk
print('sklearn {} as sk'.format(sk.__version__))

import matplotlib as mpl
print('matplotlib {} as mpl'.format(mpl.__version__))
import matplotlib.pyplot as plt
print('matplotlib.pyplot as plt'.format())
import seaborn as sns
print('seaboard {} as sns'.format(sns.__version__))





import sklearn.preprocessing
import sklearn.model_selection
import sklearn.metrics
import sklearn.linear_model
import sklearn.pipeline
import sklearn.model_selection
import sklearn.ensemble
import sklearn.feature_extraction
import sklearn.decomposition
import sklearn.compose
import sklearn.utils

# Evolutionary search
# import gamete.design_space
# import gamete.evolution_space

# Keras
from keras.models import Model
from keras.layers import GlobalAveragePooling2D, Input, Lambda, AveragePooling1D
import keras.backend as K

# import nltk
# from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
# from nltk.corpus import stopwords

from sklearn_pandas import DataFrameMapper

# Models
import lightgbm as lgb
print("lightgbm", lgb.__version__)
import xgboost as xgb
print("xgboost", xgb.__version__)
# from catboost import CatBoostClassifier
import catboost as catb
print("catboost", catb.__version__)

# Metric
from sklearn.metrics import cohen_kappa_score
def kappa(y_true, y_pred):
    return cohen_kappa_score(y_true, y_pred, weights='quadratic')


