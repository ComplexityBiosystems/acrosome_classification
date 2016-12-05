# Acrosome Classification with SVM
This repository contains data and code used in [insert reference](link). It is organized as follows:

+ [data/](data/) two csv files containing the 7 morphological features for spermatids and spermatozoa
+ [notebooks/](notebooks/) a jupyter notebook in python, which generates all results and figures of the manuscript.
+ [code/](code/) some functions are defined here, and the imported into the notebook.
+ [output/](output/) all figures and some additional ouput.

To reproduce the results of the manuscrpit in your computer, first clone the repository locally, and then simply running [this notebook](notebooks/Automatic_classification_SVM_acrosome_dataset.ipynb) will recreate all files in the [output folder](output/).

### Dependencies
The code depends only on the following standard python packages:
+ numpy
+ pandas
+ matplotlib
+ seaborn
+ sklearn
