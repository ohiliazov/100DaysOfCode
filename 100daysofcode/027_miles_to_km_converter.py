import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = tk.Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles", width=10)
miles_label.grid(column=2, row=0)

is_equal_label = tk.Label(text="is equal to", width=10)
is_equal_label.grid(column=0, row=1)

km_result_label = tk.Label(text="0.0", width=10)
km_result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km", width=10)
km_label.grid(column=2, row=1)


def miles_to_km():
    miles = float(miles_input.get() or 0)
    km = miles * 1.609344
    km_result_label.config(text=f"{km:.2f}")


button = tk.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
