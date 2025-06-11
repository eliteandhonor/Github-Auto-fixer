# Github-Auto-fixer

This repository contains **MergeMedic**, a small utility to clean files that contain Git conflict markers.

## CLI usage

Run the script with the path to the conflicted file. Optionally supply an output path.

```bash
python merge_medic.py path/to/file.txt [cleaned_output.txt]
```

The script reads the input, resolves any `<<<<<<<`, `=======`, and `>>>>>>>` blocks, and writes the cleaned result.

## GUI

The GUI now uses Tkinter's themed widgets for a modern look. It offers two tabs: **File** for selecting a file and **Paste Text** for directly pasting conflict content.
A basic graphical interface is also available. Launch it with:

```bash
python merge_medic_gui.py
```

Use the File tab to choose input and output files, or paste text in the Paste Text tab and optionally select where to save the result. Click **Clean** to produce the cleaned file.
