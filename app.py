import tkinter as tk
import tkinter.messagebox as messagebox

from datetime_checker import check_date


def clear_button_click():
    day_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)


def check_button_click():
    day = day_entry.get()
    month = month_entry.get()
    year = year_entry.get()
    check = check_date(day, month, year)
    if check['status'] is True:
        messagebox.showinfo("Message", f"{check['message']}")
    else:
        messagebox.showerror("Error", f"{check['message']}")


app = tk.Tk()
app.geometry("400x150")
app.title("Date Time Checker")

frame = tk.Frame(app)
frame.pack(pady=20)

day_label = tk.Label(frame, text="Day:")
day_label.grid(row=0, column=0)
day_entry = tk.Entry(frame)
day_entry.grid(row=0, column=1)

month_label = tk.Label(frame, text="Month:")
month_label.grid(row=1, column=0)
month_entry = tk.Entry(frame)
month_entry.grid(row=1, column=1)

year_label = tk.Label(frame, text="Year:")
year_label.grid(row=2, column=0)
year_entry = tk.Entry(frame)
year_entry.grid(row=2, column=1)

check_button = tk.Button(app, text="Check Date", command=check_button_click)
clear_button = tk.Button(app, text="Clear", command=clear_button_click)
clear_button.pack(side="left", padx=100)
check_button.pack(side="left", padx=10)
app.protocol("WM_DELETE_WINDOW", lambda: messagebox.askokcancel("Quit", "Are you sure to exit?") and app.destroy())

app.mainloop()
