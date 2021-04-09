import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.preprocessing

from sklearn.model_selection import train_test_split 

def get_train_df():
    
    train = pd.read_csv("Train_data.csv")
    
    return train

def get_test_df():
    
    test = pd.read_csv("Test_data.csv")
    
    return test


def wrangle_nids(train):
    
     # Drop redundant or unnecessary columns
    df = df.drop(['num_compromised', 'dst_host_srv_serror_rate', 'dst_host_srv_rerror_rate', 'serror_rate', 'dst_host_serror_rate', 'srv_serror_rate', 'srv_rerror_rate', 'land', 'urgent', 'is_host_login', 'is_guest_login', 'root_shell', 'num_root', 'su_attempted', 'wrong_fragment', 'num_access_files', 'num_shells', 'num_file_creations', 'num_failed_logins', 'srv_diff_host_rate'],axis=1)
    
    return train