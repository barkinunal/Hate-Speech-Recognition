# logistic regression 1gram with stop words

|              |   | precision | recall | f1-score | support |
|--------------|:-:|-----------|--------|----------|---------|
|              | 0 | 0.82      | 0.94   | 0.88     | 1156    |
|              | 1 | 0.81      | 0.57   | 0.67     | 534     |
| accuracy     |   |           |        | 0.82     | 1690    |
| macro avg    |   | 0.82      | 0.75   | 0.77     | 1690    |
| weighted avg |   | 0.82      | 0.82   | 0.81     | 1690    |

# logistic regression 1gram without stop words

|              |   | precision | recall | f1-score | support |
|--------------|:-:|-----------|--------|----------|---------|
|              | 0 | 0.83      | 0.92   | 0.88     | 1156    |
|              | 1 | 0.79      | 0.60   | 0.68     | 535     |
| accuracy     |   |           |        | 0.82     | 1691    |
| macro avg    |   | 0.81      | 0.76   | 0.78     | 1691    |
| weighted avg |   | 0.82      | 0.82   | 0.82     | 1691    |

# svm 1gram with stop words 

|              |   | precision | recall | f1-score | support |
|--------------|:-:|-----------|--------|----------|---------|
|              | 0 | 0.44      | 0.38   | 0.41     | 143     |
|              | 1 | 0.92      | 0.93   | 0.92     | 1919    |
|              | 2 | 0.81      | 0.80   | 0.81     | 417     |
| accuracy     |   |           |        | 0.87     | 2479    |
| macro avg    |   | 0.72      | 0.70   | 0.71     | 2479    |
| weighted avg |   | 0.87      | 0.87   | 0.87     | 2479    |


# svm 1gram without stop words


|              |   | precision | recall | f1-score | support |
|--------------|:-:|-----------|--------|----------|---------|
|              | 0 | 0.63      | 0.30   | 0.41     | 143     |
|              | 1 | 0.92      | 0.95   | 0.93     | 1919    |
|              | 2 | 0.81      | 0.81   | 0.81     | 416     |
| accuracy     |   |           |        | 0.89     | 2478    |
| macro avg    |   | 0.79      | 0.69   | 0.72     | 2478    |
| weighted avg |   | 0.88      | 0.89   | 0.88     | 2478    |

# naive bayes 1gram with stop words

|              |      | precision | recall | f1-score | support |
|--------------|:----:|-----------|--------|----------|---------|
|              | 0    | 0.61      | 0.94   | 0.74     | 1550    |
|              | 1    | 0.80      | 0.45   | 0.58     | 1420    |
| accuracy     |      |           |        | 0.65     | 2970    |
| macro avg    |      | 0.47      | 0.46   | 0.44     | 2970    |
| weighted avg |      | 0.59      | 0.65   | 0.58     | 2970    |

# naive bayes 1gram without stop words


|              |      | precision | recall | f1-score | support |
|--------------|:----:|-----------|--------|----------|---------|
|              | 0    | 0.67      | 0.85   | 0.75     | 1550    |
|              | 1    | 0.70      | 0.68   | 0.69     | 1420    |
| accuracy     |      |           |        | 0.68     | 2970    |
| macro avg    |      | 0.46      | 0.51   | 0.48     | 2970    |
| weighted avg |      | 0.59      | 0.68   | 0.63     | 2970    |

# with stop words 

| Dataset   | Model Name          | 1-gram  | 2-gram | 3-gram | 4-gram | 5-gram | 6-gram |
| --------- | ------------------- | ------- | ------ | ------ | ------ | ------ | ------ |
| Dataset-1 | SVM                 | 0.8889  | 0.8089 | 0.7800 | 0.7766 | 0.7762 | -      |

# without

| Dataset     | Model Name          | 1-gram | 2-gram | 3-gram | 4-gram | 5-gram | 6-gram |
| ----------- | ------------------- | ------ | ------ | ------ | ------ | ------ | ------ |
| Dataset - 1 | SVM                 | 0.8887 | 0.7961 | 0.7774 | 0.7760 | 0.7752 | -      |


