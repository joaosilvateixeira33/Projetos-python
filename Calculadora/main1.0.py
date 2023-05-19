import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.history = []

        self.display = tk.Entry(master, width=30, justify="right", foreground="red", background="black")
        self.display.grid(row=0, column=0, columnspan=4, pady=5)

        # Buttons
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "+"]

        self.buttons = []
        for i in range(len(button_list)):
            self.buttons.append(tk.Button(master, text=button_list[i], width=7, height=2, bg="#38f2e9", foreground="black"))
            row = i // 4 + 1
            column = i % 4
            self.buttons[-1].grid(row=row, column=column, padx=3, pady=3)

        # Bind buttons to functions
        for button in self.buttons:
            button.bind("<Button-1>", self.click)

        # Equal button
        self.equal_button = tk.Button(master, text="=", width=7, height=2, bg="blue", fg="white")
        self.equal_button.grid(row=4, column=3, padx=3, pady=3)
        self.equal_button.bind("<Button-1>", self.calculate)

        # Clear button
        self.clear_button = tk.Button(master, text="C", width=7, height=2, bg="blue", fg="white")
        self.clear_button.grid(row=5, column=0, padx=3, pady=3)
        self.clear_button.bind("<Button-1>", self.clear)

        self.history_button = tk.Button(master, text="History", width=7, height=2, bg="blue", fg="white")
        self.history_button.grid(row=5, column=3, padx=3, pady=3)
        self.history_button.bind("<Button-1>", self.show_history)

        # Scientific calculator button
        self.scientific_button = tk.Button(master, text="Sci", width=7, height=2, bg="blue", fg="white")
        self.scientific_button.grid(row=5, column=1, padx=3, pady=3)
        self.scientific_button.bind("<Button-1>", self.open_scientific_calculator)

        # Backspace button
        self.backspace_button = tk.Button(master, text="⌫", width=7, height=2, bg="blue", fg="white")
        self.backspace_button.grid(row=5, column=2, padx=3, pady=3)
        self.backspace_button.bind("<Button-1>", self.backspace)

    def backspace(self, event):
        current_display = self.display.get()
        new_display = current_display[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, new_display)

    def show_history(self, event):
        history_window = tk.Toplevel(self.master)
        history_window.title("History")

        history_display = tk.Text(history_window, width=30, height=10)
        history_display.pack(padx=5, pady=5)

        for item in self.history:
            history_display.insert(tk.END, item + "\n")

    def click(self, event):
        button = event.widget
        text = button["text"]
        self.display.insert(tk.END, text)

    def calculate(self, event):
        operation = self.display.get()
        try:
            result = str(eval(operation))
        except:
            result = "Error"
        self.display.delete(0, tk.END)
        self.display.insert(0, result)
        self.history.append(operation + " = " + result)

    def clear(self, event):
        self.display.delete(0, tk.END)

    def run(self):
        self.master.mainloop()
    
    def open_scientific_calculator(self, master):
        from scientific_calculator import Calculator2
        self.calculator_window = tk.Toplevel(root)
        self.calculator = Calculator2(self.calculator_window)
        self.calculator.pack()

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="grey")
    calculator = Calculator(root)
    calculator.run()