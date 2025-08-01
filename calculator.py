import tkinter as tk
import math

def safe_eval(expr):
    try:
        expr = expr.replace('^', '**')
        expr = expr.replace('π', str(math.pi))
        expr = expr.replace('e', str(math.e))
        expr = expr.replace('√', 'math.sqrt')
        expr = expr.replace('%', '/100')
        return eval(expr, {"__builtins__": None}, vars(math))
    except ZeroDivisionError:
        return "Error: ÷0"
    except:
        return "Error"

def click(text):
    if text == "=" or text == "Enter":
        result = safe_eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "DEL" or text == "BackSpace":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(0, current[:-1])
    elif text in ["sin", "cos", "tan", "log", "ln", "sqrt"]:
        if text == "ln":
            entry.insert(tk.END, "log(")
        elif text == "sqrt":
            entry.insert(tk.END, "√(")
        else:
            entry.insert(tk.END, f"{text}(")
    else:
        entry.insert(tk.END, text)

def key_event(event):
    key = event.keysym
    if key in "0123456789+-*/().%":
        click(key)
    elif key == "Return":
        click("Enter")
    elif key == "BackSpace":
        click("BackSpace")

root = tk.Tk()
root.title("Scientific Calculator - Dark Mode")
root.geometry("400x600")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

entry = tk.Entry(root, font="Arial 24", bg="#252526", fg="white", bd=10, relief=tk.FLAT, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/", "DEL"],
    ["4", "5", "6", "*", "C"],
    ["1", "2", "3", "-", "π"],
    ["0", ".", "%", "+", "e"],
    ["sin", "cos", "tan", "^", "√"],
    ["log", "ln", "(", ")", "="],
]

btn_style = {
    "font": ("Arial", 16),
    "bg": "#2d2d2d",
    "fg": "white",
    "activebackground": "#007acc",
    "activeforeground": "white",
    "relief": tk.FLAT,
    "bd": 1
}

for row in buttons:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill="both")
    for btn in row:
        button = tk.Button(frame, text=btn, **btn_style)
        button.pack(side="left", expand=True, fill="both", padx=2, pady=2)
        button.config(command=lambda b=btn: click(b))

# Bind keyboard events
root.bind("<Key>", key_event)

root.mainloop()
