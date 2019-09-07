from rasa_nlu.model import Interpreter
import json
interpreter = Interpreter.load("./models/current/nlu")
results = []
messages = ["i would like to travel from gothenburg to london", "book a flight to marrakesh tomorrow", "book a train to copenhagen leaving tomorrow", "i want to go to oslo tomorrow by bus"]
for msg in messages:
    results.append(interpreter.parse(msg))

print(json.dumps(results, indent=2))