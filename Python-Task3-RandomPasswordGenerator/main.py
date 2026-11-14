
import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password, check_password_strength


# ==========================================
# SECUREPASS - RANDOM PASSWORD GENERATOR
# ==========================================

root = tk.Tk()
root.title("SecurePass - Password Generator")
root.geometry("700x850")
root.minsize(600, 500)
root.configure(bg="#10101C")
root.resizable(True, True)


# ==========================================
# COLOR THEME
# ==========================================

BG = "#10101C"
CARD = "#1B1B2B"
PURPLE = "#8257E5"
WHITE = "#FFFFFF"
GREY = "#A5A5B5"
GREEN = "#22C55E"
BLUE = "#2563EB"


# ==========================================
# VARIABLES
# ==========================================

length_var = tk.IntVar(value=12)

uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

show_password_var = tk.BooleanVar(value=True)

password_history = []


# ==========================================
# SCROLLABLE APPLICATION LAYOUT
# ==========================================

main_frame = tk.Frame(root, bg=BG)
main_frame.pack(fill="both", expand=True)

app_canvas = tk.Canvas(
    main_frame,
    bg=BG,
    highlightthickness=0
)

scrollbar = tk.Scrollbar(
    main_frame,
    orient="vertical",
    command=app_canvas.yview
)

app_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

app_canvas.configure(yscrollcommand=scrollbar.set)

content_frame = tk.Frame(app_canvas, bg=BG)

canvas_window = app_canvas.create_window(
    (0, 0),
    window=content_frame,
    anchor="nw"
)


def update_scroll_region(event=None):
    app_canvas.configure(
        scrollregion=app_canvas.bbox("all")
    )


def resize_content(event):
    app_canvas.itemconfigure(
        canvas_window,
        width=event.width
    )


content_frame.bind("<Configure>", update_scroll_region)
app_canvas.bind("<Configure>", resize_content)


# Mouse wheel scrolling for Windows

def mouse_wheel(event):
    app_canvas.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


app_canvas.bind_all("<MouseWheel>", mouse_wheel)


# ==========================================
# PASSWORD GENERATION
# ==========================================

def generate():

    password = generate_password(
        length_var.get(),
        uppercase_var.get(),
        lowercase_var.get(),
        numbers_var.get(),
        symbols_var.get()
    )

    if not password:
        messagebox.showwarning(
            "Selection Required",
            "Please select at least one character type."
        )
        return

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(show="", state="readonly")

    show_password_var.set(True)
    show_button.config(text="Hide Password")

    update_strength(password)

    # Add password to history
    password_history.insert(0, password)

    # Keep only the latest five
    if len(password_history) > 5:
        password_history.pop()

    update_history()


# ==========================================
# PASSWORD STRENGTH
# ==========================================

def update_strength(password):

    strength = check_password_strength(password)

    if strength == "Weak":
        color = "#EF4444"
        progress = 0.33

    elif strength == "Medium":
        color = "#F59E0B"
        progress = 0.66

    else:
        color = GREEN
        progress = 1.0

    strength_label.config(
        text=f"Password Strength: {strength}",
        fg=color
    )

    strength_canvas.delete("all")

    strength_canvas.create_rectangle(
        0, 0, 520, 10,
        fill="#383849",
        outline=""
    )

    strength_canvas.create_rectangle(
        0, 0, 520 * progress, 10,
        fill=color,
        outline=""
    )


# ==========================================
# UPDATE PASSWORD HISTORY
# ==========================================

def update_history():

    history_listbox.delete(0, tk.END)

    for index, password in enumerate(password_history, start=1):
        history_listbox.insert(
            tk.END,
            f"{index}. {password}"
        )


# ==========================================
# COPY CURRENT PASSWORD
# ==========================================

def copy_password():

    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "No Password",
            "Please generate a password first."
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    copy_status.config(
        text="Password copied successfully!",
        fg=GREEN
    )

    root.after(
        2500,
        lambda: copy_status.config(text="")
    )


# ==========================================
# COPY SELECTED HISTORY PASSWORD
# ==========================================

def copy_history_password():

    selection = history_listbox.curselection()

    if not selection:
        messagebox.showwarning(
            "Select Password",
            "Please select a password from history first."
        )
        return

    index = selection[0]
    password = password_history[index]

    root.clipboard_clear()
    root.clipboard_append(password)

    copy_status.config(
        text="History password copied successfully!",
        fg=GREEN
    )

    root.after(
        2500,
        lambda: copy_status.config(text="")
    )


# ==========================================
# CLEAR PASSWORD HISTORY
# ==========================================

def clear_history():

    if not password_history:
        return

    confirm = messagebox.askyesno(
        "Clear History",
        "Are you sure you want to clear password history?"
    )

    if confirm:
        password_history.clear()
        update_history()


# ==========================================
# CLEAR CURRENT PASSWORD
# ==========================================

def clear_password():

    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

    strength_label.config(
        text="Password Strength: Not Generated",
        fg=GREY
    )

    strength_canvas.delete("all")

    strength_canvas.create_rectangle(
        0, 0, 520, 10,
        fill="#383849",
        outline=""
    )

    show_password_var.set(True)
    show_button.config(text="Show Password")

    copy_status.config(text="")


# ==========================================
# SHOW / HIDE PASSWORD
# ==========================================

def toggle_password():

    if show_password_var.get():

        password_entry.config(show="*")
        show_password_var.set(False)
        show_button.config(text="Show Password")

    else:

        password_entry.config(show="")
        show_password_var.set(True)
        show_button.config(text="Hide Password")


# ==========================================
# UPDATE PASSWORD LENGTH
# ==========================================

def update_length(value):

    length_value.config(
        text=str(int(float(value)))
    )


# ==========================================
# HEADER
# ==========================================

header = tk.Frame(content_frame, bg=BG)
header.pack(pady=(20, 10))

tk.Label(
    header,
    text="SECUREPASS",
    font=("Arial", 29, "bold"),
    bg=BG,
    fg=WHITE
).pack()

tk.Label(
    header,
    text="Create strong and secure passwords",
    font=("Arial", 11),
    bg=BG,
    fg=GREY
).pack(pady=5)


# ==========================================
# MAIN CARD
# ==========================================

card = tk.Frame(
    content_frame,
    bg=CARD,
    padx=35,
    pady=20
)

card.pack(
    padx=25,
    pady=5,
    fill="x"
)


# ==========================================
# PASSWORD LENGTH
# ==========================================

tk.Label(
    card,
    text="PASSWORD LENGTH",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=WHITE
).pack(anchor="w")

length_value = tk.Label(
    card,
    text="12",
    font=("Arial", 20, "bold"),
    bg=CARD,
    fg=PURPLE
)

length_value.pack(anchor="e")

length_slider = tk.Scale(
    card,
    from_=4,
    to=32,
    orient="horizontal",
    variable=length_var,
    command=update_length,
    showvalue=False,
    bg=CARD,
    fg=WHITE,
    troughcolor=PURPLE,
    highlightthickness=0,
    activebackground=PURPLE,
    sliderrelief="flat",
    length=520
)

length_slider.pack(fill="x", pady=(0, 15))


# ==========================================
# CHARACTER OPTIONS
# ==========================================

tk.Label(
    card,
    text="INCLUDE CHARACTERS",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=WHITE
).pack(anchor="w", pady=(5, 8))


def create_option(text, variable):

    tk.Checkbutton(
        card,
        text=text,
        variable=variable,
        bg=CARD,
        fg=WHITE,
        activebackground=CARD,
        activeforeground=WHITE,
        selectcolor="#303047",
        font=("Arial", 11),
        cursor="hand2"
    ).pack(anchor="w", pady=4)


create_option("Uppercase Letters (A-Z)", uppercase_var)
create_option("Lowercase Letters (a-z)", lowercase_var)
create_option("Numbers (0-9)", numbers_var)
create_option("Symbols (!@#$%)", symbols_var)


# ==========================================
# GENERATE BUTTON
# ==========================================

tk.Button(
    card,
    text="GENERATE PASSWORD",
    command=generate,
    bg=PURPLE,
    fg=WHITE,
    activebackground="#7044D0",
    activeforeground=WHITE,
    font=("Arial", 12, "bold"),
    relief="flat",
    cursor="hand2",
    pady=12
).pack(fill="x", pady=(18, 16))


# ==========================================
# PASSWORD DISPLAY
# ==========================================

tk.Label(
    card,
    text="YOUR GENERATED PASSWORD",
    font=("Arial", 10, "bold"),
    bg=CARD,
    fg=GREY
).pack(anchor="w", pady=(0, 8))


password_entry = tk.Entry(
    card,
    font=("Consolas", 16, "bold"),
    bg="#292940",
    fg=WHITE,
    readonlybackground="#292940",
    insertbackground=WHITE,
    relief="flat",
    justify="center",
    state="readonly"
)

password_entry.pack(fill="x", ipady=12)


# ==========================================
# SHOW / HIDE BUTTON
# ==========================================

show_button = tk.Button(
    card,
    text="Show Password",
    command=toggle_password,
    bg=CARD,
    fg=PURPLE,
    activebackground=CARD,
    activeforeground=WHITE,
    font=("Arial", 9, "bold"),
    relief="flat",
    cursor="hand2"
)

show_button.pack(anchor="e", pady=(4, 5))


# ==========================================
# PASSWORD STRENGTH
# ==========================================

strength_label = tk.Label(
    card,
    text="Password Strength: Not Generated",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=GREY
)

strength_label.pack(pady=(8, 10))


strength_canvas = tk.Canvas(
    card,
    width=520,
    height=10,
    bg=CARD,
    highlightthickness=0
)

strength_canvas.pack(pady=(0, 12))

strength_canvas.create_rectangle(
    0, 0, 520, 10,
    fill="#383849",
    outline=""
)


# ==========================================
# COPY AND CLEAR BUTTONS
# ==========================================

button_frame = tk.Frame(card, bg=CARD)
button_frame.pack(fill="x", pady=6)


tk.Button(
    button_frame,
    text="COPY PASSWORD",
    command=copy_password,
    bg=BLUE,
    fg=WHITE,
    activebackground="#1D4ED8",
    relief="flat",
    font=("Arial", 10, "bold"),
    cursor="hand2",
    pady=11
).pack(
    side="left",
    expand=True,
    fill="x",
    padx=(0, 8)
)


tk.Button(
    button_frame,
    text="CLEAR",
    command=clear_password,
    bg="#3B3B50",
    fg=WHITE,
    activebackground="#4B4B60",
    relief="flat",
    font=("Arial", 10, "bold"),
    cursor="hand2",
    pady=11
).pack(
    side="left",
    expand=True,
    fill="x",
    padx=(8, 0)
)


# ==========================================
# COPY CONFIRMATION
# ==========================================

copy_status = tk.Label(
    card,
    text="",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg=GREEN
)

copy_status.pack(pady=3)


# ==========================================
# PASSWORD HISTORY
# ==========================================

tk.Label(
    card,
    text="PASSWORD HISTORY (LAST 5)",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=WHITE
).pack(anchor="w", pady=(12, 8))


history_frame = tk.Frame(card, bg=CARD)
history_frame.pack(fill="x")


history_scrollbar = tk.Scrollbar(history_frame)
history_scrollbar.pack(side="right", fill="y")


history_listbox = tk.Listbox(
    history_frame,
    height=5,
    bg="#292940",
    fg=WHITE,
    font=("Consolas", 10),
    selectbackground=PURPLE,
    selectforeground=WHITE,
    relief="flat",
    yscrollcommand=history_scrollbar.set
)

history_listbox.pack(
    side="left",
    fill="both",
    expand=True
)

history_scrollbar.config(
    command=history_listbox.yview
)


# ==========================================
# HISTORY BUTTONS
# ==========================================

history_button_frame = tk.Frame(card, bg=CARD)
history_button_frame.pack(fill="x", pady=8)


tk.Button(
    history_button_frame,
    text="COPY SELECTED",
    command=copy_history_password,
    bg=BLUE,
    fg=WHITE,
    activebackground="#1D4ED8",
    relief="flat",
    font=("Arial", 9, "bold"),
    cursor="hand2",
    pady=9
).pack(
    side="left",
    expand=True,
    fill="x",
    padx=(0, 5)
)


tk.Button(
    history_button_frame,
    text="CLEAR HISTORY",
    command=clear_history,
    bg="#3B3B50",
    fg=WHITE,
    activebackground="#4B4B60",
    relief="flat",
    font=("Arial", 9, "bold"),
    cursor="hand2",
    pady=9
).pack(
    side="left",
    expand=True,
    fill="x",
    padx=(5, 0)
)


# ==========================================
# FOOTER
# ==========================================

tk.Label(
    content_frame,
    text="SECUREPASS | RANDOM PASSWORD GENERATOR",
    font=("Arial", 9),
    bg=BG,
    fg=GREY
).pack(pady=(12, 3))

tk.Label(
    content_frame,
    text="Developed using Python",
    font=("Arial", 9),
    bg=BG,
    fg=PURPLE
).pack(pady=(0, 15))


# ==========================================
# RUN APPLICATION
# ==========================================

root.mainloop()
