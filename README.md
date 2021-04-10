
# **Individual Project - Network Intrusion Detection**

### Goals
The goal of this project is to be able to predict anomalous behavior on a network. 

### The Data
For this dataset TCP/IP dump data was acquired by simulating a typical US Air Force LAN. For each TCP/IP connection, 41 quantitative and qualitative features are obtained from normal and attack data (3 qualitative and 38 quantitative features).
The class variable has two categories: Normal and Anomalous

>Deliverables will include:
> - This repo containing: 
>   - A Jupyter Notebook detailing the process to create this model
>   - Wrangle file that holds functions to acquire and prep the data
>   - This Readme.md detailing project planning and exection, as well as instructions for project recreation
>   - Final model created to predict anomalous behavior
> - Trello Board outlining project steps

****
# **Project Steps**
## Acquire & Prepare
### acquire.py
- Data is acquired from .csv files on [Kaggle] (https://www.kaggle.com/nidhirastogi/network-intrusion-detection-using-python). Functions are stored in the acquire file, which allows quick access to the data. Once the acquire file is imported, it can be used each time to access the data
- NOTE: This dataset came from Kaggle pre-split in two .csvs files: train and test

### prepare.py
- Dropped irrelevant and redundant columns

## Explore
- Finding which features have the highest correlation to anomalous behavior
- Visualizing variable correlation with plots



