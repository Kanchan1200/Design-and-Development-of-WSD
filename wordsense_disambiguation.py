
# Word Sense Disambiguation using TF-IDF Approach

# Here we are implementing TF IDF approach, 
# for that need data in a good data frame, 
# so lets sanitize data
import numpy as np
import pandas as pd
import re #regular expression
import csv

"""## Data Cleaning

"""

def find_label(line):
  index = line.index('<tag "')
  # print(index)
  word_end_index = line.index('</>') + 3
  label_end_index = line.index('">') 
  label = line[index+6:label_end_index]
  sentence = line[:index] + 'HARD' + line[word_end_index:]
  # print(label)
  return label, sentence



# raw data input
with open("./drive/MyDrive/A_word_sense/hard.cor",'r') as data:
  lines = data.readlines()
  data = np.array(lines)
  # checking data
  # print(data)
  # exit()
  clean_data = []
  # skipping first row, and
  # select current and every third row after it (actual data rows)
  # print()
  n = 1
  data = [ x[3:-5] for x in data[1::3]]

  for line in data[:]:
    # print(x)
    # word_class = re.search(".(HARD\d)\b", str(x))
    # print(word_class)
    # letters = re.sub("[^a-zA-Z]", " ", x)
    # print(letters)


    # 1. remove ", `, ., ',', ', 
    label, sentence = find_label(line)
    sentence = sentence.translate({ord('"'):None, ord('`'):None, ord('.'):None, ord(','):None, ord('\''):None})

    if(sentence.find('<s') != -1):
      noise = re.search("<s snum=\d+>", sentence)
      # print(noise.group())
      sentence = sentence.replace(noise.group(),'')
      # print('noise removed ', sentence)
      
    if(sentence.find('<com') != -1):
      noise = re.search("<com\w+>", sentence)
      sentence = sentence.replace(noise.group(), '')
    
    if(sentence.find('</com') != -1):
      noise = re.search("<\/com\w+>", sentence)
      sentence = sentence.replace(noise.group(), '')
    



    print(n,'\nLine:', sentence, '\nLabel:', label)
    n+=1
    # sentence = ''.join(sentence)
    clean_data.append([sentence, label])
    # row_label = re.search("hard\d+", str(x), flags=re.I)
    # print(row_label.group())
    # # row_label, sentence = find_label(x)
    # # print(row_label, '\n',sentence)


  
# print('\n\n\n')
# print(clean_data)

# save data in csv
fields = ['line', 'label']

with open('./drive/MyDrive/A_word_sense/hard3.csv', 'w') as f:
      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(clean_data)

"""## Classifier"""

# read final data

df = pd.read_csv('./drive/MyDrive/A_word_sense/hard3.csv')
# print(data.isnull())

  
# # Count total NaN at each column in a DataFrame
# print(" \nCount total NaN at each column in a DataFrame : \n\n",
#       data.isnull().sum())

print(df.head())
# print(df["label"].values)

label_map = {"HARD1": 0, "HARD2" : 1, "HARD3" : 2}
# print(label_map[df["label"].iloc[0]])

df["label"] = [label_map[i] for i in (df["label"].values)]
print(df.head())

from sklearn.model_selection import train_test_split

x,y = df["line"].values, df["label"].values

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
corpus = vectorizer.fit_transform(x) #corpus -> Collection of words.
print(type(x))

X_train, X_test, y_train, y_test = train_test_split(corpus, y, test_size=0.33, random_state=42)

print(X_train.shape)
# print(X_train)

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


model = SVC()
model.fit(X_train,y_train)
preds = model.predict(X_test)

# score check

print(accuracy_score(y_test, preds))

# Testing with custom input

test_sentence = "qualifying on the JEE exams is considered as one of the hardest battle for indian students" #@param {type:"string"}
# test_sentence = np.array([ x for x in test_sentence.split()])
print(test_sentence)
sample = vectorizer.transform((test_sentence,))

prediction = model.predict(sample)

pred_map = {0:"HARD1", 1:"HARD2", 2:"HARD3" }
# print()
print("Predicted Label:", pred_map[int(prediction)])

