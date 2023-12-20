import tkinter as tk
from tkinter import ttk
from tkinter import *


class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x280")
        self.style = ttk.Style()
        self.style = ttk.Style()
        self.style.configure(
            "TButton", font=("Arial", 19), height=5, width=6, background=("white")
        )
        self.label = tk.Label(text="This calculator was made by Tamim")
        self.label.pack(padx=5, pady=5)
        # Text Area
        self.textbox = tk.Text(
            self.root, font=("Arial", 20), height=2, background="darkgreen"
        )
        self.textbox.pack(padx=12, pady=12)
        # Buttons
        self.buttonframe = tk.Frame(self.root)
        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)
        self.buttonframe.rowconfigure(0, weight=1)
        self.buttonframe.rowconfigure(1, weight=1)
        self.buttonframe.rowconfigure(2, weight=1)
        self.buttonframe.rowconfigure(3, weight=1)

        self.variable = tk.IntVar()

        self.btn1 = ttk.Button(
            self.buttonframe,
            text="1",
            command=lambda: self.click(1),
        )
        self.btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.btn2 = ttk.Button(
            self.buttonframe, text="2", command=lambda: self.click(2)
        )
        self.btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.btn3 = ttk.Button(
            self.buttonframe, text="3", command=lambda: self.click(3), style="TButton"
        )
        self.btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

        self.plusbtn = ttk.Button(
            self.buttonframe, text="+", command=lambda: self.click("+"), style="TButton"
        )
        self.plusbtn.grid(row=0, column=3, sticky=tk.W + tk.E)

        self.btn4 = ttk.Button(
            self.buttonframe, text="4", command=lambda: self.click(4), style="TButton"
        )
        self.btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

        self.btn5 = ttk.Button(
            self.buttonframe, text="5", command=lambda: self.click(5), style="TButton"
        )
        self.btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

        self.btn6 = ttk.Button(
            self.buttonframe, text="6", command=lambda: self.click(6), style="TButton"
        )
        self.btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

        self.minusbtn = ttk.Button(
            self.buttonframe, text="-", command=lambda: self.click("-"), style="TButton"
        )
        self.minusbtn.grid(row=1, column=3, sticky=tk.W + tk.E)

        self.btn7 = ttk.Button(
            self.buttonframe, text="7", command=lambda: self.click(7), style="TButton"
        )
        self.btn7.grid(row=2, column=0, sticky=tk.W + tk.E)

        self.btn8 = ttk.Button(
            self.buttonframe, text="8", command=lambda: self.click(8), style="TButton"
        )
        self.btn8.grid(row=2, column=1, sticky=tk.W + tk.E)

        self.btn9 = ttk.Button(
            self.buttonframe, text="9", command=lambda: self.click(9), style="TButton"
        )
        self.btn9.grid(row=2, column=2, sticky=tk.W + tk.E)

        self.multiplybtn = ttk.Button(
            self.buttonframe, text="*", command=lambda: self.click("*"), style="TButton"
        )
        self.multiplybtn.grid(row=2, column=3, sticky=tk.W + tk.E)

        self.btn0 = ttk.Button(
            self.buttonframe, text="0", command=lambda: self.click(0), style="TButton"
        )
        self.btn0.grid(row=3, column=0, columnspan=2, sticky=tk.W + tk.E)

        self.equalbtn = ttk.Button(
            self.buttonframe, text="=", command=lambda: self.click("="), style="TButton"
        )
        self.equalbtn.grid(row=3, column=2, sticky=tk.W + tk.E)

        self.dividebtn = ttk.Button(
            self.buttonframe, text="/", command=lambda: self.click("/"), style="TButton"
        )
        self.dividebtn.grid(row=3, column=3, sticky=tk.W + tk.E)

        self.restartbutton = ttk.Button(self.root, text="Restart", command=self.restart)
        self.restartbutton.pack(padx=6, pady=6)

        self.buttonframe.pack(pady=10)
        # End of the loop
        self.root.mainloop()

    def click(self, arg):
        keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMOPQRSTUVWXYZ!@#$%^&()_?"
        current_text = self.textbox.get("1.0", "end-1c").strip(keys)
        if isinstance(arg, str):
            if arg == "=":
                try:
                    result = eval(current_text)
                    self.textbox.delete("1.0", tk.END)
                    self.textbox.insert(tk.END, str(result))
                except Exception as e:
                    if any(char.isalpha() for char in current_text):
                        self.textbox.delete("1.0", tk.END)
                        self.textbox.insert(tk.END, "Error")
            else:
                current_text += arg
                self.textbox.delete("1.0", tk.END)
                self.textbox.insert(tk.END, current_text)
        else:
            current_text += str(arg)
            self.textbox.delete("1.0", tk.END)
            self.textbox.insert(tk.END, current_text)

    def points(self, args) -> str:
        """This function handles button presses that are not equal signs."""
        current_text = self.textbox.get("1.0", "end-1c").strip()

        # Remove consecutive occurrences of specific symbols
        for char in "+=-/":
            current_text = current_text.replace(char * 2, "")

        # Append the argument to the current text
        current_text += str(args)

        # Update the text box with the new current text
        self.textbox.delete("1.0", tk.END)
        self.textbox.insert(tk.END, current_text)

    def restart(self):
        if self.restartbutton:
            self.textbox.delete("1.0", tk.END)


Calculator()
