'''
Sample predictive model.
You must supply at least 4 methods:
- fit: trains the model.
- predict: uses the model to perform predictions.
- save: saves the model.
- load: reloads the model.
'''
import pickle
import numpy as np   # We recommend to use numpy arrays
from os.path import isfile
from sklearn.base import BaseEstimator
from sklearn import tree
#from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest

class Preprocessor(BaseEstimator): #VERSION 1
    def __init__(self):
        self.transformer = PCA(n_components=100) #reduit le nombre de features de 200 à 100
        clf = svm.SVC(kernel='linear') #classifieur lineaire
    
    #application de la méthode pipeline
    def fit(self, X_train, Y_train):
        Pipeline(memory=None,steps=[('reduc dim', self.transformer), ('calssif svc', clf)])
            
    def fit_transform(self, X, Y):
        return self.transformer.fit_transform(X,Y)
    
    def transform(self, X, y=None):
        return self.transformer.transform(X)
    




                                    
    """
    class Preprocessor(BaseEstimator): VERSION DANS LE RAPPORT
        
        classifier = svm.SVC()
        """<Choix CLASSIFIER>"""
        n_pca=1
        n_skb=1
        def __init__(self, transformer=identity):
            self.transformer = self
        
        
        def fit(self, X, y=None):
            y_train = X['target'].values
            X_train = X.drop('target', axis=1).values
        
        PCAPip = Pipeline([('pca',PCA()),('SKB',SelectKBest()),('clf',self.classifier)])
            self.classifier.fit(X_train,y_train)
            t = []
            i=20
            while i <int(100):
                t.append(i)
                i+=15
            tab = []
            for j in range(5,20):
            tab.append(j+1)
        grid_search = GridSearchCV(PCAPip{'pca__n_components':t,'SKB__k':tab},verbose=1,scoring=make_scorer(accuracy_score))
            grid_search.fit(X_train,y_train)
            
        self.n_pca=grid_search.best_params_.get('pca__n_components')
            self.n_skb=grid_search.best_params_.get('SKB__k')
            return self


       def fit_transform(self, X, y=None):
            return self.fit(X).transform(X)


        def transform(self, X, y=None):
            y_train = X['target'].values
            X_train = X.drop('target', axis=1).values
            sel = VarianceThreshold(threshold=(0.05))
            X_train = sel.fit_transform(X_train)
            scaler=StandardScaler()
            X_train=scaler.fit_transform(X_train)
            pca = PCA(n_components=self.n_pca)
            kbest=SelectKBest(k=self.n_skb)
            X_train=pca.fit_transform(X_train)
            X_train=kbest.fit_transform(X_train,y_train)
            return X_train

    if __name__=="__main__":
        print(data.shape)
        Y_train = data['target'].values
        X_train = data.drop('target', axis=1).values
        print("*** Original data ***")
        print data

        Prepro = Preprocessor()
        data = Prepro.fit_transform(data)
        print("*** Transformed data ***")
        print data
        print(len(data),"x",len(data[0]))
"""


class model (BaseEstimator):
    def __init__(self):
        '''
        This constructor is supposed to initialize data members.
        Use triple quotes for function documentation. 
        '''
        self.num_train_samples=0
        self.num_feat=1
        self.num_labels=1
        self.is_trained=False
        self.model = clf = LogisticRegression(solver='lbfgs', multi_class='ovr',penalty='l2',tol=1e-5,C=2.365,class_weight='balanced',max_iter=1000,random_state=0)
        #self.model = clf = GradientBoostingClassifier(n_estimators=170, learning_rate=0.8,max_depth=3, random_state=0)

        
    def fit(self, X, y):
        '''
        This function should train the model parameters.
        Here we do nothing in this example...
        Args:
            X: Training data matrix of dim num_train_samples * num_feat.
            y: Training label matrix of dim num_train_samples * num_labels.
        Both inputs are numpy arrays.
        For classification, labels could be either numbers 0, 1, ... c-1 for c classe
        or one-hot encoded vector of zeros, with a 1 at the kth position for class k.
        The AutoML format support on-hot encoding, which also works for multi-labels problems.
        Use data_converter.convert_to_num() to convert to the category number format.
        For regression, labels are continuous values.
        '''
        self.num_train_samples = X.shape[0]
        if X.ndim>1: self.num_feat = X.shape[1]
        print("FIT: dim(X)= [{:d}, {:d}]".format(self.num_train_samples, self.num_feat))
        num_train_samples = y.shape[0]
        if y.ndim>1: self.num_labels = y.shape[1]
        print("FIT: dim(y)= [{:d}, {:d}]".format(num_train_samples, self.num_labels))
        if (self.num_train_samples != num_train_samples):
            print("ARRGH: number of samples in X and y do not match!")
        self.is_trained=True
        self.model = self.model.fit(X, y)

    def predict(self, X):
        '''
        This function should provide predictions of labels on (test) data.
        Here we just return zeros...
        Make sure that the predicted values are in the correct format for the scoring
        metric. For example, binary classification problems often expect predictions
        in the form of a discriminant value (if the area under the ROC curve it the metric)
        rather that predictions of the class labels themselves. For multi-class or multi-labels
        problems, class probabilities are often expected if the metric is cross-entropy.
        Scikit-learn also has a function predict-proba, we do not require it.
        The function predict eventually can return probabilities.
        '''
        num_test_samples = X.shape[0]
        if X.ndim>1: num_feat = X.shape[1]
        print("PREDICT: dim(X)= [{:d}, {:d}]".format(num_test_samples, num_feat))
        if (self.num_feat != num_feat):
            print("ARRGH: number of features in X does not match training data!")
        print("PREDICT: dim(y)= [{:d}, {:d}]".format(num_test_samples, self.num_labels))
        y = self.model.predict_proba(X)
        # If you uncomment the next line, you get pretty good results for the Iris data :-)
        #y = np.round(X[:,3])
        return y[:,1]

    def save(self, path="./"):
        pickle.dump(self.model, open(path + '_model.pickle', "wb"))

    def load(self, path="./"):
        modelfile = path + '_model.pickle'
        if isfile(modelfile):
            with open(modelfile, 'rb') as f:
                self = pickle.load(f)
            print("Model reloaded from: " + modelfile)
        return self
