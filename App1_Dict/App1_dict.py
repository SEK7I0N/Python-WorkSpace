import json
from difflib import get_close_matches

dictDataPath = "data.json"
data = json.load(open(dictDataPath))

def definition(word):
    if word in data:
        return data[word]
    if len(get_close_matches(word,data.keys(),cutoff=0.75)) > 0:
        closestMatch = get_close_matches(word,data.keys())[0]
        userConfirm = input("Did you mean %s insted?(Y/N):" % closestMatch)
        if userConfirm.lower() == "y":
            return data[closestMatch]
    return "Incorrect word!"

word = input("Enter word: ")

output = definition(word.lower())
if type(output) == list:
    for item in output:
        print("* ",item)
else:
    print(output)