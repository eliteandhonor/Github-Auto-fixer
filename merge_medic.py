import sys
from pathlib import Path


def merge_blocks(current, incoming):
    curr_text = ''.join(current)
    inc_text = ''.join(incoming)
    if curr_text == inc_text:
        return current
    if curr_text in inc_text:
        return incoming
    if inc_text in curr_text:
        return current
    merged = []
    for line in current + incoming:
        if line not in merged:
            merged.append(line)
    return merged


def resolve_conflicts(lines):
    result = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if line.startswith('<<<<<<<'):
            current = []
            i += 1
            while i < n and not lines[i].startswith('======='):
                current.append(lines[i])
                i += 1
            if i >= n:
                result.extend(current)
                break
            i += 1  # skip =======
            incoming = []
            while i < n and not lines[i].startswith('>>>>>>>'):
                incoming.append(lines[i])
                i += 1
            if i >= n:
                result.extend(current)
                result.extend(incoming)
                break
            i += 1  # skip >>>>>>>
            result.extend(merge_blocks(current, incoming))
        else:
            result.append(line)
            i += 1
    return result


def main():
    if len(sys.argv) < 2:
        print('Usage: python merge_medic.py <file> [output_file]')
        sys.exit(1)
    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else input_path
    lines = input_path.read_text(encoding="utf-8", errors="ignore").splitlines(True)
    cleaned_lines = resolve_conflicts(lines)
    output_path.write_text(''.join(cleaned_lines), encoding='utf-8')


if __name__ == '__main__':
    main()
