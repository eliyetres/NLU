# c) Create a separate data file for test data, containing at least three examples per intent, where the examples differ between training and test set. (In other words, you need to come up with your own examples.) Evaluate the model with the test data. Report the result and include your test data.

from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")

greets_results = []
greets = ["hey",
          "hello",
          "hi",
          "good morning",
          "good evening",
          "hey there",
           "how is everything", "how are things", "hiya"]
for msg in greets:
    greets_results.append(interpreter.parse(msg))

restaurants_results = []
restaurants = ["i'm looking for a place to eat", "I want to grab lunch", "I am searching for a dinner spot", "i'm looking for a place in the [north](location) of town", "show me [chinese](cuisine) restaurants", "show me a [mexican(cuisine) place in the [centre](location)",
               "i am looking for an [indian](cuisine) spot", "search for restaurants", "anywhere in the [west](location)", "anywhere near [18328](location)", "I am looking for [asian fusion](cuisine) food", "I am looking a restaurant in [29432](location)",
               "i'm looking for a place that sells tapas", "show me restaurants close to where I am", "I want to eat vegan food"]

for msg in restaurants:
    restaurants_results.append(interpreter.parse(msg))

goodbyes_results = []
goodbyes = ["thanks!", "thank you", "thx", "thanks very much", "pleasure", "cheers!", "thanks a lot", "I'm really grateful"]

for msg in goodbyes:
    goodbyes_results.append(interpreter.parse(msg))


print(json.dumps(greets_results, indent=2))
print(json.dumps(restaurants_results, indent=2))
print(json.dumps(goodbyes_results, indent=2))