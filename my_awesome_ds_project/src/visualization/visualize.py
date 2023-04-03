
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import confusion_matrix, roc_curve, auc, precision_recall_curve
from pycaret.classification import *

class Visualization:
    def __init__(self, train_data, test_data, validate_data, best_model, label_name):
        self.train_data = train_data
        self.test_data = test_data
        self.validate_data = validate_data
        self.best_model = best_model
        self.label_name = label_name
    
    def plot_categorical_features(self):
        for col in self.train_data.select_dtypes(include=['object']).columns:
            plt.figure(figsize=(10,4))
            plt.subplot(1, 3, 1)
            # sns.barplot(x=col, y=self.label_name, data=self.train_data)
            plt.title('Bar Graph of ' + col)
            plt.subplot(1, 3, 2)
            self.train_data[col].value_counts().plot.pie(autopct='%1.1f%%')
            plt.title('Pie Chart of ' + col)
            plt.subplot(1, 3, 3)
            sns.heatmap(pd.crosstab(self.train_data[col], self.train_data[self.label_name]), cmap="YlGnBu", annot=True)
            plt.title('Heatmap of ' + col)
            plt.show()
    
    def plot_numerical_features(self):
        for col in self.train_data.select_dtypes(include=['int64', 'float64']).columns:
            plt.figure(figsize=(10,4))
            plt.subplot(1, 4, 1)
            self.train_data[col].plot.hist(bins=10)
            plt.title('Histogram with 10 bins of ' + col)
            plt.subplot(1, 4, 2)
            sns.boxplot(x=self.train_data[col])
            plt.title('Box Plot of ' + col)
            plt.subplot(1, 4, 3)
            sns.kdeplot(self.train_data[col], shade=True)
            plt.title('Density Plot of ' + col)
            plt.subplot(1, 4, 4)
            sns.scatterplot(x=col, y=self.label_name, data=self.train_data)
            plt.title('Scatter Plot of ' + col)
            plt.show()
    
    def plot_model_metrics(self):
        y_pred = predict_model(self.best_model, self.test_data.drop(self.label_name, axis=1))#['prediction_score']
        y_pred = y_pred['prediction_score'] if 'prediction_score' in y_pred  else y_pred['prediction_label']
        fpr, tpr, thresholds = roc_curve(self.test_data[self.label_name], y_pred)
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 3, 1)
        plt.plot(fpr, tpr, label='AUC = %0.2f'% auc(fpr, tpr))
        plt.plot([0,1],[0,1],'r--')
        plt.xlim([0.0,1.0])
        plt.ylim([0.0,1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('AUC')
        plt.legend(loc="lower right")
        plt.subplot(1, 3, 2)
        y_pred_after_threshold = [1 if  y_in > 0.5 else 0 for y_in in y_pred]
        sns.heatmap(confusion_matrix(self.test_data[self.label_name], y_pred_after_threshold), annot=True, fmt='d')
        plt.title('Confusion Matrix')
        plt.subplot(1, 3, 3)
        precision, recall, thresholds = precision_recall_curve(self.test_data[self.label_name], y_pred)
        plt.plot(recall, precision, label='Precision-Recall Curve')
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.title('Precision Recall Curve')
        plt.legend(loc="lower left")
        plt.show()
    
    def visualize(self):
        # self.plot_categorical_features()
        # self.plot_numerical_features()
        self.plot_model_metrics()