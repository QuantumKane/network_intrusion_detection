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
    df = df.drop(['num_compromised', 'dst_host_srv_serror_rate', 'dst_host_srv_rerror_rate', 'serror_rate', 'dst_host_serror_rate', 'srv_serror_rate', 'srv_rerror_rate', 'land', 'urgent', 'is_host_login', 'is_guest_login', 'root_shell', 'num_root', 'su_attempted', 'wrong_fragment', 'num_access_files', 'num_shells', 'num_file_creations', 'num_failed_logins', 'srv_diff_host_rate', 'num_outbound_cmds', 'hot', 'rerror_rate'],axis=1)
    
    return df


def split(df, target, seed):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.2, 
                                            random_state=seed, 
                                            stratify=df[target]
                                           )
    train, validate = train_test_split(train_validate, test_size=0.3, 
                                       random_state=seed,
                                       stratify=train_validate[target]
                                      )
    return train, validate, test


def chi2(df, var, target, alpha):
    '''
    This function takes in a df, variable, a target variable, and the alpha, and runs a chi squared test. Statistical analysis is printed in the output.
    '''
    observed = pd.crosstab(df[var], df[target])
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    print('Observed\n')
    print(observed.values)
    print('---\nExpected\n')
    print(expected)
    print('---\n')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p     = {p:.4f}\n')
    if p < alpha:
        print(f'Becasue the p-value: {round(p, 4)} is less than alpha: {alpha}, we can reject the null hypothesis')
    else:
        print('There is insufficient evidence to reject the null hypothesis')