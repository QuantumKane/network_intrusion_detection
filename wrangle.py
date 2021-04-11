import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.preprocessing

from sklearn.model_selection import train_test_split 


def get_data():    
    '''
    Read in data from .csv file
    '''
    df = pd.read_csv("Train_data.csv")
    
    return df


def wrangle_nids(df):
    
     # Drop redundant or unnecessary columns
    train = train.drop(['num_compromised', 'dst_host_srv_serror_rate', 'dst_host_srv_rerror_rate', 'serror_rate', 'dst_host_serror_rate', 'srv_serror_rate', 'srv_rerror_rate', 'land', 'urgent', 'is_host_login', 'is_guest_login', 'root_shell', 'num_root', 'su_attempted', 'wrong_fragment', 'num_access_files', 'num_shells', 'num_file_creations', 'num_failed_logins', 'srv_diff_host_rate', 'num_outbound_cmds', 'hot', 'rerror_rate'],axis=1)
    
    return train


def split(df, target):
    '''
    this function takes in a dataframe and splits it into 3 samples, 
    a test, which is 20% of the entire dataframe, 
    a validate, which is 24% of the entire dataframe,
    and a train, which is 56% of the entire dataframe. 
    It then splits each of the 3 samples into a dataframe with independent variables
    and a series with the dependent, or target variable. 
    The function returns 3 dataframes and 3 series:
    X_train (df) & y_train (series), X_validate & y_validate, X_test & y_test. 
    '''
    # split df into test (20%) and train_validate (80%)
    train_validate, test = train_test_split(df, test_size=.2, random_state=123)

    # split train_validate off into train (70% of 80% = 56%) and validate (30% of 80% = 24%)
    train, validate = train_test_split(train_validate, test_size=.3, random_state=123)

    # split train into X (dataframe, drop target) & y (series, keep target only)
    X_train = train.drop(columns=[target])
    y_train = train[target]
    
    # split validate into X (dataframe, drop target) & y (series, keep target only)
    X_validate = validate.drop(columns=[target])
    y_validate = validate[target]
    
    # split test into X (dataframe, drop target) & y (series, keep target only)
    X_test = test.drop(columns=[target])
    y_test = test[target]
    
    return X_train, y_train, X_validate, y_validate, X_test, y_test