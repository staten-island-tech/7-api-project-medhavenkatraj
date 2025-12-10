""" https://uselessfacts.jsph.pl/ -> website api """
""" 
https://uselessfacts.jsph.pl/random.json
 """

import requests

def getRandom_fact():
    response = requests.get(f"https://uselessfacts.jsph.pl/random.json")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return data

random = getRandom_fact()
for key, value in random.items():
    print(f"{key.title()}: {value}")

import tkinter as tk

window = tk.Tk()
window.title("Random Facts! ")
window.geometry("400x250")
window.resizable(False, False)

prompt = tk.Label(window, text="Want to see a random fun fact? ",
font=("Arial", 14))
prompt.pack(pady=10)