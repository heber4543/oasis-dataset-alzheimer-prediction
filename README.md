# 

### This is a project for the Machine Learning course in the Master's program in Computer Engineering

### DATASET
The Open Access Series of Imaging Studies (OASIS) is a series of neuroimaging data sets that are publicly available for study and analysis. The present MRI data set consists of a longitudinal collection of 150 subjects aged 60 to 96 years, all acquired on the same scanner using identical sequences. Each subject was scanned on two or more visits, separated by at least 1 year, for a total of 373 imaging sessions (Marcus et al., 2009).

### Acces
Click [here](https://oasis-dataset-alzheimer-prediction.streamlit.app/) to access the app

### Dataset
To load the OASIS dataset, click [here](https://sites.wustl.edu/oasisbrains/home/oasis-2/).
If you prefer, you can download it from this repository, but for ethical reasons, it’s better to do it from the official page.

### Data exploration and model training and test
The source code where the dataset was explored, the data was prepared, and the model was developed can be found in the `modelo` directory, in the file named `oasis_completo.ipynb`. In this file, the data from the dataset is explored, and the results of logistic regression are compared to logistic regression using K-Fold. Additionally, linear, polynomial, and Gaussian SVM models are compared.
In the `Model`, there are also other file: `oasis_implementacion.py`, It is the `.py` file that was used to train the best models; additionally, a pipeline for data processing was implemented.

### Best model
In the folder, you will find 5 `.pkl` files corresponding to the models and the pipeline used in the app.

### APP
You will find two files: `requirements.txt` and `streamlit_app.py`. The first contains the libraries required to run the app. The second is the app code (model implementation and interface).
