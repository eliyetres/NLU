# Lab 1
## Task 1: Perform Rasa NLU’s tutorial

Using the ”spacy_sklearn” pipeline.

## Task 2: Evaluate NLU exploratively
The NLU result for the utterance ”hello there” and include the whole output in the lab report. 

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
good day: a greet with a confidence 0.60
howdy: a greet with a confidence of 0.86
hiya: a greeting with a confidence of 0.89

### b) Find and report at least 3 utterances whose intent is incorrectly classified despite expressing the respective intent.
greetings: a thankyou with a confidence  0.54 
what's up: restaurant_search with a confidence of 0.63 and a greenting of only  0.19
long time no see: restaurant_search with a confidence of 0.59 and greeting of only 0.2

### c) Explore how intent classification behaves when utterances expressing other intents than in the training data are parsed, e.g. an intent from a travel agency or tech support domain. Report your findings.

### d) Look at the confidence scores for a classification result. What is their sum? Try with at least two different classifications. Can you see any problem with the sum of the scores, in the context of dialogue systems?


## Task 3: Measure NLU performance

### a) Evaluate your trained model with the training data as test data. Report the result (precision, recall, F1) and describe what the confusion matrix looks like.

### b) Try to say something about the usefulness and relevance of what was done in the previous step. How useful is it to test a model with the same data that it’s been trained on?

### c) Create a separate data file for test data, containing at least three examples per intent, where the examples differ between training and test set. (In other words, you need to come up with your own examples.) Evaluate the model with the test data. Report the result and include your test data.



## Task 4: Improve NLU performance

In task 2, and perhaps also task 3, some shortcomings of the model were hopefully discovered.

Adress  shortcomings of the model in task 2 and 3 by modifying or extending the training data. (E.g. you can add examples or insert new intents.)

Try to validate the improvements by measuring performance as in task 3. Report the shortcomings, describe how you tried to address them, and how it went.

## Task 5: Analyze a specific problem

Compare the intent classification results for ”good bye” vs ”bye good” and report your findings. You may agree with me that there’s some kind of problem here… (If not, feel free to discuss this in the report.)

Try to find the cause of the problem. (You may want to look at the lecture slides and/or the source code for Rasa NLU.)

How could one go about to address the problem? You don’t need to solve it here and now, but try to find one or more directions one could take, and briefly discuss it/them.

 

Your submission for this lab should include a report where you include the results of the tasks (output) and your discussion around them when applicable. Additionally, you should include your train and test data.