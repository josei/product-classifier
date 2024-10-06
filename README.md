# Product Classifier

Machine learning model that can classify Amazon products.

## Usage

Docker is required to run the application as a container (Python 3.11 and Pipenv are required if not using Docker).

Additionally, the dataset is too large to be included in the repository. It needs to be downloaded first and included in the `data` folder. You can download the dataset from [this Google Drive link](https://drive.google.com/file/d/1Zf0Kdby-FHLdNXatMP0AD2nY0h-cjas3/view?usp=sharing).

To build the Docker image:

```bash
docker build -t product-classifier .
```

To run the container:

```bash
docker run --rm -it -p 8000:8000 product-classifier
```

This will show the help and the different commands to run: `train`, `test` and `start`.

Usage without Docker:

```bash
pipenv run python src/cli.py
```

### Training

This step can be skipped, as the model comes pre-trained with this repository. To train the model:

```bash
docker run --rm -it -v `pwd`/data:/usr/src/app/data -v `pwd`/models:/usr/src/app/models -p 8000:8000 product-classifier train
```

This will prepare the training and test data and replace any existing model after training.

One volume is mounted to persist the model between runs and another one so that the container has access to the dataset. You might want to rebuild the image after retraining the model, or manage volumes in a way to ensure the new model is used.

### Testing

To test the model:

```bash
docker run --rm -it -v `pwd`/data:/usr/src/app/data -v `pwd`/models:/usr/src/app/models -p 8000:8000 product-classifier test
```

### Running the API's server

To run the server that listens for requests at `0.0.0.0:8000`:

```bash
docker run --rm -it -v `pwd`/models:/usr/src/app/models -p 8000:8000 product-classifier start
```

Once running, the full OpenAPI specification is available at http://localhost:8000/openapi.json.

Here's an example of request:

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
   "also_buy" : [
      "B00VPDB9C4",
      "B00UH8KUMS"
   ],
   "also_view" : [],
   "asin" : "B00V7UNF4K",
   "brand" : "JOTO",
   "description" : [
      "Case Compatibility: Compatible with iPhone 8/7, iPhone 6s/6, Samsung Galaxy S7, S6, HTCM9, Google Pixel, Pixel 2DO NOT support Touch ID"
   ],
   "feature" : [
      "Compatible with iPhone 8/7, iPhone 6s/6, Samsung Galaxy S7, S6, HTCM9, Google Pixel, Pixel 2DO NOT support Touch ID",
      "Features: Built in key holder, ID/Credit Card/Cash Holder and earphone jack openings",
      "Quality Materials: Made from premium lightweight neoprene; sweat proof, durable and protects your device all around",
      "Full Touchscreen Compatibility: Clear protective screen window offers full function of your phone",
      "Adjustable Size: Strong elastic hook & loop with two positioning slots fits a variety of arm circumference sizes 9.5\"-16\""
   ],
   "image" : [
      "https://images-na.ssl-images-amazon.com/images/I/51b27PwTSIL._SX38_SY50_CR,0,0,38,50_.jpg",
      "https://images-na.ssl-images-amazon.com/images/I/51eNk9fgWbL._SX38_SY50_CR,0,0,38,50_.jpg",
      "https://images-na.ssl-images-amazon.com/images/I/51KxBnu9mqL._SX38_SY50_CR,0,0,38,50_.jpg",
      "https://images-na.ssl-images-amazon.com/images/I/51vpwUkq-ZL._SX38_SY50_CR,0,0,38,50_.jpg"
   ],
   "price" : "$8.99",
   "title" : "Running Armband for iPhone 8, 7, 6, 6s, Samsung Galaxy S6, S7, HTCM9, Google Pixel, Pixel 2, JOTO Phone Sport Arm Case Cover Pouch with Key Holder for Gym Jogging Walking Workout and Exercise &ndash;Black"
}'
```

Response:
```bash
{
  "main_cat": "Cell Phones & Accessories"
}
```

# Performance

The model was trained using a 70/30 split of training/test data. Only the `brand`, `description`, `title`, `feature`, and `price` fields are used as input features. The textual input features (all but `price`) are preprocessed using a sentence transformer to produce embeddings. The resulting vector is enriched with the price dimension and centroids for each main category are computed (i.e., a nearest centroid classifier is used). At inference time, the output class is obtained by finding the nearest centroid to the enriched vector.

Additional notes:
- [Model2Vec](https://github.com/MinishLab/model2vec) is used to increase the speed of the embedding model while reducing the memory footprint. Applying a standard embedding model as is was too slow with the dataset's size and the machine used (Apple M1 Pro), so testing this novel approach seemed like a promising path to explore before checking final performance. One of the author's already distilled embeddings model was used (`M2V_base_output`).
- The `price` field is normalised to 0 mean and 1 std. This field is very messy in the dataset, and only some basic parsing has been implemented (the format like `$12.99` is expected and parsed into `12.99`, with every other formatting being set to 0). This leaves room for improvement to be able to capture the price of more samples.
- The `also_buy`, `also_view`, and `asin` fields are not used as input features. They could potentially be used to enrich the embedding vector (and increase the performance on the test data set), but they'd be too specific to the given data set and would not generalize well to unseen data, where new ASINs and products would show up.
- For simplicity, the `image` field is not used as input feature, but it has the potential to be considered by using a vision model. One way would be an image-to-text model to produce a textual description of the image, which could then be included as part of the description.
- To ensure nearest centroid classification works as expected with under-represented categories, the dataset is balanced by oversampling the least common categories using [SMOTE](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html). As the dataset is not particularily imbalanced, this did not significantly improve performance, but ensures the nearest centroid classifier works as expected and prepares the model for classification of the full category tree if desired in the future.

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
