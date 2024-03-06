## Import the necessary library

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load the CSV file
df = pd.read_csv("iris.csv")

# check the first 5 rows
print(df.head())

## Try to check the dependent variable and Independent variable
X  = df[["Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width"]]
y = df["Class"]

## After than split the dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 50)


## Select the feature and extract
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

### Instansiate the model
classifier = RandomForestClassifier()

## Fit the Model
classifier.fit(X_train, y_train)

## Make the Pickle file
pickle.dump(classifier, open("model.pkl", "wb"))