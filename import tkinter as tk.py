

import tkinter as tk
from tkinter import messagebox
from math import gcd

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(plaintext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    ciphertext = ""
    for char in plaintext.upper():
        if char.isalpha():
            ciphertext += chr(((a * (ord(char) - 65) + b) % 26) + 65)
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    a_inv = mod_inverse(a, 26)
    plaintext = ""
    for char in ciphertext.upper():
        if char.isalpha():
            plaintext += chr(((a_inv * ((ord(char) - 65) - b)) % 26) + 65)
        else:
            plaintext += char
    return plaintext

def on_encrypt():
    try:
        plaintext = plaintext_entry.get()
        a = int(a_entry.get())
        b = int(b_entry.get())
        if gcd(a, 26) != 1:
            raise ValueError("Key 'a' must be coprime with 26.")
        ciphertext = affine_encrypt(plaintext, a, b)
        output_label.config(text=f"Ciphertext: {ciphertext}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def on_decrypt():
    try:
        ciphertext = plaintext_entry.get()
        a = int(a_entry.get())
        b = int(b_entry.get())
        if gcd(a, 26) != 1:
            raise ValueError("Key 'a' must be coprime with 26.")
        plaintext = affine_decrypt(ciphertext, a, b)
        output_label.config(text=f"Plaintext: {plaintext}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the GUI window
root = tk.Tk()
root.title("Affine Cipher")

# Input fields
tk.Label(root, text="Text:").grid(row=0, column=0, padx=5, pady=5)
plaintext_entry = tk.Entry(root, width=30)
plaintext_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Key (a):").grid(row=1, column=0, padx=5, pady=5)
a_entry = tk.Entry(root, width=10)
a_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Key (b):").grid(row=2, column=0, padx=5, pady=5)
b_entry = tk.Entry(root, width=10)
b_entry.grid(row=2, column=1, padx=5, pady=5)

# Buttons
encrypt_button = tk.Button(root, text="Encrypt", command=on_encrypt)
encrypt_button.grid(row=3, column=0, padx=5, pady=5)

decrypt_button = tk.Button(root, text="Decrypt", command=on_decrypt)
decrypt_button.grid(row=3, column=1, padx=5, pady=5)

# Output
output_label = tk.Label(root, text="", fg="blue")
output_label.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

# Run the GUI loop
root.mainloop()
