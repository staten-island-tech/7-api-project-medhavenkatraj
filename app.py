""" https://uselessfacts.jsph.pl/ -> website api """
""" 
https://uselessfacts.jsph.pl/random.json
 """


import requests
import tkinter as tk


def getRandom_fact():
    response = requests.get(f"https://uselessfacts.jsph.pl/random.json")
    return response.json()


def check():
    if entry.get() == fact:
        result_label.configure(text="Correct!")
    else:
        result_label.configure(text="Try again…")


fact = getRandom_fact()
reversed_fact = fact[::-1]




window = tk.Tk()
window.title("Reverse the Fact")


tk.Label(window, text = "guess the reversed fun fact ").pack()


tk.Label(window, text = reversed_fact, wraplength = 300).pack(pady = 10)


entry = tk.Entry(window, width=40)
entry.pack()


tk.Button(window, text = "Check", command=check).pack(pady = 10)


result_label = tk.Label(window, text = "")
result_label.pack()


window.mainloop()












