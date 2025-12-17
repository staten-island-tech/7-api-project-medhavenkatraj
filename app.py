""" """ """ https://uselessfacts.jsph.pl/ -> website api """
""" 
https://uselessfacts.jsph.pl/random.json """
 """"""

""" 
import requests
import tkinter as tk """

""" def check():
    if entry.get() == fact:
        result_label.config(text = "correct!")
    else:
        result_label.config(text = "try again…")

def getRandom_fact():
    response = requests.get(f"https://uselessfacts.jsph.pl/random.json")
    x = response.json()
    return  x["text"]


fact = getRandom_fact()
print(fact)

reversed_fact = fact[:: -1]

window = tk.Tk()

window.title("reverse the fact")
tk.Label(window, text = "guess the reversed fun fact ").pack()
tk.Label(window, text = reversed_fact, wraplength = 300).pack(pady = 10)
entry = tk.Entry(window, width = 40)
entry.pack()
tk.Button(window, text = "check", command = check).pack(pady = 10)
result_label = tk.Label(window, text = "")
result_label.pack()


window.mainloop() """""


import requests
import tkinter as tk

def check():
    if entry.get() == fact:
        result_label.config(text = "correct!")
    else:
        result_label.config(text = "try again…")
def getRandom_fact():
    response = requests.get(f"https://uselessfacts.jsph.pl/random.json")
    x = response.json()
    return  x["text"]


title_font = ("Arial", 60)
text_font = ("Arial", 25)
result_font = ("Arial", 30)

fact = getRandom_fact()
print(fact)

reversed_fact = fact[:: -1]

window = tk.Tk()
window.title("reverse the fact")
window.configure(bg="lightblue")


tk.Label(
window, 
text = "guess the reversed fun fact ",
Font = title_font
Bg = “purple”
).pack(pady = 10 )

tk.Label(
    window,
    text=reversed_fact,
    wraplength=300,
    font=text_font,
    bg="lightblue"
).pack(pady=10)

entry = tk.Entry(
    window,
    width=40,
    font=("Arial", 12)
)
entry.pack(pady=5)

tk.Button(
    window,
    text="Check",
    command=check,
    font=("Phenomena", 12),
    bg="white"
).pack(pady=10)


result_label = tk.Label(
    window,
    text="",
    font=result_font,
    bg="lightblue"
)
result_label.pack()

window.mainloop()












