
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ==============================
# BMI CALCULATOR - ADVANCED GUI
# ==============================

history = []


# Calculate BMI
def calculate_bmi():

    name = name_entry.get().strip()
    weight_text = weight_entry.get().strip()
    height_text = height_entry.get().strip()

    if not name or not weight_text or not height_text:
        messagebox.showwarning(
            "Missing Information",
            "Please fill in all fields."
        )
        return

    try:
        weight = float(weight_text)
        height = float(height_text)

        if weight <= 0 or height <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Weight and height must be greater than zero."
            )
            return

        bmi = weight / (height * height)

        # BMI categories and colours
        if bmi < 18.5:
            category = "Underweight"
            color = "#E67E22"

        elif bmi < 25:
            category = "Normal Weight"
            color = "#16A34A"

        elif bmi < 30:
            category = "Overweight"
            color = "#EA580C"

        else:
            category = "Obese"
            color = "#DC2626"

        # Display result
        result_name.config(
            text=f"Hello, {name}!"
        )

        result_bmi.config(
            text=f"{bmi:.2f}",
            fg=color
        )

        result_category.config(
            text=f"Category: {category}",
            fg=color
        )

        # Save calculation in history
        record = (
            f"{name} | {weight} kg | "
            f"{height} m | BMI: {bmi:.2f} | {category}"
        )

        history.append(record)

        history_list.insert(tk.END, record)

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers for weight and height."
        )


# Clear input fields
def clear_fields():

    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_name.config(text="Your result will appear here.")

    result_bmi.config(
        text="--",
        fg="#2563EB"
    )

    result_category.config(
        text="Enter your details to calculate BMI.",
        fg="#64748B"
    )


# Clear history
def clear_history():

    if not history:
        messagebox.showinfo(
            "History",
            "There is no history to clear."
        )
        return

    confirm = messagebox.askyesno(
        "Clear History",
        "Are you sure you want to delete all BMI history?"
    )

    if confirm:
        history.clear()
        history_list.delete(0, tk.END)


# ==============================
# MAIN WINDOW
# ==============================

root = tk.Tk()

root.title("Advanced BMI Calculator")
root.geometry("560x820")
root.resizable(True, True)
root.configure(bg="#F1F5F9")


# ==============================
# HEADING
# ==============================

title = tk.Label(
    root,
    text="BMI CALCULATOR",
    font=("Arial", 25, "bold"),
    bg="#F1F5F9",
    fg="#1E293B"
)

title.pack(pady=(18, 5))


subtitle = tk.Label(
    root,
    text="Your Personal Body Mass Index Calculator",
    font=("Arial", 11),
    bg="#F1F5F9",
    fg="#64748B"
)

subtitle.pack(pady=(0, 15))


# ==============================
# INPUT SECTION
# ==============================

input_frame = tk.Frame(
    root,
    bg="white",
    padx=25,
    pady=15
)

input_frame.pack(
    padx=30,
    pady=5,
    fill="x"
)


def create_input(label_text):

    tk.Label(
        input_frame,
        text=label_text,
        font=("Arial", 11, "bold"),
        bg="white",
        fg="#334155"
    ).pack(anchor="w", pady=(5, 3))

    entry = tk.Entry(
        input_frame,
        font=("Arial", 12),
        relief="solid",
        bd=1
    )

    entry.pack(
        fill="x",
        pady=(0, 8),
        ipady=5
    )

    return entry


name_entry = create_input("Your Name")

weight_entry = create_input("Weight (kg)")

height_entry = create_input("Height (metres)")


# ==============================
# BUTTONS
# ==============================

button_frame = tk.Frame(
    root,
    bg="#F1F5F9"
)

button_frame.pack(pady=12)


calculate_button = tk.Button(
    button_frame,
    text="Calculate BMI",
    command=calculate_bmi,
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="white",
    activebackground="#1D4ED8",
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=10
)

calculate_button.grid(row=0, column=0, padx=8)


clear_button = tk.Button(
    button_frame,
    text="Clear Fields",
    command=clear_fields,
    font=("Arial", 10, "bold"),
    bg="#E2E8F0",
    fg="#334155",
    relief="flat",
    cursor="hand2",
    padx=20,
    pady=10
)

clear_button.grid(row=0, column=1, padx=8)


# ==============================
# RESULT SECTION
# ==============================

result_frame = tk.Frame(
    root,
    bg="white",
    padx=20,
    pady=12
)

result_frame.pack(
    padx=30,
    pady=8,
    fill="x"
)


result_name = tk.Label(
    result_frame,
    text="Your result will appear here.",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#334155"
)

result_name.pack(pady=3)


tk.Label(
    result_frame,
    text="YOUR BMI",
    font=("Arial", 10, "bold"),
    bg="white",
    fg="#64748B"
).pack(pady=3)


result_bmi = tk.Label(
    result_frame,
    text="--",
    font=("Arial", 30, "bold"),
    bg="white",
    fg="#2563EB"
)

result_bmi.pack(pady=2)


result_category = tk.Label(
    result_frame,
    text="Enter your details to calculate BMI.",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#64748B"
)

result_category.pack(pady=5)


# ==============================
# BMI HEALTH RANGE GUIDE
# ==============================

guide_frame = tk.Frame(
    root,
    bg="white",
    padx=15,
    pady=10
)

guide_frame.pack(
    padx=30,
    pady=8,
    fill="x"
)


tk.Label(
    guide_frame,
    text="BMI CATEGORY GUIDE",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#1E293B"
).pack(pady=(0, 8))


categories = [
    ("Underweight", "Below 18.5", "#E67E22"),
    ("Normal Weight", "18.5 - 24.9", "#16A34A"),
    ("Overweight", "25 - 29.9", "#EA580C"),
    ("Obese", "30 and above", "#DC2626")
]


for category, bmi_range, color in categories:

    row = tk.Frame(
        guide_frame,
        bg="white"
    )

    row.pack(fill="x", pady=2)

    tk.Label(
        row,
        text=category,
        font=("Arial", 10, "bold"),
        bg="white",
        fg=color,
        anchor="w"
    ).pack(side="left")

    tk.Label(
        row,
        text=bmi_range,
        font=("Arial", 10),
        bg="white",
        fg="#475569"
    ).pack(side="right")


# ==============================
# BMI HISTORY
# ==============================

history_frame = tk.Frame(
    root,
    bg="white",
    padx=15,
    pady=10
)

history_frame.pack(
    padx=30,
    pady=8,
    fill="both",
    expand=True
)


tk.Label(
    history_frame,
    text="BMI CALCULATION HISTORY",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#1E293B"
).pack(pady=(0, 8))


history_list = tk.Listbox(
    history_frame,
    font=("Arial", 9),
    height=4,
    bg="#F8FAFC",
    fg="#334155",
    selectbackground="#2563EB"
)

history_list.pack(
    fill="both",
    expand=True
)


history_button = tk.Button(
    history_frame,
    text="Clear History",
    command=clear_history,
    font=("Arial", 9, "bold"),
    bg="#FEE2E2",
    fg="#DC2626",
    relief="flat",
    cursor="hand2",
    padx=15,
    pady=5
)

history_button.pack(pady=8)


# ==============================
# FOOTER
# ==============================

footer = tk.Label(
    root,
    text="BMI Calculator | Python Tkinter Project",
    font=("Arial", 9),
    bg="#F1F5F9",
    fg="#94A3B8"
)

footer.pack(pady=8)


# ==============================
# START APPLICATION
# ==============================

root.mainloop()
