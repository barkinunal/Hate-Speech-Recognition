import pandas as pd

dataset1 = pd.read_csv("cleared_test.csv")
dataset2 = pd.read_csv("cleared_train.csv")
dataset3 = pd.read_csv("cleared_val.csv")

dataset_merged = dataset1.append(dataset2)
dataset_merged = dataset_merged.append(dataset3)

dataset_merged = dataset_merged.drop(['Unnamed: 0', 'Unnamed: 0.1'], axis = 1)

index = list(range(len(dataset_merged)))
dataset_merged[['index']] = index

dataset_merged.to_csv("merged.csv")
