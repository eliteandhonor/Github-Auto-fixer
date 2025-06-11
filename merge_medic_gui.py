import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from pathlib import Path

from merge_medic import resolve_conflicts


class MergeMedicApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MergeMedic")
        self.geometry("500x350")
        self.resizable(False, False)
        ttk.Style(self).theme_use("clam")

        notebook = ttk.Notebook(self)
        self.file_frame = ttk.Frame(notebook)
        self.paste_frame = ttk.Frame(notebook)
        notebook.add(self.file_frame, text="File")
        notebook.add(self.paste_frame, text="Paste Text")
        notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.setup_file_tab()
        self.setup_paste_tab()

    def setup_file_tab(self):
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()

        ttk.Label(self.file_frame, text="Input File:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(self.file_frame, textvariable=self.input_path, width=40).grid(row=0, column=1, padx=5)
        ttk.Button(self.file_frame, text="Browse", command=self.browse_input).grid(row=0, column=2, padx=5)

        ttk.Label(self.file_frame, text="Output File:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(self.file_frame, textvariable=self.output_path, width=40).grid(row=1, column=1, padx=5)
        ttk.Button(self.file_frame, text="Browse", command=self.browse_output).grid(row=1, column=2, padx=5)

        ttk.Button(self.file_frame, text="Clean", command=self.clean_file).grid(row=2, column=1, pady=10)

    def setup_paste_tab(self):
        self.paste_output = tk.StringVar()
        self.text_input = scrolledtext.ScrolledText(self.paste_frame, width=58, height=10)
        self.text_input.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        ttk.Label(self.paste_frame, text="Output File:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        ttk.Entry(self.paste_frame, textvariable=self.paste_output, width=40).grid(row=1, column=1, padx=5)
        ttk.Button(self.paste_frame, text="Browse", command=self.browse_paste_output).grid(row=1, column=2, padx=5)

        ttk.Button(self.paste_frame, text="Clean", command=self.clean_paste).grid(row=2, column=1, pady=10)

    def browse_input(self):
        path = filedialog.askopenfilename()
        if path:
            self.input_path.set(path)

    def browse_output(self):
        path = filedialog.asksaveasfilename()
        if path:
            self.output_path.set(path)

    def browse_paste_output(self):
        path = filedialog.asksaveasfilename()
        if path:
            self.paste_output.set(path)

    def clean_file(self):
        in_path = self.input_path.get()
        out_path = self.output_path.get() or in_path
        if not in_path:
            messagebox.showerror("Error", "Please choose an input file.")
            return
        try:
            lines = Path(in_path).read_text(encoding="utf-8", errors="ignore").splitlines(True)
            cleaned = resolve_conflicts(lines)
            Path(out_path).write_text(''.join(cleaned), encoding='utf-8')
            messagebox.showinfo("Success", f"Cleaned file written to {out_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def clean_paste(self):
        text = self.text_input.get("1.0", "end-1c")
        if not text.strip():
            messagebox.showerror("Error", "Please paste some text.")
            return
        lines = text.splitlines(True)
        cleaned = resolve_conflicts(lines)
        out_path = self.paste_output.get()
        if out_path:
            try:
                Path(out_path).write_text(''.join(cleaned), encoding='utf-8')
                messagebox.showinfo("Success", f"Cleaned file written to {out_path}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            result_window = tk.Toplevel(self)
            result_window.title("Cleaned Text")
            text_widget = scrolledtext.ScrolledText(result_window, width=60, height=20)
            text_widget.pack(padx=5, pady=5)
            text_widget.insert("1.0", ''.join(cleaned))


if __name__ == "__main__":
    app = MergeMedicApp()
    app.mainloop()
