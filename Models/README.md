### Accuracy scores for Dataset1

|              | precision | recall | f1-score | support |
|:------------:| --------- | ------ | --------:| ------- |
| 0            | 0.88      | 0.67   | 0.76     | 1376    |
| 1            | 0.94      | 0.98   | 0.96     | 6803    |
| accuracy     |           |        | 0.93     | 8179    |
| macro avg    | 0.91      | 0.83   | 0.86     | 8179    |
| weighted avg | 0.93      | 0.93   | 0.93     | 8179    |

| Model                                   | Accuracy           |
| --------------------------------------- | ------------------ |
| LR  - Accuracy without stopwords 1-gram | 0.8915802018635309 |
| LR - Accuracy with stopwords 1-gram     | 0.8899259835890243 |
| LR - Accuracy without stopwords 2-gram  | 0.7825933320114955 |
| LR - Accuracy with stopwords 2-gram     | 0.7903002330146273 |
| LR - Accuracy without stopwords 3-gram  | 0.775370285539777  |
| LR - Accuracy with stopwords 3-gram     | 0.7758545144834039 |
| LR - Accuracy without stopwords 4-gram  | 0.7751685099142727 |
| LR - Accuracy with stopwords 4-gram     | 0.7750878159428627 |
| LR - Accuracy without stopwords 5-gram  | 0.7745632481529269 |
| LR - Accuracy with stopwords 5-gram     | 0.7748860728749422 |

Accuracy(without Stop words):  0.9337327301626116
Accuracy(with Stop words):  0.9288421567428781

#### Accuracy for Dataset1 CV=10, Multinomial

| Model                                       | Accuracy           |
| ------------------------------------------- | ------------------ |
| MultinomialNB  1 - gram without stopwords   | 0.8102738223026611 |
| MultinomialNB  1 - gram with stopwords      | 0.8005494743415312 |
| MultinomialNB  2 - gram without stopwords : | 0.786184710242388  |
| MultinomialNB  2 - gram with stopwords :    | 0.8034549619548355 |
| MultinomialNB  3 - gram without stopwords : | 0.7750875717609844 |
| MultinomialNB  3 - gram with stopwords :    | 0.7760561435997813 |
| MultinomialNB  4 - gram without stopwords : | 0.7748858775294394 |
| MultinomialNB  4 - gram with stopwords :    | 0.7751281385103799 |
| MultinomialNB  5 - gram without stopwords : | 0.7743211336811135 |
| MultinomialNB  5 - gram with stopwords :    | 0.7750875717609844 |
| MultinomialNB  6 - gram without stopwords : | 0.7743211336811135 |
| MultinomialNB  6 - gram with stopwords :    | 0.7748858775294394 |

### Accuracy scores for Dataset2

| Model                                  | Accuracy           |
| -------------------------------------- | ------------------ |
| LR - Accuracy without stopwords 1-gram | 0.8961996602571884 |
| LR - Accuracy with stopwords 1-gram    | 0.8997622221907049 |
| LR - Accuracy without stopwords 2-gram | 0.891173488280703  |
| LR - Accuracy with stopwords 2-gram    | 0.891173488280703  |

### Accuracy scores for Dataset3

|              | precision | recall | f1-score | support |
|:------------:| --------- | ------ | --------:| ------- |
| 0            | 0.80      | 0.94   | 0.87     | 3800    |
| 1            | 0.81      | 0.51   | 0.63     | 1780    |
| accuracy     |           |        | 0.81     |         |
| macro avg    | 0.81      | 0.73   | 0.75     | 5580    |
| weighted avg | 0.81      | 0.81   | 0.79     | 5580    |

| Model                                   | Accuracy           |
| --------------------------------------- | ------------------ |
| LR  - Accuracy without stopwords 1-gram | 0.814987582008945  |
| LR - Accuracy with stopwords 1-gram     | 0.8171164648584242 |
| LR - Accuracy without stopwords 2-gram  | 0.7350790451172993 |
| LR - Accuracy with stopwords 2-gram     | 0.7719871132581011 |
| LR - Accuracy without stopwords 3-gram  | 0.6919619139095072 |
| LR - Accuracy with stopwords 3-gram     | 0.7388058766945059 |
| LR - Accuracy without stopwords 4-gram  | 0.6874666918286406 |
| LR - Accuracy with stopwords 4-gram     | 0.7074583299659418 |
| LR - Accuracy without stopwords 5-gram  | 0.686638709325233  |
| LR - Accuracy with stopwords 5-gram     | 0.6883538459296814 |



### Accuracy scores for Dataset4

| Model                                   | Accuracy           |
| --------------------------------------- | ------------------ |
| LR  - Accuracy without stopwords 1-gram | 0.7859050194316929  |
| LR - Accuracy with stopwords 1-gram     | 0.7840201321883404 |
| LR - Accuracy without stopwords 2-gram  | 0.732604998651498 |
| LR - Accuracy with stopwords 2-gram     | 0.7481623244977638 |
| LR - Accuracy without stopwords 3-gram  | 0.6696718781158247 |
| LR - Accuracy with stopwords 3-gram     | 0.6845592722465137 |
| LR - Accuracy without stopwords 4-gram  | 0.6642844227102022 |
| LR - Accuracy with stopwords 4-gram     | 0.6715949814185607 |
| LR - Accuracy without stopwords 5-gram  | 0.6608164882060207  |
| LR - Accuracy with stopwords 5-gram     | 0.666776096177952 |


| Model                                            | Accuracy           |
| ------------------------------------------------ | ------------------ |
| Multinomial Naive Bayes with stopwords 1-gram    | 0.6145903479236813 |
| Multinomial Naive Bayes without stopwords 1-gram | 0.6264870931537598 |
| Multinomial Naive Bayes with stopwords 2-gram    | 0.5947250280583614 |
| Multinomial Naive Bayes without stopwords 2-gram | 0.5936026936026936 |
| Multinomial Naive Bayes with stopwords 3-gram    | 0.5496071829405162 |
| Multinomial Naive Bayes without stopwords 3-gram | 0.5503928170594837 |
| Multinomial Naive Bayes with stopwords 4-gram    | 0.540628507295174  |
| Multinomial Naive Bayes without stopwords 4-gram | 0.5332210998877666 |

### Accuracy scores for Dataset2 with Naive Bayes

| Model                                            | Accuracy           |
| ------------------------------------------------ | ------------------ |
| Multinomial Naive Bayes with stopwords 1-gram    | 0.8647990255785627 |
| Multinomial Naive Bayes without stopwords 1-gram | 0.8724116930572473 |
| Multinomial Naive Bayes with stopwords 2-gram    | 0.8654080389768575 |
| Multinomial Naive Bayes without stopwords 2-gram | 0.873020706455542  |
| Multinomial Naive Bayes with stopwords 3-gram    | 0.8675395858708892 |
| Multinomial Naive Bayes without stopwords 3-gram | 0.8647990255785627 |
| Multinomial Naive Bayes with stopwords 4-gram    | 0.8663215590742996 |
| Multinomial Naive Bayes without stopwords 4-gram | 0.8721071863580999 |

Accuracy with stopwords 1-gram   - Multinomial Naive Bayes :  0.8647990255785627
Accuracy without stopwords 1-gram   - Multinomial Naive Bayes :  0.8724116930572473
Accuracy with stopwords 2-gram   - Multinomial Naive Bayes :  0.8654080389768575
Accuracy without stopwords 2-gram   - Multinomial Naive Bayes :  0.873020706455542
Accuracy with stopwords 3-gram   - Multinomial Naive Bayes :  0.8675395858708892
Accuracy without stopwords 3-gram   - Multinomial Naive Bayes :  0.8647990255785627
Accuracy with stopwords 4-gram   - Multinomial Naive Bayes :  0.8663215590742996
Accuracy without stopwords 4-gram   - Multinomial Naive Bayes :  0.8721071863580999

### Accuracy scores for Dataset3 with Naive Bayes

| Model                                     | Accuracy           |
| ----------------------------------------- | ------------------ |
| MultinomialNB  1 - gram without stopwords | 0.7527053591248498 |
| MultinomialNB  1 - gram with stopwords    | 0.7296379174498268 |
| MultinomialNB  2 - gram without stopwords | 0.7360256860346887 |
| MultinomialNB  2 - gram with stopwords    | 0.766131364212258  |
| MultinomialNB  3 - gram without stopwords | 0.6885906374207426 |
| MultinomialNB  3 - gram with stopwords    | 0.7400484808248954 |
| MultinomialNB  4 - gram without stopwords | 0.6836813540418708 |
| MultinomialNB  4 - gram with stopwords    | 0.7171584836271412 |
| MultinomialNB  5 - gram without stopwords | 0.6836813540418708 |
| MultinomialNB  5 - gram with stopwords    | 0.6872300403887471 |
| MultinomialNB  6 - gram without stopwords | 0.6836813540418708 |
| MultinomialNB  6 - gram with stopwords    | 0.6836813540418708 |
