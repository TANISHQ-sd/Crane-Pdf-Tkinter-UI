import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Crane Pdf Reader & Comparator")
root.geometry("900x600")


icon = tk.PhotoImage(file="crane_icon.png")
root.iconphoto(False, icon)


file_menu_window = None

def open_file_menu(event=None):
    global file_menu_window


    if file_menu_window and file_menu_window.winfo_exists():
        file_menu_window.destroy()
        return

    file_menu_window = tk.Toplevel(root)
    file_menu_window.overrideredirect(True)
    file_menu_window.attributes("-topmost", True)


    x = file_btn.winfo_rootx()
    y = file_btn.winfo_rooty() + file_btn.winfo_height()
    file_menu_window.geometry(f"220x240+{x}+{y}")


    file_menu_window.bind("<FocusOut>", lambda e: file_menu_window.destroy())
    file_menu_window.focus_force()


    canvas = tk.Canvas(file_menu_window, borderwidth=0)
    scrollbar = ttk.Scrollbar(file_menu_window, orient="vertical", command=canvas.yview)
    frame = ttk.Frame(canvas)

    frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    file_options = [
        "Open PDF",
        "Upload PDF",
        "Save",
        "Save As",
        "Save All",
        "Print",
        "Close Window",
        "Exit"
    ]

    for option in file_options:
        btn = ttk.Button(
            frame,
            text=option,
            command=lambda o=option: print(f"{o} clicked")
        )
        btn.pack(fill="x", padx=6, pady=3)


top_frame = ttk.Frame(root)
top_frame.pack(fill="x")

file_btn = ttk.Button(top_frame, text="File", command=open_file_menu)
file_btn.pack(side="left", padx=5)

ttk.Button(top_frame, text="Operations").pack(side="left", padx=5)
ttk.Button(top_frame, text="Help").pack(side="left", padx=5)
ttk.Button(top_frame, text="About").pack(side="left", padx=5)


root.mainloop()
