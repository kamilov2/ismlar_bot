import tkinter as tk
from db import get_data_from_db, search_meaning_name
def reverse_word():
    input_text = entry.get()
    reversed_text = search_meaning_name(input_text)
    if reversed_text:
        result_label.config(text=f"{input_text} ism ning manosi: {reversed_text[0]}")
    else: 
        result_label.config(text="Bunday ism mavjud emas !")

root = tk.Tk()
root.title("Ismlar manosi")

entry = tk.Entry(root, width=50)
entry.pack(pady=20)

reverse_button = tk.Button(root, text="Ism Manosini bilish", command=reverse_word)
reverse_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()