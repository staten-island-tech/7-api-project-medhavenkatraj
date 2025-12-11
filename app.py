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
window.geometry("450x250")
window.resizable(False, False)

prompt = tk.Label(window, text="Want to see a random fun fact? ",
font=("Arial", 14))
prompt.pack(pady=10)

result_label = tk.Label(window, text =" ", font = ("Arial", 14, "bold"), fg = "blue")
result_label.pack(pady=15)


def reverse_message():
    text = entry.get()
    reversed_text = text[::-1] 
    result_label.config(text=f"Backwards: {reversed_text}")
reverse_button = tk.Button(window, text="Reverse Message!",
font=("Arial", 14),
command=reverse_message)
reverse_button.pack(pady=10)
window.mainloop()