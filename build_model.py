import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

from util.modelling import map_labels, saveModel

"""## Classifier"""

# read final data
input_file = './data/hard3.csv'

df = pd.read_csv(input_file)

label_map = {"HARD1": 0, "HARD2" : 1, "HARD3" : 2}


df = map_labels(df, label_map)

x,y = df["line"].values, df["label"].values


vectorizer = TfidfVectorizer()
corpus = vectorizer.fit_transform(x) #corpus -> Collection of words.
# print(type(x))

X_train, X_test, y_train, y_test = train_test_split(corpus, y, test_size=0.33, random_state=42)



model = SVC()
model.fit(X_train,y_train)
preds = model.predict(X_test)

# score check
print('Accuracy:',accuracy_score(y_test, preds))

saveModel(model, 'hard_svm.pkl')
saveModel(vectorizer, 'hard_vects.pkl')