import pandas as pd
import emoji

def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)

dataset = pd.read_csv("val.csv")


tweets = dataset[["text"]].values.astype('U').tolist()
tweets_cleared = []

for i in range((len(tweets))):

    tweet = tweets[i][0]

    word_list = tweet.split()
    word_list_deleted = word_list.copy()


    for word in word_list:
        if word.find("@")>=0 or word.find("http")>=0 \
                or word.find("#")>=0 or word.find("&")>=0 or word == "RT":
            word_list_deleted.remove(word)

    string = " "
    string = string.join(word_list_deleted)
    string = remove_emoji(string)

    tweets_cleared.append(string)

dataset[["text"]] = tweets_cleared

dataset.to_csv("cleared_val.csv")
print()