import pandas as pd

dataset = pd.read_csv("labeled_data.csv")


tweets = dataset[["tweet"]].values.astype('U').tolist()
tweets_cleared = []

for i in range((len(tweets))):

    tweet = tweets[i][0]

    word_list = tweet.split()
    word_list_deleted = word_list.copy()


    for word in word_list:
        if word.find("@")>=0 or word.find("http")>=0 \
                or word.find("#")>=0 or word.find("&")>=0:
            word_list_deleted.remove(word)

    string = " "
    string = string.join(word_list_deleted)

    tweets_cleared.append(string)

dataset["tweet"] = tweets_cleared

dataset.to_csv("labeled_data_cleared.csv", encoding='utf-8', index=False)