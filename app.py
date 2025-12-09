""" https://uselessfacts.jsph.pl/ -> website api """
""" 
https://uselessfacts.jsph.pl/random.json
 """

import requests

def getRandom_fact(fact):
    response = requests.get(f"https://uselessfacts.jsph.pl/random.json")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return data 

fact = getRandom_fact()
for key, value in fact.items():
    print(key, "→", value)
print(fact)







""" {
        "fact": data["fact"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    } """