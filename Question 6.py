import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

#load csv 
df = pd.read_csv("CarSharing.csv")

#Calculation of the mean
average_demand_rate = df['demand'].mean()

#sort the numerical demands into categorical bins 
df['demand_category'] = df['demand'].apply(lambda x: 1 if x > average_demand_rate else 2)

#Choosing the demand columns for the prediction 
X = df[['demand']]
y = df['demand_category']

#Training sets and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)

# Training of the data 
rf_classifier = RandomForestClassifier(random_state=4)
rf_classifier.fit(X_train, y_train)

dt_classifier = DecisionTreeClassifier(random_state=4)
dt_classifier.fit(X_train, y_train)

lr_classifier = LogisticRegression(random_state=4)
lr_classifier.fit(X_train, y_train)

#Predictions 
rf_predictions = rf_classifier.predict(X_test)
dt_predictions = dt_classifier.predict(X_test)
lr_predictions = lr_classifier.predict(X_test)

print("Random Forest Classifier Predictions:", rf_predictions)
print("Decision Tree Classifier Predictions:", dt_predictions)
print("Logistic Regression Classifier Predictions:", lr_predictions)

#Accuracy calculations 
rf_accuracy = accuracy_score(y_test, rf_predictions)
dt_accuracy = accuracy_score(y_test, dt_predictions)
lr_accuracy = accuracy_score(y_test, lr_predictions)

print("Random Forest Classifier Accuracy:", rf_accuracy)
print("Decision Tree Classifier Accuracy:", dt_accuracy)
print("Logistic Regression Classifier Accuracy:", lr_accuracy)


#making the confusion matrix 
#inspiration from: https://stackoverflow.com/questions/76784223/how-to-plot-a-confusion-matrix 
def plot_confusion_matrix(y_true, y_pred, title):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title(title)
    plt.show()

#plotting the CM for each classifier 
plot_confusion_matrix(y_test, rf_predictions, 'Random Forest Classifier Confusion Matrix')
plot_confusion_matrix(y_test, dt_predictions, 'Decision Tree Classifier Confusion Matrix')
plot_confusion_matrix(y_test, lr_predictions, 'Logistic Regression Classifier Confusion Matrix')