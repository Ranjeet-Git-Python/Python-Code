import os
import tkinter as tk
from tkinter import filedialog, messagebox
import win32com.client
from PIL import ImageGrab

# Word constants
wdActiveEndPageNumber = 3
wdFirstCharacterLineNumber = 10


# ---------- GUI FUNCTIONS ----------

def browse_input():
    file_path = filedialog.askopenfilename(
        filetypes=[("Word Files", "*.docx")]
    )
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)


def browse_output():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, folder_path)


# ---------- MAIN FUNCTION ----------

def extract_images():
    # ✅ Fix path issue (%20 → space)
    input_path = os.path.normpath(input_entry.get().replace("%20", " "))
    output_folder = os.path.normpath(output_entry.get().replace("%20", " "))

    # ✅ File validation
    if not os.path.exists(input_path):
        messagebox.showerror("Error", f"File not found:\n{input_path}")
        return

    if not os.path.isdir(output_folder):
        messagebox.showerror("Error", "Invalid output folder")
        return

    try:
        # ✅ Start Word
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        # ✅ Open document
        doc = word.Documents.Open(input_path)

        img_count = 0

        # ---------- INLINE IMAGES ----------
        for shape in doc.InlineShapes:
            rng = shape.Range

            page_num = rng.Information(wdActiveEndPageNumber)
            line_num = rng.Information(wdFirstCharacterLineNumber)

            shape.Select()
            word.Selection.Copy()

            img = ImageGrab.grabclipboard()

            if img is not None:
                img_count += 1
                filename = f"img_{img_count}_Page_{page_num}_Line_{line_num}.png"
                save_path = os.path.join(output_folder, filename)

                img.save(save_path, "PNG")

        # ---------- FLOATING IMAGES (IMPORTANT FIX) ----------
        for shape in doc.Shapes:
            try:
                rng = shape.Anchor

                page_num = rng.Information(wdActiveEndPageNumber)
                line_num = rng.Information(wdFirstCharacterLineNumber)

                shape.Select()
                word.Selection.Copy()

                img = ImageGrab.grabclipboard()

                if img is not None:
                    img_count += 1
                    filename = f"img_{img_count}_Page_{page_num}_Line_{line_num}.png"
                    save_path = os.path.join(output_folder, filename)

                    img.save(save_path, "PNG")

            except:
                continue

        # ✅ Cleanup
        doc.Close(False)
        word.Quit()

        messagebox.showinfo(
            "Success",
            f"{img_count} images extracted with exact page & line!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- GUI ----------

root = tk.Tk()
root.title("DOCX Image Extractor (Exact Page & Line)")
root.geometry("650x260")


# Input file
tk.Label(root, text="Input DOCX File:").pack(pady=5)
frame1 = tk.Frame(root)
frame1.pack()

input_entry = tk.Entry(frame1, width=55)
input_entry.pack(side=tk.LEFT, padx=5)

tk.Button(frame1, text="Browse", command=browse_input).pack(side=tk.LEFT)


# Output folder
tk.Label(root, text="Output Folder:").pack(pady=5)
frame2 = tk.Frame(root)
frame2.pack()

output_entry = tk.Entry(frame2, width=55)
output_entry.pack(side=tk.LEFT, padx=5)

tk.Button(frame2, text="Browse", command=browse_output).pack(side=tk.LEFT)


# Run button
tk.Button(
    root,
    text="Extract Images (Exact Page & Line)",
    command=extract_images,
    bg="green",
    fg="white",
    height=2
).pack(pady=20)


root.mainloop()
