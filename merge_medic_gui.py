import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

from merge_medic import resolve_conflicts


class MergeMedicApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MergeMedic")
        self.geometry("400x150")

        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()

        tk.Label(self, text="Input File:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self, textvariable=self.input_path, width=40).grid(row=0, column=1, padx=5)
        tk.Button(self, text="Browse", command=self.browse_input).grid(row=0, column=2, padx=5)

        tk.Label(self, text="Output File:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(self, textvariable=self.output_path, width=40).grid(row=1, column=1, padx=5)
        tk.Button(self, text="Browse", command=self.browse_output).grid(row=1, column=2, padx=5)

        tk.Button(self, text="Clean", command=self.clean_file).grid(row=2, column=1, pady=10)

    def browse_input(self):
        path = filedialog.askopenfilename()
        if path:
            self.input_path.set(path)

    def browse_output(self):
        path = filedialog.asksaveasfilename()
        if path:
            self.output_path.set(path)

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


if __name__ == "__main__":
    app = MergeMedicApp()
    app.mainloop()
