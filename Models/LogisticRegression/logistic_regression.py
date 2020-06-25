import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import sklearn.metrics as metrics

dataset = pd.read_csv("merged_and_cleaned.csv")
dataset.fillna("NaN")

training_data, testing_data = train_test_split(dataset, test_size=0.33)

train_class = training_data['class'].values.astype('U')
test_class = testing_data['class'].values.astype('U')

binary_train = []

for c in train_class:
    if c == "racism" or c == "sexism":
        binary_train.append(1)
    else:
        binary_train.append(0)

binary_test = []

for c in test_class:
    if c == "racism" or c == "sexism":
        binary_test.append(1)
    else:
        binary_test.append(0)

train_text = training_data['text'].values.astype('U')
test_text = testing_data['text'].values.astype('U')

def feature_extract(train_text, test_text, stop_word=True):
    # If stop words want to be excluded.
    if stop_word:
        tf_idf = TfidfVectorizer(ngram_range=(1, 1), stop_words="english")
        tf_idf.fit_transform(train_text)

        train_feature_set = tf_idf.transform(train_text)
        test_feature_set = tf_idf.transform(test_text)

    # If stop words want to be included
    if not stop_word:
        tf_idf = TfidfVectorizer(ngram_range=(1, 1))
        tf_idf.fit_transform(train_text)

        train_feature_set = tf_idf.transform(train_text)
        test_feature_set = tf_idf.transform(test_text)

    return train_feature_set, test_feature_set

for b in [True, False]:
    train_feature_set, test_feature_set = feature_extract(train_text, test_text, stop_word=b)
    logmodel = LogisticRegression(solver="liblinear", multi_class="ovr", random_state=42)
    logmodel.fit(train_feature_set, binary_train)

    predictions = logmodel.predict(test_feature_set)

    if b is True:
        print("Accuracy(without Stop words): ", metrics.accuracy_score(binary_test, predictions))
    else:
        print("Accuracy(with Stop words): ", metrics.accuracy_score(binary_test, predictions))

