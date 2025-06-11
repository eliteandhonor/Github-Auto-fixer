# Github-Auto-fixer

This repository contains **MergeMedic**, a small utility to clean files that contain Git conflict markers.

## CLI usage

Run the script with the path to the conflicted file. Optionally supply an output path.

```bash
python merge_medic.py path/to/file.txt [cleaned_output.txt]
```

The script reads the input, resolves any `<<<<<<<`, `=======`, and `>>>>>>>` blocks, and writes the cleaned result.

## GUI

A basic graphical interface is also available. Launch it with:

```bash
python merge_medic_gui.py
```

Select an input file and, optionally, an output location, then click **Clean** to produce the cleaned file.
