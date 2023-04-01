import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.title("PyIDE 1.0")
root.geometry("1000x600")
root.resizable(False, False)

# function to open file
def open_file():
    file_path = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if file_path:
        with open(file_path, "r") as file:
            code_box.delete("1.0", "end")
            code_box.insert("1.0", file.read())

# function to save file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(code_box.get("1.0", "end"))

# function to run code
def run_code():
    code = code_box.get("1.0", "end")
    with open("temp.py", "w") as file:
        file.write(code)
    os.system("python temp.py")

# create textbox for code
code_box = tk.Text(root, font=("Segoe UI", 10))
code_box.pack(fill="both", expand=True)

# create frame for buttons
button_frame = tk.Frame(root, bg="black")
button_frame.pack(fill="x")

# create open button
open_button = tk.Button(button_frame, text="Open", bg="white", fg="black", font=("Segoe UI", 10), command=open_file)
open_button.pack(side="left", padx=5, pady=5)

# create save button
save_button = tk.Button(button_frame, text="Save", bg="white", fg="black", font=("Segoe UI", 10), command=save_file)
save_button.pack(side="left", padx=5, pady=5)

# create run button
run_button = tk.Button(button_frame, text="Run", bg="white", fg="black", font=("Segoe UI", 10), command=run_code)
run_button.pack(side="left", padx=5, pady=5)

# add trademark
trademark_label = tk.Label(root, text="Created by r00ted63", font=("Segoe UI", 10), bg="black", fg="white")
trademark_label.pack(side="bottom", fill="x")

root.mainloop()
