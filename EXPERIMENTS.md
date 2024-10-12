# Experiments

## Using Model2Vec

### NearestCentroid

Same results both using SMOTE and without.

Performance on training set:
```
                           precision    recall  f1-score   support

          All Electronics       0.32      0.18      0.23     37024
           Amazon Fashion       0.58      0.88      0.70     41739
              Amazon Home       0.43      0.47      0.45     50008
    Arts, Crafts & Sewing       0.64      0.58      0.61     50759
               Automotive       0.73      0.59      0.65     51405
                    Books       0.91      0.68      0.78     48782
           Camera & Photo       0.67      0.62      0.64     25617
Cell Phones & Accessories       0.62      0.73      0.68     41433
                Computers       0.50      0.49      0.50     47060
            Digital Music       0.79      0.73      0.75     33928
                  Grocery       0.93      0.94      0.93     49090
   Health & Personal Care       0.09      0.28      0.14     10009
     Home Audio & Theater       0.36      0.53      0.42     23247
  Industrial & Scientific       0.33      0.52      0.40     38817
              Movies & TV       0.58      0.78      0.67     42484
      Musical Instruments       0.72      0.55      0.62     25100
          Office Products       0.63      0.49      0.55     50209
             Pet Supplies       0.86      0.66      0.74     40241
        Sports & Outdoors       0.51      0.50      0.50     49289
 Tools & Home Improvement       0.52      0.41      0.46     52014
             Toys & Games       0.71      0.45      0.55     50438
              Video Games       0.52      0.65      0.58     15198

                 accuracy                           0.59    873891
                macro avg       0.59      0.58      0.57    873891
             weighted avg       0.62      0.59      0.59    873891
```

Performance on test set:
```
                           precision    recall  f1-score   support

          All Electronics       0.31      0.18      0.22     15854
           Amazon Fashion       0.59      0.89      0.71     18008
              Amazon Home       0.43      0.47      0.45     21354
    Arts, Crafts & Sewing       0.64      0.58      0.61     21797
               Automotive       0.73      0.59      0.65     22029
                    Books       0.91      0.68      0.78     20903
           Camera & Photo       0.68      0.62      0.65     11070
Cell Phones & Accessories       0.63      0.74      0.68     17999
                Computers       0.50      0.49      0.50     20096
            Digital Music       0.78      0.73      0.76     14391
                  Grocery       0.93      0.94      0.94     21094
   Health & Personal Care       0.08      0.26      0.12      4107
     Home Audio & Theater       0.36      0.52      0.43     10154
  Industrial & Scientific       0.33      0.52      0.41     16686
              Movies & TV       0.58      0.78      0.67     18124
      Musical Instruments       0.72      0.54      0.62     10773
          Office Products       0.62      0.48      0.54     21472
             Pet Supplies       0.85      0.66      0.74     17249
        Sports & Outdoors       0.51      0.49      0.50     20888
 Tools & Home Improvement       0.52      0.42      0.46     22344
             Toys & Games       0.70      0.45      0.55     21596
              Video Games       0.52      0.66      0.58      6538

                 accuracy                           0.59    374526
                macro avg       0.59      0.58      0.57    374526
             weighted avg       0.62      0.59      0.59    374526
```

### KNN with SMOTE

Performance on training set:
```
                           precision    recall  f1-score   support

          All Electronics       0.66      0.70      0.68     36998
           Amazon Fashion       0.87      0.98      0.92     41912
              Amazon Home       0.82      0.77      0.79     49685
    Arts, Crafts & Sewing       0.89      0.87      0.88     50817
               Automotive       0.93      0.87      0.90     51356
                    Books       0.94      0.82      0.88     48935
           Camera & Photo       0.75      0.95      0.84     25632
Cell Phones & Accessories       0.86      0.89      0.88     41709
                Computers       0.86      0.78      0.82     46944
            Digital Music       0.86      0.94      0.90     33494
                  Grocery       0.98      0.97      0.97     49288
   Health & Personal Care       0.40      0.98      0.57      9884
     Home Audio & Theater       0.65      0.90      0.75     23422
  Industrial & Scientific       0.74      0.81      0.77     38740
              Movies & TV       0.86      0.84      0.85     42580
      Musical Instruments       0.84      0.94      0.89     25306
          Office Products       0.89      0.78      0.83     50271
             Pet Supplies       0.93      0.95      0.94     40225
        Sports & Outdoors       0.91      0.71      0.80     49281
 Tools & Home Improvement       0.89      0.74      0.81     52012
             Toys & Games       0.93      0.71      0.80     50237
              Video Games       0.67      0.99      0.80     15163

                 accuracy                           0.84    873891
                macro avg       0.82      0.86      0.83    873891
             weighted avg       0.86      0.84      0.84    873891
```


Performance on test set:
```
                           precision    recall  f1-score   support

          All Electronics       0.48      0.52      0.50     15880
           Amazon Fashion       0.82      0.97      0.89     17835
              Amazon Home       0.73      0.66      0.70     21677
    Arts, Crafts & Sewing       0.84      0.82      0.83     21739
               Automotive       0.89      0.82      0.85     22078
                    Books       0.89      0.75      0.82     20750
           Camera & Photo       0.65      0.89      0.75     11055
Cell Phones & Accessories       0.79      0.83      0.81     17723
                Computers       0.77      0.69      0.73     20212
            Digital Music       0.80      0.88      0.84     14825
                  Grocery       0.95      0.96      0.95     20896
   Health & Personal Care       0.20      0.53      0.29      4232
     Home Audio & Theater       0.49      0.74      0.59      9979
  Industrial & Scientific       0.63      0.69      0.66     16763
              Movies & TV       0.78      0.74      0.76     18028
      Musical Instruments       0.74      0.87      0.80     10567
          Office Products       0.82      0.71      0.76     21410
             Pet Supplies       0.90      0.91      0.91     17265
        Sports & Outdoors       0.84      0.60      0.70     20896
 Tools & Home Improvement       0.81      0.65      0.72     22346
             Toys & Games       0.89      0.62      0.73     21797
              Video Games       0.57      0.93      0.70      6573

                 accuracy                           0.76    374526
                macro avg       0.74      0.76      0.74    374526
             weighted avg       0.78      0.76      0.76    374526
```

### KNN without SMOTE

Performance on training set:
```
                           precision    recall  f1-score   support

          All Electronics       0.64      0.65      0.64     36998
           Amazon Fashion       0.84      0.98      0.90     41912
              Amazon Home       0.77      0.81      0.79     49685
    Arts, Crafts & Sewing       0.85      0.89      0.87     50817
               Automotive       0.89      0.91      0.90     51356
                    Books       0.87      0.86      0.87     48935
           Camera & Photo       0.81      0.90      0.85     25632
Cell Phones & Accessories       0.83      0.90      0.86     41709
                Computers       0.78      0.84      0.81     46944
            Digital Music       0.88      0.90      0.89     33494
                  Grocery       0.94      1.00      0.97     49288
   Health & Personal Care       0.79      0.31      0.44      9884
     Home Audio & Theater       0.72      0.71      0.72     23422
  Industrial & Scientific       0.80      0.74      0.77     38740
              Movies & TV       0.85      0.81      0.83     42580
      Musical Instruments       0.92      0.87      0.89     25306
          Office Products       0.85      0.82      0.83     50271
             Pet Supplies       0.93      0.94      0.94     40225
        Sports & Outdoors       0.89      0.75      0.81     49281
 Tools & Home Improvement       0.81      0.83      0.82     52012
             Toys & Games       0.90      0.77      0.83     50237
              Video Games       0.84      0.88      0.86     15163

                 accuracy                           0.84    873891
                macro avg       0.84      0.82      0.82    873891
             weighted avg       0.84      0.84      0.84    873891
```

Performance on test set:
```
                           precision    recall  f1-score   support

          All Electronics       0.50      0.51      0.50     15880
           Amazon Fashion       0.79      0.97      0.87     17835
              Amazon Home       0.69      0.71      0.70     21677
    Arts, Crafts & Sewing       0.80      0.84      0.82     21739
               Automotive       0.84      0.86      0.85     22078
                    Books       0.81      0.81      0.81     20750
           Camera & Photo       0.75      0.85      0.80     11055
Cell Phones & Accessories       0.77      0.86      0.82     17723
                Computers       0.71      0.77      0.74     20212
            Digital Music       0.84      0.84      0.84     14825
                  Grocery       0.93      0.99      0.96     20896
   Health & Personal Care       0.60      0.19      0.29      4232
     Home Audio & Theater       0.60      0.60      0.60      9979
  Industrial & Scientific       0.72      0.64      0.67     16763
              Movies & TV       0.78      0.72      0.75     18028
      Musical Instruments       0.87      0.81      0.84     10567
          Office Products       0.78      0.76      0.77     21410
             Pet Supplies       0.91      0.92      0.91     17265
        Sports & Outdoors       0.82      0.66      0.73     20896
 Tools & Home Improvement       0.72      0.75      0.73     22346
             Toys & Games       0.86      0.70      0.77     21797
              Video Games       0.78      0.83      0.80      6573

                 accuracy                           0.78    374526
                macro avg       0.77      0.76      0.75    374526
             weighted avg       0.78      0.78      0.77    374526
```

### HistGradientBoostingClassifier with SMOTE

Performance on training set:
```
                           precision    recall  f1-score   support

          All Electronics       0.54      0.39      0.45     36998
           Amazon Fashion       0.92      0.96      0.94     41912
              Amazon Home       0.68      0.63      0.66     49685
    Arts, Crafts & Sewing       0.78      0.77      0.77     50817
               Automotive       0.82      0.81      0.82     51356
                    Books       0.89      0.89      0.89     48935
           Camera & Photo       0.76      0.82      0.79     25632
Cell Phones & Accessories       0.81      0.84      0.82     41709
                Computers       0.74      0.72      0.73     46944
            Digital Music       0.86      0.90      0.88     33494
                  Grocery       0.99      0.98      0.99     49288
   Health & Personal Care       0.30      0.53      0.39      9884
     Home Audio & Theater       0.54      0.72      0.62     23422
  Industrial & Scientific       0.58      0.65      0.61     38740
              Movies & TV       0.83      0.84      0.84     42580
      Musical Instruments       0.79      0.81      0.80     25306
          Office Products       0.74      0.69      0.72     50271
             Pet Supplies       0.89      0.87      0.88     40225
        Sports & Outdoors       0.70      0.68      0.69     49281
 Tools & Home Improvement       0.68      0.66      0.67     52012
             Toys & Games       0.77      0.70      0.73     50237
              Video Games       0.80      0.89      0.84     15163

                 accuracy                           0.77    873891
                macro avg       0.75      0.76      0.75    873891
             weighted avg       0.77      0.77      0.76    873891
```

Performance on test set:
```
                           precision    recall  f1-score   support

          All Electronics       0.46      0.34      0.39     15880
           Amazon Fashion       0.91      0.95      0.93     17835
              Amazon Home       0.64      0.59      0.61     21677
    Arts, Crafts & Sewing       0.75      0.74      0.75     21739
               Automotive       0.80      0.79      0.79     22078
                    Books       0.86      0.86      0.86     20750
           Camera & Photo       0.73      0.78      0.76     11055
Cell Phones & Accessories       0.79      0.81      0.80     17723
                Computers       0.72      0.69      0.70     20212
            Digital Music       0.84      0.86      0.85     14825
                  Grocery       0.98      0.97      0.98     20896
   Health & Personal Care       0.22      0.39      0.28      4232
     Home Audio & Theater       0.50      0.66      0.57      9979
  Industrial & Scientific       0.54      0.61      0.57     16763
              Movies & TV       0.79      0.81      0.80     18028
      Musical Instruments       0.74      0.78      0.76     10567
          Office Products       0.70      0.66      0.68     21410
             Pet Supplies       0.87      0.84      0.86     17265
        Sports & Outdoors       0.66      0.64      0.65     20896
 Tools & Home Improvement       0.64      0.61      0.62     22346
             Toys & Games       0.74      0.68      0.71     21797
              Video Games       0.77      0.85      0.81      6573

                 accuracy                           0.73    374526
                macro avg       0.71      0.72      0.71    374526
             weighted avg       0.73      0.73      0.73    374526
```

### HistGradientBoostingClassifier without SMOTE

Performance on training set:
```
                           precision    recall  f1-score   support

          All Electronics       0.54      0.40      0.46     36998
           Amazon Fashion       0.92      0.96      0.94     41912
              Amazon Home       0.67      0.66      0.67     49685
    Arts, Crafts & Sewing       0.77      0.78      0.77     50817
               Automotive       0.81      0.83      0.82     51356
                    Books       0.89      0.90      0.89     48935
           Camera & Photo       0.80      0.79      0.80     25632
Cell Phones & Accessories       0.81      0.85      0.83     41709
                Computers       0.71      0.76      0.74     46944
            Digital Music       0.87      0.90      0.88     33494
                  Grocery       0.98      0.99      0.99     49288
   Health & Personal Care       0.67      0.37      0.48      9884
     Home Audio & Theater       0.61      0.64      0.62     23422
  Industrial & Scientific       0.62      0.63      0.62     38740
              Movies & TV       0.84      0.85      0.85     42580
      Musical Instruments       0.84      0.80      0.82     25306
          Office Products       0.73      0.72      0.72     50271
             Pet Supplies       0.89      0.88      0.88     40225
        Sports & Outdoors       0.69      0.71      0.70     49281
 Tools & Home Improvement       0.65      0.70      0.68     52012
             Toys & Games       0.75      0.73      0.74     50237
              Video Games       0.87      0.85      0.86     15163

                 accuracy                           0.77    873891
                macro avg       0.77      0.76      0.76    873891
             weighted avg       0.77      0.77      0.77    873891
```

Performance on test set:
```
                           precision    recall  f1-score   support

          All Electronics       0.46      0.34      0.39     15880
           Amazon Fashion       0.90      0.95      0.93     17835
              Amazon Home       0.62      0.62      0.62     21677
    Arts, Crafts & Sewing       0.74      0.76      0.75     21739
               Automotive       0.78      0.80      0.79     22078
                    Books       0.86      0.87      0.86     20750
           Camera & Photo       0.77      0.75      0.76     11055
Cell Phones & Accessories       0.78      0.82      0.80     17723
                Computers       0.68      0.73      0.70     20212
            Digital Music       0.85      0.86      0.85     14825
                  Grocery       0.97      0.98      0.98     20896
   Health & Personal Care       0.40      0.19      0.25      4232
     Home Audio & Theater       0.55      0.56      0.55      9979
  Industrial & Scientific       0.57      0.58      0.57     16763
              Movies & TV       0.79      0.82      0.81     18028
      Musical Instruments       0.79      0.75      0.77     10567
          Office Products       0.69      0.68      0.69     21410
             Pet Supplies       0.88      0.84      0.86     17265
        Sports & Outdoors       0.64      0.66      0.65     20896
 Tools & Home Improvement       0.61      0.66      0.63     22346
             Toys & Games       0.72      0.70      0.71     21797
              Video Games       0.82      0.79      0.80      6573

                 accuracy                           0.74    374526
                macro avg       0.72      0.71      0.72    374526
             weighted avg       0.73      0.74      0.73    374526
```

## Without using Model2Vec

The embedding model was switched to `baai/bge-base-en-v1.5` without using Model2Vec.

Also, all tests were done without SMOTE.

### NearestCentroid

Performance on training set:
```
                           precision    recall  f1-score   support

          All Electronics       0.34      0.26      0.30     37193
           Amazon Fashion       0.86      0.92      0.89     41581
              Amazon Home       0.54      0.52      0.53     50041
    Arts, Crafts & Sewing       0.70      0.66      0.68     50707
               Automotive       0.77      0.79      0.78     51402
                    Books       0.91      0.89      0.90     48807
           Camera & Photo       0.72      0.82      0.76     25630
Cell Phones & Accessories       0.69      0.80      0.74     41578
                Computers       0.71      0.54      0.62     47127
            Digital Music       0.84      0.93      0.88     33880
                  Grocery       0.91      0.98      0.94     49199
   Health & Personal Care       0.16      0.26      0.20      9774
     Home Audio & Theater       0.41      0.66      0.51     23301
  Industrial & Scientific       0.41      0.56      0.47     38839
              Movies & TV       0.90      0.79      0.84     42305
      Musical Instruments       0.86      0.75      0.80     25225
          Office Products       0.65      0.63      0.64     50199
             Pet Supplies       0.88      0.77      0.82     40117
        Sports & Outdoors       0.66      0.61      0.64     49016
 Tools & Home Improvement       0.60      0.48      0.54     52051
             Toys & Games       0.72      0.64      0.68     50571
              Video Games       0.67      0.85      0.75     15348

                 accuracy                           0.69    873891
                macro avg       0.68      0.69      0.68    873891
             weighted avg       0.70      0.69      0.69    873891
```

Performance on test set:
```
                           precision    recall  f1-score   support

          All Electronics       0.34      0.26      0.30     15685
           Amazon Fashion       0.86      0.92      0.89     18166
              Amazon Home       0.54      0.51      0.52     21321
    Arts, Crafts & Sewing       0.70      0.66      0.68     21849
               Automotive       0.77      0.79      0.78     22032
                    Books       0.92      0.89      0.90     20878
           Camera & Photo       0.72      0.82      0.77     11057
Cell Phones & Accessories       0.69      0.80      0.74     17854
                Computers       0.72      0.54      0.62     20029
            Digital Music       0.84      0.93      0.88     14439
                  Grocery       0.90      0.98      0.94     20985
   Health & Personal Care       0.16      0.27      0.20      4342
     Home Audio & Theater       0.41      0.66      0.51     10100
  Industrial & Scientific       0.41      0.56      0.47     16664
              Movies & TV       0.90      0.79      0.84     18303
      Musical Instruments       0.86      0.76      0.81     10648
          Office Products       0.65      0.63      0.64     21482
             Pet Supplies       0.88      0.77      0.82     17373
        Sports & Outdoors       0.66      0.60      0.63     21161
 Tools & Home Improvement       0.60      0.49      0.54     22307
             Toys & Games       0.72      0.64      0.68     21463
              Video Games       0.67      0.85      0.75      6388

                 accuracy                           0.69    374526
                macro avg       0.68      0.69      0.68    374526
             weighted avg       0.70      0.69      0.69    374526
```

### KNN

Performance on training set:
```
                           precision    recall  f1-score   support

          All Electronics       0.72      0.68      0.70     37193
           Amazon Fashion       0.89      0.96      0.93     41581
              Amazon Home       0.83      0.85      0.84     50041
    Arts, Crafts & Sewing       0.89      0.93      0.91     50707
               Automotive       0.94      0.95      0.94     51402
                    Books       0.96      0.95      0.95     48807
           Camera & Photo       0.88      0.93      0.91     25630
Cell Phones & Accessories       0.87      0.91      0.89     41578
                Computers       0.85      0.86      0.85     47127
            Digital Music       0.94      0.95      0.95     33880
                  Grocery       0.96      0.99      0.97     49199
   Health & Personal Care       0.77      0.42      0.54      9774
     Home Audio & Theater       0.78      0.77      0.77     23301
  Industrial & Scientific       0.86      0.82      0.84     38839
              Movies & TV       0.94      0.92      0.93     42305
      Musical Instruments       0.94      0.95      0.95     25225
          Office Products       0.88      0.87      0.87     50199
             Pet Supplies       0.96      0.98      0.97     40117
        Sports & Outdoors       0.91      0.87      0.89     49016
 Tools & Home Improvement       0.88      0.87      0.88     52051
             Toys & Games       0.92      0.89      0.90     50571
              Video Games       0.93      0.94      0.93     15348

                 accuracy                           0.89    873891
                macro avg       0.89      0.88      0.88    873891
             weighted avg       0.89      0.89      0.89    873891
```

Performance on test set:
```
                           precision    recall  f1-score   support

          All Electronics       0.59      0.56      0.58     15685
           Amazon Fashion       0.86      0.95      0.91     18166
              Amazon Home       0.78      0.79      0.79     21321
    Arts, Crafts & Sewing       0.86      0.90      0.88     21849
               Automotive       0.91      0.93      0.92     22032
                    Books       0.94      0.92      0.93     20878
           Camera & Photo       0.85      0.89      0.87     11057
Cell Phones & Accessories       0.83      0.88      0.85     17854
                Computers       0.79      0.81      0.80     20029
            Digital Music       0.91      0.92      0.92     14439
                  Grocery       0.95      0.99      0.97     20985
   Health & Personal Care       0.62      0.30      0.40      4342
     Home Audio & Theater       0.68      0.67      0.67     10100
  Industrial & Scientific       0.80      0.76      0.78     16664
              Movies & TV       0.90      0.88      0.89     18303
      Musical Instruments       0.93      0.93      0.93     10648
          Office Products       0.83      0.82      0.83     21482
             Pet Supplies       0.95      0.97      0.96     17373
        Sports & Outdoors       0.87      0.82      0.84     21161
 Tools & Home Improvement       0.83      0.82      0.83     22307
             Toys & Games       0.88      0.85      0.87     21463
              Video Games       0.89      0.92      0.90      6388

                 accuracy                           0.85    374526
                macro avg       0.84      0.83      0.83    374526
             weighted avg       0.85      0.85      0.85    374526
```
