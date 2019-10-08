import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
   w = w.lower()
   if w in data:
      return data[w]
   elif w.title() in data:
      return data[w.title()]
   elif w.upper() in data:
      return data[w.upper()]
   elif len(get_close_matches(w, data.keys())) > 0:
      yn = input("Did you mean %s that instead? Enter Y if yes, or N if no." % get_close_matches(w, data.keys())[0])
      yn = yn.upper()
      if yn == "Y":
         return data[get_close_matches(w, data.keys())[0]]
      elif yn == "N":
         return "The Word doesn't exist. Please double check."
      else:
         return "We didn't understand your entry."
   else:
      return "The Word doesnt exist. Please double check."

word = input("Enter Word : ")
output = translate(word)
if type(output) == list: 
   for item in output:
      print(item)
else:
   print(output)