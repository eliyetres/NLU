from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
results = []
messages = ["hello there", "hi", "hey", "greetings", "salutations", "good morning", "good day", "what's up", "good to see you", "long time no see", "how do you do", "howdy", "how have you been", "yo", "pleasure to meet you", "g'day", "how is it going", "how are you", "how is everything", "how are things", "hiya"]
for msg in messages:
    results.append(interpreter.parse(msg))

print(json.dumps(results, indent=2))