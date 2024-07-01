import tkinter as tk
from tkinter import messagebox
from monte_carlo import get_simulation

def run_simulation():
    ticker = entry_ticker.get()
    time = int(entry_time.get())
    i = int(entry_iter.get())
    
    if not ticker:
        messagebox.showerror("Please enter a stock ticker.")
        return
    
    if time <= 0:
        messagebox.showerror("Time needs to be greater than 0.")
        return
    
    if i <= 0:
        messagebox.showerror("Number of iterations needs to be greater than 0.")

    get_simulation(ticker, time, i)

root = tk.Tk()
root.title("Monte Carlo Simulation")

label_ticker = tk.Label(root, text="Stock Ticker:")
label_ticker.grid(row=0, column=0, padx=10, pady=10)

entry_ticker = tk.Entry(root)
entry_ticker.grid(row=0, column=1, padx=10, pady=10)

label_time = tk.Label(root, text="Time Intervals:")
label_time.grid(row=1, column=0, padx=10, pady=10)

entry_time = tk.Entry(root)
entry_time.grid(row=1, column=1, padx=10, pady=10)

label_iter = tk.Label(root, text="Number of Iterations:")
label_iter.grid(row=2, column=0, padx=10, pady=10)

entry_iter = tk.Entry(root)
entry_iter.grid(row=2, column=1, padx=10, pady=10)

button_run = tk.Button(root, text="Run Simulation", command=run_simulation)
button_run.grid(row=3, columnspan=3, pady=20)

root.mainloop()
