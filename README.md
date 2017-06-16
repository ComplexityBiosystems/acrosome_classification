# Acrosome Classification with SVM
This repository contains data and code used in  

A. Taloni, F. Font-Clos, L. Guidetti, S. Milan, M. Ascagni, C. Vasco, M. E. Pasini,  M. R. Gioria, E. Ciusani, S. Zapperi and C. A. M. La Porta  
Probing spermiogenesis: a digital strategy for mouse acrosome classification  
*Scientific Reports 7, Article number: 3748 (2017)*  
[Link to journal](https://www.nature.com/articles/s41598-017-03867-7)  
[Link to PDF](https://www.nature.com/articles/s41598-017-03867-7.pdf)  
doi:10.1038/s41598-017-03867-7  
  
The repository is organized as follows:

+ [data/](data/) two csv files containing the 7 morphological features for spermatids and spermatozoa acrosome cells.
+ [notebooks/](notebooks/) a jupyter notebook in python, which generates all results and figures of the manuscript.
+ [code/](code/) python code for cross validation and to compute local curvatures via vtk. 
+ [output/](output/) all figures and some additional ouput.

To reproduce the results of the manuscrpit in your computer, first clone the repository locally, and then simply running [this notebook](notebooks/Automatic_classification_SVM_acrosome_dataset.ipynb) will recreate all files in the [output folder](output/).

### Dependencies
The code depends only on the following standard python packages:
+ numpy
+ pandas
+ matplotlib
+ seaborn
+ sklearn

In addition, the [vtk](http://www.vtk.org/) package is used to extract local curvatures from mesh files, but this is not necessary to reproduce the results in the manuscript. 
