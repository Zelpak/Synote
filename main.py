import customtkinter as ctk
from tkinter import filedialog, messagebox

MAX_FONT_SIZE = 30
MIN_FONT_SIZE = 12

def change_theme(theme_choice):
    """Change the appearance mode and color theme of the application."""
    appearance_modes = {"dark": "dark", "light": "light", "system": "system"}
    if theme_choice in appearance_modes:
        ctk.set_appearance_mode(appearance_modes[theme_choice])
    else:
        ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

def show_info():
    """Display information about the application."""
    title = "Synote - NotePad App"
    message = "This is a simple text editor.\nGitHub is WIP.\nv0.1.0"
    messagebox.showinfo(title, message)

def save_file_with_dialog():
    """Save the text content to a file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get("1.0", "end"))
            update_window_title(file_path)
            messagebox.showinfo("Saved", f"File saved as {file_path}")
        except Exception as error:
            messagebox.showerror("Error", str(error))

def open_file():
    """Open a file and display its content in the text widget."""
    file_path = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
            text_area.delete("1.0", "end")
            text_area.insert("1.0", content)
            update_window_title(file_path)
            update_text_statistics()  # Make sure the statistics are updated when opening a file
        except Exception as error:
            messagebox.showerror("Error", str(error))

def update_font_size(event=None):
    """Update the font size of the text widget."""
    font_size = font_size_entry.get()
    try:
        font_size = max(MIN_FONT_SIZE, min(MAX_FONT_SIZE, int(font_size)))
        text_area.configure(font=('Helvetica', font_size))
    except ValueError:
        pass

def update_text_statistics(event=None):
    """Update the line, character, and word count in the bottom frame."""
    text = text_area.get("1.0", "end-1c")
    line_count = text.count("\n") + 1
    char_count = len(text.replace("\n", "").replace(" ", ""))  # Exclude spaces from character count
    word_count = len(text.split())  # Split by whitespace and count words
    line_count_label.configure(text=f"Lines: {line_count}")
    char_count_label.configure(text=f"Chars: {char_count}")
    word_count_label.configure(text=f"Words: {word_count}")

def update_window_title(file_path):
    """Update the title of the application window."""
    file_name = file_path.split("/")[-1].split(".")[0]
    app.title(f"{file_name} - Plexus Text Editor")

app = ctk.CTk()
app.title("Plexus - Text Editor")
app.geometry("1920x1080")

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=0)
app.grid_columnconfigure(0, weight=1)

frame = ctk.CTkFrame(app)
frame.grid(row=0, column=0, sticky="nsew")

text_area = ctk.CTkTextbox(frame, wrap="word", height=1920, width=1920)
text_area.grid(row=0, column=0, sticky="nsew")
text_area.insert("1.0", "Hello, Plexus!")
text_area.bind("<KeyRelease>", update_text_statistics)

bottom_frame = ctk.CTkFrame(app, fg_color="transparent", height=50)
bottom_frame.grid(row=1, column=0, sticky="ew")

open_button = ctk.CTkButton(bottom_frame, text="Open", command=open_file, border_color='black', hover_color='#4DA6FF')
open_button.pack(side="left", padx=10, pady=10)

save_button = ctk.CTkButton(bottom_frame, text="Save", command=save_file_with_dialog, border_color='black', hover_color='#4DA6FF')
save_button.pack(side="left", padx=10, pady=10)

about_button = ctk.CTkButton(bottom_frame, text="About", command=show_info, border_color='black', hover_color='#4DA6FF')
about_button.pack(side="left", padx=10, pady=10)

theme_option_menu = ctk.CTkOptionMenu(bottom_frame, values=["dark", "light", "system"], command=change_theme)
theme_option_menu.pack(side="left", padx=10, pady=10)
theme_option_menu.set("Theme")

theme_label = ctk.CTkLabel(bottom_frame, text="Theme")
theme_label.pack(side="left", padx=10, pady=10)

font_size_label = ctk.CTkLabel(bottom_frame, text="Font Size")
font_size_label.pack(side="left", padx=10, pady=10)

font_size_entry = ctk.CTkEntry(bottom_frame, width=50)
font_size_entry.pack(side="left", padx=10, pady=10)
font_size_entry.insert(0, "12")
font_size_entry.bind("<Return>", update_font_size)

line_count_label = ctk.CTkLabel(bottom_frame, text="Lines: 0")
line_count_label.pack(side="left", padx=10, pady=10)

char_count_label = ctk.CTkLabel(bottom_frame, text="Chars: 0")
char_count_label.pack(side="left", padx=10, pady=10)

word_count_label = ctk.CTkLabel(bottom_frame, text="Words: 0")
word_count_label.pack(side="left", padx=10, pady=10)

app.mainloop()
