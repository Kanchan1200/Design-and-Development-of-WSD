
import numpy as np 

from util.saveToCSV import save_csv
from util.data_cleaning import find_label, get_sentences, remove_punc, remove_xtags, make_line

"""## Data Cleaning

"""

def clean_dataset(dataset):
  # raw data input
  with open(dataset, "r") as data:
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
    data = get_sentences(data)

    for line in data[:]:
      # print(x)
      # word_class = re.search(".(HARD\d)\b", str(x))
      # print(word_class)
      # letters = re.sub("[^a-zA-Z]", " ", x)
      # print(letters)


      # 1. remove ", `, ., ',', ',
      line = remove_punc(line) 
      label, sentence = find_label(line)
      # sentence = remove_punc(sentence)

      sentence = remove_xtags(sentence)

      # print(n,'\nLine:', sentence, '\nLabel:', label)
      n+=1
      sentence = make_line(sentence)
      clean_data.append([sentence, label])

  save_csv(clean_data, './data/hard_clean.csv')

if(__name__ == '__main__'):

  # senseval dataset file path
  dataset = "./data/hard.cor"

  clean_dataset(dataset)