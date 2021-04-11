import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.preprocessing

from sklearn.model_selection import train_test_split 



def get_data():    
    '''
    Read in data from .csv files
    '''
    train = pd.read_csv("Train_data.csv")
    test = pd.read_csv("Test_data.csv")
    
    return train, test


def wrangle_nids(df):
    
     # Drop redundant or unnecessary columns
    train = train.drop(['num_compromised', 'dst_host_srv_serror_rate', 'dst_host_srv_rerror_rate', 'serror_rate', 'dst_host_serror_rate', 'srv_serror_rate', 'srv_rerror_rate', 'land', 'urgent', 'is_host_login', 'is_guest_login', 'root_shell', 'num_root', 'su_attempted', 'wrong_fragment', 'num_access_files', 'num_shells', 'num_file_creations', 'num_failed_logins', 'srv_diff_host_rate', 'num_outbound_cmds', 'hot', 'rerror_rate'],axis=1)
    
    return train


