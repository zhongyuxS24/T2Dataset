# T2Dataset
Dataset work for T2 Group Project
Detailed instructions see [here](https://docs.google.com/document/d/1iduLlFGqdM2pvGRIb5trPfOvfFdJDLqHqlN7Q2dW-pk/edit).

## Dataset
We are currently targeting the Google Play Store User Reivews from [here](https://www.kaggle.com/datasets/lava18/google-play-store-apps?resource=download).

## Output
There will be three datasets output, in total, at different granularity level: document, sentence, and EDU.

## Task Breakdown
- Organzie data into format of:
    - Document: DATA | Sentiment
    - Sentence and EDU: using RST parser
- Remove duplicate segments.
- Remove simple data of length 1. DONE