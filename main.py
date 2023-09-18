import customtkinter as tk
from tkinter import filedialog, messagebox
import gzip

def compress_file():
    input_file = input_file_entry.get()
    if not input_file:
        messagebox.showerror("Error", "Please select a file to compress.")
        return

    output_file = input_file + '.gz'
    try:
        with open(input_file, 'rb') as f_in:
            with gzip.open(output_file, 'wb') as f_out:
                f_out.writelines(f_in)
        messagebox.showinfo("Success", f"File '{input_file}' has been compressed and saved as '{output_file}'")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def browse_file():
    file_path = filedialog.askopenfilename()
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, file_path)
tk.set_appearance_mode('dark')
tk.set_default_color_theme('dark-blue')
app = tk.CTk()
app.title("Gzip Compressor")
app.geometry('500x500')



input_label = tk.CTkLabel(app, text="Select a file to compress:")
input_label.pack(pady=10, padx=10)

input_file_entry = tk.CTkEntry(app, width=300)
input_file_entry.pack(pady=10, padx=10)

browse_button = tk.CTkButton(app, text="Browse", command=browse_file)
browse_button.pack(pady=10, padx=10)

compress_button = tk.CTkButton(app, text="Compress", command=compress_file)
compress_button.pack(pady=10, padx=10)

app.mainloop()
