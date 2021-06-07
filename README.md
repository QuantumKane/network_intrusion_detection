
# **Individual Project - Network Intrusion Detection**

### Goals
The goal of this project is to be able to predict normal behavior on a network in order to isolate anomalous occurances. 

### The Data
For this dataset TCP/IP dump data was acquired by simulating a typical US Air Force LAN. For each TCP/IP connection, 41 quantitative and qualitative features are obtained from normal and attack data (3 qualitative and 38 quantitative features).
The class variable has two categories: Normal and Anomalous

### Resume Write-up
Using Network Intrusion data from Kaggle, I decided to find insight on anomalous activity. I went about this by predicting normal transmissions, thereby isolating suspicious activity. I used several Classification models for prediction, all with a high degree of accuracy.


>Deliverables will include:
> - This repo containing: 
>   - A Jupyter Notebook detailing the process to create this model
>   - Wrangle file that holds functions to acquire and prep the data
>   - This Readme.md detailing project planning and exection, as well as instructions for project recreation
>   - Final model created to predict normal behavior
> - [Trello Board](https://trello.com/b/G4Bv6Tsi/nid-indidual-project) outlining project steps

### Data Dictionary

As there was no data dictionary provided, my best guesses are the following:

| Feature                       | Definition                            | Data Type                          |
|-------------------------------|---------------------------------------|------------------------------------|
|dst_bytes                      |destination bytes                      |int                                 |
|logged_in                      |user is logged in                      |int - boolean                       |
|src_bytes                      |source bytes                           |int                                 |
|protocol_type                  |what protocol was used                 |object                              |
|flag                           |how the transmission was flagged       |object                              |
|duration                       |connection duration                    |int                                 |
|count                          |                                       |int                                 |
|srv_count                      |                                       |int                                 |
|same_srv_rate                  |                                       |float                               |
|diff_srv_rate                  |                                       |float                               |
|dst_host_count                 |                                       |int                                 |
|dst_host_srv_count             |                                       |int                                 |
|dst_host_same_srv_rate         |                                       |float                               |
|dst_host_diff_srv_rate         |                                       |float                               |
|dst_host_rerror_rate           |                                       |int                                 |
|dst_host_same_src_port_rate    |                                       |float                               |
|dst_host_srv_diff_host_rate    |                                       |float                               |

****
# **Project Steps**
## Acquire & Prepare
### acquire.py
- Data is acquired from .csv files on [Kaggle](https://www.kaggle.com/sampadab17/network-intrusion-detection). Functions are stored in the acquire file, which allows quick access to the data. Once the acquire file is imported, it can be used each time to access the data


### prepare.py
- I chose to limit outliers extremely conservatively because in this case the outliers ARE the story
- For the 'service' column, I dropped any service that had less than 400 occurances, as it still gave me plenty of anomalies
- I aggressively dropped rows that I deemed unnecessary
- Created dummies for all of the object-type columns

## Explore
- Finding which features have the highest correlation to normal behavior
- Visualizing variable correlation with plots

## Model
After splitting and exploring the data, progress to modeling.  
With the train data set, try four different classification models, determining which data features and model parameters create better predictions.
- 2 different Logistic Regression Models
- Decision Tree
- Random Forest

Evaluate the best model on the test data set
### Outcome
- Decision Tree, Random Forest, and Logistic Regession1 models all performed well and beat my baseline handily
- Logistic Regression2 model with the limited features had an accuracy that equalled my baseline
- My best-performing model was Random Forest. I ran it on my test data for my best outcome yet: 99% accuracy and 99% recall

# **How to Reproduce**
- Read this README.md
- Download the Train_data.csv from [Kaggle](https://www.kaggle.com/sampadab17/network-intrusion-detection)
- Download the wrangle.py, explore.py, and final_notebook.ipynb into your working directory
- Run the final_notebook.ipynb notebook


