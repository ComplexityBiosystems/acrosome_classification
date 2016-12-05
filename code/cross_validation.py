from sklearn import svm
import numpy as np
import pandas as pd

def n_fold_cross_sklearn(X,Y, n = 10, p = svm.SVC(),probs=False,class_weights=None):
    """
    X are data
    Y are class labels
    n is fold
    p is the classifier
    """
    # numb data
    N = X.shape[0]
    
    # numb classes
    C = len(list(np.unique(Y)))
    
    # create partition's size
    # this seems silly, but it just works!
    part_sizes = [0]*n
    for i in range(N):
        part_sizes[np.mod(i,n)] = part_sizes[np.mod(i,n)] + 1

    # create partition labels
    G = []
    for g in range(n):
        for i in range(part_sizes[g]):
            G.append(g)    
    np.random.shuffle(G)
    G = np.array(G)
    
    ### start cross validation
    results = pd.DataFrame(index=range(len(Y)),columns=["c"])
    
    # now iterate over the group that I leave out
    #for out in range(n):
    for out in range(n):
        x = X[G!=out]
        y = Y[G!=out]
        xt = X[G==out]
        yt = Y[G==out]
        if class_weights is None:
            p.fit(x,y)
        else:
            p.fit(x,y,np.array([class_weights[c] for c in y]))
        if probs:
            pred = p.predict_proba(xt)
            results.loc[G==out,"c"] = pred.T[0] # return probs of first class
        else:
            pred = p.predict(xt)
            results.loc[G==out,"c"] = ((pred-yt)==0)
        
    
    results = results["c"].values
    
   
    return results.sum()/float(len(list(results))),results