# Lab 1
## Task 1: Perform Rasa NLU’s tutorial

Build a model using the ”spacy_sklearn” pipeline.

## Task 2: Evaluate NLU exploratively
The NLU result for the utterance "hello there" and include the whole output in the lab report. 

```json
{
  "intent": {
    "name": "greet",
    "confidence": 0.7700637180687561
  },
  "entities": [],
  "intent_ranking": [
    {
      "name": "greet",
      "confidence": 0.7700637180687561
    },
    {
      "name": "restaurant_search",
      "confidence": 0.14459522386640253
    },
    {
      "name": "thankyou",
      "confidence": 0.08534105806484113
    }
  ],
  "text": "hello there"
}
```

### a) Find and report at least 3 utterances whose intent is correctly classified despite not being in the training data.
good day: Classified as greet with a confidence 0.60.

howdy: Classified as greet with a confidence of 0.86.

hiya: Classified as greet with a confidence of 0.89.

### b) Find and report at least 3 utterances whose intent is incorrectly classified despite expressing the respective intent.
greetings: Classified as thankyou with a confidence of 0.54.

what's up: Classified as restaurant_search with a confidence of 0.63. The confidence for a greenting was only  0.19.

long time no see: restaurant_search with a confidence of 0.59 and greeting of 0.25.


### c) Explore how intent classification behaves when utterances expressing other intents than in the training data are parsed, e.g. an intent from a travel agency or tech support domain. Report your findings.

Trying different utterances with the intent of travel, they all showed a very high confidence in restaurant_search. All utterances had a confidence level of somewhere between 0.80-0.85. The last sentence includes the words "i want", which is in the training data, but this is the also the utterance that got the lowest confidence of being a restaurant search of them all (0.80).

"i would like to travel from gothenburg to london"

"book a flight to marrakesh tomorrow"

"book a train to copenhagen leaving tomorrow"

"i want to go to oslo tomorrow by bus"


### d) Look at the confidence scores for a classification result. What is their sum? Try with at least two different classifications. Can you see any problem with the sum of the scores, in the context of dialogue systems?

They always sum up to 1.
One problem with this could be that if the user says something that doesn't really match anything in the training data, one of the categories might still have a very high confidence score.
 

## Task 3: Measure NLU performance

### a) Evaluate your trained model with the training data as test data. Report the result (precision, recall, F1) and describe what the confusion matrix looks like.

#### Results
```console
2019-09-07 15:25:02 INFO     rasa_nlu.training_data.training_data  - Training data stats:
        - intent examples: 22 (3 distinct intents)
        - Found intents: 'greet', 'thankyou', 'restaurant_search'
        - entity examples: 8 (2 distinct entities)
        - found entities: 'location', 'cuisine'

2019-09-07 15:25:02 INFO     __main__  - Intent evaluation results:
2019-09-07 15:25:02 INFO     __main__  - Intent Evaluation: Only considering those 22 examples that have a defined intent out of 22 examples
2019-09-07 15:25:02 INFO     __main__  - F1-Score:  1.0
2019-09-07 15:25:02 INFO     __main__  - Precision: 1.0
2019-09-07 15:25:02 INFO     __main__  - Accuracy:  1.0
2019-09-07 15:25:02 INFO     __main__  - Classification report:
                   precision    recall  f1-score   support

            greet       1.00      1.00      1.00         6
restaurant_search       1.00      1.00      1.00        12
         thankyou       1.00      1.00      1.00         4

        micro avg       1.00      1.00      1.00        22
        macro avg       1.00      1.00      1.00        22
     weighted avg       1.00      1.00      1.00        22

2019-09-07 15:25:02 INFO     __main__  - Your model made no errors
```

It wasn't possible to show the confusion matrix, the code gave pyploy errors.

### b) Try to say something about the usefulness and relevance of what was done in the previous step. How useful is it to test a model with the same data that it’s been trained on?

When the model trains it makes a generilization of the data that is later used to apply to new data. The purpose of the model thus is to be able to evaluate on a set of data that the model has never encountered before. If the model is trained on the same set as the test data, it's naturally expected to perform very well. 

### c) Create a separate data file for test data, containing at least three examples per intent, where the examples differ between training and test set. (In other words, you need to come up with your own examples.) Evaluate the model with the test data. Report the result and include your test data.

The model predicted the utterances "how is everything" and "how are things" falsely as restaurant searches.

#### Results
```console
2019-09-07 16:25:29 INFO     rasa_nlu.training_data.training_data  - Training data stats:
        - intent examples: 31 (3 distinct intents)
        - Found intents: 'restaurant_search', 'greet', 'thankyou'
        - entity examples: 9 (2 distinct entities)
        - found entities: 'location', 'cuisine'

2019-09-07 16:25:30 INFO     __main__  - Intent evaluation results:
2019-09-07 16:25:30 INFO     __main__  - Intent Evaluation: Only considering those 31 examples that have a defined intent out of 31 examples
2019-09-07 16:25:30 INFO     __main__  - F1-Score:  0.9334677419354839
2019-09-07 16:25:30 INFO     __main__  - Precision: 0.9430740037950663
2019-09-07 16:25:30 INFO     __main__  - Accuracy:  0.9354838709677419
2019-09-07 16:25:30 INFO     __main__  - Classification report:
                   precision    recall  f1-score   support

            greet       1.00      0.78      0.88         9
restaurant_search       0.88      1.00      0.94        15
         thankyou       1.00      1.00      1.00         7

        micro avg       0.94      0.94      0.94        31
        macro avg       0.96      0.93      0.94        31
     weighted avg       0.94      0.94      0.93        31

2019-09-07 16:25:30 INFO     __main__  - Model prediction errors saved to errors.json.

```

#### Errors
```json
[
    {
        "text": "how is everything",
        "intent": "greet",
        "intent_prediction": {
            "name": "restaurant_search",
            "confidence": 0.5607080096703879
        }
    },
    {
        "text": "how are things",
        "intent": "greet",
        "intent_prediction": {
            "name": "restaurant_search",
            "confidence": 0.552662688499982
        }
    }
]
```

## Task 4: Improve NLU performance

### In task 2, and perhaps also task 3, some shortcomings of the model were hopefully discovered. Adress  shortcomings of the model in task 2 and 3 by modifying or extending the training data. (E.g. you can add examples or insert new intents.) Try to validate the improvements by measuring performance as in task 3. Report the shortcomings, describe how you tried to address them, and how it went.

For this test I added the labels travel and support. The training data and the test data included different utterances.
The errors were mosly for greetings, many of them were different from anything in the training data. The model correctly predicted the restaurant searches and the travel utterances. A reason for this might be because they all had "keywords" like cities or technology that was present in the training data. 

#### Results
```console
2019-09-07 18:15:17 INFO     __main__  - F1-Score:  0.5670048905343023
2019-09-07 18:15:17 INFO     __main__  - Precision: 0.7984126984126984
2019-09-07 18:15:17 INFO     __main__  - Accuracy:  0.6153846153846154
2019-09-07 18:15:17 INFO     __main__  - Classification report:
                   precision    recall  f1-score   support

            greet       1.00      0.22      0.36        18
restaurant_search       0.70      1.00      0.82         7
          support       0.33      1.00      0.50         4
         thankyou       0.67      0.80      0.73         5
           travel       0.71      1.00      0.83         5

        micro avg       0.62      0.62      0.62        39
        macro avg       0.68      0.80      0.65        39
     weighted avg       0.80      0.62      0.57        39

2019-09-07 18:15:17 INFO     __main__  - Model prediction errors saved to errors.json.

```
#### Errors
```json
[
    {
        "text": "greetings",
        "intent": "greet",
        "intent_prediction": {
            "name": "thankyou",
            "confidence": 0.4538480806235871
        }
    },
    {
        "text": "salutations",
        "intent": "greet",
        "intent_prediction": {
            "name": "thankyou",
            "confidence": 0.4538480806235871
        }
    },
    {
        "text": "what's up",
        "intent": "greet",
        "intent_prediction": {
            "name": "support",
            "confidence": 0.33754388555834086
        }
    },
    {
        "text": "good to see you",
        "intent": "greet",
        "intent_prediction": {
            "name": "restaurant_search",
            "confidence": 0.26562033219926634
        }
    },
    {
        "text": "long time no see",
        "intent": "greet",
        "intent_prediction": {
            "name": "support",
            "confidence": 0.3174024515691371
        }
    },
    {
        "text": "how do you do",
        "intent": "greet",
        "intent_prediction": {
            "name": "support",
            "confidence": 0.6947155318123337
        }
    },
    {
        "text": "how have you been",
        "intent": "greet",
        "intent_prediction": {
            "name": "support",
            "confidence": 0.5444939505765036
        }
    },
    {
        "text": "yo",
        "intent": "greet",
        "intent_prediction": {
            "name": "restaurant_search",
            "confidence": 0.38069058253703314
        }
    },
    {
        "text": "pleasure to meet you",
        "intent": "greet",
        "intent_prediction": {
            "name": "travel",
            "confidence": 0.3970635142520535
        }
    },
    {
        "text": "g'day",
        "intent": "greet",
        "intent_prediction": {
            "name": "travel",
            "confidence": 0.4456319610599197
        }
    },
    {
        "text": "how is it going",
        "intent": "greet",
        "intent_prediction": {
            "name": "support",
            "confidence": 0.5581139667074168
        }
    },
    {
        "text": "how are you",
        "intent": "greet",
        "intent_prediction": {
            "name": "support",
            "confidence": 0.5366836886675658
        }
    },
    {
        "text": "how is everything",
        "intent": "greet",
        "intent_prediction": {
            "name": "support",
            "confidence": 0.5960938761822976
        }
    },
    {
        "text": "how are things",
        "intent": "greet",
        "intent_prediction": {
            "name": "support",
            "confidence": 0.5455137370634604
        }
    },
    {
        "text": "pleasure",
        "intent": "thankyou",
        "intent_prediction": {
            "name": "restaurant_search",
            "confidence": 0.2875344955821086
        }
    }
]

```

## Task 5: Analyze a specific problem

## Compare the intent classification results for ”good bye” vs ”bye good” and report your findings. You may agree with me that there’s some kind of problem here… (If not, feel free to discuss this in the report.) Try to find the cause of the problem. (You may want to look at the lecture slides and/or the source code for Rasa NLU.) How could one go about to address the problem? You don’t need to solve it here and now, but try to find one or more directions one could take, and briefly discuss it/them. 


The utterances gives the exact same confidence level, there is no difference in how the model evaluates them. This shows that the model only trains word by word, and is not interpreting the utterance "good bye" as one entity. This is  a problem because "bye good" is obviously not the same thing as "good bye". "Good bye" should be evaluated as one entity, and since it's already in the training data, the utterance should have a higher confidence level than "bye good". The full utterances present in the training data should be treated as a larger entity (eg. bigram, trigram or just the full word combination) and produce a higher confidence level, but single words should also be evaluated separatley, so that "bye good" still gives a higher confidence for the label that they exists in, but lower than an exact match.

```json
{
  "intent": {
    "name": "bye",
    "confidence": 0.509759085168469
  },
  "entities": [],
  "intent_ranking": [
    {
      "name": "bye",
      "confidence": 0.509759085168469
    },
    {
      "name": "greet",
      "confidence": 0.28607156518620896
    },
    {
      "name": "thankyou",
      "confidence": 0.20416934964532185
    }
  ],
  "text": "bye good"
}
{
  "intent": {
    "name": "bye",
    "confidence": 0.509759085168469
  },
  "entities": [],
  "intent_ranking": [
    {
      "name": "bye",
      "confidence": 0.509759085168469
    },
    {
      "name": "greet",
      "confidence": 0.28607156518620896
    },
    {
      "name": "thankyou",
      "confidence": 0.20416934964532185
    }
  ],
  "text": "good bye"
}

```
