import tkinter as tk
import random
import json

# Læs data fra JSON-fil
with open('ChatGPT/lande.json', 'r') as f:
    lande_data = json.load(f)

def vælg_tilfældigt_land():
    land = random.choice(lande_data)
    land_navn = land["navn"]
    fordele = ", ".join(land["fordele"])
    ulemper = ", ".join(land["ulemper"])
    
    result_text.set(f"Land: {land_navn}\nFordele: {fordele}\nUlemper: {ulemper}")

# Opret hovedvinduet
root = tk.Tk()
root.title("Tilfældigt Land Vælger")

result_text = tk.StringVar()

# Opret og placer en knap
button = tk.Button(root, text="Vælg et tilfældigt land", command=vælg_tilfældigt_land)
button.pack(pady=20)

# Opret og placer en label for at vise resultatet
result_label = tk.Label(root, textvariable=result_text, justify="left", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start GUI'en
root.mainloop()
