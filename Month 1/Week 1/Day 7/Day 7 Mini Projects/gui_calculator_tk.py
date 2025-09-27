import tkinter as tk
from tkinter import messagebox
import calculator_extended as calc  # Import your extended calculator functions

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Tkinter Calculator")

        # Configuration for the display entry field
        self.current_expression = ""
        self.display = tk.Entry(master, width=30, borderwidth=5, justify='right', font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # List of button texts for the grid layout
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'sqrt', '+',
            'C', 'history', '=', 'power' # Added power for completeness
        ]

        # --- Create and Place Buttons ---
        r = 1
        c = 0
        for button_text in buttons:
            self.create_button(button_text).grid(row=r, column=c, sticky="nsew")
            c += 1
            if c > 3:
                c = 0
                r += 1

        # Configure row and column weights to make the grid cells expand
        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            master.grid_columnconfigure(i, weight=1)

    def create_button(self, text):
        """Helper function to create a button and assign its command."""
        return tk.Button(self.master, text=text, padx=20, pady=20, font=('Arial', 12),
                         command=lambda: self.button_click(text))

    def button_click(self, text):
        """Handles button clicks based on the button text."""
        
        # --- Handle Clear and History ---
        if text == 'C':
            self.current_expression = ""
            self.update_display()
            return
        
        if text == 'history':
            self.show_history()
            return

        # --- Handle Equals/Calculate ---
        if text == '=':
            try:
                # Use a simple eval for basic ops, which is safer here because we control inputs
                # For complex or unary ops like 'sqrt', we need a custom parser
                
                # Check for unary ops
                if self.current_expression.startswith('sqrt(') and self.current_expression.endswith(')'):
                    num = float(self.current_expression[5:-1])
                    result = calc.square_root(num)
                
                # Check for binary ops (simpler approach for this example)
                elif '+' in self.current_expression:
                    a, b = map(float, self.current_expression.split('+'))
                    result = calc.add(a, b)
                # You would need to add elif checks for '-', '*', '/', etc.
                else:
                    result = eval(self.current_expression) 
                    
                self.current_expression = str(result)
                
            except ZeroDivisionError as e:
                messagebox.showerror("Error", str(e))
                self.current_expression = ""
            except Exception as e:
                # Catch general errors (e.g., invalid format, syntax)
                messagebox.showerror("Error", "Invalid Input")
                self.current_expression = ""
            
            self.update_display()
            return

        # --- Append to Expression ---
        # For 'sqrt', format it like a function call immediately
        if text == 'sqrt':
            self.current_expression += "sqrt("
        elif text == 'power':
            self.current_expression += "**" # Use Python's operator for simplicity
        else:
            self.current_expression += text
        
        self.update_display()

    def update_display(self):
        """Updates the text shown in the Entry widget."""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_expression)
        
    def show_history(self):
        """Opens a new window to display the calculator history."""
        history_window = tk.Toplevel(self.master)
        history_window.title("Calculation History")
        
        history_text = tk.Text(history_window, height=15, width=50)
        history_text.pack(padx=10, pady=10)
        
        try:
            if not os.path.exists(calc.LOG_FILE):
                content = "No history found yet (run a calculation first)."
            else:
                with open(calc.LOG_FILE, 'r') as f:
                    content = f.read()
            history_text.insert(tk.END, content)
        except Exception as e:
            history_text.insert(tk.END, f"Error reading log: {e}")

# --- Main Execution ---
if __name__ == "__main__":
    # Ensure os is imported for the history check in show_history
    import os 
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()